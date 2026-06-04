"""Elegant cinematic section — clean shell; premium cards like template studio."""
import re
from pathlib import Path

CINEMATIC_MARKER = "/* ═══ ELEGANT CINEMATIC — refined shell, premium cards ═══ */"

CINEMATIC_OVERRIDE = """
/* ═══ ELEGANT CINEMATIC — refined shell, premium cards ═══ */
.h-scroll-section {
  position: relative !important;
  overflow: visible !important;
  padding: 0 0 4rem !important;
  margin-bottom: 0 !important;
}
.cinematic-inner {
  position: relative !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto !important;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  isolation: auto !important;
  overflow: visible !important;
}
.cinematic-inner::before,
.cinematic-glow,
.h-card-glow {
  display: none !important;
}
.h-scroll-header {
  position: relative !important;
  z-index: 1 !important;
  text-align: center !important;
  margin-bottom: 2rem !important;
}
.h-scroll-header .section-kicker {
  display: inline-flex !important;
  align-items: center !important;
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important;
  padding: 0.35rem 0.85rem !important;
  margin-bottom: 0.85rem !important;
  box-shadow: none !important;
}
.h-scroll-header .section-kicker::before {
  display: none !important;
}
.h-scroll-header h2 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  line-height: 1.12 !important;
  margin-bottom: 0.5rem !important;
  text-shadow: none !important;
}
.h-scroll-header p {
  color: #64748b !important;
  max-width: 520px !important;
  margin: 0 auto !important;
  font-size: 0.95rem !important;
  line-height: 1.65 !important;
}
.h-scroll-wrap {
  position: relative !important;
  z-index: 1 !important;
  display: grid !important;
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
  gap: clamp(0.65rem, 1vw, 0.85rem) !important;
  align-items: end !important;
  overflow: visible !important;
  padding: 0 !important;
  margin-top: 0.5rem !important;
}
.h-scroll-wrap::before {
  display: none !important;
}
/* Premium cards — aligned with template studio */
.h-card {
  position: relative !important;
  width: 100% !important;
  border-radius: 22px !important;
  overflow: hidden !important;
  background: #0f172a !important;
  border: 2px solid rgba(37, 99, 235, 0.2) !important;
  box-shadow: 0 16px 44px rgba(37, 99, 235, 0.12) !important;
  cursor: pointer !important;
  isolation: isolate !important;
  transition: border-color 0.35s ease, box-shadow 0.35s ease !important;
  aspect-ratio: 3 / 4 !important;
}
.h-card:nth-child(2) {
  aspect-ratio: 3 / 3.55 !important;
  margin-bottom: 0.75rem !important;
}
.h-card:nth-child(3) {
  aspect-ratio: 3 / 4.35 !important;
}
.h-card:nth-child(4) {
  aspect-ratio: 3 / 3.6 !important;
  margin-bottom: 0.65rem !important;
}
.h-card:nth-child(5) {
  aspect-ratio: 3 / 4 !important;
}
.h-card::after {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  height: 3px !important;
  background: linear-gradient(90deg, #2563eb, #60a5fa, #818cf8) !important;
  z-index: 6 !important;
  opacity: 0.6 !important;
  transition: opacity 0.35s ease !important;
  pointer-events: none !important;
}
.h-card:hover,
.h-card:focus-visible {
  border-color: rgba(37, 99, 235, 0.4) !important;
  box-shadow: 0 20px 48px rgba(15, 23, 42, 0.22) !important;
  outline: none !important;
}
.h-card:hover::after,
.h-card:focus-visible::after {
  opacity: 1 !important;
}
.h-card-media {
  position: absolute !important;
  inset: 0 !important;
  overflow: hidden !important;
  z-index: 0 !important;
}
.h-card-media::after {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(180deg, rgba(15, 23, 42, 0.42) 0%, transparent 32%),
    linear-gradient(0deg, rgba(15, 23, 42, 0.92) 0%, rgba(15, 23, 42, 0.42) 46%, transparent 72%) !important;
  pointer-events: none !important;
  z-index: 2 !important;
}
.h-card-media img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  display: block !important;
  filter: saturate(1.08) contrast(1.06) !important;
  transition: transform 0.65s cubic-bezier(0.22, 1, 0.36, 1) !important;
}
.h-card:hover .h-card-media img,
.h-card:focus-visible .h-card-media img {
  transform: scale(1.06) !important;
}
.h-card-num {
  position: absolute !important;
  top: 0.7rem !important;
  right: 0.8rem !important;
  z-index: 6 !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.5rem, 2vw, 2rem) !important;
  font-weight: 700 !important;
  line-height: 1 !important;
  color: rgba(255, 255, 255, 0.38) !important;
  text-shadow: 0 2px 10px rgba(15, 23, 42, 0.75) !important;
  pointer-events: none !important;
}
.h-card-content {
  position: absolute !important;
  inset: 0 !important;
  z-index: 4 !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-end !important;
  padding: 1rem 0.95rem !important;
  background: transparent !important;
  pointer-events: none !important;
}
.h-card-tag {
  position: absolute !important;
  top: 10px !important;
  left: 10px !important;
  z-index: 5 !important;
  display: inline-block !important;
  width: fit-content !important;
  margin-bottom: 0 !important;
  padding: 0.28rem 0.55rem !important;
  border-radius: 999px !important;
  font-size: 0.58rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  color: #fff !important;
  background: rgba(37, 99, 235, 0.82) !important;
  border: 1px solid rgba(255, 255, 255, 0.28) !important;
  box-shadow: none !important;
}
.h-card h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(0.92rem, 1.05vw, 1.08rem) !important;
  font-weight: 600 !important;
  color: #fff !important;
  margin-bottom: 0.3rem !important;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.35) !important;
  line-height: 1.2 !important;
  transition: color 0.35s ease !important;
}
.h-card:hover h3,
.h-card:focus-visible h3 {
  color: #dbeafe !important;
}
.h-card p {
  font-size: clamp(0.72rem, 0.8vw, 0.82rem) !important;
  color: rgba(255, 255, 255, 0.82) !important;
  line-height: 1.5 !important;
  margin: 0 !important;
}
.h-card-hint {
  position: absolute !important;
  bottom: 0.95rem !important;
  right: 0.95rem !important;
  z-index: 5 !important;
  font-size: 0.58rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.1em !important;
  text-transform: uppercase !important;
  background: rgba(255, 255, 255, 0.92) !important;
  color: #2563eb !important;
  padding: 0.32rem 0.6rem !important;
  border-radius: 8px !important;
  border: 1px solid rgba(37, 99, 235, 0.2) !important;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15) !important;
  opacity: 0 !important;
  animation: none !important;
  transition: opacity 0.35s ease !important;
  pointer-events: none !important;
}
.h-card:hover .h-card-hint,
.h-card:focus-visible .h-card-hint {
  opacity: 1 !important;
  color: #2563eb !important;
}
@media (max-width: 1100px) {
  .h-scroll-wrap {
    grid-template-columns: repeat(6, minmax(0, 1fr)) !important;
    gap: 0.75rem !important;
  }
  .h-card {
    grid-column: span 2 !important;
    margin-bottom: 0 !important;
    aspect-ratio: 3 / 4 !important;
  }
  .h-card:nth-child(4) {
    grid-column: 2 / span 2 !important;
  }
  .h-card:nth-child(5) {
    grid-column: 4 / span 2 !important;
  }
}
@media (max-width: 640px) {
  .cinematic-inner {
    width: calc(100% - 1.5rem) !important;
    padding: 2.5rem 1rem 2rem !important;
    border-radius: 10px !important;
  }
  .h-scroll-wrap {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
  .h-card {
    grid-column: span 1 !important;
  }
  .h-card:nth-child(5) {
    grid-column: 1 / -1 !important;
    max-width: 280px !important;
    margin: 0 auto !important;
    width: 100% !important;
  }
}
"""

SHELL_DECOR = [
    '<div class="cinematic-glow cinematic-glow-a" aria-hidden="true"></div> ',
    '<div class="cinematic-glow cinematic-glow-b" aria-hidden="true"></div> ',
]
CARD_GLOW_RE = re.compile(r'<div class="h-card-glow" aria-hidden="true"></div>\s*')


def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if CINEMATIC_MARKER in text:
        start = text.index(CINEMATIC_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + CINEMATIC_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing cinematic override block")
    else:
        text = text.replace("</style>", CINEMATIC_OVERRIDE + "\n</style>", 1)
        print("Injected cinematic override block")

    for chunk in SHELL_DECOR:
        if chunk in text:
            text = text.replace(chunk, "", 1)
            print("Removed shell decor")

    new_text, n = CARD_GLOW_RE.subn("", text)
    if n:
        print(f"Removed glow FX from {n} h-cards")
    text = new_text

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)


if __name__ == "__main__":
    main()
