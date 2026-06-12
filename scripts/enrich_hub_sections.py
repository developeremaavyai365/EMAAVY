"""Enrich hub zones with visuals, quick links, quotes — single card stays."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"

ICONS = {
    "cap": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg>',
    "int": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="12" r="3"/><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/></svg>',
    "agent": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M12 2a4 4 0 0 1 4 4v1a4 4 0 0 1-8 0V6a4 4 0 0 1 4-4z"/><path d="M6 21v-2a6 6 0 0 1 12 0v2"/></svg>',
    "cs": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><path d="M3 3v18h18"/><path d="M7 16l4-5 4 3 5-7"/></svg>',
    "imx": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>',
    "clc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
    "faq": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75"><circle cx="12" cy="12" r="10"/><path d="M9.5 9.5a2.5 2.5 0 0 1 5 0c0 2-2.5 2-2.5 4"/><path d="M12 17h.01"/></svg>',
}

MARQUEE = """
<div class="hub-marquee-wrap" aria-hidden="true">
  <div class="hub-marquee">
    <span>Real-time transcription</span><span>22 Indian languages</span><span>AI voice agents</span><span>Intent scoring</span><span>CRM automation</span><span>SOC 2 aligned</span><span>Sub-500ms latency</span><span>Campaign orchestration</span>
    <span>Real-time transcription</span><span>22 Indian languages</span><span>AI voice agents</span><span>Intent scoring</span><span>CRM automation</span><span>SOC 2 aligned</span><span>Sub-500ms latency</span><span>Campaign orchestration</span>
  </div>
</div>
"""

CONNECTOR = '<div class="hub-connector reveal" aria-hidden="true"><span class="hub-connector-dot"></span></div>'


def card(icon, kicker, title, lead, quote, highlights, tags, quick_links_html, stats, primary_href, primary_label, secondary_href, secondary_label, mini_flow=""):
    flow_block = f'<div class="hub-mini-flow" aria-label="Flow">{mini_flow}</div>' if mini_flow else ""
    return f"""
      <article class="hub-single-card reveal">
        <div class="hub-card-accent" aria-hidden="true"></div>
        <div class="hub-card-body">
          <div class="hub-card-top">
            <div class="hub-card-icon" aria-hidden="true">{ICONS[icon]}</div>
            <div class="hub-card-top-text">
              <span class="section-kicker">{kicker}</span>
              <h3>{title}</h3>
            </div>
          </div>
          <p class="hub-single-card-lead">{lead}</p>
          <blockquote class="hub-card-quote">{quote}</blockquote>
          {flow_block}
          <ul class="hub-single-card-highlights" aria-label="Highlights">{highlights}</ul>
          <div class="hub-single-card-tags" aria-label="Topics">{tags}</div>
          <div class="hub-quick-links">{quick_links_html}</div>
          <div class="hub-single-card-stats">{stats}</div>
          <div class="hub-single-card-actions">
            <a href="{primary_href}" class="hub-btn-primary">{primary_label}</a>
            <a href="{secondary_href}" class="hub-btn-secondary">{secondary_label}</a>
          </div>
        </div>
      </article>"""


def zone(num, title, alt_class, extra_class, inner):
    alt = " hub-zone--alt" if alt_class else ""
    ex = f" {extra_class}" if extra_class else ""
    return f"""
<section id="{inner.split('id="')[1].split('"')[0] if 'id="' in inner else ''}" class="hub-zone hub-zone--{num}{alt}{ex}">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">{num:02d}</span>
    <p class="hub-zone-title">{title}</p>
  </div>
  {inner.strip()}
</section>
{CONNECTOR}
{MARQUEE if num == 1 else ""}
"""


# Build sections individually (cleaner)
SECTIONS = {}

SECTIONS["features"] = """
<section id="features" class="hub-zone hub-zone--1">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">01</span>
    <p class="hub-zone-title">Platform capabilities</p>
  </div>
  <div class="int-showcase reveal">
    <div class="int-shell hub-single-card-shell">
