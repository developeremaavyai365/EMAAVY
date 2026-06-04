#!/usr/bin/env python3
"""Generate AI Workforce hub + per-role agent pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "pages" / "agents"

HEAD_COMMON = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/masthead-flex.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
  <link rel="stylesheet" href="../../assets/emaavy-theme.css" />
"""

ROLES = [
    {
        "slug": "sales-agent",
        "name": "Sales Agent",
        "short": "Sales",
        "region": "Revenue · Outbound & inbound sales",
        "tag": "Voice · Sales",
        "route": "agent-sales-agent",
        "logo": '<span class="brand-mark">SA</span>',
        "title": "Sales Agent — EMAAVY",
        "h1": "Sales Agent",
        "meta": "EMAAVY Sales Agent — qualifies leads, handles objections, and books meetings with human-like persuasion in 22 languages.",
        "lead": "The Sales Agent is built for revenue teams — it prospects, discovers pain, handles multi-step objections, and books meetings live on the call while syncing outcomes to your CRM.",
        "stats": [("28%", "Conversion lift"), ("24/7", "Coverage"), ("Live", "Booking")],
        "about": [
            "Sales voice agents replace repetitive SDR dialers with conversations that adapt when prospects push back. EMAAVY routes flagship LLMs, expressive TTS, and Cal.com or Google Calendar booking so a verbal yes becomes a confirmed slot before hang-up.",
            "Unlike static IVR scripts, the Sales Agent scores intent on every turn — escalating pricing, legal, or custom requests to humans with full transcript context.",
        ],
        "emaavy": [
            ("Objection intelligence", "Dynamic rebuttals grounded in your playbook and live transcript."),
            ("Meeting capture", "Cal.com or Google Calendar events created during the call."),
            ("CRM dispositions", "Salesforce and HubSpot fields updated from extracted outcomes."),
            ("Language routing", "Hinglish and regional voices via Bulbul; global English via ElevenLabs."),
        ],
        "features": [
            ("Multi-step discovery", "Qualify budget, authority, need, and timeline naturally."),
            ("Dynamic scripts", "LLM-backed responses — not fixed audio trees."),
            ("Intent scoring", "Hot leads flagged for human takeover in real time."),
            ("Campaign pacing", "Timezone-aware outreach with retry rules."),
            ("WhatsApp follow-up", "Send brochures or links after positive disposition."),
            ("QA & coaching", "Full transcripts and scores for every conversation."),
        ],
        "uses": [
            ("SDR outbound", "Top-of-funnel qualification at scale."),
            ("Inbound sales lines", "Answer marketing hotlines and route qualified buyers."),
            ("Event registration", "Confirm attendance with personalized voice outreach."),
        ],
        "setup": [
            ("Clone Sales template", "Start from EMAAVY Sales Agent preset in the builder."),
            ("Upload playbook", "Objection handlers and pricing guardrails."),
            ("Connect CRM & calendar", "Wire Salesforce or HubSpot plus scheduling tool."),
            ("Pilot one segment", "A/B against human SDRs on a single cohort."),
        ],
        "hub_desc": "Qualifies leads, handles objections, and books meetings — with natural Hinglish and regional fluency.",
        "hub_points": ["Multi-step objection handling", "Live Cal.com booking", "Intent scoring & CRM sync"],
        "hub_badge": "Voice · Sales",
    },
    {
        "slug": "support-agent",
        "name": "Support Agent",
        "short": "Support",
        "region": "CX · Empathetic resolution",
        "tag": "Voice · Support",
        "route": "agent-support-agent",
        "logo": '<span class="brand-mark">SU</span>',
        "title": "Support Agent — EMAAVY",
        "h1": "Support Agent",
        "meta": "EMAAVY Support Agent — empathetic ticket triage, FAQ resolution, and escalation with full context.",
        "lead": "The Support Agent de-escalates frustrated callers, answers FAQs from your knowledge base, and opens tickets or escalates to specialists — with sentiment-aware tone on every turn.",
        "stats": [("61%", "Faster resolution"), ("22", "Languages"), ("Live", "Escalation")],
        "about": [
            "Support programs drown in repeat questions and long hold times. EMAAVY Support Agents answer 24/7 with empathy calibrated to sentiment — warming tone when frustration spikes and firm clarity for policy boundaries.",
            "When complexity exceeds agent scope, EMAAVY packages transcript, intent, and customer history for human specialists in Slack or your ticketing system.",
        ],
        "emaavy": [
            ("Sentiment-aware voice", "Tone adapts when CSAT risk rises mid-call."),
            ("Knowledge grounding", "FAQ and policy snippets injected per turn."),
            ("Ticket automation", "Zendesk-style payloads via webhooks or CRM."),
            ("Human handoff", "Supervisor join with full conversation context."),
        ],
        "features": [
            ("FAQ resolution", "Answer common questions without queue wait."),
            ("Order & account lookup", "Integrate via tools layer webhooks."),
            ("Escalation rules", "Route on keywords, sentiment, or VIP tags."),
            ("CSAT surveys", "Optional post-call feedback capture."),
            ("Multilingual support", "Regional languages on domestic hotlines."),
            ("Compliance logging", "Full audit trail for regulated industries."),
        ],
        "uses": [
            ("Consumer support hotlines", "Billing, shipping, and product help."),
            ("BPO overflow", "Night and weekend coverage without hiring."),
            ("Internal IT helpdesk", "Password resets and policy FAQs."),
        ],
        "setup": [
            ("Import knowledge base", "PDFs, URLs, or structured FAQ entries."),
            ("Define escalation matrix", "Map intents to queues and Slack channels."),
            ("Connect ticketing", "Webhook or native CRM sync."),
            ("Tune empathy prompts", "Brand voice review with QA team."),
        ],
        "hub_desc": "Resolves issues, de-escalates frustrated callers, and routes complex cases with full context.",
        "hub_points": ["Sentiment-aware responses", "Auto ticket creation", "Human escalation triggers"],
        "hub_badge": "Voice · Support",
    },
    {
        "slug": "outbound-agent",
        "name": "Outbound Agent",
        "short": "Outbound",
        "region": "Outbound · Proactive dial",
        "tag": "Outbound · Calls",
        "route": "agent-outbound-agent",
        "logo": '<span class="brand-mark">OB</span>',
        "title": "Outbound Agent — EMAAVY",
        "h1": "Outbound Agent",
        "meta": "EMAAVY Outbound Agent — proactive outbound calls, dialer pacing, and campaign programs at any scale.",
        "lead": "The Outbound Agent places every proactive call in your programs — personalized openers, intelligent pacing across time zones, and live CRM updates — plus high-volume campaigns for registrations, reminders, and nurture sequences.",
        "stats": [("10M+", "Contacts/month"), ("68%", "Peak registration"), ("Smart", "Pacing")],
        "about": [
            "Outbound voice fails when dialers sound robotic or dispositions never reach your CRM. EMAAVY Outbound Agents combine Bulbul and ElevenLabs voices with Qwen or GPT reasoning for natural Hinglish and English calls — from one-off follow-ups to millions of contacts per month.",
            "Run classic outbound programs (collections, renewals, SDR lists) and campaign-style flows (events, registrations) on the same agent template — case studies like Warehouse by Mudita show 68% registration when voice replaces email.",
        ],
        "emaavy": [
            ("Proactive dialer", "Upload lists, assign agent, launch from EMAAVY campaigns UI."),
            ("Pacing & retry", "Timezone windows, max attempts, and backoff rules."),
            ("Personalized openers", "Name and context variables from contact rows."),
            ("Post-call WhatsApp", "Template messages after positive disposition."),
        ],
        "features": [
            ("High-volume outbound", "Tens of thousands of calls placed per day."),
            ("Registration flows", "Capture yes/no and send confirmation paths."),
            ("Reminder programs", "Appointments, payments, and renewals."),
            ("Real-time analytics", "Connect rates and disposition dashboards."),
            ("DNC & compliance", "Respect opt-out flags on contact lists."),
            ("Multi-language cohorts", "Split programs by language automatically."),
        ],
        "uses": [
            ("SDR & lead lists", "Proactive qualification and follow-up calls."),
            ("Exhibition & events", "Voice invitations with high conversion."),
            ("Collections", "Polite reminder programs with escalation paths."),
        ],
        "setup": [
            ("Create outbound program", "EMAAVY five-step campaign builder."),
            ("Upload contact list", "CSV with required disposition fields."),
            ("Assign Outbound Agent", "Select voice and script template."),
            ("Monitor live", "Supervisor dashboard for connect and conversion."),
        ],
        "hub_desc": "Places outbound calls at scale — pacing, personalized scripts, and campaign programs from one agent.",
        "hub_points": ["Proactive dialer & pacing", "Personalized scripts", "Campaign & list programs"],
        "hub_badge": "Outbound · Calls",
    },
    {
        "slug": "inbound-agent",
        "name": "Inbound Agent",
        "short": "Inbound",
        "region": "Inbound · 24/7 answer",
        "tag": "Inbound · Calls",
        "route": "agent-inbound-agent",
        "logo": '<span class="brand-mark">IB</span>',
        "title": "Inbound Agent — EMAAVY",
        "h1": "Inbound Agent",
        "meta": "EMAAVY Inbound Agent — answer customer calls 24/7, route by intent, and hand off to humans with zero hold-queue backlog.",
        "lead": "The Inbound Agent answers every call to your DID or toll-free line — greeting callers, resolving tier-1 requests, and queuing or transferring to humans when the conversation requires it, without business-hour gaps.",
        "stats": [("24/7", "Always answering"), ("&lt;2s", "Time to greet"), ("0", "Queue backlog")],
        "about": [
            "Inbound voice is where brand trust is won or lost — long hold music and outdated IVR trees drive churn. EMAAVY Inbound Agents pick up on the first ring, understand natural speech, and resolve FAQs or route by intent using the same intelligence layer as outbound programs.",
            "Pair inbound agents with support or sales playbooks: billing questions stay in support flows, while high-intent buyers transfer to live closers with transcript summaries delivered in Slack or CRM.",
        ],
        "emaavy": [
            ("DID & toll-free ready", "Connect any inbound number from your telephony layer."),
            ("IVR replacement", "Natural language menu — callers speak instead of pressing keys."),
            ("Intent-based routing", "Sales vs. support vs. billing paths without caller frustration."),
            ("After-hours coverage", "Same quality at 2 AM as peak Monday morning."),
        ],
        "features": [
            ("Instant answer", "Sub-second greeting on connect."),
            ("FAQ & status checks", "Order tracking, balance, and policy answers."),
            ("Warm transfer", "Human specialist receives context before join."),
            ("Voicemail capture", "Structured callbacks when humans unavailable."),
            ("Multilingual lines", "Hindi, English, and regional language per DID."),
            ("Call analytics", "Volume, intent mix, and resolution rate live."),
        ],
        "uses": [
            ("Customer support hotlines", "Replace legacy IVR with conversational AI."),
            ("Sales inquiry lines", "Capture marketing campaign call-backs."),
            ("Healthcare & services", "Appointment booking and triage on inbound DID."),
        ],
        "setup": [
            ("Provision inbound DID", "Map number to Inbound Agent in telephony settings."),
            ("Define intent routes", "Support, sales, and escalation queues."),
            ("Load knowledge & scripts", "Greeting, verification, and FAQ content."),
            ("Test warm transfer", "Validate human handoff with supervisor desk."),
        ],
        "hub_desc": "Answers inbound calls 24/7 — route by intent, resolve tier-1 issues, and warm-transfer to your team.",
        "hub_points": ["Instant answer on every DID", "Natural language routing", "Warm transfer with context"],
        "hub_badge": "Inbound · Calls",
    },
]


