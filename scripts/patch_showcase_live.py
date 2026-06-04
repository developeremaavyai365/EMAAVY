"""Fix duplicate Live preview + upgrade hero showcase."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

CSS_START = "/* Dynamic platform showcase — site-matched, contain-fit */"
CSS_END = "/* ═══ ELEGANT SIGNAL — refined, no glow ═══ */"

NEW_CSS = r"""/* Dynamic platform showcase — live preview + cinematic slides */
.hero-showcase {
  position: relative !important;
  width: 100% !important;
  max-width: 580px !important;
  margin-left: auto !important;
  z-index: 1 !important;
}
.hero-showcase:focus { outline: none !important; }
.hero-showcase:focus-visible {
  outline: 2px solid #2563eb !important;
  outline-offset: 6px !important;
  border-radius: 16px !important;
}
.hero-showcase::before {
  content: '' !important;
  position: absolute !important;
  inset: -10% -8% -12% -6% !important;
  background: radial-gradient(ellipse 75% 65% at 50% 40%, rgba(37, 99, 235, 0.18) 0%, rgba(59, 130, 246, 0.07) 42%, transparent 70%) !important;
  filter: blur(24px) !important;
  pointer-events: none !important;
  z-index: 0 !important;
  animation: heroGlowBreath 5s ease-in-out infinite !important;
}
.hero-showcase-device {
  position: relative !important;
  z-index: 1 !important;
  border-radius: 14px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow:
    0 1px 2px rgba(15, 23, 42, 0.05),
    0 24px 56px -14px rgba(30, 64, 175, 0.28),
    0 0 0 1px rgba(255, 255, 255, 0.85) inset !important;
  overflow: hidden !important;
  animation: heroShowcaseLift 7s ease-in-out infinite !important;
}
.hero-showcase-device::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important; left: 0 !important; right: 0 !important;
  height: 3px !important;
  background: linear-gradient(90deg, #1e40af, #2563eb, #60a5fa, #2563eb, #1e40af) !important;
  background-size: 200% 100% !important;
  animation: heroShowcaseBar 6s linear infinite !important;
  z-index: 12 !important;
  pointer-events: none !important;
}
.hero-showcase-chrome {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  padding: 0.5rem 0.75rem !important;
  background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%) !important;
  border-bottom: 1px solid #e2e8f0 !important;
  position: relative !important;
  z-index: 11 !important;
}
.hero-showcase-dot {
  width: 9px !important; height: 9px !important;
  border-radius: 50% !important;
  border: 1px solid rgba(15, 23, 42, 0.08) !important;
  flex-shrink: 0 !important;
}
.hero-showcase-dot:nth-child(1) { background: #f87171 !important; }
.hero-showcase-dot:nth-child(2) { background: #fbbf24 !important; }
.hero-showcase-dot:nth-child(3) { background: #4ade80 !important; }
.hero-showcase-live-badge {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.35rem !important;
  margin-left: 0.15rem !important;
  padding: 0.22rem 0.55rem 0.22rem 0.4rem !important;
  border-radius: 999px !important;
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%) !important;
  border: 1px solid #bfdbfe !important;
  font-size: 0.58rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: #1e40af !important;
  box-shadow: 0 0 12px rgba(37, 99, 235, 0.15) !important;
}
.hero-showcase-live-badge.is-syncing {
  animation: heroLivePulse 0.6s ease !important;
}
.hero-showcase-pulse {
  width: 7px !important; height: 7px !important;
  border-radius: 50% !important;
  background: #2563eb !important;
  box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.5) !important;
  animation: heroShowcasePulse 1.8s ease-in-out infinite !important;
}
.hero-showcase-url {
  margin-left: auto !important;
  padding: 0.22rem 0.5rem !important;
  border-radius: 6px !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  font-size: 0.58rem !important;
  color: #475569 !important;
  font-family: ui-monospace, 'SF Mono', monospace !important;
  max-width: 52% !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
  white-space: nowrap !important;
  transition: color 0.25s !important;
}
.hero-showcase-url.is-typing { color: #2563eb !important; }
.hero-showcase-viewport {
  position: relative !important;
  aspect-ratio: 16 / 10 !important;
  min-height: clamp(220px, 42vw, 340px) !important;
  width: 100% !important;
  background: #07080c !important;
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
  flex-direction: column !important;
  justify-content: flex-end !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  z-index: 1 !important;
}
.hero-slide.is-active {
  opacity: 1 !important;
  visibility: visible !important;
  z-index: 3 !important;
  pointer-events: auto !important;
}
.hero-slide-frame {
  position: absolute !important;
  inset: 0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: clamp(8px, 1.4vw, 14px) !important;
  box-sizing: border-box !important;
}
.hero-slide-frame img {
  display: block !important;
  max-width: 100% !important;
  max-height: 100% !important;
  width: auto !important;
  height: auto !important;
  object-fit: contain !important;
  border-radius: 5px !important;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.45) !important;
  transform: scale(0.94) translateY(6px) !important;
  filter: blur(6px) brightness(0.85) !important;
  transition: none !important;
}
.hero-slide.is-active .hero-slide-frame img {
  animation: heroImgFloat 9s ease-in-out infinite !important;
}
.hero-slide-story {
  position: relative !important;
  z-index: 5 !important;
  margin: 0 clamp(10px, 2vw, 16px) clamp(10px, 2vw, 14px) !important;
  padding: 0.65rem 0.85rem 0.7rem !important;
  border-radius: 10px !important;
  background: linear-gradient(135deg, rgba(255,255,255,0.97) 0%, rgba(248,250,252,0.94) 100%) !important;
  border: 1px solid rgba(226, 232, 240, 0.95) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  box-shadow:
    0 4px 24px rgba(15, 23, 42, 0.12),
    0 0 0 1px rgba(255, 255, 255, 0.6) inset !important;
  display: grid !important;
  grid-template-columns: auto 1fr !important;
  gap: 0.65rem !important;
  align-items: start !important;
  transform: translateY(18px) !important;
  opacity: 0 !important;
}
.hero-slide-index {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.35rem !important;
  font-weight: 700 !important;
  line-height: 1 !important;
  background: linear-gradient(180deg, #1e40af, #3b82f6) !important;
  -webkit-background-clip: text !important;
  background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  opacity: 0.35 !important;
}
.hero-slide-name {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  letter-spacing: -0.02em !important;
  margin: 0 0 0.15rem !important;
}
.hero-slide-desc {
  margin: 0 !important;
  font-size: 0.68rem !important;
  line-height: 1.45 !important;
  color: #475569 !important;
}
/* Enter / exit motion per effect */
.hero-slide.is-enter .hero-slide-frame img,
.hero-slide.is-active:not(.is-exit) .hero-slide-frame img {
  filter: blur(0) brightness(1) !important;
}
.hero-slide[data-effect="zoom"].is-enter .hero-slide-frame img {
  animation: heroEnterZoom 0.85s cubic-bezier(0.22, 1, 0.36, 1) forwards, heroImgFloat 9s ease-in-out 0.85s infinite !important;
}
.hero-slide[data-effect="slide-left"].is-enter .hero-slide-frame img {
  animation: heroEnterSlideLeft 0.9s cubic-bezier(0.22, 1, 0.36, 1) forwards, heroImgFloat 9s ease-in-out 0.9s infinite !important;
}
.hero-slide[data-effect="slide-up"].is-enter .hero-slide-frame img {
  animation: heroEnterSlideUp 0.9s cubic-bezier(0.22, 1, 0.36, 1) forwards, heroImgFloat 9s ease-in-out 0.9s infinite !important;
}
.hero-slide[data-effect="fade-blur"].is-enter .hero-slide-frame img {
  animation: heroEnterFadeBlur 0.95s cubic-bezier(0.22, 1, 0.36, 1) forwards, heroImgFloat 9s ease-in-out 0.95s infinite !important;
}
.hero-slide.is-exit .hero-slide-frame img {
  animation: heroExitFade 0.55s cubic-bezier(0.4, 0, 0.2, 1) forwards !important;
}
.hero-slide.is-enter .hero-slide-story {
  animation: heroStoryIn 0.7s cubic-bezier(0.22, 1, 0.36, 1) 0.12s forwards !important;
}
.hero-slide.is-active .hero-slide-story {
  transform: translateY(0) !important;
  opacity: 1 !important;
}
.hero-slide.is-exit .hero-slide-story {
  animation: heroStoryOut 0.4s ease forwards !important;
}
.hero-showcase-livefx {
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  z-index: 8 !important;
  overflow: hidden !important;
}
.hero-showcase-scanline {
  position: absolute !important;
  left: 0 !important;
  right: 0 !important;
  height: 2px !important;
  background: linear-gradient(90deg, transparent, rgba(96, 165, 250, 0.5), transparent) !important;
  box-shadow: 0 0 14px rgba(59, 130, 246, 0.35) !important;
  animation: heroScanline 4.5s linear infinite !important;
  opacity: 0.65 !important;
}
.hero-showcase-shimmer {
  position: absolute !important;
  inset: 0 !important;
  background: linear-gradient(105deg, transparent 40%, rgba(255,255,255,0.04) 50%, transparent 60%) !important;
  background-size: 200% 100% !important;
  animation: heroShimmer 3.5s ease-in-out infinite !important;
}
.hero-showcase-vignette {
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  z-index: 6 !important;
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.05) !important;
  background: linear-gradient(180deg, rgba(37,99,235,0.06) 0%, transparent 18%, transparent 55%, rgba(0,0,0,0.35) 100%) !important;
}
.hero-showcase-footer {
  padding: 0.65rem 0.75rem 0.75rem !important;
  background: linear-gradient(180deg, #fafbfc 0%, #f8fafc 100%) !important;
  border-top: 1px solid #e2e8f0 !important;
}
.hero-showcase-dots {
  display: flex !important;
  gap: 0.35rem !important;
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
}
.hero-showcase-dots button:hover { background: #cbd5e1 !important; }
.hero-showcase-dots button.is-active { background: #dbeafe !important; }
.hero-showcase-dots button.is-active .hero-showcase-progress { display: block !important; }
.hero-showcase-progress {
  display: none !important;
  position: absolute !important;
  inset: 0 auto 0 0 !important;
  width: 100% !important;
  background: linear-gradient(90deg, #1e40af, #2563eb, #60a5fa) !important;
  transform: scaleX(0) !important;
  transform-origin: left center !important;
  border-radius: inherit !important;
}
@keyframes heroGlowBreath {
  0%, 100% { opacity: 0.85; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.03); }
}
@keyframes heroEnterZoom {
  from { transform: scale(0.88) translateY(12px); filter: blur(8px) brightness(0.8); opacity: 0; }
  to { transform: scale(1) translateY(0); filter: blur(0) brightness(1); opacity: 1; }
}
@keyframes heroEnterSlideLeft {
  from { transform: translateX(12%) scale(0.96); filter: blur(6px); opacity: 0; }
  to { transform: translateX(0) scale(1); filter: blur(0); opacity: 1; }
}
@keyframes heroEnterSlideUp {
  from { transform: translateY(10%) scale(0.96); filter: blur(6px); opacity: 0; }
  to { transform: translateY(0) scale(1); filter: blur(0); opacity: 1; }
}
@keyframes heroEnterFadeBlur {
  from { transform: scale(1.04); filter: blur(12px) brightness(1.1); opacity: 0; }
  to { transform: scale(1); filter: blur(0) brightness(1); opacity: 1; }
}
@keyframes heroExitFade {
  to { transform: scale(0.97) translateY(-4px); filter: blur(4px); opacity: 0; }
}
@keyframes heroStoryIn {
  from { transform: translateY(22px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}
@keyframes heroStoryOut {
  to { transform: translateY(10px); opacity: 0; }
}
@keyframes heroImgFloat {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-4px) scale(1.008); }
}
@keyframes heroScanline {
  0% { top: -4%; opacity: 0; }
  8% { opacity: 0.7; }
  92% { opacity: 0.5; }
  100% { top: 104%; opacity: 0; }
}
@keyframes heroShimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
@keyframes heroShowcaseProgress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
@keyframes heroShowcaseLift {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
}
@keyframes heroShowcaseBar {
  to { background-position: 200% 0; }
}
@keyframes heroShowcasePulse {
  0% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0.45); }
  70% { box-shadow: 0 0 0 7px rgba(37, 99, 235, 0); }
  100% { box-shadow: 0 0 0 0 rgba(37, 99, 235, 0); }
}
@keyframes heroLivePulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.04); }
}
@media (prefers-reduced-motion: reduce) {
  .hero-showcase::before,
  .hero-showcase-device,
  .hero-showcase-device::before,
  .hero-showcase-pulse,
  .hero-showcase-scanline,
  .hero-showcase-shimmer,
  .hero-showcase-progress,
  .hero-slide.is-active .hero-slide-frame img {
    animation: none !important;
  }
  .hero-slide-frame img { filter: none !important; transform: none !important; }
}
@media (max-width: 1024px) {
  .hero-showcase { max-width: 100% !important; margin-left: 0 !important; }
  .hero-showcase-device { animation: none !important; }
}
@media (min-width: 1200px) {
  .hero-inner { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr) !important; }
  .hero-showcase { max-width: 620px !important; }
}