""" + card(
    "cap", "Platform Capabilities",
    "Everything your enterprise needs to run voice AI at scale",
    "EMAAVY is the operating system for AI-powered conversations — from the first outbound dial to live transcription, reasoning, and automated follow-through. One platform replaces fragmented dialers, STT vendors, and manual QA.",
    "Teams that consolidate on EMAAVY cut vendor sprawl and see every call in one intelligence layer — not five dashboards.",
    """<li><strong>Campaigns</strong>Personalized outbound at population scale</li>
          <li><strong>Intelligence</strong>Sentiment, intent, and risk live on every call</li>
          <li><strong>Automation</strong>Webhooks and CRM the moment events fire</li>
          <li><strong>Security</strong>Encryption, compliance, deployment you control</li>""",
    "<span>Bulk calling</span><span>API triggers</span><span>Real-time STT</span><span>Voice agents</span><span>Call intelligence</span><span>Enterprise security</span>",
    """<span class="hub-quick-links-label">Explore capabilities</span>
          <a class="hub-quick-link" href="pages/features.html">All features</a>
          <a class="hub-quick-link" href="pages/how-it-works.html">How it works</a>
          <a class="hub-quick-link" href="pages/pricing.html">Pricing</a>""",
    """<div class="hub-stat"><b>6</b><span>Core capabilities</span></div>
          <div class="hub-stat"><b>17+</b><span>Partners</span></div>
          <div class="hub-stat"><b>1</b><span>Unified API</span></div>
          <div class="hub-stat"><b>22</b><span>Languages</span></div>""",
    "pages/features.html", "Explore all capabilities",
    "book-demo.html", "Book a demo",
) + """
    </div>
  </div>
</section>
""" + CONNECTOR + MARQUEE

SECTIONS["integrations"] = """
<section id="integrations" class="hub-zone hub-zone--2 hub-zone--alt hub-zone--integrations">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">02</span>
    <p class="hub-zone-title">Integrations</p>
  </div>
  <div class="int-showcase reveal integrations-promo-wrap" id="integrations-emaavy">
    <div class="int-shell hub-single-card-shell">
""" + card(
    "int", "Integrations",
    "Your entire AI stack — one connective layer",
    "EMAAVY wires telephony, reasoning, speech, voice, and workflow tools into a single voice agent platform. Configure once, scale globally, and open any layer for full specs on its own page.",
    "Swap Deepgram for Sarvam on Hindi campaigns while keeping the same agent flow — routing is per call, not per contract.",
    """<li><strong>Five layers</strong>Telephony, LLMs, STT, TTS, tools as one pipeline</li>
          <li><strong>17+ partners</strong>Carriers, models, CRMs — one vendor map</li>
          <li><strong>Per-call routing</strong>By language, campaign, or intent</li>
          <li><strong>Enterprise ready</strong>Sub-second targets, 99.9% uptime</li>""",
    "<span>Telephony</span><span>LLMs</span><span>STT</span><span>TTS</span><span>CRM &amp; tools</span>",
    """<span class="hub-quick-links-label">Open integration layers</span>
          <a class="hub-quick-link" href="pages/integrations/telephony.html">Telephony</a>
          <a class="hub-quick-link" href="pages/integrations/llms.html">LLMs</a>
          <a class="hub-quick-link" href="pages/integrations/stt.html">Speech-to-text</a>
          <a class="hub-quick-link" href="pages/integrations/tts.html">Text-to-speech</a>
          <a class="hub-quick-link" href="pages/integrations/tools.html">Tools &amp; CRM</a>
          <a class="hub-quick-link" href="pages/integrations/index.html">All integrations</a>""",
    """<div class="hub-stat"><b>5</b><span>Stack layers</span></div>
          <div class="hub-stat"><b>17+</b><span>Partners</span></div>
          <div class="hub-stat"><b>1</b><span>Unified API</span></div>
          <div class="hub-stat"><b>99.9%</b><span>Uptime</span></div>""",
    "pages/integrations/index.html", "Explore all integrations",
    "book-demo.html", "Book a demo",
    '<span>Telephony</span><em>→</em><span>LLM</span><em>→</em><span>STT</span><em>→</em><span>TTS</span><em>→</em><span>Act</span>',
) + """
    </div>
  </div>
