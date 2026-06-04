"""Convert landing hub promos to unified single-card layout."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
CSS_LINK = '<link rel="stylesheet" href="assets/hub-single-card.css" />'

CARDS = {
    "features": """
<section id="features" class="cap-section cap-section--promo">
  <div class="int-showcase reveal">
    <div class="int-shell hub-single-card-shell">
      <article class="hub-single-card reveal">
        <span class="section-kicker">Platform Capabilities</span>
        <h3>Everything your enterprise needs to run voice AI at scale</h3>
        <p class="hub-single-card-lead">EMAAVY is the operating system for AI-powered conversations — from the first outbound dial to live transcription, reasoning, and automated follow-through. One platform replaces fragmented dialers, STT vendors, and manual QA.</p>
        <ul class="hub-single-card-highlights" aria-label="Core capabilities">
          <li><strong>Campaigns</strong> — personalized outbound at population scale</li>
          <li><strong>Intelligence</strong> — sentiment, intent, and risk on every live call</li>
          <li><strong>Automation</strong> — webhooks and CRM actions the moment events fire</li>
          <li><strong>Security</strong> — encryption, compliance, and deployment you control</li>
        </ul>
        <div class="hub-single-card-tags" aria-label="Capability areas">
          <span>Bulk calling</span><span>API triggers</span><span>Real-time STT</span><span>Voice agents</span><span>Call intelligence</span><span>Enterprise security</span>
        </div>
        <div class="hub-single-card-stats">
          <div class="hub-stat"><b>6</b><span>Core capabilities</span></div>
          <div class="hub-stat"><b>17+</b><span>Integration partners</span></div>
          <div class="hub-stat"><b>1</b><span>Unified API</span></div>
          <div class="hub-stat"><b>22</b><span>Languages</span></div>
        </div>
        <div class="hub-single-card-actions">
          <a href="pages/features.html" class="hub-btn-primary">Explore all capabilities</a>
          <a href="book-demo.html" class="hub-btn-secondary">Book a demo</a>
        </div>
      </article>
    </div>
  </div>
</section>""",
    "integrations": """
<section id="integrations">
  <div class="int-showcase reveal integrations-promo-wrap" id="integrations-emaavy">
    <div class="int-shell hub-single-card-shell">
      <article class="hub-single-card reveal">
        <span class="section-kicker">Integrations</span>
        <h3>Your entire AI stack — one connective layer</h3>
        <p class="hub-single-card-lead">EMAAVY wires telephony, reasoning, speech, voice, and workflow tools into a single voice agent platform. Configure once, scale globally, and open any layer for full specs on its own page.</p>
        <ul class="hub-single-card-highlights" aria-label="Integration highlights">
          <li><strong>Five layers</strong> — telephony, LLMs, STT, TTS, and tools as one pipeline</li>
          <li><strong>17+ partners</strong> — carriers, models, and CRMs without fragmented vendors</li>
          <li><strong>Per-call routing</strong> — swap providers by language, campaign, or intent</li>
          <li><strong>Enterprise ready</strong> — sub-second latency targets and 99.9% uptime</li>
        </ul>
        <div class="hub-single-card-tags" aria-label="Integration layers">
          <span>Telephony</span><span>LLMs</span><span>STT</span><span>TTS</span><span>Tools &amp; CRM</span>
        </div>
        <div class="hub-single-card-stats">
          <div class="hub-stat"><b>5</b><span>Stack layers</span></div>
          <div class="hub-stat"><b>17+</b><span>Partners</span></div>
          <div class="hub-stat"><b>1</b><span>Unified API</span></div>
          <div class="hub-stat"><b>99.9%</b><span>Platform uptime</span></div>
        </div>
        <div class="hub-single-card-actions">
          <a href="pages/integrations/index.html" class="hub-btn-primary">Explore all integrations</a>
          <a href="book-demo.html" class="hub-btn-secondary">Book a demo</a>
        </div>
      </article>
    </div>
  </div>
</section>""",
    "agents": """