"""

NEW_SHOWCASE = r"""<div class="hero-showcase" id="heroVisual" tabindex="0" aria-label="EMAAVY live platform preview" aria-live="polite"> <div class="hero-showcase-device"> <div class="hero-showcase-chrome"> <span class="hero-showcase-dot" aria-hidden="true"></span><span class="hero-showcase-dot" aria-hidden="true"></span><span class="hero-showcase-dot" aria-hidden="true"></span> <span class="hero-showcase-live-badge" id="heroShowcaseLive"><span class="hero-showcase-pulse" aria-hidden="true"></span>Live preview</span> <span class="hero-showcase-url" id="heroShowcaseUrl">app.emaavy.com/dashboard</span> </div> <div class="hero-showcase-viewport"> <div class="hero-showcase-slides" id="heroShowcaseTrack"> <figure class="hero-slide is-active" data-effect="zoom" data-path="/dashboard" data-index="01" data-caption="Dashboard" data-desc="Real-time KPIs, call volume charts, and success rates—updated live as conversations flow in."> <div class="hero-slide-frame"><img src="assets/hero/dashboard.png" alt="EMAAVY dashboard" decoding="async" fetchpriority="high" /></div> <figcaption class="hero-slide-story"><span class="hero-slide-index" aria-hidden="true">01</span><div><strong class="hero-slide-name">Dashboard</strong><p class="hero-slide-desc">Real-time KPIs, call volume charts, and success rates—updated live as conversations flow in.</p></div></figcaption> </figure> <figure class="hero-slide" data-effect="slide-left" data-path="/campaigns" data-index="02" data-caption="Campaigns" data-desc="Launch outbound and inbound campaigns from one screen—routing, scripts, and schedules unified."> <div class="hero-slide-frame"><img src="assets/hero/campaigns.png" alt="EMAAVY campaigns" loading="lazy" decoding="async" /></div> <figcaption class="hero-slide-story"><span class="hero-slide-index" aria-hidden="true">02</span><div><strong class="hero-slide-name">Campaigns</strong><p class="hero-slide-desc">Launch outbound and inbound campaigns from one screen—routing, scripts, and schedules unified.</p></div></figcaption> </figure> <figure class="hero-slide" data-effect="slide-up" data-path="/agents" data-index="03" data-caption="AI Agents" data-desc="Deploy voice agents at scale—monitor performance, tune prompts, and iterate in minutes."> <div class="hero-slide-frame"><img src="assets/hero/agents.png" alt="EMAAVY AI agents" loading="lazy" decoding="async" /></div> <figcaption class="hero-slide-story"><span class="hero-slide-index" aria-hidden="true">03</span><div><strong class="hero-slide-name">AI Agents</strong><p class="hero-slide-desc">Deploy voice agents at scale—monitor performance, tune prompts, and iterate in minutes.</p></div></figcaption> </figure> <figure class="hero-slide" data-effect="fade-blur" data-path="/integrations" data-index="04" data-caption="Integrations" data-desc="Connect CRMs, LLMs, telephony, and speech APIs—your full stack in one hub."> <div class="hero-slide-frame"><img src="assets/hero/integrations.png" alt="EMAAVY integrations" loading="lazy" decoding="async" /></div> <figcaption class="hero-slide-story"><span class="hero-slide-index" aria-hidden="true">04</span><div><strong class="hero-slide-name">Integrations</strong><p class="hero-slide-desc">Connect CRMs, LLMs, telephony, and speech APIs—your full stack in one hub.</p></div></figcaption> </figure> </div> <div class="hero-showcase-livefx" aria-hidden="true"><span class="hero-showcase-scanline"></span><span class="hero-showcase-shimmer"></span></div> <div class="hero-showcase-vignette" aria-hidden="true"></div> </div> <footer class="hero-showcase-footer"> <nav class="hero-showcase-dots" role="tablist" aria-label="Platform views"> <button type="button" class="is-active" role="tab" aria-label="Dashboard" aria-selected="true" data-slide="0"><span class="hero-showcase-progress" aria-hidden="true"></span></button> <button type="button" role="tab" aria-label="Campaigns" aria-selected="false" data-slide="1"><span class="hero-showcase-progress" aria-hidden="true"></span></button> <button type="button" role="tab" aria-label="AI Agents" aria-selected="false" data-slide="2"><span class="hero-showcase-progress" aria-hidden="true"></span></button> <button type="button" role="tab" aria-label="Integrations" aria-selected="false" data-slide="3"><span class="hero-showcase-progress" aria-hidden="true"></span></button> </nav> </footer> </div> </div>"""


def main():
    text = HTML.read_text(encoding="utf-8")

    s = text.find(CSS_START)
    e = text.find(CSS_END)
    if s < 0 or e < 0:
        raise SystemExit("CSS markers missing")
    text = text[:s] + NEW_CSS + text[e:]

    m = re.search(r'<div class="hero-showcase" id="heroVisual".*?</div> </div> </section>', text, re.DOTALL)
    if not m:
        raise SystemExit("showcase block not found")
    text = text[: m.start()] + NEW_SHOWCASE + " </div> </section>" + text[m.end() :]

    HTML.write_text(text, encoding="utf-8")
    print("Live showcase patched. Live preview count:", text.count("Live preview"))


if __name__ == "__main__":
    main()
