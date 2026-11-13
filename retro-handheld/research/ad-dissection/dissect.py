#!/usr/bin/env python3.13
"""
Ad dissection helper (2026-11-13).

For each video it produces, in the output folder:
  <name>.jpg   one sheet: top row = the hook (0, 0.5, 1, 1.5, 2, 3 s),
               rows below = 12 frames spread over the rest of the ad
  <name>.json  length, size, cut times, transcript with timestamps, and
               the hook numbers (when speech starts, words in the first 3 s,
               cuts in the first 3 s, cuts per 10 s, words per second)
and appends one row per ad to rollup.csv.

Usage:
  python3.13 dissect.py OUT_DIR video1.mp4 [video2.mp4 ...]

Needs: ffmpeg, Pillow, numpy, faster-whisper (models base.en / small.en).
The sheets are for a person (or Claude) to read: what is on screen, what moves,
what the on-screen text says. The numbers are only the parts a script can count.
"""
import csv, json, os, re, subprocess as sp, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HOOK_T = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]
BODY_N = 12
CELL_W = 180
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def probe(path):
    out = sp.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,width,height',
                  '-of', 'json', path], capture_output=True, text=True).stdout
    j = json.loads(out)
    v = next(s for s in j['streams'] if s['codec_type'] == 'video')
    return float(j['format']['duration']), v['width'], v['height'], any(s['codec_type'] == 'audio' for s in j['streams'])


def frame(path, t, w, tmp):
    f = os.path.join(tmp, f'{t:.2f}.png')
    sp.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', path, '-frames:v', '1', '-vf', f'scale={w}:-2', f], check=False)
    return Image.open(f).convert('RGB') if os.path.exists(f) else None


def cuts(path):
    err = sp.run(['ffmpeg', '-i', path, '-filter:v', "select='gt(scene,0.30)',showinfo", '-an', '-f', 'null', '-'],
                 capture_output=True, text=True).stderr
    return sorted({round(float(x), 2) for x in re.findall(r'pts_time:([0-9.]+)', err)})


def sheet(path, dur, out_png):
    font = ImageFont.truetype(FONT, 13)
    with tempfile.TemporaryDirectory() as tmp:
        body_t = [3.0 + (dur - 3.2) * (i + 1) / BODY_N for i in range(BODY_N)] if dur > 4 else []
        times = [t for t in HOOK_T if t < dur - 0.05] + body_t
        frames = [(t, frame(path, t, CELL_W, tmp)) for t in times]
        frames = [(t, f) for t, f in frames if f is not None]
        if not frames:
            return
        ch = max(f.height for _, f in frames)
        rows = [frames[:len([t for t in HOOK_T if t < dur - 0.05])]]
        rest = frames[len(rows[0]):]
        rows += [rest[i:i + 6] for i in range(0, len(rest), 6)]
        W, H = 6 * (CELL_W + 4) + 4, len(rows) * (ch + 22) + 4
        img = Image.new('RGB', (W, H), (18, 18, 24)); d = ImageDraw.Draw(img)
        for r, row in enumerate(rows):
            for c, (t, f) in enumerate(row):
                x, y = 4 + c * (CELL_W + 4), 4 + r * (ch + 22)
                img.paste(f, (x, y + 18))
                d.text((x + 2, y + 1), f'{t:.1f}s' + (' HOOK' if r == 0 else ''), font=font, fill=(242, 193, 78) if r == 0 else (200, 200, 210))
        img.save(out_png, quality=78)


def transcript(path, model):
    raw = sp.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    if audio.size == 0:
        return [], []
    segs, _ = model.transcribe(audio, vad_filter=True, word_timestamps=True)
    S, Wd = [], []
    for s in segs:
        S.append({'start': round(s.start, 2), 'end': round(s.end, 2), 'text': s.text.strip()})
        for w in (s.words or []):
            Wd.append({'t': round(w.start, 2), 'w': w.word.strip()})
    return S, Wd


def main():
    out, files = sys.argv[1], sys.argv[2:]
    os.makedirs(out, exist_ok=True)
    from faster_whisper import WhisperModel
    model = WhisperModel('small.en', device='cpu', compute_type='int8')
    rollup = os.path.join(out, 'rollup.csv'); new = not os.path.exists(rollup)
    with open(rollup, 'a', newline='') as fh:
        wr = csv.writer(fh)
        if new:
            wr.writerow(['ad', 'seconds', 'size', 'speech_starts_s', 'words_first_3s', 'words_per_s', 'cuts_first_3s', 'cuts_per_10s', 'first_line'])
        for path in files:
            name = os.path.splitext(os.path.basename(path))[0]
            dur, w, h, has_audio = probe(path)
            c = cuts(path)
            segs, words = transcript(path, model) if has_audio else ([], [])
            sheet(path, dur, os.path.join(out, name + '.jpg'))
            first = words[0]['t'] if words else None
            w3 = [x['w'] for x in words if x['t'] < 3.0]
            info = {
                'ad': name, 'seconds': round(dur, 1), 'size': f'{w}x{h}',
                'speech_starts_s': first, 'words_first_3s': len(w3), 'hook_words': ' '.join(w3),
                'words_per_s': round(len(words) / dur, 2) if words else 0,
                'cuts': c, 'cuts_first_3s': len([x for x in c if x < 3.0]),
                'cuts_per_10s': round(len(c) / dur * 10, 1), 'segments': segs,
            }
            json.dump(info, open(os.path.join(out, name + '.json'), 'w'), indent=1)
            wr.writerow([name, info['seconds'], info['size'], first, len(w3), info['words_per_s'], info['cuts_first_3s'],
                         info['cuts_per_10s'], (segs[0]['text'][:90] if segs else '(no speech)')])
            print(f"{name}: {info['seconds']}s, speech at {first}, {len(w3)} words in 3s, {info['cuts_first_3s']} cuts in 3s, {info['cuts_per_10s']} cuts/10s")
            print('   ', ' '.join(s['text'] for s in segs)[:300] or '(no speech)')


if __name__ == '__main__':
    main()
