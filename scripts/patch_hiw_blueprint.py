#!/usr/bin/env python3
"""Replace HIW pipeline + cards with blueprint journey diagram."""
from pathlib import Path
import re

PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

HIW_HTML = r'''<section id="how-it-works" class="hiw-stage">
  <div class="hiw-mesh" aria-hidden="true"></div>
  <div class="hiw-mesh-lines" aria-hidden="true"></div>
  <div class="hiw-head reveal">
    <span class="section-kicker">The EMAAVY Method</span>
    <h2>How it works</h2>
    <p>From the first ring to the final insight — four steps that turn every call into compounding intelligence.</p>
  </div>
  <div class="hiw-blueprint reveal" aria-label="EMAAVY call intelligence process">
    <span class="hiw-frame hiw-frame--tl" aria-hidden="true"></span>
    <span class="hiw-frame hiw-frame--tr" aria-hidden="true"></span>
    <span class="hiw-frame hiw-frame--bl" aria-hidden="true"></span>
    <span class="hiw-frame hiw-frame--br" aria-hidden="true"></span>
    <div class="hiw-blueprint-label">End-to-end call intelligence</div>
    <svg class="hiw-blueprint-svg" viewBox="0 0 1000 120" preserveAspectRatio="none" aria-hidden="true">
      <defs>
        <linearGradient id="hiwPathGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stop-color="#4A658B" stop-opacity="0.35"/>
          <stop offset="50%" stop-color="#4A658B"/>
          <stop offset="100%" stop-color="#18345D"/>
        </linearGradient>
      </defs>
      <path class="hiw-path-line" d="M 80 60 H 920" fill="none" stroke="url(#hiwPathGrad)" stroke-width="2" stroke-linecap="round"/>
      <circle cx="80" cy="60" r="6" fill="#ffffff" stroke="#4A658B" stroke-width="2"/>
      <circle cx="360" cy="60" r="6" fill="#ffffff" stroke="#4A658B" stroke-width="2"/>
      <circle cx="640" cy="60" r="6" fill="#ffffff" stroke="#4A658B" stroke-width="2"/>
      <circle cx="920" cy="60" r="6" fill="#ffffff" stroke="#18345D" stroke-width="2"/>
    </svg>
    <ol class="hiw-journey">
      <li class="hiw-journey-step reveal click-detail" data-detail="hiw-connect" tabindex="0">
        <div class="hiw-journey-pin"><span>01</span></div>
        <div class="hiw-journey-panel">
          <div class="hiw-journey-art hiw-journey-art--connect" aria-hidden="true">
            <span class="hiw-art-ring"></span>
            <span class="hiw-art-signal"></span>
          </div>
          <div class="hiw-journey-copy">
            <span class="hiw-journey-phase">Telephony</span>
            <h3>Connect</h3>
            <p>Plug in your telephony via Vobiz. EMAAVY listens from the first second of every call.</p>
            <span class="hiw-journey-more">View step details</span>
          </div>
        </div>
      </li>
      <li class="hiw-journey-step reveal click-detail" data-detail="hiw-transcribe" tabindex="0">
        <div class="hiw-journey-pin"><span>02</span></div>
        <div class="hiw-journey-panel">
          <div class="hiw-journey-art hiw-journey-art--transcribe" aria-hidden="true">
            <span class="hiw-art-bar"></span><span class="hiw-art-bar"></span><span class="hiw-art-bar"></span><span class="hiw-art-bar"></span><span class="hiw-art-bar"></span>
          </div>
          <div class="hiw-journey-copy">
            <span class="hiw-journey-phase">Speech-to-Text</span>
            <h3>Transcribe</h3>
            <p>Real-time STT across 9 providers — 22 Indian languages, structured text in under 500ms.</p>
            <span class="hiw-journey-more">View step details</span>
          </div>
        </div>
      </li>
      <li class="hiw-journey-step reveal click-detail" data-detail="hiw-reason" tabindex="0">
        <div class="hiw-journey-pin"><span>03</span></div>
        <div class="hiw-journey-panel">
          <div class="hiw-journey-art hiw-journey-art--reason" aria-hidden="true">
            <span class="hiw-art-core"></span>
            <span class="hiw-art-orbit"></span>
          </div>
          <div class="hiw-journey-copy">
            <span class="hiw-journey-phase">Intelligence</span>
            <h3>Reason</h3>
            <p>GPT, Claude, Gemini, Qwen, or Grok — intent, sentiment, and risk analyzed in real time.</p>
            <span class="hiw-journey-more">View step details</span>
          </div>
        </div>
      </li>
      <li class="hiw-journey-step reveal click-detail" data-detail="hiw-act" tabindex="0">
        <div class="hiw-journey-pin"><span>04</span></div>
        <div class="hiw-journey-panel">
          <div class="hiw-journey-art hiw-journey-art--act" aria-hidden="true">
            <span class="hiw-art-node"></span><span class="hiw-art-node"></span><span class="hiw-art-node hiw-art-node--active"></span>
          </div>
          <div class="hiw-journey-copy">
            <span class="hiw-journey-phase">Automation</span>
            <h3>Act</h3>
            <p>Triggers fire automatically — WhatsApp, CRM, calendars. No human in the loop required.</p>
            <span class="hiw-journey-more">View step details</span>
          </div>
        </div>
      </li>
    </ol>
  </div>
</section>'''

