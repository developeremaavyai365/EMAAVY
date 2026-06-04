"""Hero: brand left + dynamic screenshot showcase right."""
from pathlib import Path

HTML_PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
MARKER_START = "/* ═══ ELEGANT HERO — unified split, no cards ═══ */"
MARKER_END = "/* ═══ ELEGANT SIGNAL — refined, no glow ═══ */"

NEW_HERO = """<section class="hero" id="top"> <div class="hero-inner"> <div class="hero-copy"> <div class="hero-brand"> <div class="hero-brand-stack"> <span class="hero-brand-letters" aria-label="EMAAVY"> <span class="hero-brand-letter">E</span> <span class="hero-brand-letter">M</span> <span class="hero-brand-letter">A</span> <span class="hero-brand-letter">A</span> <span class="hero-brand-letter">V</span> <span class="hero-brand-letter">Y</span> </span> </div> <p class="hero-tagline">Call Intelligence</p> </div> <p class="hero-kicker"><span class="hero-kicker-line" aria-hidden="true"></span><span>Every call. Fully understood.</span><span class="hero-kicker-line" aria-hidden="true"></span></p> <h1 class="hero-title" aria-label="Decode every call"> <span class="line line-decode"><span class="inner">Decode</span></span> <span class="line line-every"><span class="inner outline">every</span></span> <span class="line line-call"><span class="inner glow">call<span class="hero-title-mark" aria-hidden="true">.</span></span></span> </h1> <p class="hero-pitch">Record, transcribe, and act on every call—<strong>one enterprise platform</strong> built so your team never misses what matters.</p> <div class="hero-actions"> <button class="btn-magnetic btn-fill" type="button" data-open-demo>Try EMAAVY</button> </div> </div> <div class="hero-showcase" id="heroVisual" aria-label="EMAAVY platform preview"> <div class="hero-showcase-device"> <div class="hero-showcase-chrome" aria-hidden="true"><span class="hero-showcase-dot"></span><span class="hero-showcase-dot"></span><span class="hero-showcase-dot"></span><span class="hero-showcase-url">app.emaavy.com</span></div> <div class="hero-showcase-viewport"> <div class="hero-showcase-slides"> <figure class="hero-slide is-active" data-caption="Dashboard" data-title="Real-time call analytics"><img src="assets/hero/dashboard.png" alt="EMAAVY dashboard with metrics and call volume chart" width="1200" height="750" /></figure> <figure class="hero-slide" data-caption="Campaigns" data-title="Outbound &amp; inbound workflows"><img src="assets/hero/campaigns.png" alt="EMAAVY create campaign — outbound and inbound" loading="lazy" width="1200" height="750" /></figure> <figure class="hero-slide" data-caption="AI Agents" data-title="Voice agents at scale"><img src="assets/hero/agents.png" alt="EMAAVY AI agents management screen" loading="lazy" width="1200" height="750" /></figure> <figure class="hero-slide" data-caption="Integrations" data-title="Connect your entire stack"><img src="assets/hero/integrations.png" alt="EMAAVY integrations hub" loading="lazy" width="1200" height="750" /></figure> </div> <div class="hero-showcase-shine" aria-hidden="true"></div> </div> <div class="hero-showcase-meta"> <span class="hero-showcase-live"><span class="hero-showcase-pulse" aria-hidden="true"></span>Live preview</span> <div class="hero-showcase-label"><strong id="heroShowcaseCaption">Dashboard</strong><span id="heroShowcaseTitle">Real-time call analytics</span></div> </div> <div class="hero-showcase-dots" role="tablist" aria-label="Platform views"> <button type="button" class="is-active" aria-label="Dashboard" aria-selected="true" data-slide="0"></button> <button type="button" aria-label="Campaigns" aria-selected="false" data-slide="1"></button> <button type="button" aria-label="AI Agents" aria-selected="false" data-slide="2"></button> <button type="button" aria-label="Integrations" aria-selected="false" data-slide="3"></button> </div> </div> </div> </div> </section>"""