def role_nav(current: str) -> str:
    links = []
    for r in ROLES:
        cls = ' class="is-current"' if r["slug"] == current else ""
        links.append(f'<a href="{r["slug"]}.html"{cls}>{r["short"]}</a>')
    links.append('<a href="workforce.html">Workforce overview</a>')
    return "\n          ".join(links)


def render_role(r: dict) -> str:
    stats = "".join(
        f'<div class="agents-role-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in r["stats"]
    )
    about = "".join(f"<p>{para}</p>" for para in r["about"])
    benefits = "".join(
        f'<li><div><strong>{t}</strong><span>{d}</span></div></li>'
        for t, d in r["emaavy"]
    )
    features = "".join(
        f'<article class="agents-feature-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in r["features"]
    )
    uses = "".join(
        f'<article class="agents-use-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in r["uses"]
    )
    setup = "".join(
        f'<li><div><strong>{t}</strong><p>{d}</p></div></li>'
        for t, d in r["setup"]
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{r['title']}</title>
  <meta name="description" content="{r['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{r['title']}" />
  <meta property="og:description" content="{r['meta']}" />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/agents-role.css" />
</head>
<body data-base="../../" data-route="{r['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main agents-role-page">
    <section class="agents-role-hero">
      <div class="container agents-role-hero-grid">
        <div class="agents-role-hero-copy">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="../../index.html">Home</a>
            <span aria-hidden="true"> / </span>
            <a href="../../index.html#agents">Agents</a>
            <span aria-hidden="true"> / </span>
            <a href="workforce.html">AI Workforce</a>
            <span aria-hidden="true"> / </span>
            <span>{r['short']}</span>
          </nav>
          <span class="agents-role-kicker">AI Voice Agent · {r['tag']}</span>
          <h1>{r['h1']}</h1>
          <p class="agents-role-lead">{r['lead']}</p>
          <div class="agents-role-stats">{stats}</div>
          <div class="agents-role-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Deploy {r['name']}</a>
            <a href="workforce.html" class="btn-outline">All agent roles</a>
          </div>
        </div>
        <aside class="agents-role-hero-card" aria-label="{r['name']} overview">
          <div class="agents-role-hero-logo">{r['logo']}</div>
          <span class="agents-role-hero-region">{r['region']}</span>
          <p>Powered by EMAAVY — voice, LLM, STT, TTS, and tools layers orchestrated per agent.</p>
        </aside>
      </div>
    </section>

    <section class="agents-role-section">
      <div class="container">
        <header class="agents-role-section-head">
          <h2>What the {r['name']} does</h2>
          <p>Role overview and when to deploy this agent on your voice programs.</p>
        </header>
        <div class="agents-role-prose">{about}</div>
      </div>
    </section>

    <section class="agents-role-section alt">
      <div class="container agents-role-split">
        <header class="agents-role-section-head">
          <h2>How EMAAVY runs the {r['name']}</h2>
          <p>One platform — unique voice, prompts, and integrations per role without rebuilding your stack.</p>
        </header>
        <ul class="agents-role-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="agents-role-section">
      <div class="container">
        <header class="agents-role-section-head">
          <h2>Key capabilities</h2>
          <p>What teams enable when the {r['name']} is live on EMAAVY.</p>
        </header>
        <div class="agents-feature-grid">{features}</div>
      </div>
    </section>

    <section class="agents-role-section alt"{' id="campaigns"' if r['slug'] == 'outbound-agent' else ''}>
      <div class="container">
        <header class="agents-role-section-head">
          <h2>Ideal use cases</h2>
          <p>Where the {r['name']} delivers the strongest outcomes.</p>
        </header>
        <div class="agents-use-grid">{uses}</div>
      </div>
    </section>

    <section class="agents-role-section">
      <div class="container">
        <header class="agents-role-section-head">
          <h2>Getting started</h2>
          <p>From template to production calls on EMAAVY.</p>
        </header>
        <ol class="agents-setup-steps">{setup}</ol>
      </div>
    </section>

    <section class="agents-role-section alt">
      <div class="container">
        <header class="agents-role-section-head">
          <h2>Explore other agent roles</h2>
          <p>Mix sales, support, outbound campaigns, and inbound lines — one workforce, many missions.</p>
        </header>
        <nav class="agents-role-nav-strip" aria-label="Agent roles">
          {role_nav(r['slug'])}
        </nav>
      </div>
    </section>

    <section class="agents-role-cta">
      <div class="container">
        <h2>Ready to deploy the {r['name']}?</h2>
        <p>Book a walkthrough — hear a live call, review scripts, and map your first campaign.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="workforce.html" class="btn-outline">AI Workforce overview</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""


def card_html(r: dict) -> str:
    points = "".join(f"<li>{x}</li>" for x in r["hub_points"])
    badge = f'<span class="agents-role-badge">{r["hub_badge"]}</span>'
    return f"""          <a href="{r['slug']}.html" id="{r['slug'].replace('-agent', '')}" class="agents-role-card">
            <div class="agents-role-card-top">
              <div class="agents-role-card-logo">{r['logo']}</div>
              {badge}
            </div>
            <h3>{r['name']}</h3>
            <p class="agents-role-card-desc">{r['hub_desc']}</p>
            <ul class="agents-role-card-points">{points}</ul>
            <span class="agents-role-card-cta">Explore role →</span>
          </a>"""


def render_workforce() -> str:
    cards = "\n".join(card_html(r) for r in ROLES)
    jumps = " ".join(
        f'<a href="#{r["slug"].replace("-agent", "")}">{r["short"]}</a>' for r in ROLES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Voice Workforce — EMAAVY</title>
  <meta name="description" content="Deploy EMAAVY AI voice agents for sales, support, inbound, and outbound campaigns — human-like voice, live intelligence, and visual builder flows." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="AI Voice Workforce — EMAAVY" />
  <meta property="og:description" content="Meet your EMAAVY AI workforce — sales, support, outbound, and inbound agents with dedicated specs and deployment paths." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/agents-hub.css" />
</head>
<body data-base="../../" data-route="agents-workforce">
  <div id="site-nav-root"></div>
  <main class="page-main agents-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../index.html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../index.html#agents">Agents</a>
          <span aria-hidden="true"> / </span>
          <span>AI Workforce</span>
        </nav>
        <span class="page-kicker">AI Workforce · Voice Agents</span>
        <h1>Meet your AI workforce</h1>
        <p class="telephony-hero-lead">Agents that speak like humans, think faster, and never call in sick. Deploy in minutes — each with its own voice, flow, and mission — running 24/7 across outbound, inbound, and every language you serve.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>24/7</b><span>Always on</span></div>
          <div class="stat-box"><b>22</b><span>Languages</span></div>
          <div class="stat-box"><b>4</b><span>Agent roles</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#workforce-layer">How EMAAVY runs agents</a>
          <a href="#roles">Agent roles</a>
          <a href="#builder">Custom builder</a>
          <a href="#deploy">Deploy flow</a>
          {jumps}
        </div>
      </div>
    </section>

    <section id="workforce-layer" class="agents-hub-workforce">
      <div class="container">
        <article class="agents-hub-workforce-card">
          <div class="agents-hub-workforce-meta">
            <span class="agents-hub-workforce-num">AI Workforce</span>
            <span class="agents-hub-workforce-tag">EMAAVY · Voice Agents</span>
            <h2>How EMAAVY runs your voice agents</h2>
            <p class="agents-hub-workforce-lead">One platform for every conversational role. Operations launches campaigns; engineering wires LLM, STT, TTS, and tools once — then swaps voices and flows per agent without rebuilding the stack.</p>
          </div>
          <div class="agents-hub-pill-grid">
            <div class="agents-hub-pill"><strong>Per-agent routing</strong><span>Unique voice, prompt stack, and integrations per role.</span></div>
            <div class="agents-hub-pill"><strong>Live handoff</strong><span>Supervisors join when sentiment or intent signals escalation.</span></div>
            <div class="agents-hub-pill"><strong>Inbound &amp; outbound</strong><span>Same intelligence layer for DID lines and dialer campaigns.</span></div>
            <div class="agents-hub-pill"><strong>Full logging</strong><span>Transcripts, scores, and CRM dispositions on every call.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="roles" class="agents-hub-roles page-section alt">
      <div class="container">
        <header class="agents-hub-roles-head">
          <h2>Agent roles</h2>
          <p>Four mission-ready agents — each with a dedicated page covering capabilities, EMAAVY orchestration, and rollout steps.</p>
        </header>
        <div class="agents-role-grid agents-role-grid--quad">
{cards}
        </div>
      </div>
    </section>

    <section id="builder" class="agents-hub-builder">
      <div class="container">
        <article class="agents-builder-card" id="builder">
          <div class="agents-builder-meta">
            <span class="agents-hub-workforce-num">Custom</span>
            <span class="agents-builder-tag">AI Agents · Builder</span>
            <h2>Custom Agent Builder</h2>
            <p class="agents-builder-lead">Design any voice flow in minutes — pick a voice, set prompts, branch logic, and deploy across languages. No code required to go live.</p>
            <ul class="agents-builder-points">
              <li>Visual drag-and-drop flow builder</li>
              <li>Bulbul V3 &amp; ElevenTurbo voice selection</li>
              <li>Custom multi-step branching logic</li>
              <li>Per-agent LLM &amp; STT routing</li>
            </ul>
            <div class="cta-row">
              <a href="../../book-demo.html" class="btn-primary">Build your agent</a>
              <a href="../../pages/documentation.html" class="btn-outline">Agent builder docs</a>
            </div>
          </div>
          <div class="agents-hub-pill-grid">
            <div class="agents-hub-pill"><strong>Clone any role</strong><span>Start from Sales, Support, Outbound, or Inbound templates.</span></div>
            <div class="agents-hub-pill"><strong>Test sandbox</strong><span>Simulate calls before attaching live DIDs or lists.</span></div>
            <div class="agents-hub-pill"><strong>Version control</strong><span>Publish prompt changes without downtime.</span></div>
            <div class="agents-hub-pill"><strong>Multi-campaign</strong><span>One agent definition, many campaign assignments.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="deploy" class="agents-hub-flow">
      <div class="container">
        <header class="agents-hub-flow-head">
          <h2>From idea to live calls</h2>
          <p>Typical path from template to optimized production traffic.</p>
        </header>
        <div class="agents-flow-track">
          <article class="agents-flow-step"><strong>Choose a role</strong><p>Sales, Support, Outbound, Inbound, or blank builder.</p></article>
          <article class="agents-flow-step"><strong>Configure voice</strong><p>Prompts, branching, languages, and triggers.</p></article>
          <article class="agents-flow-step"><strong>Connect stack</strong><p>Telephony, LLM, STT, TTS, and CRM layers.</p></article>
          <article class="agents-flow-step"><strong>Launch</strong><p>Outbound lists or inbound DIDs go live.</p></article>
          <article class="agents-flow-step"><strong>Optimize</strong><p>Scores and transcripts feed coaching loops.</p></article>
        </div>
      </div>
    </section>

    <section class="agents-hub-cta">
      <div class="container">
        <h2>Deploy your AI workforce on EMAAVY</h2>
        <p>See live agents on sales, support, inbound, and campaign calls in a tailored demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="index.html" class="btn-outline">Agent directory</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""


def render_index() -> str:
    cards = "\n".join(
        f"""          <a href="{r['slug']}.html" class="glow-card"><div class="card-icon"><span class="brand-mark">{r['logo'].replace('<span class="brand-mark">', '').replace('</span>', '')[:2] if 'brand-mark' in r['logo'] else 'AG'}</span></div><h3>{r['name']}</h3><p>{r['hub_desc'][:90]}…</p><span class="card-tag">Explore →</span></a>"""
        for r in ROLES
    )
    # Fix index cards - use explicit marks
    marks = {"sales-agent": "SA", "support-agent": "SU", "outbound-agent": "OB", "inbound-agent": "IB"}
    cards = "\n".join(
        f'          <a href="{r["slug"]}.html" class="glow-card"><div class="card-icon"><span class="brand-mark">{marks[r["slug"]]}</span></div><h3>{r["name"]}</h3><p>{r["hub_desc"]}</p><span class="card-tag">Explore →</span></a>'
        for r in ROLES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Voice Agents — EMAAVY</title>
  <meta name="description" content="Deploy EMAAVY AI voice agents for sales, support, inbound lines, and outbound campaigns at any scale." />
  <meta name="robots" content="index, follow" />
{HEAD_COMMON}
</head>
<body data-base="../../" data-route="agents">
  <div id="site-nav-root"></div>
  <main class="page-main">
    <section class="page-hero">
      <div class="container">
        <span class="page-kicker">AI Workforce</span>
        <h1>Meet your AI agents</h1>
        <p>Agents that speak like humans, think faster, and never call in sick — explore the full workforce overview or jump to a role.</p>
        <div class="cta-row" style="margin-top:1.25rem">
          <a href="workforce.html" class="btn-primary">Full workforce overview →</a>
        </div>
      </div>
    </section>
    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">
          <a href="workforce.html" class="int-layer-pill">Overview</a>
          <a href="sales-agent.html" class="int-layer-pill">Sales</a>
          <a href="support-agent.html" class="int-layer-pill">Support</a>
          <a href="outbound-agent.html" class="int-layer-pill">Outbound</a>
          <a href="inbound-agent.html" class="int-layer-pill">Inbound</a>
          <a href="workforce.html#builder" class="int-layer-pill">Builder</a>
        </div>
        <div class="card-grid cols-2">
{cards}
          <a href="workforce.html#builder" class="glow-card"><div class="card-icon"><span class="brand-mark">CB</span></div><h3>Custom Agent Builder</h3><p>Visual flows, custom prompts, and multi-language deployment in minutes.</p><span class="card-tag">Build →</span></a>
        </div>
        <div class="cta-row" style="margin-top:2rem"><a href="../../book-demo.html" class="btn-primary">Build your agent →</a></div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""


def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = [
        "      { id: 'workforce', label: 'AI Workforce', path: 'pages/agents/workforce.html' },",
    ]
    for r in ROLES:
        label = r["name"]
        rid = r["slug"].replace("-agent", "-agent")  # keep slug as id
        lines.append(
            f"      {{ id: '{r['slug']}', label: '{label}', path: 'pages/agents/{r['slug']}.html' }},"
        )
    block = "    agents: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"  agents: \[[\s\S]*?\n  \],", block, text, count=1)
    path.write_text(text, encoding="utf-8")


def patch_landing():
    outbound_card = (
        '      <a href="pages/agents/outbound-agent.html" class="hub-clear-card hub-clear-card--no-num" role="listitem">'
        '<h3 class="hub-clear-card-title">Outbound calls</h3>'
        '<p class="hub-clear-card-desc">Proactive dialer, pacing, and personalized outreach at scale.</p></a>\n'
    )
    inbound_card = (
        '      <a href="pages/agents/inbound-agent.html" class="hub-clear-card hub-clear-card--no-num" role="listitem">'
        '<h3 class="hub-clear-card-title">Inbound calls</h3>'
        '<p class="hub-clear-card-desc">24/7 answer, intent routing, and warm transfer.</p></a>\n'
    )
    for name in ["emaavy_white_blue (2).html", "index.html"]:
        path = ROOT / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        agents_cards = (
            '      <a href="pages/agents/outbound-agent.html" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Outbound calls</h3><p class="hub-clear-card-desc">Proactive dialer, pacing, and personalized outreach at scale.</p></a>\n'
            + inbound_card
            + '      <a href="pages/agents/outbound-agent.html#campaigns" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Campaigns &amp; outreach</h3><p class="hub-clear-card-desc">Registrations, follow-ups, and lead programs.</p></a>\n'
        )
        if "Outbound calls</h3>" not in text and "Customer experience</h3>" in text:
            text = text.replace(
                '      <a href="pages/agents/support-agent.html" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Customer experience</h3><p class="hub-clear-card-desc">Support, triage, and specialist escalation.</p></a>\n',
                '      <a href="pages/agents/support-agent.html" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Customer experience</h3><p class="hub-clear-card-desc">Support, triage, and specialist escalation.</p></a>\n'
                + agents_cards,
                1,
            )
        if "Inbound calls</h3>" not in text:
            old = """      <a href="pages/agents/outbound-agent.html" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Campaigns &amp; outreach</h3><p class="hub-clear-card-desc">Registrations, follow-ups, and lead programs.</p></a>
      <a href="pages/agents/workforce.html" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Industry workflows</h3>"""
            new = outbound_card + inbound_card + """      <a href="pages/agents/outbound-agent.html#campaigns" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Campaigns &amp; outreach</h3><p class="hub-clear-card-desc">Registrations, follow-ups, and lead programs.</p></a>
      <a href="pages/agents/workforce.html" class="hub-clear-card hub-clear-card--no-num" role="listitem"><h3 class="hub-clear-card-title">Industry workflows</h3>"""
            if old in text:
                text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")


def main():
    AGENTS.mkdir(parents=True, exist_ok=True)
    (AGENTS / "workforce.html").write_text(render_workforce(), encoding="utf-8")
    (AGENTS / "index.html").write_text(render_index(), encoding="utf-8")
    for r in ROLES:
        (AGENTS / f"{r['slug']}.html").write_text(render_role(r), encoding="utf-8")
    update_routes()
    patch_landing()
    print(f"OK: workforce hub + index + {len(ROLES)} role pages (incl. inbound), routes & landing updated")


if __name__ == "__main__":
    main()
