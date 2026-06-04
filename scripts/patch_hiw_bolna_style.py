#!/usr/bin/env python3
"""HIW: Bolna-inspired staggered flow + code panel, EMAAVY colors."""
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
  <div class="hiw-split reveal">
    <div class="hiw-flow-col" aria-label="Process steps">
      <svg class="hiw-flow-arrows" viewBox="0 0 280 520" preserveAspectRatio="xMidYMid meet" aria-hidden="true">
        <path class="hiw-arrow-path" d="M 200 88 C 240 110, 248 130, 200 152" fill="none" stroke="#4A658B" stroke-width="2.5" stroke-linecap="round" opacity="0.45"/>
        <path class="hiw-arrow-path" d="M 80 208 C 40 230, 32 250, 80 272" fill="none" stroke="#4A658B" stroke-width="2.5" stroke-linecap="round" opacity="0.45"/>
        <path class="hiw-arrow-path" d="M 200 328 C 240 350, 248 370, 200 392" fill="none" stroke="#18345D" stroke-width="2.5" stroke-linecap="round" opacity="0.5"/>
        <polygon points="196,148 208,152 196,158" fill="#4A658B" opacity="0.55"/>
        <polygon points="84,268 72,272 84,278" fill="#4A658B" opacity="0.55"/>
        <polygon points="196,388 208,392 196,398" fill="#18345D" opacity="0.6"/>
      </svg>
      <ol class="hiw-flow-steps">
        <li class="hiw-flow-card hiw-flow-card--a reveal click-detail" data-detail="hiw-connect" tabindex="0">
          <span class="hiw-flow-card-kicker">Step one</span>
          <span class="hiw-flow-card-num" aria-hidden="true">1</span>
          <h3>Connect</h3>
          <p>Plug in telephony via Vobiz — EMAAVY listens from the first second of every call.</p>
        </li>
        <li class="hiw-flow-card hiw-flow-card--b reveal click-detail" data-detail="hiw-transcribe" tabindex="0">
          <span class="hiw-flow-card-kicker">Step two</span>
          <span class="hiw-flow-card-num" aria-hidden="true">2</span>
          <h3>Transcribe</h3>
          <p>Real-time speech-to-text across nine providers, 22 languages, under 500ms.</p>
        </li>
        <li class="hiw-flow-card hiw-flow-card--c reveal click-detail" data-detail="hiw-reason" tabindex="0">
          <span class="hiw-flow-card-kicker">Step three</span>
          <span class="hiw-flow-card-num" aria-hidden="true">3</span>
          <h3>Reason</h3>
          <p>Your LLM analyzes intent, sentiment, and risk on every live conversation.</p>
        </li>
        <li class="hiw-flow-card hiw-flow-card--d reveal click-detail" data-detail="hiw-act" tabindex="0">
          <span class="hiw-flow-card-kicker">Step four</span>
          <span class="hiw-flow-card-num" aria-hidden="true">4</span>
          <h3>Act</h3>
          <p>Automations fire — WhatsApp, CRM updates, and calendar booking without handoffs.</p>
        </li>
      </ol>
    </div>
    <div class="hiw-code-col">
      <div class="hiw-code-window reveal" aria-label="EMAAVY API integration example">
        <div class="hiw-code-titlebar">
          <span class="hiw-code-dot hiw-code-dot--close"></span>
          <span class="hiw-code-dot hiw-code-dot--min"></span>
          <span class="hiw-code-dot hiw-code-dot--max"></span>
          <span class="hiw-code-title">integration.py</span>
        </div>
        <div class="hiw-code-body">
          <pre><code><span class="hiw-c-kw">import</span> <span class="hiw-c-mod">requests</span>

<span class="hiw-c-id">url</span> = <span class="hiw-c-str">"https://api.emaavy.com/v1/calls"</span>
<span class="hiw-c-id">payload</span> = {
    <span class="hiw-c-str">"agent_id"</span>: <span class="hiw-c-str">"your-agent-id"</span>,
    <span class="hiw-c-str">"recipient"</span>: <span class="hiw-c-str">"+91XXXXXXXXXX"</span>,
    <span class="hiw-c-str">"telephony"</span>: <span class="hiw-c-str">"vobiz"</span>,
    <span class="hiw-c-str">"stt"</span>: <span class="hiw-c-str">"deepgram"</span>,
    <span class="hiw-c-str">"llm"</span>: <span class="hiw-c-str">"gpt-4o"</span>,
}
<span class="hiw-c-id">headers</span> = {
    <span class="hiw-c-str">"Authorization"</span>: <span class="hiw-c-str">"Bearer YOUR_API_KEY"</span>,
    <span class="hiw-c-str">"Content-Type"</span>: <span class="hiw-c-str">"application/json"</span>,
}

