"""Unify hero: one flowing layout, no separate cards."""
from pathlib import Path

HTML_PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

OLD_HERO = Path(__file__).resolve().parent / "_hero_current.html"
OLD_HERO = OLD_HERO.read_text(encoding="utf-8").strip()

NEW_HERO = """<section class="hero" id="top"> <div class="hero-inner"> <div class="hero-copy"> <p class="hero-kicker"><span class="hero-kicker-line" aria-hidden="true"></span><span>Every call. Fully understood.</span><span class="hero-kicker-line" aria-hidden="true"></span></p> <h1 class="hero-title" aria-label="Decode every call"> <span class="line line-decode"><span class="inner">Decode</span></span> <span class="line line-every"><span class="inner outline">every</span></span> <span class="line line-call"><span class="inner glow">call<span class="hero-title-mark" aria-hidden="true">.</span></span></span> </h1> <p class="hero-pitch">Record, transcribe, and act on every call—<strong>one enterprise platform</strong> built so your team never misses what matters.</p> </div> <div class="hero-aside" id="heroVisual"> <p class="hero-aside-eyebrow">Experience the platform</p> <h2 class="hero-aside-title" id="heroTryTitle">Try EMAAVY</h2> <p class="hero-aside-desc">Run a sample call through transcription, intent detection, and workflow triggers—no setup required.</p> <ul class="hero-aside-list"> <li>Real-time transcript preview</li> <li>Sentiment and intent scoring</li> <li>Export insights to your stack</li> </ul> <button class="btn-magnetic btn-fill hero-aside-btn" type="button" data-open-demo>Try EMAAVY</button> </div> </div> </section>"""

MARKER_START = "/* ═══ ELEGANT HERO — refined, no glow ═══ */"
MARKER_END = "/* ═══ ELEGANT SIGNAL — refined, no glow ═══ */"

