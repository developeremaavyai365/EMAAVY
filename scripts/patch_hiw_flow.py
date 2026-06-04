#!/usr/bin/env python3
"""Upgrade How It Works with flow diagram, grid mesh, template panels — navy theme."""
from pathlib import Path
import re

PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

HIW_HTML = '''<section id="how-it-works" class="hiw-stage">
  <div class="hiw-mesh" aria-hidden="true"></div>
  <div class="hiw-mesh-lines" aria-hidden="true"></div>
  <div class="hiw-head reveal">
    <span class="section-kicker">The EMAAVY Method</span>
    <h2>How it works</h2>
    <p>From the first ring to the final insight — four steps that turn every call into compounding intelligence.</p>
  </div>
  <div class="hiw-flow-band reveal" aria-label="End-to-end process flow">
    <p class="hiw-flow-kicker">Live pipeline</p>
    <div class="hiw-flow-diagram">
      <div class="hiw-flow-node">
        <span class="hiw-flow-node-ring"><span class="hiw-flow-node-num">1</span></span>
        <span class="hiw-flow-node-label">Connect</span>
      </div>
      <div class="hiw-flow-bridge" aria-hidden="true"><span class="hiw-flow-bridge-line"></span><span class="hiw-flow-bridge-arrow"></span></div>
      <div class="hiw-flow-node">
        <span class="hiw-flow-node-ring"><span class="hiw-flow-node-num">2</span></span>
        <span class="hiw-flow-node-label">Transcribe</span>
      </div>
      <div class="hiw-flow-bridge" aria-hidden="true"><span class="hiw-flow-bridge-line"></span><span class="hiw-flow-bridge-arrow"></span></div>
      <div class="hiw-flow-node">
        <span class="hiw-flow-node-ring"><span class="hiw-flow-node-num">3</span></span>
        <span class="hiw-flow-node-label">Reason</span>
      </div>
      <div class="hiw-flow-bridge" aria-hidden="true"><span class="hiw-flow-bridge-line"></span><span class="hiw-flow-bridge-arrow"></span></div>
      <div class="hiw-flow-node">
        <span class="hiw-flow-node-ring"><span class="hiw-flow-node-num">4</span></span>
        <span class="hiw-flow-node-label">Act</span>
      </div>
    </div>
    <div class="hiw-flow-metrics">
      <span class="hiw-flow-metric"><b>&lt;500ms</b> transcription</span>
      <span class="hiw-flow-metric"><b>22</b> languages</span>
      <span class="hiw-flow-metric"><b>Real-time</b> intelligence</span>
      <span class="hiw-flow-metric"><b>Zero</b> manual handoff</span>
    </div>
  </div>
  <div class="hiw-steps hiw-steps--pipeline">
    <article class="hiw-step reveal click-detail" data-detail="hiw-connect" tabindex="0">
      <div class="hiw-step-num">1</div>
      <div class="hiw-step-template hiw-step-template--connect" aria-hidden="true">
        <div class="hiw-tpl-chrome"><span></span><span></span><span></span></div>
        <div class="hiw-tpl-body"><span class="hiw-tpl-pulse"></span><span class="hiw-tpl-line w80"></span><span class="hiw-tpl-line w60"></span></div>
      </div>
      <span class="hiw-step-icon" aria-hidden="true"></span>
      <h4>Connect</h4>
      <p>Plug in your telephony via Vobiz. EMAAVY starts listening from the very first second of every call.</p>
      <span class="hiw-step-tag">Telephony</span>
      <span class="hiw-step-hint">Tap for details →</span>
    </article>
    <article class="hiw-step reveal click-detail" data-detail="hiw-transcribe" tabindex="0">
      <div class="hiw-step-num">2</div>
      <div class="hiw-step-template hiw-step-template--transcribe" aria-hidden="true">
        <div class="hiw-tpl-chrome"><span></span><span></span><span></span></div>
        <div class="hiw-tpl-wave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
      </div>
      <span class="hiw-step-icon" aria-hidden="true"></span>
      <h4>Transcribe</h4>
      <p>Real-time STT via your choice of 9 providers — in 22 Indian languages, structured text in under 500ms.</p>
      <span class="hiw-step-tag">Speech-to-Text</span>
      <span class="hiw-step-hint">Tap for details →</span>
    </article>
    <article class="hiw-step reveal click-detail" data-detail="hiw-reason" tabindex="0">
      <div class="hiw-step-num">3</div>
      <div class="hiw-step-template hiw-step-template--reason" aria-hidden="true">
        <div class="hiw-tpl-chrome"><span></span><span></span><span></span></div>
        <div class="hiw-tpl-neural"><span class="hiw-tpl-core"></span><span class="hiw-tpl-orbit"></span><span class="hiw-tpl-orbit hiw-tpl-orbit-b"></span></div>
      </div>
      <span class="hiw-step-icon" aria-hidden="true"></span>
      <h4>Reason</h4>
      <p>Your chosen LLM — GPT, Claude, Gemini, Qwen, or Grok — analyzes intent, sentiment, and risk in real time.</p>
      <span class="hiw-step-tag">Intelligence</span>
      <span class="hiw-step-hint">Tap for details →</span>
    </article>
    <article class="hiw-step reveal click-detail" data-detail="hiw-act" tabindex="0">
      <div class="hiw-step-num">4</div>
      <div class="hiw-step-template hiw-step-template--act" aria-hidden="true">
        <div class="hiw-tpl-chrome"><span></span><span></span><span></span></div>
        <div class="hiw-tpl-actions"><span class="hiw-tpl-chip"></span><span class="hiw-tpl-chip"></span><span class="hiw-tpl-chip hiw-tpl-chip--on"></span></div>
      </div>
      <span class="hiw-step-icon" aria-hidden="true"></span>
      <h4>Act</h4>
      <p>Triggers fire automatically — WhatsApp sends, CRM updates, calendars book. No human in the loop required.</p>
      <span class="hiw-step-tag">Automation</span>
      <span class="hiw-step-hint">Tap for details →</span>
    </article>
  </div>
</section>'''

