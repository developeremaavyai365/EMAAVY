"""
Build premium Vivo B1G2 commercial MP4 from original poster.
All on-screen text comes from the source image — no regenerated typography.
"""
from __future__ import annotations

import math
from pathlib import Path

import imageio.v2 as imageio
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
POSTER = ROOT / "assets" / "vivo-b1g2-poster.png"
OUT_DIR = ROOT / "assets" / "video"
OUT = OUT_DIR / "vivo-b1g2-commercial.mp4"

W, H = 1080, 1920
FPS = 30
DURATION = 11.0
BG = (8, 42, 28)

RNG = np.random.default_rng(42)


def ease_out_cubic(t: float) -> float:
    return 1.0 - (1.0 - t) ** 3


def ease_in_out_cubic(t: float) -> float:
    if t < 0.5:
        return 4 * t * t * t
    return 1 - (-2 * t + 2) ** 3 / 2


def ease_out_back(t: float, s: float = 1.6) -> float:
    return 1 + (s + 1) * (t - 1) ** 3 + s * (t - 1) ** 2


def clamp(v: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, v))


class PosterLayout:
    def __init__(self, poster: Image.Image):
        scale = W / poster.width
        self.pw = W
        self.ph = int(poster.height * scale)
        self.poster = poster.resize((self.pw, self.ph), Image.Resampling.LANCZOS)
        self.ox = 0
        self.oy = (H - self.ph) // 2

    def region(self, y0: float, y1: float, x0: float = 0.0, x1: float = 1.0) -> tuple[int, int, int, int]:
        return (
            int(self.ox + x0 * self.pw),
            int(self.oy + y0 * self.ph),
            int(self.ox + x1 * self.pw),
            int(self.oy + y1 * self.ph),
        )


def make_particles(n: int) -> dict:
    return {
        "x": RNG.random(n),
        "y": RNG.random(n),
        "spd": RNG.uniform(0.15, 0.9, n),
        "size": RNG.uniform(1.0, 3.5, n),
        "phase": RNG.random(n) * math.tau,
        "hue": RNG.choice([0, 1, 2], n, p=[0.5, 0.35, 0.15]),
    }


PARTICLES = make_particles(180)
CONFETTI = {
    "x": RNG.uniform(0.05, 0.95, 55),
    "y0": RNG.uniform(-0.1, 0.2, 55),
    "spd": RNG.uniform(0.25, 0.7, 55),
    "hue": RNG.choice([0, 1, 2, 3], 55, p=[0.3, 0.3, 0.25, 0.15]),
    "size": RNG.uniform(3, 8, 55),
}
STREAKS = {
    "y": RNG.uniform(0.05, 0.95, 12),
    "spd": RNG.uniform(0.4, 1.2, 12),
    "phase": RNG.random(12),
    "w": RNG.uniform(120, 280, 12),
}


def draw_particles(canvas: np.ndarray, t: float, intensity: float = 1.0) -> None:
    h, w = canvas.shape[:2]
    for i in range(len(PARTICLES["x"])):
        hue = PARTICLES["hue"][i]
        if hue == 0:
            col = np.array([40, 255, 120], dtype=np.float32)
        elif hue == 1:
            col = np.array([255, 220, 80], dtype=np.float32)
        else:
            col = np.array([255, 255, 255], dtype=np.float32)
        px = int((PARTICLES["x"][i] + math.sin(t * PARTICLES["spd"][i] + PARTICLES["phase"][i]) * 0.02) * w) % w
        py = int(((PARTICLES["y"][i] - t * PARTICLES["spd"][i] * 0.04) % 1.0) * h)
        alpha = 0.35 * intensity * (0.5 + 0.5 * math.sin(t * 3 + PARTICLES["phase"][i]))
        r = max(1, int(PARTICLES["size"][i]))
        y0, y1 = max(0, py - r), min(h, py + r + 1)
        x0, x1 = max(0, px - r), min(w, px + r + 1)
        canvas[y0:y1, x0:x1] = np.clip(
            canvas[y0:y1, x0:x1].astype(np.float32) + col * alpha, 0, 255
        ).astype(np.uint8)