</section>
""" + CONNECTOR

SECTIONS["agents"] = """
<section id="agents" class="hub-zone hub-zone--3 hub-zone--agents">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">03</span>
    <p class="hub-zone-title">Voice agents</p>
  </div>
  <div class="int-showcase reveal agents-promo-wrap" id="agents-emaavy">
    <div class="int-shell hub-single-card-shell">
""" + card(
    "agent", "Voice Agents",
    "Voice agents that sell, support, and scale",
    "EMAAVY is where your AI workforce lives — dedicated agents with their own voice, flow, and mission. Configure once, run 24/7 across 22 languages, and open any role on its own page.",
    "A campaign agent booked 68% of exhibition slots while supervisors watched live intent scores — no manual dialer queue.",
    """<li><strong>Four roles</strong>Sales, support, campaigns, custom builder</li>
          <li><strong>Human-like voice</strong>Bulbul V3 &amp; ElevenTurbo, Hinglish native</li>
          <li><strong>Live intelligence</strong>Intent, CRM sync, supervisor handoff</li>
          <li><strong>Fast deploy</strong>Visual flows — live in minutes</li>""",
    "<span>Sales</span><span>Support</span><span>Campaign</span><span>Builder</span>",
    """<span class="hub-quick-links-label">Meet your agents</span>
          <a class="hub-quick-link" href="pages/agents/real-estate.html">Sales template</a>
          <a class="hub-quick-link" href="pages/agents/support-playbook.html">Support template</a>
          <a class="hub-quick-link" href="pages/agents/event-agent.html">Event outreach</a>
          <a class="hub-quick-link" href="pages/agents/workforce.html">All templates</a>""",
    """<div class="hub-stat"><b>24/7</b><span>Always on</span></div>
          <div class="hub-stat"><b>22</b><span>Languages</span></div>
          <div class="hub-stat"><b>4</b><span>Agent roles</span></div>
          <div class="hub-stat"><b>&lt;15m</b><span>First call</span></div>""",
    "pages/agents/workforce.html", "Explore all agents",
    "book-demo.html", "Book a demo",
) + """
    </div>
  </div>
</section>
""" + CONNECTOR

SECTIONS["case-studies"] = """
<section id="case-studies" class="hub-zone hub-zone--4 hub-zone--alt">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">04</span>
    <p class="hub-zone-title">Case studies</p>
  </div>
  <div class="int-showcase reveal cs-promo-wrap" id="case-studies-emaavy">
    <div class="int-shell hub-single-card-shell">
""" + card(
    "cs", "Case Studies",
    "Proof from the field — not slide decks",
    "EMAAVY powers exhibition registrations, BPO quality at scale, and multilingual logistics follow-ups. Each case study covers the challenge, implementation, and measured results.",
    "NextCall replaced 5% manual QA sampling with 100% call coverage — coaching alerts fire while the call is still live.",
    """<li><strong>Events</strong>68% registration vs 12% email baseline</li>
          <li><strong>BPO</strong>61% faster QA with full coverage</li>
          <li><strong>Logistics</strong>28% CSAT lift across 50K calls/mo</li>
          <li><strong>Same-tab depth</strong>Full stories on dedicated pages</li>""",
    "<span>Mudita</span><span>NextCall</span><span>FleetIQ</span>",
    """<span class="hub-quick-links-label">Read client stories</span>
          <a class="hub-quick-link" href="pages/case-studies/mudita.html">Warehouse by Mudita</a>
          <a class="hub-quick-link" href="pages/case-studies/nextcall.html">NextCall BPO</a>
          <a class="hub-quick-link" href="pages/case-studies/fleetiq.html">FleetIQ Logistics</a>
          <a class="hub-quick-link" href="pages/case-studies.html">All case studies</a>""",
    """<div class="hub-stat"><b>68%</b><span>Peak conversion</span></div>
          <div class="hub-stat"><b>50K+</b><span>Calls / mo</span></div>
          <div class="hub-stat"><b>61%</b><span>Faster QA</span></div>
          <div class="hub-stat"><b>28%</b><span>CSAT lift</span></div>""",
    "pages/case-studies.html", "Explore all case studies",
    "book-demo.html", "Book a demo",
) + """
    </div>
  </div>