<span class="hiw-c-id">response</span> = <span class="hiw-c-fn">requests.post</span>(url, json=payload, headers=headers)
<span class="hiw-c-fn">print</span>(response.json())</code></pre>
        </div>
      </div>
    </div>
  </div>
</section>'''

HIW_CSS = r"""
/* ═══ HOW IT WORKS — staggered flow + integration panel (EMAAVY) ═══ */
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
  opacity: 0.65 !important;
  background-image:
    linear-gradient(rgba(74, 101, 139, 0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(74, 101, 139, 0.08) 1px, transparent 1px) !important;
  background-size: 32px 32px !important;
  mask-image: radial-gradient(ellipse 95% 85% at 50% 45%, #000 10%, transparent 75%) !important;
}
#how-it-works .hiw-mesh-lines {
  position: absolute !important;
  inset: 0 !important;
  pointer-events: none !important;
  z-index: 0 !important;
  background:
    radial-gradient(circle at 18% 22%, rgba(74, 101, 139, 0.07) 0%, transparent 45%),
    radial-gradient(circle at 82% 78%, rgba(24, 52, 93, 0.06) 0%, transparent 42%) !important;
}
#how-it-works .hiw-glow,
#how-it-works .hiw-step-glow {
  display: none !important;
}
#how-it-works .hiw-head {
  position: relative !important;
  z-index: 2 !important;
  text-align: center !important;
  margin-bottom: 2.25rem !important;
}
#how-it-works .section-kicker,
#how-it-works .hiw-head .section-kicker {
  display: inline-flex !important;
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
/* Two-column split */
#how-it-works .hiw-split {
  position: relative !important;
  z-index: 2 !important;
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.05fr) !important;
  gap: clamp(1.5rem, 4vw, 2.75rem) !important;
  align-items: center !important;
}
/* Left: staggered flow */
#how-it-works .hiw-flow-col {
  position: relative !important;
  min-height: 420px !important;
  padding: 0.25rem 0 !important;
}
#how-it-works .hiw-flow-arrows {
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 100% !important;
  height: 100% !important;
  pointer-events: none !important;
  z-index: 0 !important;
}
#how-it-works .hiw-flow-steps {
  position: relative !important;
  z-index: 1 !important;
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  display: flex !important;
  flex-direction: column !important;
  gap: 1.1rem !important;
}
#how-it-works .hiw-flow-card {
  position: relative !important;
  display: block !important;
  padding: 1.15rem 1.2rem 1.1rem !important;
  border-radius: 10px !important;
  border: 1px solid rgba(74, 101, 139, 0.18) !important;
  cursor: pointer !important;
  outline: none !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease !important;
  max-width: 92% !important;
}
#how-it-works .hiw-flow-card--a {
  margin-right: auto !important;
  background: linear-gradient(135deg, #f0f4f8 0%, #ffffff 100%) !important;
}
#how-it-works .hiw-flow-card--b {
  margin-left: auto !important;
  margin-right: 0 !important;
  background: linear-gradient(135deg, rgba(74, 101, 139, 0.12) 0%, rgba(74, 101, 139, 0.04) 100%) !important;
  border-color: rgba(74, 101, 139, 0.28) !important;
}
#how-it-works .hiw-flow-card--c {
  margin-right: auto !important;
  background: #ffffff !important;
  box-shadow: inset 3px 0 0 #4A658B !important;
}
#how-it-works .hiw-flow-card--d {
  margin-left: auto !important;
  margin-right: 0 !important;
  background: linear-gradient(135deg, rgba(24, 52, 93, 0.1) 0%, #f8fafc 100%) !important;
  border-color: rgba(24, 52, 93, 0.22) !important;
}
#how-it-works .hiw-flow-card:hover,
#how-it-works .hiw-flow-card:focus-visible {
  border-color: #4A658B !important;
  box-shadow: 0 10px 28px rgba(24, 52, 93, 0.1) !important;
  transform: translateY(-1px) !important;
}
#how-it-works .hiw-flow-card-kicker {
  display: block !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  color: #4A658B !important;
  margin-bottom: 0.35rem !important;
}
#how-it-works .hiw-flow-card-num {
  position: absolute !important;
  top: 0.85rem !important;
  right: 1rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(2rem, 5vw, 2.75rem) !important;
  font-weight: 600 !important;
  line-height: 1 !important;
  color: rgba(74, 101, 139, 0.22) !important;
  pointer-events: none !important;
}
#how-it-works .hiw-flow-card--d .hiw-flow-card-num {
  color: rgba(24, 52, 93, 0.2) !important;
}
#how-it-works .hiw-flow-card h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.05rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 2.5rem 0.4rem 0 !important;
  line-height: 1.2 !important;
  transition: color 0.2s ease !important;
}
#how-it-works .hiw-flow-card:hover h3,
#how-it-works .hiw-flow-card:focus-visible h3 {
  color: #4A658B !important;
}
#how-it-works .hiw-flow-card p {
  font-size: 0.82rem !important;
  line-height: 1.55 !important;
  color: #475569 !important;
  margin: 0 !important;
  max-width: 28ch !important;
}
/* Right: code window */
#how-it-works .hiw-code-col {
  position: relative !important;
  min-width: 0 !important;
}
#how-it-works .hiw-code-window {
  border-radius: 12px !important;
  overflow: hidden !important;
  border: 1px solid #1e3a5f !important;
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.06) inset,
    0 20px 50px -12px rgba(24, 52, 93, 0.35) !important;
  background: #0f1f33 !important;
}
#how-it-works .hiw-code-titlebar {
  display: flex !important;
  align-items: center !important;
  gap: 0.4rem !important;
  padding: 0.65rem 0.85rem !important;
  background: #18345D !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
}
#how-it-works .hiw-code-dot {
  width: 10px !important;
  height: 10px !important;
  border-radius: 50% !important;
  flex-shrink: 0 !important;
}
#how-it-works .hiw-code-dot--close { background: #e8a0a0 !important; }
#how-it-works .hiw-code-dot--min { background: #e8d4a8 !important; }
#how-it-works .hiw-code-dot--max { background: #a8d4b8 !important; }
#how-it-works .hiw-code-title {
  flex: 1 !important;
  text-align: center !important;
  font-size: 0.72rem !important;
  font-weight: 500 !important;
  color: rgba(255, 255, 255, 0.72) !important;
  letter-spacing: 0.04em !important;
  margin-right: 2.2rem !important;
}
#how-it-works .hiw-code-body {
  padding: 0 !important;
  overflow: auto !important;
  max-height: min(420px, 52vh) !important;
  background: #0f1f33 !important;
}
#how-it-works .hiw-code-body pre {
  margin: 0 !important;
  padding: 1rem 1rem 1.15rem !important;
  font-family: ui-monospace, 'Cascadia Code', 'Consolas', monospace !important;
  font-size: 0.72rem !important;
  line-height: 1.65 !important;
  color: #c5d4e8 !important;
  tab-size: 2 !important;
}
#how-it-works .hiw-code-body code {
  font: inherit !important;
  color: inherit !important;
}
#how-it-works .hiw-c-kw { color: #7eb8ff !important; }
#how-it-works .hiw-c-mod { color: #a8c8f0 !important; }
#how-it-works .hiw-c-id { color: #8eb4e8 !important; }
#how-it-works .hiw-c-str { color: #d4b896 !important; }
#how-it-works .hiw-c-fn { color: #6b9fd4 !important; }
/* Reveal */
#how-it-works .hiw-flow-card.reveal,
#how-it-works .hiw-code-window.reveal {
  opacity: 0 !important;
  transform: translateY(18px) !important;
  transition: opacity 0.55s cubic-bezier(0.16, 1, 0.3, 1), transform 0.55s cubic-bezier(0.16, 1, 0.3, 1) !important;
}
#how-it-works .hiw-flow-card.reveal.in,
#how-it-works .hiw-code-window.reveal.in {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
#how-it-works .hiw-flow-card--a.reveal { transition-delay: 0.06s !important; }
#how-it-works .hiw-flow-card--b.reveal { transition-delay: 0.14s !important; }
#how-it-works .hiw-flow-card--c.reveal { transition-delay: 0.22s !important; }
#how-it-works .hiw-flow-card--d.reveal { transition-delay: 0.3s !important; }
#how-it-works .hiw-code-window.reveal { transition-delay: 0.12s !important; }
@media (max-width: 960px) {
  #how-it-works .hiw-split {
    grid-template-columns: 1fr !important;
    gap: 2rem !important;
  }
  #how-it-works .hiw-flow-col {
    min-height: 0 !important;
  }
  #how-it-works .hiw-flow-arrows {
    display: none !important;
  }
  #how-it-works .hiw-flow-card {
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }
  #how-it-works.hiw-stage {
    margin-inline: 1rem !important;
    padding: 2.5rem 1.25rem 2rem !important;
  }
}
@media (max-width: 520px) {
  #how-it-works.hiw-stage {
    border-radius: 10px !important;
  }
  #how-it-works .hiw-code-body pre {
    font-size: 0.65rem !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  #how-it-works .hiw-flow-card.reveal,
  #how-it-works .hiw-code-window.reveal {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }
  #how-it-works .hiw-flow-card:hover,
  #how-it-works .hiw-flow-card:focus-visible {
    transform: none !important;
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
        raise SystemExit("CSS block not found")
    html = html[:i] + HIW_CSS + "\n\n" + html[j:]
    PATH.write_text(html, encoding="utf-8")
    print("Bolna-style HIW applied")


if __name__ == "__main__":
    main()