HIW_CSS = r"""
/* ═══ HOW IT WORKS — blueprint journey (no pipeline / no cards) ═══ */
#how-it-works.hiw-stage {
  position: relative !important;
  overflow: hidden !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto 4rem !important;
  padding: 3rem clamp(1.25rem, 4vw, 2.5rem) 2.5rem !important;
  border-radius: 12px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  box-shadow: none !important;
  isolation: isolate !important;
  scroll-margin-top: 100px !important;
}
#how-it-works .hiw-mesh {
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  z-index: 0 !important;
  opacity: 0.5 !important;
  background-image:
    linear-gradient(rgba(74, 101, 139, 0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(74, 101, 139, 0.06) 1px, transparent 1px) !important;
  background-size: 24px 24px !important;
  mask-image: radial-gradient(ellipse 90% 80% at 50% 40%, #000 15%, transparent 70%) !important;
}
#how-it-works .hiw-mesh-lines {
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  z-index: 0 !important;
  background:
    radial-gradient(circle at 8% 12%, rgba(74, 101, 139, 0.1) 0%, transparent 38%),
    radial-gradient(circle at 92% 88%, rgba(24, 52, 93, 0.08) 0%, transparent 36%) !important;
}
#how-it-works .hiw-glow,
#how-it-works .hiw-step-glow {
  display: none !important;
}
#how-it-works .hiw-head {
  position: relative !important;
  z-index: 2 !important;
  text-align: center !important;
  margin-bottom: 2rem !important;
}
#how-it-works .section-kicker,
#how-it-works .hiw-head .section-kicker {
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
}
#how-it-works .section-kicker::before,
#how-it-works .hiw-head .section-kicker::before {
  display: none !important;
}
#how-it-works .hiw-head h2 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.75rem, 3.5vw, 2.25rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.02em !important;
  color: #0f172a !important;
  margin-bottom: 0.5rem !important;
}
#how-it-works .hiw-head p {
  color: #64748b !important;
  max-width: 520px !important;
  margin: 0 auto !important;
  line-height: 1.65 !important;
  font-size: 0.95rem !important;
}
/* Blueprint canvas */
#how-it-works .hiw-blueprint {
  position: relative !important;
  z-index: 2 !important;
  padding: 1.75rem clamp(1rem, 3vw, 2rem) 1.5rem !important;
  border-radius: 10px !important;
  border: 1px solid #e2e8f0 !important;
  background:
    linear-gradient(180deg, rgba(248, 250, 252, 0.95) 0%, #ffffff 42%, #ffffff 100%) !important;
}
#how-it-works .hiw-blueprint-label {
  position: absolute !important;
  top: 1rem !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  white-space: nowrap !important;
}
#how-it-works .hiw-frame {
  position: absolute !important;
  width: 18px !important;
  height: 18px !important;
  border-color: #4A658B !important;
  border-style: solid !important;
  opacity: 0.45 !important;
  pointer-events: none !important;
}
#how-it-works .hiw-frame--tl { top: 0.85rem; left: 0.85rem; border-width: 2px 0 0 2px; }
#how-it-works .hiw-frame--tr { top: 0.85rem; right: 0.85rem; border-width: 2px 2px 0 0; }
#how-it-works .hiw-frame--bl { bottom: 0.85rem; left: 0.85rem; border-width: 0 0 2px 2px; }
#how-it-works .hiw-frame--br { bottom: 0.85rem; right: 0.85rem; border-width: 0 2px 2px 0; }
#how-it-works .hiw-blueprint-svg {
  position: relative !important;
  z-index: 1 !important;
  display: block !important;
  width: 100% !important;
  height: 48px !important;
  margin: 1.5rem 0 0.25rem !important;
  max-width: 100% !important;
}
#how-it-works .hiw-journey {
  position: relative !important;
  z-index: 2 !important;
  list-style: none !important;
  margin: 0 !important;
  padding: 0.5rem 0 0 !important;
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 1rem 0.75rem !important;
}
#how-it-works .hiw-journey-step {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  margin: 0 !important;
  padding: 0 !important;
  cursor: pointer !important;
  outline: none !important;
}
#how-it-works .hiw-journey-pin {
  width: 44px !important;
  height: 44px !important;
  margin-bottom: 0.65rem !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: linear-gradient(135deg, #4A658B 0%, #18345D 100%) !important;
  border: 2px solid #ffffff !important;
  box-shadow: 0 4px 12px rgba(24, 52, 93, 0.2) !important;
  transition: box-shadow 0.2s ease, transform 0.2s ease !important;
}
#how-it-works .hiw-journey-pin span {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.78rem !important;
  font-weight: 600 !important;
  color: #ffffff !important;
  letter-spacing: 0.04em !important;
}
#how-it-works .hiw-journey-panel {
  width: 100% !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 0.65rem !important;
  padding: 0.85rem 0.75rem 1rem !important;
  border-radius: 8px !important;
  border: 1px solid #e2e8f0 !important;
  background: #ffffff !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
#how-it-works .hiw-journey-step:hover .hiw-journey-panel,
#how-it-works .hiw-journey-step:focus-visible .hiw-journey-panel {
  border-color: #cbd5e1 !important;
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.07) !important;
}
#how-it-works .hiw-journey-step:hover .hiw-journey-pin,
#how-it-works .hiw-journey-step:focus-visible .hiw-journey-pin {
  box-shadow: 0 6px 18px rgba(24, 52, 93, 0.28) !important;
}
#how-it-works .hiw-journey-art {
  min-height: 52px !important;
  border-radius: 6px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  position: relative !important;
  overflow: hidden !important;
}
#how-it-works .hiw-journey-art--connect .hiw-art-ring {
  width: 28px !important;
  height: 28px !important;
  border-radius: 50% !important;
  border: 2px solid #4A658B !important;
  opacity: 0.5 !important;
}
#how-it-works .hiw-journey-art--connect .hiw-art-signal {
  position: absolute !important;
  width: 8px !important;
  height: 8px !important;
  border-radius: 50% !important;
  background: #4A658B !important;
}
#how-it-works .hiw-journey-art--transcribe {
  gap: 4px !important;
  align-items: flex-end !important;
  padding-bottom: 10px !important;
}
#how-it-works .hiw-art-bar {
  width: 5px !important;
  border-radius: 2px !important;
  background: #4A658B !important;
  height: 14px !important;
}
#how-it-works .hiw-art-bar:nth-child(2) { height: 22px !important; background: #6b87ab !important; }
#how-it-works .hiw-art-bar:nth-child(3) { height: 32px !important; }
#how-it-works .hiw-art-bar:nth-child(4) { height: 18px !important; background: #6b87ab !important; }
#how-it-works .hiw-art-bar:nth-child(5) { height: 26px !important; background: #18345D !important; }
#how-it-works .hiw-journey-art--reason .hiw-art-core {
  width: 10px !important;
  height: 10px !important;
  border-radius: 50% !important;
  background: #4A658B !important;
  z-index: 1 !important;
}
#how-it-works .hiw-journey-art--reason .hiw-art-orbit {
  position: absolute !important;
  width: 32px !important;
  height: 32px !important;
  border: 1px dashed #cbd5e1 !important;
  border-radius: 50% !important;
}
#how-it-works .hiw-journey-art--act {
  gap: 6px !important;
}
#how-it-works .hiw-art-node {
  width: 22px !important;
  height: 10px !important;
  border-radius: 4px !important;
  background: #e2e8f0 !important;
}
#how-it-works .hiw-art-node--active {
  background: linear-gradient(135deg, #4A658B, #18345D) !important;
}
#how-it-works .hiw-journey-phase {
  display: inline-block !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #4A658B !important;
  margin-bottom: 0.35rem !important;
}
#how-it-works .hiw-journey-copy h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.95rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 0 0.4rem !important;
  line-height: 1.25 !important;
  transition: color 0.2s ease !important;
}
#how-it-works .hiw-journey-step:hover .hiw-journey-copy h3,
#how-it-works .hiw-journey-step:focus-visible .hiw-journey-copy h3 {
  color: #4A658B !important;
}
#how-it-works .hiw-journey-copy p {
  font-size: 0.78rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  margin: 0 0 0.5rem !important;
}
#how-it-works .hiw-journey-more {
  font-size: 0.58rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  transition: color 0.2s ease !important;
}
#how-it-works .hiw-journey-step:hover .hiw-journey-more,
#how-it-works .hiw-journey-step:focus-visible .hiw-journey-more {
  color: #4A658B !important;
}
#how-it-works .hiw-journey-step.reveal {
  opacity: 0 !important;
  transform: translateY(20px) !important;
  transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#how-it-works .hiw-journey-step.reveal.in {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
#how-it-works .hiw-journey-step.reveal:nth-child(1) { transition-delay: 0.05s !important; }
#how-it-works .hiw-journey-step.reveal:nth-child(2) { transition-delay: 0.12s !important; }
#how-it-works .hiw-journey-step.reveal:nth-child(3) { transition-delay: 0.19s !important; }
#how-it-works .hiw-journey-step.reveal:nth-child(4) { transition-delay: 0.26s !important; }
@media (max-width: 900px) {
  #how-it-works .hiw-journey {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 1.25rem 0.85rem !important;
  }
  #how-it-works .hiw-blueprint-svg {
    display: none !important;
  }
  #how-it-works.hiw-stage {
    margin-inline: 1rem !important;
    padding: 2.5rem 1.25rem 2rem !important;
  }
}
@media (max-width: 560px) {
  #how-it-works .hiw-journey {
    grid-template-columns: 1fr !important;
  }
  #how-it-works .hiw-blueprint-label {
    position: static !important;
    transform: none !important;
    text-align: center !important;
    margin-bottom: 0.75rem !important;
  }
}
@media (max-width: 520px) {
  #how-it-works.hiw-stage {
    border-radius: 10px !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  #how-it-works .hiw-journey-step.reveal {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }
}

"""

CSS_START = "/* ═══ HOW IT WORKS —"
CSS_END = "/* ═══ ELEGANT FEATURES — refined shell (HIW cards below) ═══ */"


def main():
    html = PATH.read_text(encoding="utf-8")
    html = re.sub(
        r'<section id="how-it-works"[^>]*>.*?</section>',
        HIW_HTML,
        html,
        count=1,
        flags=re.DOTALL,
    )
    i = html.find(CSS_START)
    j = html.find(CSS_END, i)
    if i < 0 or j < 0:
        raise SystemExit("CSS markers not found")
    html = html[:i] + HIW_CSS + "\n\n" + html[j:]
    PATH.write_text(html, encoding="utf-8")
    print("HIW blueprint applied")


if __name__ == "__main__":
    main()