</section>
""" + CONNECTOR

SECTIONS["bento"] = """
<section id="bento" class="hub-zone hub-zone--5">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">05</span>
    <p class="hub-zone-title">Intelligence matrix</p>
  </div>
  <div class="int-showcase reveal imx-promo-wrap" id="intelligence-matrix-emaavy">
    <div class="int-shell hub-single-card-shell">
""" + card(
    "imx", "Intelligence Matrix",
    "Every metric decoded in real time",
    "EMAAVY's intelligence matrix is the unified dashboard layer — live transcripts, intent funnels, operator leaderboards, latency SLAs, and compliance controls. Open any module on its own page.",
    "Supervisors intervene on negative sentiment shifts before the call ends — not in tomorrow's spreadsheet.",
    """<li><strong>Six modules</strong>Volume, live feed, intent, ops, latency, security</li>
          <li><strong>Live + historical</strong>Real-time ops with exportable trends</li>
          <li><strong>Human + AI</strong>Fair operator vs agent benchmarks</li>
          <li><strong>Enterprise</strong>SOC-aligned security &amp; audit</li>""",
    "<span>Volume</span><span>Live</span><span>Intent</span><span>Ops</span><span>Latency</span><span>Security</span>",
    """<span class="hub-quick-links-label">Analytics modules</span>
          <a class="hub-quick-link" href="pages/intelligence-matrix/volume.html">Calls processed</a>
          <a class="hub-quick-link" href="pages/intelligence-matrix/realtime.html">Real-time feed</a>
          <a class="hub-quick-link" href="pages/intelligence-matrix/intent.html">Intent mapping</a>
          <a class="hub-quick-link" href="pages/intelligence-matrix/ops.html">Operator performance</a>
          <a class="hub-quick-link" href="pages/intelligence-matrix/latency.html">System latency</a>
          <a class="hub-quick-link" href="pages/intelligence-matrix/security.html">Enterprise security</a>""",
    """<div class="hub-stat"><b>10M+</b><span>Calls decoded</span></div>
          <div class="hub-stat"><b>99%</b><span>Accuracy</span></div>
          <div class="hub-stat"><b>&lt;0.5s</b><span>Live latency</span></div>
          <div class="hub-stat"><b>6</b><span>Modules</span></div>""",
    "pages/intelligence-matrix/index.html", "Explore intelligence matrix",
    "book-demo.html", "Book a demo",
) + """
    </div>
  </div>
</section>
""" + CONNECTOR

SECTIONS["journey"] = """
<section id="journey" class="hub-zone hub-zone--6 hub-zone--alt">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">06</span>
    <p class="hub-zone-title">Call lifecycle</p>
  </div>
  <div class="int-showcase reveal clc-promo-wrap" id="call-lifecycle-emaavy">
    <div class="int-shell hub-single-card-shell">
""" + card(
    "clc", "Call Lifecycle",
    "From ring to learn — fully automated",
    "EMAAVY runs the complete call lifecycle without batch jobs or manual handoffs. Every stage has dedicated documentation so your team knows exactly what happens on the wire.",
    "Triggers fire on intent thresholds while the caller is still on the line — CRM updates land before hang-up.",
    """<li><strong>Five stages</strong>Ring → transcribe → analyze → act → learn</li>
          <li><strong>Real-time</strong>Intelligence during the call, not after</li>
          <li><strong>Closed loop</strong>Outcomes feed the next campaign</li>
          <li><strong>Zero handoffs</strong>No ops copy-paste between systems</li>""",
    "<span>Ring</span><span>Transcribe</span><span>Analyze</span><span>Act</span><span>Learn</span>",
    """<span class="hub-quick-links-label">Lifecycle stages</span>
          <a class="hub-quick-link" href="pages/call-lifecycle/ring.html">Call connects</a>
          <a class="hub-quick-link" href="pages/call-lifecycle/transcribe.html">Transcribe</a>
          <a class="hub-quick-link" href="pages/call-lifecycle/analyze.html">Analyze</a>
          <a class="hub-quick-link" href="pages/call-lifecycle/act.html">Act</a>
          <a class="hub-quick-link" href="pages/call-lifecycle/learn.html">Learn</a>
          <a class="hub-quick-link" href="pages/call-lifecycle/index.html">Full lifecycle</a>""",
    """<div class="hub-stat"><b>5</b><span>Stages</span></div>
          <div class="hub-stat"><b>&lt;0.5s</b><span>Transcription</span></div>
          <div class="hub-stat"><b>100%</b><span>Automated</span></div>
          <div class="hub-stat"><b>0</b><span>Manual steps</span></div>""",
    "pages/call-lifecycle/index.html", "Explore call lifecycle",
    "book-demo.html", "Book a demo",
    '<span>Ring</span><em>→</em><span>Transcribe</span><em>→</em><span>Analyze</span><em>→</em><span>Act</span><em>→</em><span>Learn</span>',
) + """
    </div>
  </div>
