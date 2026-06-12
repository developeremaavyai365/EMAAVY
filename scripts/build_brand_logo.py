"""Build canonical Emaavy logo assets from official reference image."""
from __future__ import annotations

import base64
import io
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BRAND_DIR = ROOT / "assets" / "brand"
BRAND_COLOR = "#18345d"
FALLBACK_REFERENCE = BRAND_DIR / "emaavy-logo-source.png"
REFERENCE_CANDIDATES = [
    BRAND_DIR / "emaavy-logo-source.png",
    ROOT
    / "assets"
    / "c__Users_DELL_AppData_Roaming_Cursor_User_workspaceStorage_34e64ea1338e1dd425d2d1837d9e68ad_images_Screenshot__81_-3709121b-4769-42fc-ade0-10e50fc17b8c.png",
]


def colorize(im: Image.Image, hex_color: str) -> Image.Image:
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    px = im.load()
    out = Image.new("RGBA", im.size, (0, 0, 0, 0))
    opx = out.load()
    for y in range(im.height):
        for x in range(im.width):
            pr, pg, pb, pa = px[x, y]
            lum = (pr + pg + pb) / 3
            if lum < 200:
                alpha = max(0, min(255, int((200 - lum) * 2.5)))
                opx[x, y] = (r, g, b, alpha)
    return out


def main() -> None:
    BRAND_DIR.mkdir(parents=True, exist_ok=True)
    src_path = next((p for p in REFERENCE_CANDIDATES if p.exists()), None)
    if src_path is None:
        raise SystemExit(f"Reference logo not found in {REFERENCE_CANDIDATES}")

    img = Image.open(src_path).convert("RGBA")
    arr = np.array(img)
    grey = arr[:, :, :3].mean(axis=2)
    mask = grey < 200
    ys, xs = np.where(mask)
    x0, y0, x1, y1 = xs.min(), ys.min(), xs.max() + 1, ys.max() + 1
    crop = img.crop((x0, y0, x1, y1))

    scale = 4
    up = crop.resize((crop.width * scale, crop.height * scale), Image.Resampling.LANCZOS)
    colored = colorize(up, BRAND_COLOR)
    colored.save(BRAND_DIR / "emaavy-logo.png")

    mask_img = Image.new("RGBA", up.size, (0, 0, 0, 255))
    mp = mask_img.load()
    cp = up.load()
    for y in range(up.height):
        for x in range(up.width):
            pr, pg, pb, pa = cp[x, y]
            if pa > 20 or (pr + pg + pb) / 3 < 200:
                mp[x, y] = (255, 255, 255, 255)
    buf = io.BytesIO()
    colored.save(buf, format="PNG")
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    vw, vh = up.size
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'viewBox="0 0 {vw} {vh}" width="{vw}" height="{vh}" '
        f'role="img" aria-label="Emaavy">\n'
        f'  <image width="{vw}" height="{vh}" preserveAspectRatio="xMidYMid meet" '
        f'xlink:href="data:image/png;base64,{b64}"/>\n'
        f'</svg>\n'
    )
    (BRAND_DIR / "emaavy-logo.svg").write_text(svg, encoding="utf-8")
    print(f"Built assets in {BRAND_DIR} ({vw}x{vh})")


if __name__ == "__main__":
    main()
