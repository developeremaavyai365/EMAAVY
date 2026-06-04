"""Crop full emaavy wordmark (e + maavy) from brand screenshot."""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    raise SystemExit("PIL required") from None

src = Path(__file__).resolve().parents[1] / "assets" / "emaavy-wordmark-source.png"
out = Path(__file__).resolve().parents[1] / "assets" / "emaavy-wordmark.png"

im = Image.open(src).convert("RGBA")
w, h = im.size
pixels = im.load()
minx, miny, maxx, maxy = w, h, 0, 0

def is_ink(r, g, b, a=255):
    if a < 20:
        return False
    return r < 248 or g < 248 or b < 248

for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        if is_ink(r, g, b, a):
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)

# trim thin right-edge stroke
trim = 0
for x in range(maxx, minx, -1):
    dark = sum(
        1 for y in range(miny, maxy + 1)
        if pixels[x, y][0] < 200 and pixels[x, y][1] < 200 and pixels[x, y][2] < 220
    )
    if dark > (maxy - miny + 1) * 0.55:
        trim += 1
    else:
        break
if 0 < trim < 40:
    maxx -= trim

pad = 8
minx = max(0, minx - pad)
miny = max(0, miny - pad)
maxx = min(w - 1, maxx + pad)
maxy = min(h - 1, maxy + pad)

crop = im.crop((minx, miny, maxx + 1, maxy + 1))
# white background -> transparent for navbar flexibility
bg = Image.new("RGBA", crop.size, (255, 255, 255, 0))
data = crop.getdata()
new = []
for r, g, b, a in data:
    if r > 245 and g > 245 and b > 245:
        new.append((255, 255, 255, 0))
    else:
        new.append((r, g, b, a))
crop.putdata(new)
crop.save(out, optimize=True)
print("Saved", out, crop.size)