HIW_CSS = r"""
/* ═══ HOW IT WORKS — flow diagram + grid mesh + template panels ═══ */
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
  opacity: 0.55 !important;
  background-image:
    linear-gradient(rgba(74, 101, 139, 0.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(74, 101, 139, 0.07) 1px, transparent 1px) !important;
  background-size: 28px 28px !important;
  mask-image: radial-gradient(ellipse 85% 75% at 50% 35%, #000 20%, transparent 72%) !important;
}
#how-it-works .hiw-mesh-lines {
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  z-index: 0 !important;
  background:
    radial-gradient(circle at 12% 18%, rgba(74, 101, 139, 0.09) 0%, transparent 42%),
    radial-gradient(circle at 88% 82%, rgba(24, 52, 93, 0.07) 0%, transparent 40%) !important;
}
#how-it-works .hiw-glow,
#how-it-works .hiw-step-glow {
  display: none !important;
}
#how-it-works .hiw-head {
  position: relative !important;
  z-index: 2 !important;
  text-align: center !important;
  margin-bottom: 1.75rem !important;
}
#how-it-works .section-kicker,
#how-it-works .hiw-head .section-kicker {
  display: inline-flex !important;
  align-items: center !important;
  gap: 0.5rem !important;
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
/* ── Flow diagram band ── */
#how-it-works .hiw-flow-band {
  position: relative !important;
  z-index: 2 !important;
  margin: 0 auto 2rem !important;
  padding: 1.35rem clamp(1rem, 3vw, 1.75rem) 1.25rem !important;
  border-radius: 10px !important;
  border: 1px solid #e2e8f0 !important;
  background: linear-gradient(165deg, #f8fafc 0%, #ffffff 55%, #f0f4f8 100%) !important;
}
#how-it-works .hiw-flow-kicker {
  display: block !important;
  text-align: center !important;
  font-size: 0.62rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: #4A658B !important;
  margin: 0 0 1rem !important;
}
#how-it-works .hiw-flow-diagram {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  flex-wrap: wrap !important;
  gap: 0.35rem 0.15rem !important;
  max-width: 720px !important;
  margin: 0 auto !important;
}
#how-it-works .hiw-flow-node {
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  gap: 0.45rem !important;
  min-width: 72px !important;
}
#how-it-works .hiw-flow-node-ring {
  width: 48px !important;
  height: 48px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: linear-gradient(135deg, #4A658B 0%, #18345D 100%) !important;
  border: 2px solid rgba(255, 255, 255, 0.9) !important;
  box-shadow: 0 4px 14px rgba(24, 52, 93, 0.18) !important;
}
#how-it-works .hiw-flow-node-num {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  color: #ffffff !important;
}
#how-it-works .hiw-flow-node-label {
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  letter-spacing: 0.02em !important;
}
#how-it-works .hiw-flow-bridge {
  display: flex !important;
  align-items: center !important;
  width: clamp(28px, 6vw, 52px) !important;
  height: 48px !important;
  flex-shrink: 0 !important;
}
#how-it-works .hiw-flow-bridge-line {
  flex: 1 !important;
  height: 2px !important;
  background: linear-gradient(90deg, #4A658B 0%, #94a3b8 55%, #cbd5e1 100%) !important;
  border-radius: 2px !important;
}
#how-it-works .hiw-flow-bridge-arrow {
  width: 0 !important;
  height: 0 !important;
  border-top: 4px solid transparent !important;
  border-bottom: 4px solid transparent !important;
  border-left: 6px solid #4A658B !important;
  margin-left: -1px !important;
}
#how-it-works .hiw-flow-metrics {
  display: flex !important;
  flex-wrap: wrap !important;
  justify-content: center !important;
  gap: 0.45rem !important;
  margin-top: 1.1rem !important;
  padding-top: 1rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
#how-it-works .hiw-flow-metric {
  font-size: 0.72rem !important;
  color: #64748b !important;
  padding: 0.35rem 0.65rem !important;
  border-radius: 6px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
}
#how-it-works .hiw-flow-metric b {
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  margin-right: 0.25rem !important;
}
/* ── Pipeline grid + cards ── */
#how-it-works .hiw-steps--pipeline {
  position: relative !important;
  z-index: 2 !important;
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 1rem !important;
}
#how-it-works .hiw-steps--pipeline::before {
  content: '' !important;
  position: absolute !important;
  top: 2.65rem !important;
  left: 10% !important;
  right: 10% !important;
  height: 2px !important;
  background: linear-gradient(90deg, transparent 0%, #4A658B 8%, #4A658B 92%, transparent 100%) !important;
  pointer-events: none !important;
  z-index: 0 !important;
  opacity: 0.35 !important;
}
#how-it-works .hiw-steps--pipeline .hiw-step {
  position: relative !important;
  z-index: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  padding: 1.15rem 1rem 1.1rem !important;
  border-radius: 10px !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: none !important;
  cursor: pointer !important;
  overflow: hidden !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
#how-it-works .hiw-steps--pipeline .hiw-step::after {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  height: 3px !important;
  background: linear-gradient(90deg, #4A658B, #6b87ab) !important;
  opacity: 0 !important;
  transition: opacity 0.2s ease !important;
}
#how-it-works .hiw-steps--pipeline .hiw-step:hover::after,
#how-it-works .hiw-steps--pipeline .hiw-step:focus-visible::after {
  opacity: 1 !important;
}
#how-it-works .hiw-steps--pipeline .hiw-step:hover,
#how-it-works .hiw-steps--pipeline .hiw-step:focus-visible {
  border-color: #cbd5e1 !important;
  box-shadow: 0 6px 20px rgba(15, 23, 42, 0.07) !important;
  outline: none !important;
  transform: none !important;
}
#how-it-works .hiw-step-num {
  position: relative !important;
  z-index: 2 !important;
  width: 40px !important;
  height: 40px !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 0.65rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-weight: 600 !important;
  font-size: 1rem !important;
  color: #ffffff !important;
  background: #4A658B !important;
  border: 2px solid #ffffff !important;
  box-shadow: 0 2px 8px rgba(24, 52, 93, 0.15) !important;
  transition: background 0.2s ease !important;
}
#how-it-works .hiw-step:hover .hiw-step-num,
#how-it-works .hiw-step:focus-visible .hiw-step-num {
  background: #18345D !important;
}
#how-it-works .hiw-step-icon {
  display: none !important;
}
/* Template mini-panels */
#how-it-works .hiw-step-template {
  width: 100% !important;
  max-width: 168px !important;
  margin: 0 auto 0.75rem !important;
  padding: 0.5rem 0.55rem 0.55rem !important;
  border-radius: 8px !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
}
#how-it-works .hiw-tpl-chrome {
  display: flex !important;
  gap: 0.28rem !important;
  margin-bottom: 0.45rem !important;
}
#how-it-works .hiw-tpl-chrome span {
  width: 5px !important;
  height: 5px !important;
  border-radius: 50% !important;
  background: #cbd5e1 !important;
}
#how-it-works .hiw-tpl-chrome span:first-child { background: #4A658B !important; }
#how-it-works .hiw-tpl-chrome span:nth-child(2) { background: #6b87ab !important; }
#how-it-works .hiw-tpl-chrome span:nth-child(3) { background: #18345D !important; }
#how-it-works .hiw-tpl-body {
  display: flex !important;
  flex-direction: column !important;
  gap: 0.35rem !important;
  align-items: flex-start !important;
}
#how-it-works .hiw-tpl-pulse {
  width: 10px !important;
  height: 10px !important;
  border-radius: 50% !important;
  background: #4A658B !important;
  opacity: 0.85 !important;
}
#how-it-works .hiw-tpl-line {
  display: block !important;
  height: 4px !important;
  border-radius: 3px !important;
  background: #e2e8f0 !important;
}
#how-it-works .hiw-tpl-line.w80 { width: 80% !important; }
#how-it-works .hiw-tpl-line.w60 { width: 60% !important; background: #cbd5e1 !important; }
#how-it-works .hiw-tpl-wave {
  display: flex !important;
  align-items: flex-end !important;
  justify-content: center !important;
  gap: 3px !important;
  height: 28px !important;
}
#how-it-works .hiw-tpl-wave i {
  display: block !important;
  width: 4px !important;
  border-radius: 2px !important;
  background: #4A658B !important;
  height: 35% !important;
}
#how-it-works .hiw-tpl-wave i:nth-child(2) { height: 55% !important; background: #6b87ab !important; }
#how-it-works .hiw-tpl-wave i:nth-child(3) { height: 80% !important; }
#how-it-works .hiw-tpl-wave i:nth-child(4) { height: 50% !important; }
#how-it-works .hiw-tpl-wave i:nth-child(5) { height: 90% !important; background: #18345D !important; }
#how-it-works .hiw-tpl-wave i:nth-child(6) { height: 45% !important; }
#how-it-works .hiw-tpl-wave i:nth-child(7) { height: 65% !important; background: #6b87ab !important; }
#how-it-works .hiw-tpl-neural {
  position: relative !important;
  height: 36px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}
#how-it-works .hiw-tpl-core {
  width: 12px !important;
  height: 12px !important;
  border-radius: 50% !important;
  background: #4A658B !important;
  position: relative !important;
  z-index: 1 !important;
}
#how-it-works .hiw-tpl-orbit {
  position: absolute !important;
  width: 28px !important;
  height: 28px !important;
  border: 1px solid #cbd5e1 !important;
  border-radius: 50% !important;
}
#how-it-works .hiw-tpl-orbit-b {
  width: 20px !important;
  height: 20px !important;
  border-color: #4A658B !important;
  opacity: 0.45 !important;
}
#how-it-works .hiw-tpl-actions {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 0.3rem !important;
  justify-content: center !important;
}
#how-it-works .hiw-tpl-chip {
  width: 36px !important;
  height: 14px !important;
  border-radius: 4px !important;
  background: #e2e8f0 !important;
}
#how-it-works .hiw-tpl-chip--on {
  background: linear-gradient(135deg, #4A658B, #18345D) !important;
}
#how-it-works .hiw-step h4 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.4rem !important;
  transition: color 0.2s ease !important;
}
#how-it-works .hiw-step:hover h4,
#how-it-works .hiw-step:focus-visible h4 {
  color: #4A658B !important;
}
#how-it-works .hiw-step p {
  font-size: 0.82rem !important;
  color: #64748b !important;
  line-height: 1.55 !important;
  margin: 0 0 0.75rem !important;
}
#how-it-works .hiw-step-tag {
  margin-top: auto !important;
  font-size: 0.6rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 4px !important;
  padding: 0.25rem 0.55rem !important;
  transition: background 0.2s ease, border-color 0.2s ease, color 0.2s ease !important;
}
#how-it-works .hiw-step:hover .hiw-step-tag,
#how-it-works .hiw-step:focus-visible .hiw-step-tag {
  background: #f0f4f8 !important;
  border-color: #cbd5e1 !important;
  color: #4A658B !important;
}
#how-it-works .hiw-step-hint {
  margin-top: 0.5rem !important;
  font-size: 0.6rem !important;
  font-weight: 500 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #94a3b8 !important;
  transition: color 0.2s ease !important;
}
#how-it-works .hiw-step:hover .hiw-step-hint,
#how-it-works .hiw-step:focus-visible .hiw-step-hint {
  color: #64748b !important;
}
@media (max-width: 900px) {
  #how-it-works .hiw-steps--pipeline {
    grid-template-columns: repeat(2, 1fr) !important;
  }
  #how-it-works .hiw-steps--pipeline::before {
    display: none !important;
  }
  #how-it-works .hiw-flow-bridge {
    width: 36px !important;
  }
  #how-it-works.hiw-stage {
    margin-inline: 1rem !important;
    padding: 2.5rem 1.25rem 2rem !important;
  }
}
@media (max-width: 640px) {
  #how-it-works .hiw-flow-diagram {
    display: grid !important;
    grid-template-columns: 1fr auto 1fr !important;
    justify-items: center !important;
    max-width: 280px !important;
  }
  #how-it-works .hiw-flow-bridge {
    width: 2px !important;
    height: 24px !important;
    flex-direction: column !important;
    grid-column: 2 !important;
  }
  #how-it-works .hiw-flow-bridge-line {
    width: 2px !important;
    height: 100% !important;
    background: linear-gradient(180deg, #4A658B, #cbd5e1) !important;
  }
  #how-it-works .hiw-flow-bridge-arrow {
    border-left: 4px solid transparent !important;
    border-right: 4px solid transparent !important;
    border-top: 6px solid #4A658B !important;
    border-bottom: none !important;
    margin: -2px 0 0 0 !important;
  }
  #how-it-works .hiw-flow-node {
    grid-column: 1 / -1 !important;
  }
  #how-it-works .hiw-steps--pipeline {
    grid-template-columns: 1fr !important;
  }
}
@media (max-width: 520px) {
  #how-it-works.hiw-stage {
    border-radius: 10px !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  #how-it-works .hiw-step,
  #how-it-works .hiw-flow-band {
    transition: none !important;
  }
}

"""

CSS_START = "/* ═══ ELEGANT HIW — refined, no glow ═══ */"
CSS_END = "/* ═══ ELEGANT FEATURES — refined shell (HIW cards below) ═══ */"


def main():
    html = PATH.read_text(encoding="utf-8")
    # Replace section HTML
    html = re.sub(
        r'<section id="how-it-works"[^>]*>.*?</section>',
        HIW_HTML,
        html,
        count=1,
        flags=re.DOTALL,
    )
    # Replace CSS block
    i = html.find(CSS_START)
    j = html.find(CSS_END, i)
    if i < 0 or j < 0:
        raise SystemExit("HIW CSS markers not found")
    html = html[:i] + HIW_CSS + "\n\n" + html[j:]
    PATH.write_text(html, encoding="utf-8")
    print("Patched How It Works flow + templates")


if __name__ == "__main__":
    main()
