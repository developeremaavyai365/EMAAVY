"""Upgrade hero showcase: site-matched design + contain-fit screenshots."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

OLD_CSS_START = "/* Dynamic platform showcase */"
OLD_CSS_END = "/* ═══ ELEGANT SIGNAL — refined, no glow ═══ */"

NEW_CSS = r"""/* Dynamic platform showcase — site-matched, contain-fit */
.hero-showcase {
  position: relative !important;
  width: 100% !important;
  max-width: 580px !important;
  margin-left: auto !important;
  z-index: 1 !important;
}
.hero-showcase::before {
  content: '' !important;
  position: absolute !important;
  inset: -8% -6% -10% -4% !important;
  background: radial-gradient(ellipse 70% 60% at 55% 45%, rgba(37, 99, 235, 0.14) 0%, rgba(59, 130, 246, 0.06) 45%, transparent 72%) !important;
  filter: blur(20px) !important;
  pointer-events: none !important;
  z-index: 0 !important;
}
.hero-showcase-device {
  position: relative !important;
  z-index: 1 !important;
  border-radius: 14px !important;
  background: #ffffff !important;
  padding: 0 !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow:
    0 1px 2px rgba(15, 23, 42, 0.04),
    0 20px 50px -12px rgba(30, 64, 175, 0.22),
    0 0 0 1px rgba(255, 255, 255, 0.8) inset !important;
  overflow: hidden !important;
  transform: translateY(0) !important;
  animation: heroShowcaseLift 6s ease-in-out infinite !important;
}
.hero-showcase-device::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  height: 3px !important;
  background: linear-gradient(90deg, #1e40af, #2563eb, #3b82f6, #2563eb) !important;
  background-size: 200% 100% !important;
  animation: heroShowcaseBar 8s linear infinite !important;
  z-index: 3 !important;
  pointer-events: none !important;
}
.hero-showcase-chrome {
  display: flex !important;
  align-items: center !important;
  gap: 7px !important;
  padding: 0.55rem 0.85rem !important;
  background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%) !important;
  border-bottom: 1px solid #e2e8f0 !important;
}
.hero-showcase-dot {
  width: 9px !important;
  height: 9px !important;
  border-radius: 50% !important;
  border: 1px solid rgba(15, 23, 42, 0.08) !important;
  background: #cbd5e1 !important;
  flex-shrink: 0 !important;
}
.hero-showcase-dot:nth-child(1) { background: #f87171 !important; }
.hero-showcase-dot:nth-child(2) { background: #fbbf24 !important; }
.hero-showcase-dot:nth-child(3) { background: #4ade80 !important; }
.hero-showcase-url {
  margin-left: auto !important;
  padding: 0.2rem 0.55rem !important;
  border-radius: 6px !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  font-size: 0.6rem !important;
  color: #64748b !important;
  letter-spacing: 0.03em !important;
  font-family: ui-monospace, 'SF Mono', monospace !important;
}
.hero-showcase-viewport {
  position: relative !important;
  aspect-ratio: 16 / 9 !important;
  width: 100% !important;
  background: #0a0a0c !important;
  overflow: hidden !important;
  isolation: isolate !important;
}
.hero-showcase-slides {
  position: absolute !important;
  inset: 0 !important;
}
.hero-slide {
  position: absolute !important;
  inset: 0 !important;
  margin: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: clamp(6px, 1.2vw, 10px) !important;
  box-sizing: border-box !important;
  opacity: 0 !important;
  visibility: hidden !important;
  transition: opacity 0.55s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.55s !important;
  will-change: opacity !important;
  pointer-events: none !important;
}
.hero-slide.is-active {
  opacity: 1 !important;
  visibility: visible !important;
  z-index: 2 !important;
  pointer-events: auto !important;
}
.hero-slide img {
  display: block !important;
  width: auto !important;
  height: auto !important;
  max-width: 100% !important;
  max-height: 100% !important;
  object-fit: contain !important;
  object-position: center center !important;
  border-radius: 4px !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.35) !important;
  transform: none !important;
  animation: none !important;
}
.hero-showcase-vignette {
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  z-index: 3 !important;
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.06) !important;
  background: linear-gradient(180deg, rgba(255,255,255,0.04) 0%, transparent 12%, transparent 88%, rgba(0,0,0,0.15) 100%) !important;
}
.hero-showcase-meta {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 1rem !important;
  margin-top: 0.75rem !important;
  padding: 0 2px !important;
}
.hero-showcase-live {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.4rem !important;
  padding: 0.35rem 0.65rem !important;
  border-radius: 999px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  font-size: 0.62rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.hero-showcase-pulse {
  width: 6px !important;
  height: 6px !important;
  border-radius: 50% !important;
  background: #2563eb !important;
  box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.45) !important;
  animation: heroShowcasePulse 2s ease-in-out infinite !important;
}
.hero-showcase-label {
  text-align: right !important;
  line-height: 1.25 !important;
  min-width: 0 !important;
}
.hero-showcase-label strong {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  color: #0f172a !important;
  letter-spacing: -0.02em !important;
}
.hero-showcase-label span {
  display: block !important;
  font-size: 0.7rem !important;
  color: #64748b !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  max-width: 14rem !important;
}
.hero-showcase-nav {
  margin-top: 0.65rem !important;
}
.hero-showcase-dots {
  display: flex !important;
  gap: 0.4rem !important;
  padding: 0 2px !important;
}
.hero-showcase-dots button {
  flex: 1 !important;
  position: relative !important;
  height: 4px !important;
  border: none !important;
  border-radius: 999px !important;
  background: #e2e8f0 !important;
  cursor: pointer !important;
  padding: 0 !important;
  overflow: hidden !important;
  transition: background 0.2s !important;
}
.hero-showcase-dots button:hover {
  background: #cbd5e1 !important;
}
.hero-showcase-dots button.is-active {
  background: #dbeafe !important;
}
.hero-showcase-dots button.is-active .hero-showcase-progress {
  display: block !important;
}
.hero-showcase-progress {
  display: none !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 100% !important;
  background: linear-gradient(90deg, #1e40af, #2563eb, #3b82f6) !important;
  transform: scaleX(0) !important;
  transform-origin: left center !important;
  border-radius: inherit !important;
}
@keyframes heroShowcaseProgress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
@keyframes heroShowcaseLift {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
@keyframes heroShowcaseBar {
  to { background-position: 200% 0; }
}
@keyframes heroShowcasePulse {
  0% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.4); }
  70% { box-shadow: 0 0 0 6px rgba(37, 99, 235, 0); }
  100% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0); }
}
@media (prefers-reduced-motion: reduce) {
  .hero-showcase-device,
  .hero-showcase-device::before,
  .hero-showcase-pulse,
  .hero-showcase-progress {
    animation: none !important;
  }
  .hero-slide { transition-duration: 0.15s !important; }
}
@media (max-width: 1024px) {
  .hero-showcase {
    max-width: 100% !important;
    margin-left: 0 !important;
  }
  .hero-showcase-device {
    animation: none !important;
  }
}
@media (min-width: 1200px) {
  .hero-inner {
    grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr) !important;
  }
  .hero-showcase {
    max-width: 620px !important;
  }
}

