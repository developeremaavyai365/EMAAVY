"""Restore left hero copy + Try EMAAVY panel on the right."""
from pathlib import Path

HTML_PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

OLD_HERO = Path(__file__).resolve().parent / "_hero_current.html"
OLD_HERO = OLD_HERO.read_text(encoding="utf-8").strip()

NEW_HERO = """<section class="hero" id="top"> <div class="hero-copy"> <div class="hero-headline"> <p class="hero-headline-kicker"><span class="hero-headline-kicker-line" aria-hidden="true"></span><span>Every call. Fully understood.</span><span class="hero-headline-kicker-line" aria-hidden="true"></span></p> <h1 class="hero-title" aria-label="Decode every call"> <span class="line line-decode"><span class="inner">Decode</span></span> <span class="line line-every"><span class="inner outline">every</span></span> <span class="line line-call"><span class="inner glow">call<span class="hero-title-mark" aria-hidden="true">.</span></span></span> </h1> <p class="hero-pitch">Record, transcribe, and act on every call—<strong>one enterprise platform</strong> built so your team never misses what matters.</p> </div> </div> <div class="hero-visual" id="heroVisual"> <aside class="hero-try-panel" aria-labelledby="heroTryTitle"> <p class="hero-try-kicker">Experience the platform</p> <h2 class="hero-try-title" id="heroTryTitle">Try EMAAVY</h2> <p class="hero-try-desc">Run a sample call through transcription, intent detection, and workflow triggers—no setup required.</p> <ul class="hero-try-points"> <li>Real-time transcript preview</li> <li>Sentiment and intent scoring</li> <li>Export insights to your stack</li> </ul> <button class="btn-magnetic btn-fill hero-try-btn" type="button" data-open-demo>Try EMAAVY</button> </aside> </div> <a href="#snapshots" class="hero-scroll-tag" id="heroScrollCue" aria-label="Scroll to platform overview"> <span class="hero-scroll-line" aria-hidden="true"></span> <span class="hero-scroll-label">Explore platform</span> </a> </section>"""

CSS_HERO_OPEN_OLD = """.hero {
  --hero-brand-size: clamp(2.35rem, 5.8vmin, 4.15rem);
  --hero-title-size: clamp(3.35rem, 10.5vmin, 6.85rem);
  --hero-pitch-size: clamp(1.08rem, 2.45vmin, 1.32rem);
  --hero-badge-size: clamp(0.8rem, 1.65vmin, 0.98rem);
  --hero-tagline-size: clamp(0.8rem, 1.75vmin, 1rem);
  --hero-btn-size: clamp(1.02rem, 2.05vmin, 1.18rem);
  --hero-stack-gap: clamp(0.7rem, 2.6vmin, 1.65rem);
  background: #ffffff !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  text-align: center !important;
  box-sizing: border-box !important;
  height: 100dvh !important;
  min-height: 100dvh !important;
  max-height: 100dvh !important;
  padding: calc(var(--masthead-h-compact) + 0.75rem) clamp(1.25rem, 4vw, 2.5rem) 1.25rem !important;
  gap: 0 !important;
  overflow: hidden !important;
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
  max-width: min(880px, 96vw) !important;
  max-height: calc(100dvh - var(--masthead-h-compact) - 1rem) !important;
  margin: 0 auto !important;
  flex: 1 1 auto !important;
  min-height: 0 !important;
  gap: var(--hero-stack-gap) !important;
  z-index: 5 !important;
}"""

CSS_HERO_OPEN_NEW = """.hero {
  --hero-title-size: clamp(2.85rem, 6.5vw, 5.75rem);
  --hero-pitch-size: clamp(1rem, 1.75vw, 1.2rem);
  --hero-btn-size: clamp(1rem, 1.6vw, 1.12rem);
  background: #ffffff !important;
  display: grid !important;
  grid-template-columns: 1fr 1.05fr !important;
  gap: clamp(1.75rem, 4vw, 3rem) !important;
  align-items: center !important;
  justify-items: stretch !important;
  text-align: left !important;
  box-sizing: border-box !important;
  min-height: min(100vh, 100dvh) !important;
  height: auto !important;
  max-height: none !important;
  padding: calc(var(--masthead-h-compact) + 2rem) clamp(1.5rem, 4vw, 3rem) clamp(2.5rem, 5vw, 3.5rem) !important;
  overflow: visible !important;
  position: relative !important;
}
@media (max-width: 1024px) {
  .hero {
    grid-template-columns: 1fr !important;
    align-items: start !important;
    min-height: auto !important;
    padding-bottom: 4rem !important;
  }
}
.hero::before,
.hero-glow-layer {
  display: none !important;
}
.hero-copy {
  padding-bottom: 0 !important;
  max-width: 560px !important;
  width: 100% !important;
  position: relative !important;
  z-index: 5 !important;
}
.hero-center {
  display: none !important;
}"""

CSS_HEADLINE_ALIGN = """  align-items: center !important;
  justify-content: center !important;
  padding: clamp(0.85rem, 2vmin, 1.35rem) clamp(1rem, 3vw, 1.75rem) clamp(0.9rem, 2vmin, 1.25rem) !important;
  text-align: center !important;"""