</section>
""" + CONNECTOR

SECTIONS["faq"] = """
<section id="faq" class="hub-zone hub-zone--7 hub-zone--faq faq-hub-section">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">07</span>
    <p class="hub-zone-title">FAQ &amp; support</p>
  </div>
  <div class="int-showcase reveal faq-promo-wrap" id="faq-emaavy">
    <div class="int-shell hub-single-card-shell">
""" + card(
    "faq", "FAQ",
    "Answers that match how you buy and build",
    "From go-live timelines and custom voice models to compliance, pricing, CRM wiring, and Enterprise success — six guided topics for operators, engineers, and leadership.",
    "Most teams go live on Starter within 48 hours — same-day if you already have numbers and a CRM webhook endpoint.",
    """<li><strong>Go-live</strong>Timelines, trials, and first campaign</li>
          <li><strong>Voice &amp; AI</strong>Custom models and Hinglish flows</li>
          <li><strong>Compliance</strong>SOC, retention, audit exports</li>
          <li><strong>Scale</strong>Pricing, CRM, Enterprise success</li>""",
    "<span>Launch</span><span>Voices</span><span>Security</span><span>Pricing</span><span>CRM</span><span>Enterprise</span>",
    """<span class="hub-quick-links-label">Popular topics</span>
          <a class="hub-quick-link" href="pages/faq/go-live.html">How fast to go live?</a>
          <a class="hub-quick-link" href="pages/faq/voice-models.html">Custom voice models</a>
          <a class="hub-quick-link" href="pages/faq/compliance.html">Compliance &amp; audit</a>
          <a class="hub-quick-link" href="pages/faq/pricing-scale.html">Pricing at scale</a>
          <a class="hub-quick-link" href="pages/faq/crm-integrations.html">CRM integrations</a>
          <a class="hub-quick-link" href="pages/faq/enterprise-support.html">Enterprise support</a>""",
    """<div class="hub-stat"><b>6</b><span>Topic guides</span></div>
          <div class="hub-stat"><b>&lt;48h</b><span>Go-live</span></div>
          <div class="hub-stat"><b>SOC 2</b><span>Aligned</span></div>
          <div class="hub-stat"><b>99.99%</b><span>Enterprise SLA</span></div>""",
    "pages/faq.html", "Browse all topics",
    "pages/contact.html", "Contact support",
) + """
    </div>
  </div>
</section>
"""


def replace_section(text: str, section_id: str, new_block: str) -> str:
    pattern = rf'<section id="{re.escape(section_id)}"[^>]*>.*?</section>'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        raise SystemExit(f"section {section_id} not found")
    return text[: m.start()] + new_block.strip() + text[m.end() :]


def main():
    text = HTML.read_text(encoding="utf-8")
    if "hub-single-card.js" not in text:
        text = text.replace(
            '<link rel="stylesheet" href="assets/hub-single-card.css" />',
            '<link rel="stylesheet" href="assets/hub-single-card.css" />\n  <script src="assets/hub-single-card.js" defer></script>',
        )
    for sid, block in SECTIONS.items():
        text = replace_section(text, sid, block)
        print(f"OK: enriched {sid}")
    HTML.write_text(text, encoding="utf-8")
    print("Done")


if __name__ == "__main__":
    main()