"""

NEW_SHOWCASE_INNER = """<div class="hero-showcase" id="heroVisual" aria-label="EMAAVY platform preview"> <div class="hero-showcase-device"> <div class="hero-showcase-chrome" aria-hidden="true"><span class="hero-showcase-dot"></span><span class="hero-showcase-dot"></span><span class="hero-showcase-dot"></span><span class="hero-showcase-url">app.emaavy.com</span></div> <div class="hero-showcase-viewport"> <div class="hero-showcase-slides"> <figure class="hero-slide is-active" data-caption="Dashboard" data-title="Real-time call analytics"><img src="assets/hero/dashboard.png" alt="EMAAVY dashboard with metrics and call volume chart" decoding="async" fetchpriority="high" /></figure> <figure class="hero-slide" data-caption="Campaigns" data-title="Outbound and inbound workflows"><img src="assets/hero/campaigns.png" alt="EMAAVY create campaign — outbound and inbound" loading="lazy" decoding="async" /></figure> <figure class="hero-slide" data-caption="AI Agents" data-title="Voice agents at scale"><img src="assets/hero/agents.png" alt="EMAAVY AI agents management screen" loading="lazy" decoding="async" /></figure> <figure class="hero-slide" data-caption="Integrations" data-title="Connect your entire stack"><img src="assets/hero/integrations.png" alt="EMAAVY integrations hub" loading="lazy" decoding="async" /></figure> </div> <div class="hero-showcase-vignette" aria-hidden="true"></div> </div> <div class="hero-showcase-meta"> <span class="hero-showcase-live"><span class="hero-showcase-pulse" aria-hidden="true"></span>Live preview</span> <div class="hero-showcase-label"><strong id="heroShowcaseCaption">Dashboard</strong><span id="heroShowcaseTitle">Real-time call analytics</span></div> </div> <nav class="hero-showcase-nav" aria-label="Platform views"> <div class="hero-showcase-dots" role="tablist"> <button type="button" class="is-active" role="tab" aria-label="Dashboard" aria-selected="true" data-slide="0"><span class="hero-showcase-progress" aria-hidden="true"></span></button> <button type="button" role="tab" aria-label="Campaigns" aria-selected="false" data-slide="1"><span class="hero-showcase-progress" aria-hidden="true"></span></button> <button type="button" role="tab" aria-label="AI Agents" aria-selected="false" data-slide="2"><span class="hero-showcase-progress" aria-hidden="true"></span></button> <button type="button" role="tab" aria-label="Integrations" aria-selected="false" data-slide="3"><span class="hero-showcase-progress" aria-hidden="true"></span></button> </div> </nav> </div>"""


def main():
    text = HTML.read_text(encoding="utf-8")

    start = text.find(OLD_CSS_START)
    end = text.find(OLD_CSS_END)
    if start < 0 or end < 0:
        raise SystemExit("CSS markers not found")
    text = text[:start] + NEW_CSS + text[end:]

    m = re.search(
        r'<div class="hero-showcase" id="heroVisual".*?</div> </div>',
        text,
        re.DOTALL,
    )
    if not m:
        raise SystemExit("hero-showcase HTML not found")
    text = text[: m.start()] + NEW_SHOWCASE_INNER + text[m.end() :]

    HTML.write_text(text, encoding="utf-8")
    print("Showcase v2 applied.")


if __name__ == "__main__":
    main()