CSS_HEADLINE_ALIGN_NEW = """  align-items: flex-start !important;
  justify-content: flex-start !important;
  padding: clamp(1rem, 2.2vw, 1.5rem) clamp(1.15rem, 2.5vw, 1.65rem) clamp(1rem, 2vw, 1.35rem) !important;
  text-align: left !important;"""

CSS_KICKER = """  justify-content: center !important;"""

CSS_KICKER_NEW = """  justify-content: flex-start !important;"""

CSS_TITLE_ALIGN = """  text-align: center !important;
  width: 100% !important;"""

CSS_TITLE_ALIGN_NEW = """  text-align: left !important;
  width: 100% !important;"""

CSS_PITCH_ALIGN = """  text-align: center !important;
}"""

CSS_PITCH_ALIGN_NEW = """  text-align: left !important;
  max-width: 28rem !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
}"""

CSS_TRY_PANEL = """
/* Try EMAAVY — right column */
.hero-visual {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  position: relative !important;
  height: auto !important;
  min-height: min(420px, 52vh) !important;
  width: 100% !important;
  z-index: 4 !important;
}
.hero-try-panel {
  width: 100% !important;
  max-width: 440px !important;
  margin: 0 auto !important;
  padding: clamp(1.35rem, 3vw, 2rem) !important;
  border-radius: 20px !important;
  border: 1px solid #e2e8f0 !important;
  background: linear-gradient(165deg, #ffffff 0%, #f8fafc 45%, #eff6ff 100%) !important;
  box-shadow:
    0 1px 2px rgba(15, 23, 42, 0.04),
    0 20px 48px -16px rgba(30, 64, 175, 0.18) !important;
  text-align: left !important;
}
.hero-try-kicker {
  margin: 0 0 0.65rem !important;
  font-size: 0.68rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.hero-try-title {
  margin: 0 0 0.75rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.85rem, 4vw, 2.5rem) !important;
  font-weight: 700 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.05 !important;
  color: #0f172a !important;
  background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 55%, #3b82f6 100%) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}
.hero-try-desc {
  margin: 0 0 1.15rem !important;
  font-size: clamp(0.95rem, 1.6vw, 1.05rem) !important;
  line-height: 1.6 !important;
  color: #475569 !important;
}
.hero-try-points {
  margin: 0 0 1.5rem !important;
  padding: 0 !important;
  list-style: none !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.55rem !important;
}
.hero-try-points li {
  position: relative !important;
  padding-left: 1.35rem !important;
  font-size: 0.9rem !important;
  color: #334155 !important;
  line-height: 1.45 !important;
}
.hero-try-points li::before {
  content: '' !important;
  position: absolute !important;
  left: 0 !important;
  top: 0.45em !important;
  width: 7px !important;
  height: 7px !important;
  border-radius: 50% !important;
  background: #2563eb !important;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15) !important;
}
.hero-try-btn {
  width: 100% !important;
  min-width: 0 !important;
  border-radius: 8px !important;
  clip-path: none !important;
  padding: 0.95rem 1.5rem !important;
  font-size: var(--hero-btn-size) !important;
  font-weight: 600 !important;
  background: #1e40af !important;
  color: #fff !important;
  box-shadow: none !important;
  transition: background 0.2s !important;
}
.hero-try-btn:hover {
  background: #1e3a8a !important;
}
.hero-actions {
  display: none !important;
}
.hero-badge,
.hero-brand {
  display: none !important;
}
@media (max-width: 1024px) {
  .hero-visual {
    min-height: 0 !important;
    padding-top: 0.5rem !important;
  }
  .hero-try-panel {
    max-width: 100% !important;
  }
}
"""


def main():
    text = HTML_PATH.read_text(encoding="utf-8")

    if OLD_HERO not in text:
        raise SystemExit("Current hero block not found — run _extract_hero.py first")

    text = text.replace(OLD_HERO, NEW_HERO, 1)

    if CSS_HERO_OPEN_OLD not in text:
        raise SystemExit("Hero CSS open block not found")
    text = text.replace(CSS_HERO_OPEN_OLD, CSS_HERO_OPEN_NEW, 1)

    for old, new in [
        (CSS_HEADLINE_ALIGN, CSS_HEADLINE_ALIGN_NEW),
        (CSS_KICKER, CSS_KICKER_NEW),
        (CSS_TITLE_ALIGN, CSS_TITLE_ALIGN_NEW),
        (CSS_PITCH_ALIGN, CSS_PITCH_ALIGN_NEW),
    ]:
        if old not in text:
            raise SystemExit(f"CSS fragment not found: {old[:40]}...")
        text = text.replace(old, new, 1)

    marker = ".hero-scroll-arrow {\n  display: none !important;\n}"
    if marker not in text:
        raise SystemExit("hero-scroll-arrow block not found")
    text = text.replace(marker, CSS_TRY_PANEL.strip() + "\n" + marker, 1)

    HTML_PATH.write_text(text, encoding="utf-8")
    print("Updated:", HTML_PATH.name)


if __name__ == "__main__":
    main()
