from pathlib import Path

OLD = Path(__file__).resolve().parent / "_hero_snippet.txt"
NEW = """<section class="hero" id="top"> <div class="hero-center"> <div class="hero-brand"> <div class="hero-brand-stack"> <span class="hero-brand-letters" aria-hidden="true"> <span class="hero-brand-letter">E</span> <span class="hero-brand-letter">M</span> <span class="hero-brand-letter">A</span> <span class="hero-brand-letter">A</span> <span class="hero-brand-letter">V</span> <span class="hero-brand-letter">Y</span> </span> </div> <p class="hero-tagline">Call Intelligence</p> </div> <div class="hero-actions"> <button class="btn-magnetic btn-fill" type="button" data-open-demo>Try EMAAVY</button> </div> </div> <a href="#snapshots" class="hero-scroll-tag" id="heroScrollCue" aria-label="Scroll to platform overview"> <span class="hero-scroll-line" aria-hidden="true"></span> <span class="hero-scroll-label">Explore platform</span> </a> </section>"""

HERO_CSS_MARKER = "/* ═══ ELEGANT HERO — refined, no glow ═══ */"

CENTER_CSS = """
/* ═══ ELEGANT HERO — refined, no glow ═══ */
.hero {
  background: #ffffff !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  min-height: min(88vh, 820px) !important;
  padding: calc(var(--masthead-h-compact) + 4rem) clamp(1.5rem, 4vw, 3rem) 5.5rem !important;
  gap: 0 !important;
  overflow: visible !important;
  position: relative !important;
  grid-template-columns: unset !important;
}
.hero::before,
.hero-glow-layer,
.hero-visual,
.hero-visual::before,
.hero-visual::after,
.hero-gallery,
.hero-gallery-bridge {
  display: none !important;
}
.hero-center {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  width: 100% !important;
  max-width: 640px !important;
  margin: 0 auto !important;
  flex: 1 !important;
  z-index: 5 !important;
}
.hero-brand {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  margin-bottom: 2.25rem !important;
}
.hero-brand-stack {
  position: relative !important;
  display: inline-flex !important;
  line-height: 1 !important;
  margin-bottom: 0.85rem !important;
}
.hero-brand-letters {
  display: inline-flex !important;
  justify-content: center !important;
  flex-wrap: wrap !important;
  gap: 0 !important;
}
.hero-brand-letter {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  font-size: clamp(3.25rem, 10vw, 5.5rem) !important;
  letter-spacing: -0.06em !important;
  display: inline-block !important;
  background: linear-gradient(180deg, #1e40af 0%, #2563eb 50%, #3b82f6 100%) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  color: transparent !important;
  filter: none !important;
  animation: none !important;
}
.hero-tagline {
  margin: 0 !important;
  font-size: clamp(0.65rem, 1.8vw, 0.78rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.42em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  padding-left: 0.42em !important;
}
.hero-actions {
  display: flex !important;
  justify-content: center !important;
  animation: none !important;
  opacity: 1 !important;
  gap: 0 !important;
  margin: 0 !important;
}
.hero-actions .btn-magnetic {
  border-radius: 6px !important;
  clip-path: none !important;
  padding: 0.9rem 2rem !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.02em !important;
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
    min-height: min(82vh, 720px) !important;
    padding-bottom: 6rem !important;
  }
  .hero-scroll-tag {
    bottom: 1rem !important;
  }
}
@media (max-width: 560px) {
  .hero-tagline {
    letter-spacing: 0.32em !important;
  }
}
"""

def main():
    html_path = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
    text = html_path.read_text(encoding="utf-8")
    old = OLD.read_text(encoding="utf-8").strip()
    if old not in text:
        raise SystemExit("Hero snippet not found in HTML")
    text = text.replace(old, NEW.strip(), 1)
    start = text.index(HERO_CSS_MARKER)
    end = text.index("/* ═══ ELEGANT SIGNAL", start)
    text = text[:start] + CENTER_CSS.strip() + "\n\n" + text[end:]
    html_path.write_text(text, encoding="utf-8")
    print("Hero centered:", html_path.name)


if __name__ == "__main__":
    main()
