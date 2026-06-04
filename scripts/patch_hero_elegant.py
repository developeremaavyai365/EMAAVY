"""Inject elegant hero CSS override and clean hero markup."""
from pathlib import Path

HERO_MARKER = "/* ═══ ELEGANT HERO — refined, no glow ═══ */"

HERO_OVERRIDE = """
/* ═══ ELEGANT HERO — refined, no glow ═══ */
.hero {
  background: #ffffff !important;
  min-height: auto !important;
  padding: calc(var(--masthead-h-compact) + 3rem) clamp(1.5rem, 4vw, 3rem) 5rem !important;
  align-items: center !important;
  gap: clamp(2rem, 4vw, 4rem) !important;
  overflow: visible !important;
}
.hero::before,
.hero-glow-layer,
.hero-visual::before,
.hero-visual::after,
.hero-gallery-bridge {
  display: none !important;
}
.hero-copy {
  padding-bottom: 0 !important;
  max-width: 540px;
}
.hero-eyebrow {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.65rem !important;
  margin-bottom: 1.5rem !important;
  padding: 0.4rem 0.85rem 0.4rem 0.65rem !important;
  border-radius: 6px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  color: #64748b !important;
  font-size: 0.68rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  transition: border-color 0.2s, background 0.2s !important;
}
.hero-eyebrow::before {
  content: '' !important;
  width: 24px !important;
  height: 1px !important;
  background: #1e40af !important;
  box-shadow: none !important;
  border-radius: 0 !important;
}
.hero-eyebrow:hover {
  border-color: #cbd5e1 !important;
  box-shadow: none !important;
  transform: none !important;
}
.hero h1 {
  font-size: clamp(2.75rem, 5.5vw, 4.25rem) !important;
  line-height: 1.06 !important;
  letter-spacing: -0.03em !important;
  margin-bottom: 1.25rem !important;
  color: #0f172a !important;
}
.hero h1 .line {
  overflow: visible !important;
}
.hero h1 .inner {
  animation: none !important;
  transform: none !important;
  opacity: 1 !important;
}
.hero h1 .outline {
  -webkit-text-stroke: 0 !important;
  color: #64748b !important;
  opacity: 1 !important;
  text-shadow: none !important;
  font-weight: 500 !important;
}
.hero-copy:hover .hero h1 .outline {
  text-shadow: none !important;
}
.hero h1 .inner.glow,
.hero h1 .glow {
  background: none !important;
  -webkit-background-clip: unset !important;
  background-clip: unset !important;
  -webkit-text-fill-color: #1e40af !important;
  color: #1e40af !important;
  filter: none !important;
  text-shadow: none !important;
  animation: none !important;
}
.hero-desc {
  animation: none !important;
  opacity: 1 !important;
  color: #64748b !important;
  font-size: 1.05rem !important;
  max-width: 440px !important;
  line-height: 1.7 !important;
  margin-bottom: 2rem !important;
  text-shadow: none !important;
}
.hero-copy:hover .hero-desc {
  color: #475569 !important;
  text-shadow: none !important;
}
.hero-actions {
  animation: none !important;
  opacity: 1 !important;
  gap: 0.75rem !important;
}
.hero-actions .btn-magnetic {
  border-radius: 6px !important;
  clip-path: none !important;
  padding: 0.85rem 1.5rem !important;
  font-size: 0.875rem !important;
  font-weight: 600 !important;
  transition: background 0.2s, border-color 0.2s, color 0.2s !important;
}
.hero-actions .btn-fill {
  background: #1e40af !important;
  color: #fff !important;
  box-shadow: none !important;
  animation: none !important;
}
.hero-actions .btn-fill:hover {
  background: #1e3a8a !important;
  box-shadow: none !important;
}
.hero-actions .btn-line {
  border: 1px solid #e2e8f0 !important;
  background: #fff !important;
  color: #475569 !important;
  backdrop-filter: none !important;
}
.hero-actions .btn-line:hover {
  border-color: #cbd5e1 !important;
  color: #0f172a !important;
  background: #f8fafc !important;
  box-shadow: none !important;
}
.hero-visual {
  height: auto !important;
  min-height: 0 !important;
}
.hero-gallery {
  position: relative !important;
  top: auto !important;
  right: auto !important;
  transform: none !important;
  width: 100% !important;
  max-width: 460px !important;
  height: auto !important;
  min-height: 380px !important;
  padding: 0.5rem !important;
  border-radius: 12px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  gap: 0.5rem !important;
}
.float-card {
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
  box-shadow: none !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.float-card::before {
  display: none !important;
}
.float-card::after {
  background: linear-gradient(180deg, transparent 50%, rgba(15, 23, 42, 0.45) 100%) !important;
}
.float-card:hover {
  border-color: #cbd5e1 !important;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.08) !important;
}
.float-card .cap {
  border-radius: 4px !important;
  background: rgba(255, 255, 255, 0.96) !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  color: #475569 !important;
  font-size: 0.62rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.05em !important;
  padding: 0.35rem 0.65rem !important;
}
.float-card:hover .cap {
  border-color: #cbd5e1 !important;
  box-shadow: none !important;
}
.float-card-inner,
.fc-1 .float-card-inner,
.fc-2 .float-card-inner,
.fc-3 .float-card-inner {
  animation: none !important;
  transform: none !important;
}
.float-card:hover img {
  transform: scale(1.02) !important;
}
.hero-scroll-tag {
  position: absolute !important;
  bottom: 1.5rem !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.65rem !important;
  padding: 0.55rem 1rem !important;
  border-radius: 6px !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  backdrop-filter: none !important;
  font-size: 0.72rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  animation: none !important;
  opacity: 1 !important;
  transition: border-color 0.2s, color 0.2s, background 0.2s !important;
}
.hero-scroll-tag:hover {
  border-color: #cbd5e1 !important;
  color: #0f172a !important;
  background: #f8fafc !important;
  box-shadow: none !important;
  transform: translateX(-50%) !important;
}
.hero-scroll-line {
  width: 2px !important;
  height: 28px !important;
  background: #94a3b8 !important;
  box-shadow: none !important;
  animation: none !important;
  border-radius: 1px !important;
}
.hero-scroll-label {
  color: inherit !important;
  text-shadow: none !important;
}
.hero-scroll-arrow {
  display: none !important;
}
@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr !important;
    padding-bottom: 6rem !important;
  }
  .hero-gallery {
    max-width: 100% !important;
    min-height: 320px !important;
  }
  .hero-scroll-tag {
    bottom: 1rem !important;
  }
}
"""

GLOW_LAYER_HTML = '<div class="hero-glow-layer" aria-hidden="true"> <div class="hero-glow-blob hero-glow-blob-a"></div> <div class="hero-glow-blob hero-glow-blob-b"></div> <div class="hero-glow-blob hero-glow-blob-c"></div> </div> '


def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")

    if HERO_MARKER in text:
        start = text.index(HERO_MARKER)
        end = text.index("</style>", start)
        text = text[:start] + HERO_OVERRIDE.strip() + "\n" + text[end:]
        print("Updated existing hero override block")
    else:
        text = text.replace("</style>", HERO_OVERRIDE + "\n</style>", 1)
        print("Injected hero override block")

    if GLOW_LAYER_HTML in text:
        text = text.replace(GLOW_LAYER_HTML, "", 1)
        print("Removed hero-glow-layer markup")

    html_path.write_text(text, encoding="utf-8")
    print("Done:", html_path.name)


if __name__ == "__main__":
    main()