NEW_CSS = r"""/* ═══ ELEGANT HERO — brand + dynamic showcase ═══ */
.hero {
  --hero-brand-size: clamp(2.5rem, 7vw, 4.5rem);
  --hero-title-size: clamp(2.35rem, 5.5vw, 4.25rem);
  --hero-pitch-size: clamp(0.98rem, 1.6vw, 1.12rem);
  --hero-btn-size: clamp(0.95rem, 1.5vw, 1.08rem);
  background: #ffffff !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  min-height: min(100vh, 100dvh) !important;
  padding: calc(var(--masthead-h-compact) + 2rem) clamp(1.25rem, 4vw, 3rem) clamp(2rem, 4vw, 3rem) !important;
  overflow: hidden !important;
  position: relative !important;
}
.hero::before,
.hero-glow-layer {
  display: none !important;
}
.hero-inner {
  display: grid !important;
  grid-template-columns: minmax(0, 0.92fr) minmax(0, 1.08fr) !important;
  gap: clamp(1.75rem, 4vw, 3.5rem) !important;
  align-items: center !important;
  width: 100% !important;
  max-width: 1280px !important;
  margin: 0 auto !important;
}
.hero-copy {
  display: flex !important;
  flex-direction: column !important;
  align-items: flex-start !important;
  z-index: 2 !important;
}
.hero-brand {
  margin-bottom: clamp(1.25rem, 3vw, 2rem) !important;
}
.hero-brand-stack {
  line-height: 1 !important;
  margin-bottom: 0.55rem !important;
}
.hero-brand-letters {
  display: inline-flex !important;
  flex-wrap: wrap !important;
  gap: 0 !important;
}
.hero-brand-letter {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 700 !important;
  font-size: var(--hero-brand-size) !important;
  letter-spacing: -0.06em !important;
  background: linear-gradient(180deg, #1e40af 0%, #2563eb 50%, #3b82f6 100%) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}
.hero-tagline {
  margin: 0 !important;
  font-size: clamp(0.68rem, 1.4vw, 0.82rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.38em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  padding-left: 0.38em !important;
}
.hero-kicker {
  display: flex !important;
  align-items: center !important;
  gap: 0.75rem !important;
  margin: 0 0 1rem !important;
  font-size: clamp(0.6rem, 1.1vw, 0.72rem) !important;
  font-weight: 600 !important;
  letter-spacing: 0.18em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.hero-kicker-line {
  width: clamp(28px, 5vw, 48px) !important;
  height: 1px !important;
  background: linear-gradient(90deg, transparent, #93c5fd 55%, #2563eb) !important;
  flex-shrink: 0 !important;
}
.hero-kicker-line:last-child {
  background: linear-gradient(90deg, #2563eb, #93c5fd 45%, transparent) !important;
}
.hero-title,
.hero h1.hero-title {
  margin: 0 0 1rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: var(--hero-title-size) !important;
  line-height: 0.94 !important;
  letter-spacing: -0.045em !important;
  color: #0f172a !important;
}
.hero-title .line { display: block !important; overflow: visible !important; }
.hero-title .line-decode .inner { font-weight: 700 !important; color: #0f172a !important; }
.hero-title .line-every .outline,
.hero h1 .outline {
  color: transparent !important;
  -webkit-text-stroke: 2.5px #2563eb !important;
  text-stroke: 2.5px #2563eb !important;
}
.hero-title .line-call .glow,
.hero h1 .glow {
  background: linear-gradient(135deg, #1e3a8a, #2563eb 40%, #3b82f6 75%, #60a5fa) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}
.hero-title-mark {
  background: linear-gradient(180deg, #2563eb, #1d4ed8) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
}
.hero-title .inner { animation: none !important; transform: none !important; opacity: 1 !important; }
.hero-pitch {
  margin: 0 0 1.35rem !important;
  max-width: 30rem !important;
  font-size: var(--hero-pitch-size) !important;
  line-height: 1.6 !important;
  color: #475569 !important;
}
.hero-pitch strong { color: #1e40af !important; font-weight: 600 !important; }
.hero-actions {
  display: flex !important;
  margin: 0 !important;
  opacity: 1 !important;
}
.hero-actions .btn-fill {
  border-radius: 8px !important;
  clip-path: none !important;
  padding: 0.88rem 1.75rem !important;
  font-size: var(--hero-btn-size) !important;
  background: #1e40af !important;
  color: #fff !important;
  box-shadow: none !important;
}
.hero-actions .btn-fill:hover { background: #1e3a8a !important; }

/* Dynamic platform showcase */
.hero-showcase {
  position: relative !important;
  width: 100% !important;
  perspective: 1400px !important;
  z-index: 1 !important;
}
.hero-showcase::before {
  content: '' !important;
  position: absolute !important;
  inset: 8% 5% 12% 8% !important;
  background: radial-gradient(ellipse at 50% 45%, rgba(37, 99, 235, 0.2) 0%, rgba(163, 255, 18, 0.08) 35%, transparent 68%) !important;
  filter: blur(28px) !important;
  pointer-events: none !important;
  z-index: 0 !important;
  animation: heroGlowPulse 5s ease-in-out infinite !important;
}
.hero-showcase-device {
  position: relative !important;
  z-index: 1 !important;
  border-radius: 16px !important;
  background: linear-gradient(145deg, #0f1115 0%, #1a1d24 100%) !important;
  padding: 10px 10px 14px !important;
  box-shadow:
    0 4px 6px rgba(15, 23, 42, 0.06),
    0 28px 64px -12px rgba(30, 64, 175, 0.35),
    0 0 0 1px rgba(37, 99, 235, 0.12) !important;
  transform: rotateY(-6deg) rotateX(3deg) !important;
  transform-style: preserve-3d !important;
  animation: heroDeviceFloat 7s ease-in-out infinite !important;
}
.hero-showcase-chrome {
  display: flex !important;
  align-items: center !important;
  gap: 6px !important;
  padding: 6px 10px 10px !important;
}
.hero-showcase-dot {
  width: 8px !important;
  height: 8px !important;
  border-radius: 50% !important;
  background: #334155 !important;
}
.hero-showcase-dot:nth-child(1) { background: #ef4444 !important; }
.hero-showcase-dot:nth-child(2) { background: #eab308 !important; }
.hero-showcase-dot:nth-child(3) { background: #22c55e !important; }
.hero-showcase-url {
  margin-left: auto !important;
  font-size: 0.62rem !important;
  color: #64748b !important;
  letter-spacing: 0.04em !important;
  font-family: ui-monospace, monospace !important;
}
.hero-showcase-viewport {
  position: relative !important;
  border-radius: 10px !important;
  overflow: hidden !important;
  aspect-ratio: 16 / 10 !important;
  background: #0b0c10 !important;
}
.hero-showcase-slides {
  position: absolute !important;
  inset: 0 !important;
}
.hero-slide {
  position: absolute !important;
  inset: 0 !important;
  margin: 0 !important;
  opacity: 0 !important;
  transform: scale(1.04) translateX(3%) !important;
  transition: opacity 0.85s cubic-bezier(0.4, 0, 0.2, 1), transform 0.85s cubic-bezier(0.4, 0, 0.2, 1) !important;
  pointer-events: none !important;
}
.hero-slide.is-active {
  opacity: 1 !important;
  transform: scale(1) translateX(0) !important;
  pointer-events: auto !important;
  z-index: 2 !important;
}
.hero-slide.is-exit {
  opacity: 0 !important;
  transform: scale(0.98) translateX(-2%) !important;
  z-index: 1 !important;
}
.hero-slide img {
  width: 100% !important;
  height: 100% !important;
  object-fit: cover !important;
  object-position: top center !important;
  display: block !important;
}
.hero-slide.is-active img {
  animation: heroKenBurns 4.2s ease-out forwards !important;
}
.hero-showcase-shine {
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(105deg, transparent 38%, rgba(255, 255, 255, 0.14) 50%, transparent 62%) !important;
  transform: translateX(-120%) !important;
  animation: heroShineSweep 4.2s ease-in-out infinite !important;
  pointer-events: none !important;
  z-index: 4 !important;
}
.hero-showcase-meta {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 1rem !important;
  margin-top: 0.85rem !important;
  padding: 0 4px !important;
}
.hero-showcase-live {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.45rem !important;
  font-size: 0.65rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.hero-showcase-pulse {
  width: 7px !important;
  height: 7px !important;
  border-radius: 50% !important;
  background: #22c55e !important;
  box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.5) !important;
  animation: heroPulse 2s ease-in-out infinite !important;
}
.hero-showcase-label {
  text-align: right !important;
  line-height: 1.3 !important;
}
.hero-showcase-label strong {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.95rem !important;
  color: #0f172a !important;
  letter-spacing: -0.02em !important;
}
.hero-showcase-label span {
  display: block !important;
  font-size: 0.72rem !important;
  color: #94a3b8 !important;
}
.hero-showcase-dots {
  display: flex !important;
  gap: 0.45rem !important;
  margin-top: 0.65rem !important;
  padding: 0 4px !important;
}
.hero-showcase-dots button {
  flex: 1 !important;
  height: 3px !important;
  border: none !important;
  border-radius: 999px !important;
  background: #e2e8f0 !important;
  cursor: pointer !important;
  padding: 0 !important;
  transition: background 0.25s, transform 0.25s !important;
}
.hero-showcase-dots button.is-active {
  background: linear-gradient(90deg, #2563eb, #3b82f6) !important;
  transform: scaleY(1.35) !important;
}
@keyframes heroDeviceFloat {
  0%, 100% { transform: rotateY(-6deg) rotateX(3deg) translateY(0); }
  50% { transform: rotateY(-4deg) rotateX(2deg) translateY(-10px); }
}
@keyframes heroKenBurns {
  from { transform: scale(1.03); }
  to { transform: scale(1); }
}
@keyframes heroShineSweep {
  0%, 55% { transform: translateX(-120%); }
  100% { transform: translateX(120%); }
}
@keyframes heroGlowPulse {
  0%, 100% { opacity: 0.75; }
  50% { opacity: 1; }
}
@keyframes heroPulse {
  0% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0.45); }
  70% { box-shadow: 0 0 0 8px rgba(34, 197, 94, 0); }
  100% { box-shadow: 0 0 0 0 rgba(34, 197, 94, 0); }
}
@media (prefers-reduced-motion: reduce) {
  .hero-showcase-device,
  .hero-showcase-shine,
  .hero-slide.is-active img,
  .hero-showcase::before,
  .hero-showcase-pulse {
    animation: none !important;
  }
  .hero-slide { transition-duration: 0.2s !important; }
}
@media (max-width: 1024px) {
  .hero { min-height: auto !important; align-items: flex-start !important; }
  .hero-inner { grid-template-columns: 1fr !important; gap: 2rem !important; }
  .hero-showcase-device {
    transform: none !important;
    animation: none !important;
  }
}
@media (min-width: 1200px) {
  .hero { --hero-title-size: clamp(2.75rem, 4.8vw, 4.75rem); --hero-brand-size: clamp(2.85rem, 6vw, 4.75rem); }
}
@media (max-width: 560px) {
  .hero-brand-letter { font-size: clamp(2.2rem, 12vw, 3rem) !important; }
  .hero-tagline { letter-spacing: 0.28em !important; }
  .hero-actions .btn-fill { width: 100% !important; }
}

"""

SCRIPT_TAG = '<script src="assets/hero-showcase.js" defer></script>'


def main():
    text = HTML_PATH.read_text(encoding="utf-8")

    import re
    m = re.search(r'<section class="hero"[^>]*>.*?</section>', text, re.DOTALL)
    if not m:
        raise SystemExit("Hero section not found")
    text = text[: m.start()] + NEW_HERO + text[m.end() :]

    start = text.find(MARKER_START)
    end = text.find(MARKER_END)
    if start < 0 or end < 0:
        raise SystemExit("CSS markers not found")
    text = text[:start] + NEW_CSS + text[end:]

    if SCRIPT_TAG not in text:
        text = text.replace("</body>", SCRIPT_TAG + "\n</body>", 1)

    HTML_PATH.write_text(text, encoding="utf-8")
    print("Hero showcase updated.")


if __name__ == "__main__":
    main()
