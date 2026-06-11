"""Build hero demo MP4 from EMAAVY platform screenshots (Ken Burns tour)."""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "assets" / "video"
OUT = OUT_DIR / "emaavy-hero.mp4"

SCENES = [
    ("dashboard.png", "Dashboard — live KPIs & call intelligence"),
    ("campaigns.png", "Campaigns — guided outbound & inbound"),
    ("agents.png", "AI Agents — voice workforce at scale"),
    ("integrations.png", "Integrations — full enterprise stack"),
]

W, H = 1920, 1080
FPS = 30
SEC_PER_SCENE = 5
BG = (12, 15, 20)  # #0c0f14 device chrome


def load_scene(name: str) -> Image.Image:
    path = ROOT / "assets" / "hero" / name
    img = Image.open(path).convert("RGB")
    scale = min((W * 0.92) / img.width, (H * 0.78) / img.height)
    nw, nh = int(img.width * scale), int(img.height * scale)
    return img.resize((nw, nh), Image.Resampling.LANCZOS)


def render_frame(img: Image.Image, t: float, caption: str) -> np.ndarray:
    """t in [0,1] within scene — slow zoom + pan."""
    canvas = Image.new("RGB", (W, H), BG)
    zoom = 1.0 + 0.06 * t
    iw, ih = img.size
    zw, zh = int(iw * zoom), int(ih * zoom)
    zoomed = img.resize((zw, zh), Image.Resampling.LANCZOS)
    pan_x = int((zw - iw) * 0.35 * t)
    pan_y = int((zh - ih) * 0.12 * t)
    crop = zoomed.crop((pan_x, pan_y, pan_x + iw, pan_y + ih))
    x = (W - iw) // 2
    y = (H - ih) // 2 - 24
    canvas.paste(crop, (x, y))

    draw = ImageDraw.Draw(canvas)
    bar_h = 56
    draw.rectangle((0, 0, W, bar_h), fill=(10, 13, 18))
    draw.rectangle((0, bar_h - 1, W, bar_h), fill=(30, 41, 59))
    try:
        font = ImageFont.truetype("arial.ttf", 22)
        font_sm = ImageFont.truetype("arial.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
        font_sm = font
    draw.ellipse((28, 20, 40, 32), fill=(62, 207, 142))
    draw.text((52, 16), "EMAAVY Cloud", fill=(226, 232, 240), font=font)
    draw.text((W - 320, 18), "Live platform tour", fill=(148, 163, 184), font=font_sm)
    draw.rectangle((0, H - 72, W, H), fill=(15, 23, 42, 180))
    draw.text((40, H - 48), caption, fill=(241, 245, 249), font=font_sm)
    return np.asarray(canvas)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    frames = []
    for filename, caption in SCENES:
        img = load_scene(filename)
        n = SEC_PER_SCENE * FPS
        for i in range(n):
            t = i / max(n - 1, 1)
            frames.append(render_frame(img, t, caption))

    imageio.mimsave(
        OUT,
        frames,
        fps=FPS,
        codec="libx264",
        quality=8,
        pixelformat="yuv420p",
        macro_block_size=1,
    )
    print(f"Wrote {OUT} ({len(frames)} frames, {len(frames)/FPS:.1f}s)")


if __name__ == "__main__":
    main()
