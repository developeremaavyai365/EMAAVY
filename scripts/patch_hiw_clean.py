#!/usr/bin/env python3
"""Remove integration.py panel; clean How It Works section."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

HIW_HTML = r'''<section id="how-it-works" class="hiw-stage">
  <div class="hiw-head reveal">
    <span class="section-kicker">The EMAAVY Method</span>
    <h2>How it works</h2>
    <p>Every call follows the same path — connect, understand, decide, and act — so your team gets insight without manual handoffs.</p>
  </div>
  <div class="hiw-pipeline reveal" aria-label="Four-step call intelligence flow">
    <ol class="hiw-steps-grid">
      <li class="hiw-step-card reveal click-detail" data-detail="hiw-connect" tabindex="0">
        <span class="hiw-step-badge" aria-hidden="true">1</span>
        <div class="hiw-step-body">
          <h3>Connect</h3>
          <p>Plug in telephony (Vobiz or your SIP stack). EMAAVY captures every inbound and outbound call from the first ring.</p>
        </div>
      </li>
      <li class="hiw-step-card reveal click-detail" data-detail="hiw-transcribe" tabindex="0">
        <span class="hiw-step-badge" aria-hidden="true">2</span>
        <div class="hiw-step-body">
          <h3>Transcribe</h3>
          <p>Speech-to-text streams in real time — nine providers, 22 languages, typically under 500ms latency.</p>
        </div>
      </li>
      <li class="hiw-step-card reveal click-detail" data-detail="hiw-reason" tabindex="0">
        <span class="hiw-step-badge" aria-hidden="true">3</span>
        <div class="hiw-step-body">
          <h3>Reason</h3>
          <p>Your chosen LLM scores intent, sentiment, objections, and compliance risk on every turn — while the call is still live.</p>
        </div>
      </li>
      <li class="hiw-step-card reveal click-detail" data-detail="hiw-act" tabindex="0">
        <span class="hiw-step-badge" aria-hidden="true">4</span>
        <div class="hiw-step-body">
          <h3>Act</h3>
          <p>Triggers fire automatically: CRM updates, WhatsApp follow-ups, calendar bookings, and coaching alerts — no copy-paste.</p>
        </div>
      </li>
    </ol>
  </div>
  <div class="hiw-outcomes reveal" aria-label="Key outcomes">
    <div class="hiw-outcome"><strong>&lt;500ms</strong><span>Live transcription</span></div>
    <div class="hiw-outcome"><strong>22</strong><span>Languages</span></div>
    <div class="hiw-outcome"><strong>Real-time</strong><span>Intent &amp; sentiment</span></div>
    <div class="hiw-outcome"><strong>Zero</strong><span>Manual handoff</span></div>
  </div>
</section>'''

HIW_CSS = r'''/* ═══ HOW IT WORKS — clear four-step pipeline ═══ */
#how-it-works.hiw-stage {
  position: relative !important;
  overflow: hidden !important;
  width: min(1200px, calc(100% - 2rem)) !important;
  margin: 0 auto 4rem !important;
  padding: clamp(2.5rem, 5vw, 3.5rem) clamp(1.25rem, 4vw, 2.5rem) !important;
  border-radius: 16px !important;
  border: 1px solid #e2e8f0 !important;
  background: linear-gradient(180deg, #f8fafc 0%, #ffffff 42%) !important;
  box-shadow: 0 12px 40px rgba(24, 52, 93, 0.06) !important;
  isolation: isolate !important;
  scroll-margin-top: 100px !important;
}
#how-it-works .hiw-glow,
#how-it-works .hiw-step-glow,
#how-it-works .hiw-flow-arrows,
#how-it-works .hiw-code-col {
  display: none !important;
}
#how-it-works .hiw-head {
  position: relative !important;
  z-index: 2 !important;
  text-align: center !important;
  margin-bottom: clamp(2rem, 4vw, 2.75rem) !important;
  max-width: 640px !important;
  margin-left: auto !important;
  margin-right: auto !important;
}
#how-it-works .section-kicker,
#how-it-works .hiw-head .section-kicker {
  display: inline-flex !important;
  font-size: 0.68rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  color: #4a658b !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 999px !important;
  padding: 0.4rem 0.95rem !important;
  margin-bottom: 1rem !important;
}
#how-it-works .section-kicker::before,
#how-it-works .hiw-head .section-kicker::before {
  display: none !important;
}
#how-it-works .hiw-head h2 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.85rem, 4vw, 2.5rem) !important;
  font-weight: 700 !important;
  letter-spacing: -0.03em !important;
  color: #0f172a !important;
  margin-bottom: 0.65rem !important;
  line-height: 1.1 !important;
}
#how-it-works .hiw-head p {
  color: #475569 !important;
  margin: 0 auto !important;
  line-height: 1.7 !important;
  font-size: 1.02rem !important;
}
#how-it-works .hiw-pipeline {
  position: relative !important;
  z-index: 2 !important;
  margin-bottom: 2rem !important;
}
#how-it-works .hiw-steps-grid {
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 1rem !important;
  position: relative !important;
}
#how-it-works .hiw-steps-grid::before {
  content: '' !important;
  position: absolute !important;
  top: 2.35rem !important;
  left: 12% !important;
  right: 12% !important;
  height: 2px !important;
  background: linear-gradient(90deg, #e2e8f0, #4a658b 20%, #4a658b 80%, #e2e8f0) !important;
  z-index: 0 !important;
  pointer-events: none !important;
}
#how-it-works .hiw-step-card {
  position: relative !important;
  z-index: 1 !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  padding: 0 0.5rem 1.25rem !important;
  border: none !important;
  background: transparent !important;
  cursor: pointer !important;
  outline: none !important;
  transition: transform 0.25s ease !important;
}
#how-it-works .hiw-step-badge {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 3.25rem !important;
  height: 3.25rem !important;
  margin-bottom: 1.1rem !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.1rem !important;
  font-weight: 700 !important;
  color: #ffffff !important;
  background: linear-gradient(135deg, #4a658b 0%, #18345d 100%) !important;
  border-radius: 50% !important;
  box-shadow: 0 8px 24px rgba(74, 101, 139, 0.35) !important;
  flex-shrink: 0 !important;
}
#how-it-works .hiw-step-card:nth-child(4) .hiw-step-badge {
  background: #18345d !important;
}
#how-it-works .hiw-step-body {
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 14px !important;
  padding: 1.25rem 1.1rem 1.2rem !important;
  width: 100% !important;
  box-sizing: border-box !important;
  min-height: 9.5rem !important;
  transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
}
#how-it-works .hiw-step-card:hover .hiw-step-body,
#how-it-works .hiw-step-card:focus-visible .hiw-step-body {
  border-color: #4a658b !important;
  box-shadow: 0 14px 32px rgba(24, 52, 93, 0.1) !important;
}
#how-it-works .hiw-step-card:hover,
#how-it-works .hiw-step-card:focus-visible {
  transform: translateY(-4px) !important;
}
#how-it-works .hiw-step-body h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.12rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin: 0 0 0.5rem !important;
  line-height: 1.2 !important;
}
#how-it-works .hiw-step-body p {
  font-size: 0.84rem !important;
  line-height: 1.6 !important;
  color: #64748b !important;
  margin: 0 !important;
}
#how-it-works .hiw-outcomes {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.75rem !important;
  padding: 1.25rem 1rem !important;
  background: #ffffff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 12px !important;
}
#how-it-works .hiw-outcome {
  text-align: center !important;
  padding: 0.35rem 0.5rem !important;
}
#how-it-works .hiw-outcome strong {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.35rem !important;
  font-weight: 700 !important;
  color: #18345d !important;
  line-height: 1.1 !important;
  margin-bottom: 0.2rem !important;
}
#how-it-works .hiw-outcome span {
  display: block !important;
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
#how-it-works .hiw-step-card.reveal {
  opacity: 0 !important;
  transform: translateY(16px) !important;
  transition: opacity 0.5s ease, transform 0.5s ease !important;
}
#how-it-works .hiw-step-card.reveal.in {
  opacity: 1 !important;
  transform: translateY(0) !important;
}
#how-it-works .hiw-step-card:nth-child(1).reveal { transition-delay: 0.05s !important; }
#how-it-works .hiw-step-card:nth-child(2).reveal { transition-delay: 0.12s !important; }
#how-it-works .hiw-step-card:nth-child(3).reveal { transition-delay: 0.19s !important; }
#how-it-works .hiw-step-card:nth-child(4).reveal { transition-delay: 0.26s !important; }
@media (max-width: 900px) {
  #how-it-works .hiw-steps-grid {
    grid-template-columns: 1fr 1fr !important;
    gap: 1.25rem !important;
  }
  #how-it-works .hiw-steps-grid::before {
    display: none !important;
  }
  #how-it-works .hiw-step-body {
    min-height: 0 !important;
  }
  #how-it-works .hiw-outcomes {
    grid-template-columns: 1fr 1fr !important;
  }
}
@media (max-width: 520px) {
  #how-it-works.hiw-stage {
    margin-inline: 1rem !important;
    border-radius: 12px !important;
  }
  #how-it-works .hiw-steps-grid {
    grid-template-columns: 1fr !important;
  }
  #how-it-works .hiw-step-card {
    flex-direction: row !important;
    align-items: flex-start !important;
    text-align: left !important;
    gap: 1rem !important;
    padding: 0 !important;
  }
  #how-it-works .hiw-step-badge {
    margin-bottom: 0 !important;
    width: 2.75rem !important;
    height: 2.75rem !important;
    font-size: 0.95rem !important;
  }
  #how-it-works .hiw-outcomes {
    grid-template-columns: 1fr !important;
  }
}
@media (prefers-reduced-motion: reduce) {
  #how-it-works .hiw-step-card.reveal {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }
  #how-it-works .hiw-step-card:hover,
  #how-it-works .hiw-step-card:focus-visible {
    transform: none !important;
  }
}

'''

HTML_START = "<!-- HOW IT WORKS -->"
HTML_END = "<!-- INTEGRATIONS HUB -->"
CSS_START = "/* ═══ HOW IT WORKS"
CSS_END = "/* ═══ ELEGANT FEATURES"


def patch_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    html_pat = re.compile(
        re.escape(HTML_START) + r"\s*<section id=\"how-it-works\".*?</section>\s*"
        + re.escape(HTML_END),
        re.DOTALL,
    )
    if not html_pat.search(text):
        raise SystemExit(f"HIW HTML block not found in {path}")
    text = html_pat.sub(HTML_START + " " + HIW_HTML + " " + HTML_END, text, count=1)

    css_pat = re.compile(
        re.escape(CSS_START) + r".*?(?=" + re.escape(CSS_END) + r")",
        re.DOTALL,
    )
    if not css_pat.search(text):
        raise SystemExit(f"HIW CSS block not found in {path}")
    text = css_pat.sub(HIW_CSS, text, count=1)

    path.write_text(text, encoding="utf-8")
    print("patched", path.relative_to(ROOT))


def main():
    for name in ("emaavy_white_blue (2).html", "index.html"):
        p = ROOT / name
        if p.exists():
            patch_file(p)


if __name__ == "__main__":
    main()