NEW_CSS = """/* ═══ ELEGANT HERO — unified split, no cards ═══ */
.hero {
  --hero-title-size: clamp(2.75rem, 6.2vw, 5.5rem);
  --hero-pitch-size: clamp(1rem, 1.7vw, 1.18rem);
  --hero-btn-size: clamp(0.95rem, 1.5vw, 1.08rem);
  background: #ffffff !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-sizing: border-box !important;
  min-height: min(100vh, 100dvh) !important;
  height: auto !important;
  max-height: none !important;
  padding: calc(var(--masthead-h-compact) + 2.25rem) clamp(1.5rem, 5vw, 3.5rem) clamp(2.5rem, 5vw, 3.5rem) !important;
  overflow: visible !important;
  position: relative !important;
  text-align: left !important;
}
.hero::before,
.hero-glow-layer {
  display: none !important;
}
.hero-inner {
  display: grid !important;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.95fr) !important;
  gap: clamp(2rem, 5vw, 4.5rem) !important;
  align-items: center !important;
  width: 100% !important;
  max-width: 1240px !important;
  margin: 0 auto !important;
}
.hero-copy {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  gap: 0 !important;
  max-width: none !important;
  padding: 0 !important;
  position: relative !important;
  z-index: 1 !important;
}
.hero-kicker {
  display: flex !important;
  align-items: center !important;
  gap: 0.85rem !important;
  margin: 0 0 1.25rem !important;
  font-size: clamp(0.62rem, 1.2vw, 0.75rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.2em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.hero-kicker-line {
  display: block !important;
  width: clamp(32px, 6vw, 56px) !important;
  height: 1px !important;
  background: linear-gradient(90deg, transparent, #93c5fd 55%, #2563eb 100%) !important;
  flex-shrink: 0 !important;
}
.hero-kicker-line:last-child {
  background: linear-gradient(90deg, #2563eb, #93c5fd 45%, transparent) !important;
}
.hero-title,
.hero h1.hero-title {
  margin: 0 0 1.25rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: var(--hero-title-size) !important;
  line-height: 0.94 !important;
  letter-spacing: -0.045em !important;
  color: #0f172a !important;
  text-align: left !important;
  width: 100% !important;
}
.hero-title .line,
.hero h1 .line {
  display: block !important;
  overflow: visible !important;
}
.hero-title .line-decode .inner,
.hero h1 .line-decode .inner {
  display: inline-block !important;
  font-weight: 700 !important;
  color: #0f172a !important;
}
.hero-title .line-every,
.hero h1 .line-every {
  margin: 0.05em 0 0.02em !important;
}
.hero-title .line-every .outline,
.hero h1 .line-every .outline,
.hero h1 .outline {
  display: inline-block !important;
  font-weight: 600 !important;
  color: transparent !important;
  -webkit-text-stroke: 2.5px #2563eb !important;
  text-stroke: 2.5px #2563eb !important;
  paint-order: stroke fill !important;
}
.hero-title .line-call .inner,
.hero-title .line-call .glow,
.hero h1 .line-call .inner,
.hero h1 .inner.glow,
.hero h1 .glow {
  display: inline-block !important;
  font-weight: 700 !important;
  font-size: 1.06em !important;
  background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 38%, #3b82f6 72%, #60a5fa 100%) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  animation: none !important;
}
.hero-title-mark {
  display: inline-block !important;
  background: linear-gradient(180deg, #2563eb, #1d4ed8) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}
.hero-title .inner {
  animation: none !important;
  transform: none !important;
  opacity: 1 !important;
}
.hero-pitch {
  margin: 0 !important;
  max-width: 32rem !important;
  font-family: 'General Sans', system-ui, sans-serif !important;
  font-size: var(--hero-pitch-size) !important;
  line-height: 1.6 !important;
  color: #475569 !important;
  text-align: left !important;
}
.hero-pitch strong {
  font-weight: 600 !important;
  color: #1e40af !important;
}
.hero-aside {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  justify-content: center !important;
  padding: 0 0 0 clamp(2rem, 4vw, 3.25rem) !important;
  border-left: 1px solid #e2e8f0 !important;
  position: relative !important;
  min-height: 0 !important;
  height: auto !important;
}
.hero-aside-eyebrow {
  margin: 0 0 0.5rem !important;
  font-size: clamp(0.62rem, 1.1vw, 0.72rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.16em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
}
.hero-aside-title {
  margin: 0 0 0.65rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.5rem, 2.8vw, 2rem) !important;
  font-weight: 700 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.1 !important;
  color: #0f172a !important;
}
.hero-aside-desc {
  margin: 0 0 1.25rem !important;
  font-size: clamp(0.92rem, 1.45vw, 1.02rem) !important;
  line-height: 1.6 !important;
  color: #64748b !important;
  max-width: 22rem !important;
}
.hero-aside-list {
  margin: 0 0 1.5rem !important;
  padding: 0 !important;
  list-style: none !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.5rem !important;
}
.hero-aside-list li {
  position: relative !important;
  padding-left: 1.1rem !important;
  font-size: 0.88rem !important;
  color: #475569 !important;
  line-height: 1.5 !important;
}
.hero-aside-list li::before {
  content: '' !important;
  position: absolute !important;
  left: 0 !important;
  top: 0.55em !important;
  width: 5px !important;
  height: 5px !important;
  border-radius: 50% !important;
  background: #2563eb !important;
}
.hero-aside-btn {
  width: auto !important;
  min-width: 11.5rem !important;
  border-radius: 8px !important;
  clip-path: none !important;
  padding: 0.9rem 1.75rem !important;
  font-size: var(--hero-btn-size) !important;
  font-weight: 600 !important;
  background: #1e40af !important;
  color: #fff !important;
  box-shadow: none !important;
  transition: background 0.2s !important;
}
.hero-aside-btn:hover {
  background: #1e3a8a !important;
}
@media (max-width: 1024px) {
  .hero {
    min-height: auto !important;
    align-items: flex-start !important;
    padding-bottom: 3.5rem !important;
  }
  .hero-inner {
    grid-template-columns: 1fr !important;
    gap: 2.25rem !important;
  }
  .hero-aside {
    padding: 2rem 0 0 !important;
    border-left: none !important;
    border-top: 1px solid #e2e8f0 !important;
    width: 100% !important;
  }
}
@media (min-width: 1200px) {
  .hero {
    --hero-title-size: clamp(3.25rem, 5.5vw, 5.75rem);
  }
  .hero-title .line-every .outline,
  .hero h1 .line-every .outline {
    -webkit-text-stroke-width: 3px !important;
  }
}
@media (max-height: 720px) {
  .hero {
    --hero-title-size: clamp(2.35rem, 5.5vw, 3.75rem);
    --hero-pitch-size: clamp(0.95rem, 1.6vw, 1.05rem);
    padding-top: calc(var(--masthead-h-compact) + 1.5rem) !important;
  }
  .hero-kicker {
    margin-bottom: 0.85rem !important;
  }
  .hero-title,
  .hero h1.hero-title {
    margin-bottom: 0.85rem !important;
  }
}
@media (max-width: 560px) {
  .hero {
    --hero-title-size: clamp(2.5rem, 11vw, 3.35rem);
    padding-left: 1.15rem !important;
    padding-right: 1.15rem !important;
  }
  .hero-kicker {
    letter-spacing: 0.14em !important;
    gap: 0.55rem !important;
  }
  .hero-title .line-every .outline,
  .hero h1 .line-every .outline {
    -webkit-text-stroke-width: 2px !important;
  }
  .hero-aside-btn {
    width: 100% !important;
    min-width: 0 !important;
  }
}

"""


def main():
    text = HTML_PATH.read_text(encoding="utf-8")

    if OLD_HERO not in text:
        raise SystemExit("Hero HTML not found")

    text = text.replace(OLD_HERO, NEW_HERO, 1)

    start = text.find(MARKER_START)
    end = text.find(MARKER_END)
    if start < 0 or end < 0:
        raise SystemExit("Hero CSS markers not found")

    text = text[:start] + NEW_CSS + text[end:]
    HTML_PATH.write_text(text, encoding="utf-8")
    print("Unified hero:", HTML_PATH.name)


if __name__ == "__main__":
    main()