def draw_streaks(canvas: np.ndarray, t: float, intensity: float = 1.0) -> None:
    h, w = canvas.shape[:2]
    overlay = np.zeros_like(canvas, dtype=np.float32)
    for i in range(len(STREAKS["y"])):
        y = int(STREAKS["y"][i] * h)
        x = int(((t * STREAKS["spd"][i] + STREAKS["phase"][i]) % 1.4 - 0.2) * w)
        sw = int(STREAKS["w"][i])
        x0, x1 = max(0, x), min(w, x + sw)
        if x1 <= x0:
            continue
        grad = np.linspace(0, 1, x1 - x0, dtype=np.float32)
        grad = np.sin(grad * math.pi) ** 2
        alpha = grad * 0.22 * intensity
        color = np.array([60, 255, 140], dtype=np.float32)
        band = overlay[max(0, y - 2) : min(h, y + 3), x0:x1]
        band[:] = band + color[None, None, :] * alpha[:, None]
    canvas[:] = np.clip(canvas.astype(np.float32) + overlay, 0, 255).astype(np.uint8)


def draw_confetti(canvas: np.ndarray, t: float, intensity: float = 1.0) -> None:
    h, w = canvas.shape[:2]
    colors = [
        np.array([255, 220, 50], dtype=np.float32),
        np.array([255, 60, 50], dtype=np.float32),
        np.array([50, 255, 120], dtype=np.float32),
        np.array([255, 255, 255], dtype=np.float32),
    ]
    for i in range(len(CONFETTI["x"])):
        px = int(CONFETTI["x"][i] * w)
        py = int((CONFETTI["y0"][i] + t * CONFETTI["spd"][i] * 0.12) % 1.1 * h)
        col = colors[CONFETTI["hue"][i]]
        s = int(CONFETTI["size"][i])
        y0, y1 = max(0, py - s), min(h, py + s + 1)
        x0, x1 = max(0, px - s // 2), min(w, px + s // 2 + 1)
        canvas[y0:y1, x0:x1] = np.clip(
            canvas[y0:y1, x0:x1].astype(np.float32) + col * 0.5 * intensity, 0, 255
        ).astype(np.uint8)


def radial_glow(canvas: np.ndarray, cx: int, cy: int, radius: int, color: tuple, strength: float) -> None:
    h, w = canvas.shape[:2]
    y0, y1 = max(0, cy - radius), min(h, cy + radius)
    x0, x1 = max(0, cx - radius), min(w, cx + radius)
    yy, xx = np.mgrid[y0:y1, x0:x1]
    dist = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    mask = np.clip(1 - dist / radius, 0, 1) ** 2
    col = np.array(color, dtype=np.float32)
    patch = canvas[y0:y1, x0:x1].astype(np.float32)
    patch += col[None, None, :] * mask[:, :, None] * strength
    canvas[y0:y1, x0:x1] = np.clip(patch, 0, 255).astype(np.uint8)


def shine_sweep(canvas: np.ndarray, t: float, region: tuple[int, int, int, int], width_frac: float = 0.35) -> None:
    x0, y0, x1, y1 = region
    rw, rh = x1 - x0, y1 - y0
    if rw <= 0 or rh <= 0:
        return
    sweep_x = x0 + int((t % 1.0) * (rw + int(rw * width_frac))) - int(rw * width_frac * 0.5)
    sw = max(30, int(rw * width_frac))
    overlay = np.zeros((rh, rw, 3), dtype=np.float32)
    for x in range(rw):
        lx = x + x0 - sweep_x
        if 0 <= lx < sw:
            a = math.sin(lx / sw * math.pi) ** 2 * 0.55
            overlay[:, x] += np.array([255, 245, 200]) * a
    canvas[y0:y1, x0:x1] = np.clip(
        canvas[y0:y1, x0:x1].astype(np.float32) + overlay, 0, 255
    ).astype(np.uint8)


def flash(canvas: np.ndarray, strength: float, tint: tuple = (255, 240, 180)) -> None:
    if strength <= 0:
        return
    col = np.array(tint, dtype=np.float32) * strength
    canvas[:] = np.clip(canvas.astype(np.float32) + col, 0, 255).astype(np.uint8)


def pulse_region(canvas: np.ndarray, region: tuple[int, int, int, int], t: float, color=(50, 255, 120)) -> None:
    x0, y0, x1, y1 = region
    pulse = 0.15 + 0.2 * (0.5 + 0.5 * math.sin(t * math.tau * 2))
    patch = canvas[y0:y1, x0:x1].astype(np.float32)
    col = np.array(color, dtype=np.float32)
    patch += col * pulse
    canvas[y0:y1, x0:x1] = np.clip(patch, 0, 255).astype(np.uint8)


def vignette(canvas: np.ndarray, strength: float = 0.35) -> None:
    h, w = canvas.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    cx, cy = w / 2, h / 2
    dist = np.sqrt(((xx - cx) / w) ** 2 + ((yy - cy) / h) ** 2)
    mask = 1 - np.clip(dist * 1.35, 0, 1) * strength
    canvas[:] = (canvas.astype(np.float32) * mask[:, :, None]).astype(np.uint8)


def render_poster_layer(
    layout: PosterLayout,
    zoom: float,
    focus_x: float,
    focus_y: float,
    rise: float = 0.0,
) -> Image.Image:
    """Zoom toward normalized focus point; rise offsets hero vertically."""
    pw, ph = layout.pw, layout.ph
    zw, zh = int(pw * zoom), int(ph * zoom)
    enlarged = layout.poster.resize((zw, zh), Image.Resampling.LANCZOS)
    cx = int(focus_x * zw - W / 2)
    cy = int(focus_y * zh - H / 2) + int(rise)
    cx = clamp(cx, 0, max(0, zw - W))
    cy = clamp(cy, 0, max(0, zh - H))
    crop = enlarged.crop((cx, cy, cx + W, cy + H))
    if crop.size != (W, H):
        bg = Image.new("RGB", (W, H), BG)
        ox = (W - crop.width) // 2
        oy = (H - crop.height) // 2
        bg.paste(crop, (ox, oy))
        return bg
    return crop


def scene_camera(t_sec: float) -> tuple[float, float, float, float]:
    """Return zoom, focus_x, focus_y, rise for elapsed seconds."""
    if t_sec < 2:
        p = ease_out_cubic(t_sec / 2)
        return 1.05 + 0.18 * p, 0.5, 0.12, 0
    if t_sec < 4:
        p = ease_out_back(clamp((t_sec - 2) / 2))
        return 1.18 + 0.08 * p, 0.5, 0.26, 0
    if t_sec < 6:
        p = ease_in_out_cubic(clamp((t_sec - 4) / 2))
        return 1.22 - 0.04 * p, 0.5 + 0.04 * math.sin(p * math.pi), 0.48 - 0.06 * p, -30 * (1 - p)
    if t_sec < 8:
        p = ease_in_out_cubic(clamp((t_sec - 6) / 2))
        return 1.16 + 0.06 * p, 0.5, 0.68 + 0.04 * p, 0
    if t_sec < 10:
        p = ease_in_out_cubic(clamp((t_sec - 8) / 2))
        return 1.18 + 0.05 * p, 0.5, 0.78 + 0.06 * p, 0
    p = ease_in_out_cubic(clamp((t_sec - 10) / 2))
    return 1.24 + 0.08 * p, 0.5, 0.55 - 0.1 * p, 0


def render_frame(layout: PosterLayout, frame_idx: int) -> np.ndarray:
    t_sec = frame_idx / FPS
    t_norm = t_sec / DURATION
    zoom, fx, fy, rise = scene_camera(t_sec)

    base = render_poster_layer(layout, zoom, fx, fy, rise)
    canvas = np.array(base, dtype=np.uint8)

    # Dark green ambient underlay pulse
    ambient = 0.04 + 0.03 * math.sin(t_sec * 2.5)
    canvas = np.clip(canvas.astype(np.float32) + np.array([0, ambient * 40, ambient * 20]), 0, 255).astype(np.uint8)

    scene = int(t_sec // 2)  # 0..5

    if scene == 0:
        p = clamp(t_sec / 2)
        flash(canvas, 0.45 * max(0, 1 - p * 3) * (0.5 + 0.5 * math.sin(t_sec * 20)))
        cx, cy = layout.region(0.35, 0.55, 0.2, 0.8)[0] + int(0.3 * layout.pw), layout.region(0.05, 0.22)[1] + int(0.08 * layout.ph)
        radial_glow(canvas, cx, cy, int(220 * ease_out_cubic(p)), (255, 60, 40), 0.35)
        radial_glow(canvas, W // 2, int(H * 0.14), int(280 * p), (255, 210, 60), 0.28)
        draw_streaks(canvas, t_sec * 1.8, 0.8 + 0.4 * p)
        draw_particles(canvas, t_sec * 2.2, 0.9)

    elif scene == 1:
        p = clamp((t_sec - 2) / 2)
        punch = ease_out_back(p)
        scale_pulse = 1 + 0.06 * max(0, math.sin(p * math.pi * 2))
        flash(canvas, 0.12 * max(0, math.sin(p * math.pi * 3)))
        r_buy = layout.region(0.18, 0.34, 0.08, 0.92)
        shine_sweep(canvas, p * 1.2, r_buy)
        cx1 = layout.region(0.22, 0.34, 0.38, 0.46)[0] + int(0.04 * layout.pw)
        cx2 = layout.region(0.22, 0.34, 0.54, 0.62)[0] + int(0.04 * layout.pw)
        cy = (layout.region(0.22, 0.34)[1] + layout.region(0.22, 0.34)[3]) // 2
        radial_glow(canvas, cx1, cy, int(90 * scale_pulse * punch), (255, 200, 50), 0.45 * punch)
        radial_glow(canvas, cx2, cy, int(90 * scale_pulse * punch), (255, 200, 50), 0.45 * punch)
        draw_streaks(canvas, t_sec * 1.4, 1.0)
        draw_confetti(canvas, t_sec - 2, 0.85 * punch)
        draw_particles(canvas, t_sec * 1.6, 0.7)

    elif scene == 2:
        p = clamp((t_sec - 4) / 2)
        r_left = layout.region(0.34, 0.62, 0.02, 0.48)
        r_right = layout.region(0.34, 0.62, 0.52, 0.98)
        r_free = layout.region(0.58, 0.68, 0.55, 0.95)
        pulse_region(canvas, r_left, t_sec * 2, (40, 255, 100))
        if p > 0.25:
            gift_p = ease_out_cubic(clamp((p - 0.25) / 0.75))
            cx = (r_right[0] + r_right[2]) // 2
            cy = (r_right[1] + r_right[3]) // 2
            radial_glow(canvas, cx, cy, int(160 * gift_p), (255, 190, 50), 0.5 * gift_p)
            flash(canvas, 0.18 * max(0, 1 - gift_p * 2))
        if p > 0.55:
            shine_sweep(canvas, clamp((p - 0.55) / 0.45) * 1.5, r_free)
        draw_particles(canvas, t_sec, 0.6)
        draw_streaks(canvas, t_sec * 0.9, 0.5)

    elif scene == 3:
        p = clamp((t_sec - 6) / 2)
        benefits = [
            layout.region(0.66, 0.74, 0.02, 0.34),
            layout.region(0.66, 0.74, 0.34, 0.66),
            layout.region(0.66, 0.74, 0.66, 0.98),
        ]
        for i, reg in enumerate(benefits):
            start = i * 0.28
            if p > start:
                bp = ease_out_cubic(clamp((p - start) / 0.35))
                pulse_region(canvas, reg, t_sec * 2 + i, (45, 255, 110))
                shine_sweep(canvas, bp, reg, 0.45)
        draw_particles(canvas, t_sec * 0.8, 0.45)

    elif scene == 4:
        p = clamp((t_sec - 8) / 2)
        badges = [
            layout.region(0.74, 0.82, 0.0, 0.25),
            layout.region(0.74, 0.82, 0.25, 0.5),
            layout.region(0.74, 0.82, 0.5, 0.75),
            layout.region(0.74, 0.82, 0.75, 1.0),
        ]
        for i, reg in enumerate(badges):
            start = i * 0.18
            if p > start:
                bp = ease_out_cubic(clamp((p - start) / 0.3))
                pulse_region(canvas, reg, t_sec + i * 0.5, (35, 220, 90))
                radial_glow(
                    canvas,
                    (reg[0] + reg[2]) // 2,
                    (reg[1] + reg[3]) // 2,
                    int(50 * bp),
                    (255, 215, 80),
                    0.2 * bp,
                )
        draw_particles(canvas, t_sec * 0.6, 0.35)

    else:
        p = clamp((t_sec - 10) / 2)
        r_urgent = layout.region(0.82, 0.9, 0.05, 0.95)
        r_store = layout.region(0.9, 0.98, 0.02, 0.55)
        flash(canvas, 0.15 * (0.5 + 0.5 * math.sin(t_sec * 12)) * p)
        pulse_region(canvas, r_urgent, t_sec * 4, (255, 220, 60))
        shine_sweep(canvas, p * 1.3, r_urgent, 0.4)
        pulse_region(canvas, r_store, t_sec * 2, (50, 255, 100))
        radial_glow(canvas, W // 2, int(H * 0.55), int(320 * p), (30, 255, 100), 0.22 * p)
        draw_streaks(canvas, t_sec * 1.1, 0.8)
        draw_particles(canvas, t_sec * 1.4, 0.85)

    vignette(canvas, 0.28)
    return canvas


def main() -> None:
    if not POSTER.exists():
        raise FileNotFoundError(f"Poster not found: {POSTER}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    poster = Image.open(POSTER).convert("RGB")
    layout = PosterLayout(poster)
    total = int(DURATION * FPS)
    frames = [render_frame(layout, i) for i in range(total)]
    imageio.mimsave(
        OUT,
        frames,
        fps=FPS,
        codec="libx264",
        quality=8,
        pixelformat="yuv420p",
        macro_block_size=1,
    )
    print(f"Wrote {OUT} ({len(frames)} frames, {len(frames) / FPS:.1f}s)")


if __name__ == "__main__":
    main()
