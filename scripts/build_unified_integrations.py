"""
Unify home integrations into one EMAAVY promo block.
Create category pages: llms.html, stt.html, tts.html, tools.html
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
PAGES = ROOT / "pages" / "integrations"
SITE_CSS = ROOT / "assets" / "site.css"
ROUTES = ROOT / "assets" / "routes.js"

PAGE_SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — EMAAVY</title>
  <meta name="description" content="{desc}" />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="{route}">
  <div id="site-nav-root"></div>
  <main class="page-main int-category-page">
{content}
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""

CATEGORIES = {
    "llms": {
        "route": "integration-llms",
        "title": "LLMs",
        "kicker": "Reasoning layer · LLMs",
        "h1": "The reasoning engine behind every conversation",
        "lead": "EMAAVY routes flagship reasoning, real-time inference, and multilingual models per agent, per intent, or mid-call — without losing context.",
        "stats": [("5", "Model families"), ("128K", "Max context"), ("Per-agent", "Routing")],
        "jump": [("emaavy-llm", "EMAAVY &amp; LLMs"), ("providers", "Model partners"), ("flow", "Orchestration")],
        "overview_title": "How EMAAVY orchestrates LLMs",
        "overview_lead": "One conversation layer, many models. Engineering picks defaults; operations swaps models by campaign without rebuilding agents.",
        "overview_points": [
            "<strong>Per-agent routing</strong> — assign GPT, Claude, Gemini, Qwen, or Grok per workflow.",
            "<strong>Mid-call switching</strong> — escalate to a heavier model when intent complexity spikes.",
            "<strong>Structured extraction</strong> — JSON dispositions and scores from live transcripts.",
            "<strong>Cost control</strong> — flash models for classification, flagship models for closing.",
        ],
        "flow_title": "How EMAAVY uses your LLM stack",
        "flow_steps": [
            ("Transcript in", "Live speech becomes text in the reasoning pipeline."),
            ("Model selected", "EMAAVY picks the model for intent, language, and SLA."),
            ("Intent detected", "Buyer signals scored on every conversational turn."),
            ("Data extracted", "Structured fields mapped to CRM and campaigns."),
            ("Agent responds", "The voice agent speaks with model-backed replies."),
        ],
        "providers": [
            ("openai", "GPT-5.5 / GPT-5.4", "Flagship", "Flagship reasoning for complex sales flows and multi-step objection handling.", "https://cdn.worldvectorlogo.com/logos/openai-2.svg", "openai.html"),
            ("claude", "Claude Opus · Sonnet · Haiku", "Enterprise", "Best-in-class comprehension for nuanced and compliance-sensitive calls.", "https://cdn.simpleicons.org/anthropic/191919", "claude.html"),
            ("gemini", "Gemini Flash Preview", "Real-time", "Ultra-fast inference for real-time intent detection during live calls.", "https://cdn.simpleicons.org/google/4285F4", "gemini.html"),
            ("qwen", "Qwen 3.6", "Multilingual", "Cost-efficient multilingual model optimized for Hinglish and regional dialects.", None, "qwen.html"),
            ("grok", "Grok Beta", "Experimental", "Creative outbound scripts and dynamic rebuttals for pilot campaigns.", None, "grok.html"),
        ],
    },
    "stt": {
        "route": "integration-stt",
        "title": "Speech-to-Text",
        "kicker": "Capture layer · Speech-to-Text",
        "h1": "Every word captured — in real time",
        "lead": "Nine STT providers, one EMAAVY platform. Pick the best engine per language, accent, or latency — routing is automatic so nothing gets lost.",
        "stats": [("9", "STT providers"), ("<0.5s", "Latency"), ("22", "Languages")],
        "jump": [("emaavy-stt", "EMAAVY &amp; STT"), ("providers", "STT partners"), ("flow", "Speech pipeline")],
        "overview_title": "How EMAAVY handles transcription",
        "overview_lead": "Telephony audio streams into the STT layer the moment a call connects. Supervisors and agents see words as they are spoken.",
        "overview_points": [
            "<strong>Provider choice</strong> — Deepgram, Sarvam, Gladia, Azure, Google, and more.",
            "<strong>Language-aware routing</strong> — Indian dialects to Sarvam; global English to Deepgram.",
            "<strong>Keyword boosting</strong> — brand names and compliance phrases recognized reliably.",
            "<strong>Live feeds</strong> — transcripts power intent scoring before hang-up.",
        ],
        "flow_title": "From speech to structured insight",
        "flow_steps": [
            ("Audio captured", "EMAAVY ingests the live media stream from the voice channel."),
            ("STT transcribes", "Your chosen engine streams words with sub-second latency."),
            ("Intent parsed", "LLM layer classifies buyer signals from the transcript."),
            ("Score assigned", "Sentiment and compliance scores update in real time."),
            ("Action triggered", "CRM, webhooks, and coaching rules fire automatically."),
        ],
        "providers": [
            ("assemblyai", "AssemblyAI", "Real-time", "Real-time transcription with strong punctuation for live voice agents.", "https://cdn.simpleicons.org/assemblyai/2545D0", "assemblyai.html"),
            ("azure-stt", "Azure Speech", "Enterprise", "Enterprise-grade speech recognition with global language support.", "https://cdn.simpleicons.org/microsoftazure/0078D4", "azure-stt.html"),
            ("deepgram", "Deepgram", "Low latency", "High-accuracy, low-latency transcription with keyword boosting.", "https://cdn.simpleicons.org/deepgram/13EF93", "deepgram.html"),
            ("elevenlabs-stt", "ElevenLabs STT", "Unified stack", "Same API key for STT and TTS in a unified voice stack.", "../../assets/logos/elevenlabs.svg", "elevenlabs-stt.html"),
            ("gladia", "Gladia", "Multilingual", "Multilingual transcription with code-switching and sub-300ms latency.", None, "gladia.html"),
            ("google-stt", "Google STT", "Global", "Broad language coverage with telephony-optimized models.", "https://cdn.simpleicons.org/google/4285F4", "google-stt.html"),
            ("openai-stt", "OpenAI Whisper", "Whisper", "Accurate speech recognition across languages and accents.", "https://cdn.worldvectorlogo.com/logos/openai-2.svg", "openai-stt.html"),
            ("sarvam", "Sarvam AI", "India · 22 langs", "Optimized for Hindi, Tamil, Telugu — 22 Indian languages natively.", "../../assets/logos/flash-bulbul.svg", "sarvam.html"),
            ("smallest", "Smallest AI", "Lightweight", "Lightweight, fast transcription for low-latency conversations.", None, "smallest.html"),
        ],
    },
    "tts": {
        "route": "integration-tts",
        "title": "Text-to-Speech",
        "kicker": "Voice layer · Text-to-Speech",
        "h1": "Voices that sound human — not robotic",
        "lead": "Natural, empathetic synthesis in every language your customers speak. EMAAVY connects premium TTS engines built for live conversations where tone matters.",
        "stats": [("2", "Premium engines"), ("<300ms", "Voice latency"), ("22", "Languages")],
        "jump": [("emaavy-tts", "EMAAVY &amp; voice"), ("providers", "TTS engines"), ("flow", "Voice pipeline")],
        "overview_title": "How EMAAVY delivers agent voice",
        "overview_lead": "Scripts become speech in milliseconds. Tone adapts per call stage — opener, objection, close — without manual audio editing.",
        "overview_points": [
            "<strong>ElevenTurbo v2</strong> — expressive global voices for persuasive outbound.",
            "<strong>Flash · Bulbul</strong> — native Indian cadence and Hinglish code-switching.",
            "<strong>Low latency</strong> — sub-300ms targets for natural turn-taking.",
            "<strong>Brand consistency</strong> — voice cloning and per-campaign voice profiles.",
        ],
        "flow_title": "How your agent finds its voice",
        "flow_steps": [
            ("Script generated", "LLM produces the next spoken line for the agent."),
            ("TTS synthesizes", "EMAAVY calls your TTS engine with tone parameters."),
            ("Tone adjusted", "Warmth and pace tuned for sales or support context."),
            ("Delivered live", "Audio streams back into the active call."),
        ],
        "providers": [
            ("elevenlabs", "ElevenTurbo v2", "Expressive", "Low-latency expressive voice synthesis for warm, persuasive outbound agents.", "../../assets/logos/elevenlabs.svg", "elevenlabs.html"),
            ("flash-bulbul", "Flash v2 · Bulbul V3", "India native", "Native Indian voice models with natural Hinglish cadence for sales and support.", "../../assets/logos/flash-bulbul.svg", "flash-bulbul.html"),
        ],
    },
    "tools": {
        "route": "integration-tools",
        "title": "Tools & Workflow",
        "kicker": "Action layer · Tools &amp; Workflow",
        "h1": "Every call triggers the right action — instantly",
        "lead": "CRM updates, calendar bookings, WhatsApp follow-ups, and custom webhooks — all fired from what was actually said. Zero manual entry through EMAAVY.",
        "stats": [("6+", "Integrations"), ("Zero", "Manual entry"), ("Real-time", "Sync")],
        "jump": [("emaavy-tools", "EMAAVY &amp; actions"), ("providers", "Connected tools"), ("flow", "Post-call automation")],
        "overview_title": "How EMAAVY automates follow-through",
        "overview_lead": "Conversation intelligence becomes operational motion the moment a call ends — or mid-call when rules require it.",
        "overview_points": [
            "<strong>CRM sync</strong> — Salesforce and HubSpot updated from live dispositions.",
            "<strong>Scheduling</strong> — Cal.com and Google Calendar bookings during calls.",
            "<strong>Messaging</strong> — WhatsApp confirmations and links after hang-up.",
            "<strong>Custom logic</strong> — webhooks with full transcript and score payloads.",
        ],
        "flow_title": "What fires when a call ends",
        "flow_steps": [
            ("Call completes", "EMAAVY finalizes transcript, scores, and metadata."),
            ("Trigger matched", "Rules map intent and keywords to actions."),
            ("CRM updated", "Records, tasks, and deals sync automatically."),
            ("Meeting booked", "Calendar events created with invites."),
            ("Follow-up sent", "WhatsApp, email, or webhook payloads delivered."),
        ],
        "providers": [
            ("webhooks", "Webhooks", "Events", "Push call events, transcripts, and scores to any endpoint.", None, "webhooks.html"),
            ("calcom", "Cal.com", "Scheduling", "Book meetings live during calls — agent captures the slot instantly.", "https://cdn.simpleicons.org/caldotcom/292929", "calcom.html"),
            ("google-calendar", "Google Calendar", "Calendar", "Sync confirmed appointments into shared Google Calendars.", "https://cdn.simpleicons.org/googlecalendar/4285F4", "google-calendar.html"),
            ("whatsapp", "WhatsApp", "Messaging", "Send confirmations, links, and follow-ups when a call concludes.", "https://cdn.simpleicons.org/whatsapp/25D366", "whatsapp.html"),
            ("slack", "Slack", "Alerts", "Route call intelligence and coaching notifications to Slack.", "https://cdn.simpleicons.org/slack/4A154B", "slack.html"),
            ("salesforce", "Salesforce", "CRM", "Update records, log dispositions, and push intent scores automatically.", "https://cdn.worldvectorlogo.com/logos/salesforce-2.svg", "salesforce.html"),
            ("hubspot", "HubSpot", "CRM", "Create deals, update contacts, and trigger workflows from call intel.", "https://cdn.simpleicons.org/hubspot/FF7A59", "hubspot.html"),
        ],
    },
}


def logo_html(src, name, pid):
    if src:
        return f'<img src="{src}" alt="{name}" width="32" height="32" loading="lazy" />'
    marks = {"qwen": "QW", "grok": "GX", "gladia": "GL", "smallest": "SM", "webhooks": "WH"}
    m = marks.get(pid, pid[:2].upper())
    return f'<span class="brand-mark">{m}</span>'


def build_category_page(key, cfg):
    stats = "".join(f'<div class="stat-box"><b>{b}</b><span>{s}</span></div>' for b, s in cfg["stats"])
    jump = "".join(f'<a href="#{a}">{l}</a>' for a, l in cfg["jump"])
    points = "".join(f"<li>{p}</li>" for p in cfg["overview_points"])
    flow = "".join(
        f'<li><span class="telephony-flow-num">{i+1:02d}</span><strong>{t}</strong><p>{d}</p></li>'
        for i, (t, d) in enumerate(cfg["flow_steps"])
    )
    cards = []
    for pid, name, tag, desc, img, href in cfg["providers"]:
        logo = logo_html(img, name, pid)
        cards.append(f"""          <article id="{pid}" class="telephony-provider-card">
            <div class="telephony-provider-logo">{logo}</div>
            <span class="telephony-provider-tag">{tag}</span>
            <h3>{name}</h3>
            <p>{desc}</p>
            <a href="{href}" class="telephony-provider-link">Integration details →</a>
          </article>""")
    cards_html = "\n".join(cards)

    content = f"""    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../emaavy_white_blue%20(2).html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../emaavy_white_blue%20(2).html#integrations">Integrations</a>
          <span aria-hidden="true"> / </span>
          <span>{cfg['title']}</span>
        </nav>
        <span class="page-kicker">{cfg['kicker']}</span>
        <h1>{cfg['h1']}</h1>
        <p class="telephony-hero-lead">{cfg['lead']}</p>
        <div class="stat-row telephony-hero-stats">{stats}</div>
        <div class="capabilities-jump telephony-jump">{jump}</div>
      </div>
    </section>

    <section id="{cfg['jump'][0][0]}" class="page-section">
      <div class="container">
        <article class="capability-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">—</span>
              <span class="capability-tag">EMAAVY · {cfg['title']}</span>
            </div>
            <div class="capability-content">
              <h2>{cfg['overview_title']}</h2>
              <p class="capability-lead">{cfg['overview_lead']}</p>
              <ul class="capability-points">{points}</ul>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="providers" class="page-section alt">
      <div class="container">
        <h2 class="section-title">Connected partners</h2>
        <p class="section-desc">Unified through EMAAVY — configure once, swap providers without re-architecting agents.</p>
        <div class="telephony-provider-grid">
{cards_html}
        </div>
      </div>
    </section>

    <section id="flow" class="page-section">
      <div class="container">
        <h2 class="section-title">{cfg['flow_title']}</h2>
        <div class="telephony-flow-panel">
          <ol class="telephony-flow-steps">{flow}</ol>
        </div>
      </div>
    </section>

    <section class="page-section alt">
      <div class="container capabilities-page-cta">
        <h2>Connect {cfg['title']} to EMAAVY</h2>
        <p>See live routing and agent handoff in a tailored demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="index.html" class="btn-outline">All integrations</a>
        </div>
      </div>
    </section>"""

    out = PAGES / f"{key}.html"
    out.write_text(
        PAGE_SHELL.format(
            title=cfg["title"],
            desc=cfg["lead"][:155],
            route=cfg["route"],
            content=content,
        ),
        encoding="utf-8",
    )
    print("wrote", out.name)


UNIFIED_PROMO = r'''<div class="int-showcase reveal integrations-promo-wrap" id="integrations-emaavy">
  <div class="int-shell integrations-promo-shell">
    <div class="integrations-promo reveal">
      <div class="integrations-promo-copy">
        <span class="section-kicker">Integrations · EMAAVY</span>
        <h3>Your entire AI stack — one connective layer</h3>
        <p class="integrations-promo-lead">EMAAVY is the operating system that wires telephony, reasoning, speech, voice, and workflow tools into a single voice agent platform. Configure once, scale globally, and open any layer for full specs on its own page.</p>
        <ul class="integrations-promo-highlights" aria-label="Integration highlights">
          <li><strong>Five layers</strong> — telephony, LLMs, STT, TTS, and tools working as one pipeline</li>
          <li><strong>17+ partners</strong> — carriers, models, and CRMs without fragmented vendors</li>
          <li><strong>Per-call routing</strong> — swap providers by language, campaign, or intent</li>
          <li><strong>Enterprise ready</strong> — sub-second latency targets and 99.9% platform uptime</li>
        </ul>
        <div class="integrations-promo-actions">
          <a href="pages/integrations/index.html" class="btn-integrations-explore">Explore all integrations</a>
          <a href="book-demo.html" class="btn-integrations-secondary">Book a demo</a>
        </div>
      </div>
      <div class="integrations-promo-panel" aria-hidden="true">
        <div class="integrations-promo-panel-head">Five layers EMAAVY connects</div>
        <div class="integrations-layer-cards">
          <a href="pages/integrations/telephony.html" class="integrations-layer-card">
            <span class="integrations-layer-label">01 · Telephony</span>
            <strong>Voice infrastructure</strong>
            <span class="integrations-layer-meta">8+ carriers · 180+ countries</span>
          </a>
          <a href="pages/integrations/llms.html" class="integrations-layer-card">
            <span class="integrations-layer-label">02 · LLMs</span>
            <strong>Reasoning engine</strong>
            <span class="integrations-layer-meta">5 model families · 128K context</span>
          </a>
          <a href="pages/integrations/stt.html" class="integrations-layer-card">
            <span class="integrations-layer-label">03 · Speech-to-Text</span>
            <strong>Live transcription</strong>
            <span class="integrations-layer-meta">9 providers · &lt;0.5s latency</span>
          </a>
          <a href="pages/integrations/tts.html" class="integrations-layer-card">
            <span class="integrations-layer-label">04 · Text-to-Speech</span>
            <strong>Human-like voice</strong>
            <span class="integrations-layer-meta">2 engines · 22 languages</span>
          </a>
          <a href="pages/integrations/tools.html" class="integrations-layer-card">
            <span class="integrations-layer-label">05 · Tools</span>
            <strong>Workflow automation</strong>
            <span class="integrations-layer-meta">CRM · calendar · messaging</span>
          </a>
        </div>
      </div>
    </div>
    <div class="integrations-promo-stats">
      <div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>5</b><span>Stack layers</span></div>
      <div class="int-stat"><b>17+</b><span>Partners</span></div>
      <div class="int-stat"><b>1</b><span>Unified API</span></div>
      <div class="int-stat"><b>99.9%</b><span>Platform uptime</span></div>
    </div>
  </div>
</div>
</section>'''

INTEGRATIONS_CSS = r"""
/* ═══ INTEGRATIONS — unified landing promo ═══ */
.integrations-promo-shell {
  padding: clamp(2rem, 4vw, 2.75rem) clamp(1.25rem, 4vw, 2.25rem) !important;
}
.integrations-promo {
  display: grid !important;
  grid-template-columns: 1.05fr 0.95fr !important;
  gap: clamp(1.5rem, 4vw, 2.25rem) !important;
  align-items: start !important;
  text-align: left !important;
  margin-bottom: 1.75rem !important;
}
.integrations-promo h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.5rem, 3.2vw, 2.1rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.12 !important;
  color: #0f172a !important;
  margin: 0 0 1rem !important;
  max-width: 22ch !important;
}
.integrations-promo-lead {
  font-size: clamp(0.9rem, 1.45vw, 1.02rem) !important;
  line-height: 1.7 !important;
  color: #475569 !important;
  margin: 0 0 1.2rem !important;
  max-width: 54ch !important;
}
.integrations-promo-highlights {
  list-style: none !important;
  margin: 0 0 1.6rem !important;
  padding: 0 !important;
  display: grid !important;
  gap: 0.5rem !important;
}
.integrations-promo-highlights li {
  font-size: 0.86rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  padding: 0.32rem 0 0.32rem 0.85rem !important;
  border-left: 3px solid #4A658B !important;
}
.integrations-promo-highlights strong { color: #0f172a !important; font-weight: 600 !important; }
.integrations-promo-actions {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 0.7rem !important;
}
.btn-integrations-explore {
  display: inline-flex !important;
  align-items: center !important;
  padding: 0.82rem 1.5rem !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important;
  color: #fff !important;
  background: #4A658B !important;
  border: none !important;
  border-radius: 8px !important;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(74, 101, 139, 0.28) !important;
}
.btn-integrations-explore:hover { background: #18345D !important; transform: translateY(-1px) !important; }
.btn-integrations-secondary {
  display: inline-flex !important;
  align-items: center !important;
  padding: 0.8rem 1.3rem !important;
  font-size: 0.86rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  background: #fff !important;
  border: 1px solid #cbd5e1 !important;
  border-radius: 8px !important;
  text-decoration: none !important;
}
.btn-integrations-secondary:hover { border-color: #4A658B !important; background: #f8fafc !important; }
.integrations-promo-panel {
  padding: 1.2rem 1rem !important;
  border-radius: 10px !important;
  background: linear-gradient(145deg, #f8fafc 0%, #f0f4f8 100%) !important;
  border: 1px solid #e2e8f0 !important;
}
.integrations-promo-panel-head {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.75rem !important;
}
.integrations-layer-cards {
  display: grid !important;
  gap: 0.45rem !important;
}
.integrations-layer-card {
  display: grid !important;
  grid-template-columns: 1fr auto !important;
  grid-template-rows: auto auto !important;
  gap: 0.1rem 0.5rem !important;
  padding: 0.65rem 0.75rem !important;
  border-radius: 8px !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  text-decoration: none !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.integrations-layer-card:hover {
  border-color: #4A658B !important;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06) !important;
}
.integrations-layer-label {
  grid-column: 1 !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.integrations-layer-card strong {
  grid-column: 1 !important;
  font-size: 0.88rem !important;
  color: #0f172a !important;
  font-weight: 600 !important;
}
.integrations-layer-meta {
  grid-column: 2 !important;
  grid-row: 1 / span 2 !important;
  align-self: center !important;
  font-size: 0.62rem !important;
  color: #4A658B !important;
  text-align: right !important;
  max-width: 11ch !important;
  line-height: 1.35 !important;
}
.integrations-promo-stats {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.65rem !important;
  padding-top: 0.25rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
.integrations-promo-stats .int-stat {
  text-align: center !important;
  padding: 0.85rem 0.5rem !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
}
.integrations-promo-stats .int-stat b {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.25rem !important;
  color: #4A658B !important;
  margin-bottom: 0.2rem !important;
}
@media (max-width: 900px) {
  .integrations-promo { grid-template-columns: 1fr !important; }
  .integrations-promo h3 { max-width: none !important; }
  .integrations-promo-stats { grid-template-columns: repeat(2, 1fr) !important; }
  .integrations-layer-meta { display: none !important; }
}
"""


def patch_home():
    text = HTML.read_text(encoding="utf-8")
    pat = re.compile(
        r'<p class="int-hub-desc">.*?</p>\s*</div>\s*'
        r'<div class="int-showcase reveal(?: telephony-promo-wrap)?" id="integration-telephony">.*?'
        r'</div>\s*</div>\s*</section>\s*<!-- AGENTS -->',
        re.S,
    )
    hub_desc = (
        '<p class="int-hub-desc">EMAAVY connects your full AI voice stack in five layers. '
        "Explore telephony, models, speech, voice, and tools on dedicated pages — same tab, no scroll marathon.</p>"
    )
    repl = f"</div>\n {hub_desc}\n {UNIFIED_PROMO}\n <!-- AGENTS -->"
    text2, n = pat.subn(repl, text, count=1)
    if not n:
        raise SystemExit("home replace failed")
    HTML.write_text(text2, encoding="utf-8")
    print("patched home")


def patch_css():
    text = HTML.read_text(encoding="utf-8")
    if "INTEGRATIONS — unified landing promo" not in text:
        marker = "/* ═══ TELEPHONY — landing promo"
        if marker in text:
            text = text.replace(marker, INTEGRATIONS_CSS + "\n" + marker, 1)
        else:
            text = text.replace(
                "/* ═══ PLATFORM CAPABILITIES — landing promo ═══ */",
                "/* ═══ PLATFORM CAPABILITIES — landing promo ═══ */" + INTEGRATIONS_CSS,
                1,
            )
        HTML.write_text(text, encoding="utf-8")
    print("patched inline css")


def patch_routes():
    text = ROUTES.read_text(encoding="utf-8")
    text = text.replace(
        "{ id: 'telephony', label: 'Explore telephony', path: 'pages/integrations/telephony.html' },",
        "{ id: 'telephony', label: 'Telephony layer', path: 'pages/integrations/telephony.html' },",
    )
    llm_block = """    llm: [
      { id: 'llms', label: 'LLM layer', path: 'pages/integrations/llms.html' },
      { id: 'openai', label: 'OpenAI GPT', path: 'pages/integrations/openai.html' },
      { id: 'claude', label: 'Claude', path: 'pages/integrations/claude.html' },
      { id: 'gemini', label: 'Gemini', path: 'pages/integrations/gemini.html' },
      { id: 'qwen', label: 'Qwen', path: 'pages/integrations/qwen.html' },
      { id: 'grok', label: 'Grok', path: 'pages/integrations/grok.html' },
    ],"""
    stt_block = """    stt: [
      { id: 'stt', label: 'STT layer', path: 'pages/integrations/stt.html' },
      { id: 'assemblyai', label: 'AssemblyAI', path: 'pages/integrations/assemblyai.html' },
      { id: 'azure-stt', label: 'Azure Speech', path: 'pages/integrations/azure-stt.html' },
      { id: 'deepgram', label: 'Deepgram', path: 'pages/integrations/deepgram.html' },
      { id: 'elevenlabs-stt', label: 'ElevenLabs STT', path: 'pages/integrations/elevenlabs-stt.html' },
      { id: 'gladia', label: 'Gladia', path: 'pages/integrations/gladia.html' },
      { id: 'google-stt', label: 'Google STT', path: 'pages/integrations/google-stt.html' },
      { id: 'openai-stt', label: 'OpenAI Whisper', path: 'pages/integrations/openai-stt.html' },
      { id: 'sarvam', label: 'Sarvam AI', path: 'pages/integrations/sarvam.html' },
      { id: 'smallest', label: 'Smallest AI', path: 'pages/integrations/smallest.html' },
    ],"""
    tts_block = """    tts: [
      { id: 'tts', label: 'TTS layer', path: 'pages/integrations/tts.html' },
      { id: 'elevenlabs', label: 'ElevenLabs', path: 'pages/integrations/elevenlabs.html' },
      { id: 'flash-bulbul', label: 'Flash · Bulbul', path: 'pages/integrations/flash-bulbul.html' },
    ],"""
    tools_block = """    tools: [
      { id: 'tools', label: 'Tools layer', path: 'pages/integrations/tools.html' },
      { id: 'webhooks', label: 'Webhooks', path: 'pages/integrations/webhooks.html' },
      { id: 'calcom', label: 'Cal.com', path: 'pages/integrations/calcom.html' },
      { id: 'google-calendar', label: 'Google Calendar', path: 'pages/integrations/google-calendar.html' },
      { id: 'whatsapp', label: 'WhatsApp', path: 'pages/integrations/whatsapp.html' },
      { id: 'slack', label: 'Slack', path: 'pages/integrations/slack.html' },
      { id: 'salesforce', label: 'Salesforce', path: 'pages/integrations/salesforce.html' },
      { id: 'hubspot', label: 'HubSpot', path: 'pages/integrations/hubspot.html' },
    ],"""
    text = re.sub(r"    llm: \[.*?\],", llm_block, text, count=1, flags=re.S)
    text = re.sub(r"    stt: \[.*?\],", stt_block, text, count=1, flags=re.S)
    text = re.sub(r"    tts: \[.*?\],", tts_block, text, count=1, flags=re.S)
    text = re.sub(r"    tools: \[.*?\],", tools_block, text, count=1, flags=re.S)
    text = text.replace("title: '🧠 LLMs'", "title: 'LLMs'")
    text = text.replace("title: '🎙 STT'", "title: 'STT'")
    text = text.replace("title: '🔊 TTS'", "title: 'TTS'")
    text = text.replace("title: '🔧 Tools'", "title: 'Tools'")
    ROUTES.write_text(text, encoding="utf-8")
    print("patched routes")


def patch_masthead_dropdown():
    text = HTML.read_text(encoding="utf-8")
    # Replace inline masthead integration dropdown sections with layer links
    new_dropdown = """<div class="dropdown-section"> <div class="dropdown-section-title"> Integrations</div> <div class="dropdown-link-grid"> <a href="pages/integrations/index.html">All integrations</a> <a href="pages/integrations/telephony.html">Telephony</a> <a href="pages/integrations/llms.html">LLMs</a> <a href="pages/integrations/stt.html">Speech-to-Text</a> <a href="pages/integrations/tts.html">Text-to-Speech</a> <a href="pages/integrations/tools.html">Tools</a> </div> </div>"""
    # Keep LLM/STT/etc subsections - simplify to one integrations block + maybe keep provider links?
    # User asked single segment - simplify masthead to layers only
    pat = re.compile(
        r'<div class="nav-dropdown-menu mega">.*?</div>\s*</div>\s*</div>\s*</nav>',
        re.S,
    )
    m = pat.search(text)
    if not m:
        print("masthead dropdown skip")
        return
    inner = m.group(0)
    if "pages/integrations/llms.html" in inner:
        print("masthead already patched")
        return
    # Replace mega menu content only
    mega_pat = re.compile(r'(<div class="nav-dropdown-menu mega">).*?(</div>\s*</div>\s*</div>\s*</nav>)', re.S)
    def replacer(mm):
        return mm.group(1) + new_dropdown + " " + mm.group(2)
    text2 = mega_pat.sub(replacer, text, count=1)
    HTML.write_text(text2, encoding="utf-8")
    print("patched masthead dropdown")


def patch_nav_scroll():
    text = HTML.read_text(encoding="utf-8")
    old = "'integrations', 'integration-telephony', 'integration-llm', 'integration-stt', 'integration-tts', 'integration-tools'"
    new = "'integrations'"
    if old in text:
        text = text.replace(old, new)
        HTML.write_text(text, encoding="utf-8")
        print("patched nav scroll sections")


def patch_index():
    path = PAGES / "index.html"
    s = path.read_text(encoding="utf-8")
    layers = """        <div class="int-layer-nav">
          <a href="telephony.html" class="int-layer-pill">Telephony</a>
          <a href="llms.html" class="int-layer-pill">LLMs</a>
          <a href="stt.html" class="int-layer-pill">STT</a>
          <a href="tts.html" class="int-layer-pill">TTS</a>
          <a href="tools.html" class="int-layer-pill">Tools</a>
        </div>
"""
    if "int-layer-nav" not in s:
        s = s.replace('<div class="card-grid">', layers + '        <div class="card-grid">', 1)
        path.write_text(s, encoding="utf-8")
    if "int-layer-pill" not in (SITE_CSS.read_text(encoding="utf-8")):
        SITE_CSS.write_text(
            SITE_CSS.read_text(encoding="utf-8")
            + """
.int-layer-nav { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.5rem; }
.int-layer-pill {
  padding: 0.45rem 0.9rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: #4A658B;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 999px;
  text-decoration: none;
}
.int-layer-pill:hover { background: #4A658B; color: #fff; border-color: #4A658B; }
""",
            encoding="utf-8",
        )
    print("patched index")


if __name__ == "__main__":
    for key, cfg in CATEGORIES.items():
        build_category_page(key, cfg)
    patch_home()
    patch_css()
    patch_routes()
    patch_masthead_dropdown()
    patch_nav_scroll()
    patch_index()