<section id="agents" class="cap-section">
  <div class="int-showcase reveal agents-promo-wrap" id="agents-emaavy">
    <div class="int-shell hub-single-card-shell">
      <article class="hub-single-card reveal">
        <span class="section-kicker">Voice Agents</span>
        <h3>Voice agents that sell, support, and scale</h3>
        <p class="hub-single-card-lead">EMAAVY is where your AI workforce lives — dedicated agents with their own voice, flow, and mission. Configure once, run 24/7 across 22 languages, and open any role on its own page.</p>
        <ul class="hub-single-card-highlights" aria-label="Agent highlights">
          <li><strong>Four ready roles</strong> — sales, support, outbound campaigns, and custom builder</li>
          <li><strong>Human-like voice</strong> — Bulbul V3 and ElevenTurbo with natural Hinglish fluency</li>
          <li><strong>Live intelligence</strong> — intent scoring, CRM sync, and supervisor handoff</li>
          <li><strong>Minutes to deploy</strong> — visual flow builder, no code required</li>
        </ul>
        <div class="hub-single-card-tags" aria-label="Agent roles">
          <span>Sales</span><span>Support</span><span>Campaign</span><span>Custom builder</span>
        </div>
        <div class="hub-single-card-stats">
          <div class="hub-stat"><b>24/7</b><span>Always on</span></div>
          <div class="hub-stat"><b>22</b><span>Languages</span></div>
          <div class="hub-stat"><b>4</b><span>Agent roles</span></div>
          <div class="hub-stat"><b>&lt;15m</b><span>To first call</span></div>
        </div>
        <div class="hub-single-card-actions">
          <a href="pages/agents/workforce.html" class="hub-btn-primary">Explore all agents</a>
          <a href="book-demo.html" class="hub-btn-secondary">Book a demo</a>
        </div>
      </article>
    </div>
  </div>
</section>""",
    "case-studies": """
<section id="case-studies" class="cap-section">
  <div class="int-showcase reveal cs-promo-wrap" id="case-studies-emaavy">
    <div class="int-shell hub-single-card-shell">
      <article class="hub-single-card reveal">
        <span class="section-kicker">Case Studies</span>
        <h3>Proof from the field — not slide decks</h3>
        <p class="hub-single-card-lead">EMAAVY powers exhibition registrations, BPO quality at scale, and multilingual logistics follow-ups. Each case study covers the challenge, implementation, and measured results.</p>
        <ul class="hub-single-card-highlights" aria-label="Case study highlights">
          <li><strong>Three industries</strong> — events, BPO, and logistics with deep dives</li>
          <li><strong>Full-funnel voice</strong> — outbound, live QA, and support automation</li>
          <li><strong>Measurable ROI</strong> — registration rates, QA speed, and CSAT documented</li>
          <li><strong>Dedicated pages</strong> — open any story in the same tab</li>
        </ul>
        <div class="hub-single-card-tags" aria-label="Featured clients">
          <span>Mudita</span><span>NextCall BPO</span><span>FleetIQ</span>
        </div>
        <div class="hub-single-card-stats">
          <div class="hub-stat"><b>68%</b><span>Peak conversion</span></div>
          <div class="hub-stat"><b>50K+</b><span>Calls / month</span></div>
          <div class="hub-stat"><b>61%</b><span>Faster QA</span></div>
          <div class="hub-stat"><b>28%</b><span>CSAT lift</span></div>
        </div>
        <div class="hub-single-card-actions">
          <a href="pages/case-studies.html" class="hub-btn-primary">Explore all case studies</a>
          <a href="book-demo.html" class="hub-btn-secondary">Book a demo</a>
        </div>
      </article>
    </div>
  </div>
</section>""",
    "bento": """
<section id="bento" class="cap-section">
  <div class="int-showcase reveal imx-promo-wrap" id="intelligence-matrix-emaavy">
    <div class="int-shell hub-single-card-shell">
      <article class="hub-single-card reveal">
        <span class="section-kicker">Intelligence Matrix</span>
        <h3>Every metric decoded in real time</h3>
        <p class="hub-single-card-lead">EMAAVY's intelligence matrix is the unified dashboard layer — live transcripts, intent funnels, operator leaderboards, latency SLAs, and compliance controls. Open any module on its own page.</p>
        <ul class="hub-single-card-highlights" aria-label="Intelligence matrix highlights">
          <li><strong>Six modules</strong> — volume, real-time feed, intent, ops, latency, security</li>
          <li><strong>Live + historical</strong> — real-time operations with exportable trends</li>
          <li><strong>Human + AI</strong> — compare operator and voice agent performance</li>
          <li><strong>Enterprise ready</strong> — SOC-aligned security and audit built in</li>
        </ul>
        <div class="hub-single-card-tags" aria-label="Analytics modules">
          <span>Volume</span><span>Live feed</span><span>Intent</span><span>Operators</span><span>Latency</span><span>Security</span>
        </div>
        <div class="hub-single-card-stats">
          <div class="hub-stat"><b>10M+</b><span>Calls processed</span></div>
          <div class="hub-stat"><b>99%</b><span>Decode accuracy</span></div>
          <div class="hub-stat"><b>&lt;0.5s</b><span>Live latency</span></div>
          <div class="hub-stat"><b>6</b><span>Modules</span></div>
        </div>
        <div class="hub-single-card-actions">
          <a href="pages/intelligence-matrix/index.html" class="hub-btn-primary">Explore intelligence matrix</a>
          <a href="book-demo.html" class="hub-btn-secondary">Book a demo</a>
        </div>
      </article>
    </div>
  </div>
