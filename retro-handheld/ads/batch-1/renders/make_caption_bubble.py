import sys
from PIL import Image, ImageDraw, ImageFont
out, l1, l2 = sys.argv[1], sys.argv[2], sys.argv[3]
emoji = sys.argv[4] if len(sys.argv) > 4 else ''
minw = int(sys.argv[5]) if len(sys.argv) > 5 else 0
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 44)
E = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf', 109)
def tw(t): b = F.getbbox(t); return b[2]-b[0]
eh = 46
w2 = tw(l2) + (eh + 8 if emoji else 0)
W = max(tw(l1), w2) + 64; W = max(W, minw); H = 150
img = Image.new('RGBA', (W, H), (0,0,0,0)); d = ImageDraw.Draw(img)
d.rounded_rectangle([0,0,W-1,H-1], radius=22, fill=(255,255,255,255))
d.text(((W-tw(l1))/2, 22), l1, font=F, fill=(0,0,0,255))
x2 = (W-w2)/2; d.text((x2, 80), l2, font=F, fill=(0,0,0,255))
if emoji:
    e = Image.new('RGBA', (140,140), (0,0,0,0)); ImageDraw.Draw(e).text((0,0), emoji, font=E, embedded_color=True)
    e = e.crop(e.getbbox()).resize((eh, eh), Image.LANCZOS)
    img.alpha_composite(e, (int(x2 + tw(l2) + 8), 86))
img.save(out)
print(W, H)
