import sys
from PIL import Image, ImageDraw, ImageFont
# big_bubble.py OUT "line 1" "line 2"   (an emoji at the end of a line is drawn in colour)
out, lines = sys.argv[1], sys.argv[2:4]
W, H, SIZE = 712, 230, 47
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', SIZE)
E = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf', 109)
def split(l):
    if l and ord(l[-1]) > 0x2000: return l[:-1].rstrip(), l[-1]
    return l, ''
def tw(t): b = F.getbbox(t); return b[2] - b[0]
img = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
d.rounded_rectangle([0, 0, W - 1, H - 1], radius=30, fill=(255, 255, 255, 255))
eh = 54
for i, l in enumerate(lines):
    t, e = split(l); w = tw(t) + (eh + 10 if e else 0); x = (W - w) / 2; y = 48 + i * 78
    d.text((x, y), t, font=F, fill=(0, 0, 0, 255))
    if e:
        em = Image.new('RGBA', (140, 140), (0, 0, 0, 0)); ImageDraw.Draw(em).text((0, 0), e, font=E, embedded_color=True)
        em = em.crop(em.getbbox()).resize((eh, eh), Image.LANCZOS)
        img.alpha_composite(em, (int(x + tw(t) + 10), y + 2))
img.save(out)