</section>""",
    "journey": """
<section id="journey" class="cap-section">
  <div class="int-showcase reveal clc-promo-wrap" id="call-lifecycle-emaavy">
    <div class="int-shell hub-single-card-shell">
      <article class="hub-single-card reveal">
        <span class="section-kicker">Call Lifecycle</span>
        <h3>From ring to learn — fully automated</h3>
        <p class="hub-single-card-lead">EMAAVY runs the complete call lifecycle without batch jobs or manual handoffs. Every stage has dedicated documentation so your team knows exactly what happens on the wire.</p>
        <ul class="hub-single-card-highlights" aria-label="Call lifecycle highlights">
          <li><strong>Five stages</strong> — ring, transcribe, analyze, act, and learn in sequence</li>
          <li><strong>Real-time pipeline</strong> — intelligence during the call, not after hang-up</li>
          <li><strong>Closed loop</strong> — outcomes feed the next campaign and agent version</li>
          <li><strong>100% automated</strong> — triggers and learning without ops copy-paste</li>
        </ul>
        <div class="hub-single-card-tags" aria-label="Lifecycle stages">
          <span>Ring</span><span>Transcribe</span><span>Analyze</span><span>Act</span><span>Learn</span>
        </div>
        <div class="hub-single-card-stats">
          <div class="hub-stat"><b>5</b><span>Lifecycle stages</span></div>
          <div class="hub-stat"><b>&lt;0.5s</b><span>Transcription</span></div>
          <div class="hub-stat"><b>100%</b><span>Automated</span></div>
          <div class="hub-stat"><b>0</b><span>Manual handoffs</span></div>
        </div>
        <div class="hub-single-card-actions">
          <a href="pages/call-lifecycle/index.html" class="hub-btn-primary">Explore call lifecycle</a>
          <a href="book-demo.html" class="hub-btn-secondary">Book a demo</a>
        </div>
      </article>
    </div>
  </div>
</section>""",
    "faq": """
<section id="faq" class="cap-section faq-hub-section">
  <div class="int-showcase reveal faq-promo-wrap" id="faq-emaavy">
    <div class="int-shell hub-single-card-shell">
      <article class="hub-single-card reveal">
        <span class="section-kicker">FAQ</span>
        <h3>Answers that match how you buy and build</h3>
        <p class="hub-single-card-lead">From go-live timelines and custom voice models to compliance, pricing, CRM wiring, and Enterprise success — six guided topics for operators, engineers, and leadership.</p>
        <ul class="hub-single-card-highlights" aria-label="FAQ highlights">
          <li><strong>Six deep-dive topics</strong> — launch, voices, security, pricing, integrations, Enterprise</li>
          <li><strong>Same-tab pages</strong> — full narratives without losing your place</li>
          <li><strong>Brand-consistent</strong> — slate blues and EMAAVY patterns throughout</li>
          <li><strong>Still have questions?</strong> — book a demo or contact support anytime</li>
        </ul>
        <div class="hub-single-card-tags" aria-label="FAQ topics">
          <span>Go-live</span><span>Voice models</span><span>Compliance</span><span>Pricing</span><span>CRM</span><span>Enterprise</span>
        </div>
        <div class="hub-single-card-stats">
          <div class="hub-stat"><b>6</b><span>Topic guides</span></div>
          <div class="hub-stat"><b>&lt;48h</b><span>Typical go-live</span></div>
          <div class="hub-stat"><b>SOC 2</b><span>Aligned</span></div>
          <div class="hub-stat"><b>99.99%</b><span>Enterprise SLA</span></div>
        </div>
        <div class="hub-single-card-actions">
          <a href="pages/faq.html" class="hub-btn-primary">Browse all topics</a>
          <a href="pages/contact.html" class="hub-btn-secondary">Contact support</a>
        </div>
      </article>
    </div>
  </div>
</section>""",
}


def replace_section(text: str, section_id: str, new_block: str) -> str:
    pattern = rf'<section id="{re.escape(section_id)}"[^>]*>.*?</section>'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        raise SystemExit(f"section {section_id} not found")
    return text[: m.start()] + new_block.strip() + text[m.end() :]


def main():
    text = HTML.read_text(encoding="utf-8")
    if "hub-single-card.css" not in text:
        text = text.replace("</head>", f"  {CSS_LINK}\n</head>", 1)

    for sid, block in CARDS.items():
        text = replace_section(text, sid, block)
        print(f"OK: {sid}")

    HTML.write_text(text, encoding="utf-8")
    print("Done: hub single-card layout applied")


if __name__ == "__main__":
    main()
