#!/usr/bin/env python3
"""Generate LLM hub + per-model integration pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

HEAD_COMMON = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/masthead-flex.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
  <link rel="stylesheet" href="../../assets/emaavy-theme.css" />
"""

MODELS = [
    {
        "slug": "openai",
        "name": "OpenAI GPT",
        "short": "OpenAI",
        "region": "Flagship reasoning",
        "tag": "Flagship",
        "featured": True,
        "logo": '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "OpenAI GPT — EMAAVY",
        "h1": "OpenAI GPT",
        "meta": "Connect OpenAI GPT with EMAAVY — flagship reasoning for sales flows, objection handling, and structured extraction from live calls.",
        "lead": "OpenAI's GPT family delivers the deepest reasoning available for voice agents — multi-step objection handling, dynamic scripts, and reliable JSON extraction when every turn shapes revenue.",
        "stats": [("128K", "Context window"), ("Top tier", "Reasoning"), ("Per-agent", "Routing")],
        "about": [
            "OpenAI builds frontier large language models used across enterprise copilots, support automation, and sales enablement. GPT models excel at following complex instructions, maintaining conversational coherence over long calls, and producing structured outputs for CRM systems.",
            "Teams choose OpenAI when calls involve high-value deals, technical products, or multi-objection sequences where lighter models lose thread. API access supports streaming for low-latency voice loops and function calling for live tool use during calls.",
        ],
        "emaavy": [
            ("Flagship agent brain", "Assign GPT-5.x class models to closing agents and enterprise outbound programs by default."),
            ("Structured dispositions", "Extract JSON fields — budget, timeline, objections — straight from live transcripts."),
            ("Mid-call escalation", "Start on a fast model for greeting; escalate to GPT when intent complexity spikes."),
            ("Cost governance", "Cap tokens per campaign while keeping premium models on high-intent segments only."),
        ],
        "features": [
            ("Multi-step reasoning", "Handle nested objections without losing campaign context."),
            ("Function calling", "Book meetings, query knowledge bases, and update CRM mid-call."),
            ("Streaming responses", "Token streams feed TTS for natural voice pacing."),
            ("JSON mode", "Reliable structured outputs for scoring and disposition codes."),
            ("Long context", "Full call history plus knowledge snippets in one prompt."),
            ("Fine-tuning ready", "Optional custom models for brand tone and compliance phrasing."),
        ],
        "uses": [
            ("Enterprise sales", "Complex B2B cycles with technical discovery and legal hurdles."),
            ("High-ACV outbound", "Agents that must reason before offering discounts or trials."),
            ("Compliance review", "Calls where nuanced language and audit trails matter."),
        ],
        "setup": [
            ("Add OpenAI API key", "Store organization keys in EMAAVY with role-based access."),
            ("Pick default models", "Map GPT variants per agent type — closer vs. support vs. survey."),
            ("Define extraction schemas", "Configure JSON fields synced to Salesforce or HubSpot."),
            ("Pilot on one campaign", "Compare conversion and handle time against your baseline model."),
        ],
        "hub_desc": "Flagship reasoning for complex sales flows, multi-step objection handling, and structured data extraction.",
        "hub_points": ["Multi-step objection handling", "Structured JSON extraction", "Dynamic script adaptation"],
        "hub_badge": "Flagship",
    },
    {
        "slug": "claude",
        "name": "Claude",
        "short": "Claude",
        "region": "Enterprise · Anthropic",
        "tag": "Enterprise",
        "logo": '<img src="https://cdn.simpleicons.org/anthropic/191919" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/anthropic/191919" alt="" width="32" height="32" loading="lazy" />',
        "title": "Claude — EMAAVY",
        "h1": "Claude",
        "meta": "Anthropic Claude and EMAAVY — nuanced comprehension for compliance-sensitive and high-empathy voice programs.",
        "lead": "Claude Opus, Sonnet, and Haiku give EMAAVY teams a spectrum from maximum comprehension to cost-efficient turns — ideal when tone, policy, and long-context memory define call quality.",
        "stats": [("200K", "Context (Opus)"), ("3 tiers", "Opus · Sonnet · Haiku"), ("Enterprise", "Ready")],
        "about": [
            "Anthropic's Claude models are known for careful instruction following, reduced hallucination risk on policy-heavy topics, and strong performance on long documents. Enterprises in finance, healthcare, and regulated BPOs often standardize on Claude for customer-facing AI.",
            "The model family lets you pair Haiku-class speed for intent classification with Sonnet or Opus for negotiation and escalation — all through the same EMAAVY agent configuration layer.",
        ],
        "emaavy": [
            ("Compliance-first tone", "Claude excels on scripts with legal disclaimers and sensitive data handling."),
            ("Long-call memory", "Maintain context across 30+ minute support or onboarding sessions."),
            ("Tiered routing", "Route simple FAQs to Haiku; escalate to Opus for dispute resolution."),
            ("Human handoff briefs", "Generate supervisor summaries with cited transcript spans."),
        ],
        "features": [
            ("Opus depth", "Maximum reasoning for escalations and executive-facing calls."),
            ("Sonnet balance", "Default workhorse for sales and support agents at scale."),
            ("Haiku speed", "Sub-second classifications and slot-filling during live audio."),
            ("Document grounding", "Inject policy PDFs and playbooks into the prompt stack."),
            ("Consistent voice", "Stable personality across marathon conversations."),
            ("Safety alignment", "Built-in refusals align with enterprise acceptable-use policies."),
        ],
        "uses": [
            ("Regulated industries", "Banking, insurance, and healthcare voice programs."),
            ("Empathy-heavy support", "Billing disputes, cancellations saves, and VIP care."),
            ("Long-form discovery", "Calls that require many qualifying questions before close."),
        ],
        "setup": [
            ("Connect Anthropic API", "Add keys and set allowed model IDs per environment."),
            ("Map tiers to intents", "Define when EMAAVY upgrades from Haiku to Sonnet or Opus."),
            ("Upload playbooks", "Attach policy docs agents may cite during calls."),
            ("Review sample calls", "QA team validates tone before full traffic migration."),
        ],
        "hub_desc": "Best-in-class comprehension for nuanced, compliance-sensitive, and high-empathy conversations.",
        "hub_points": ["Opus · Sonnet · Haiku tiers", "Long-context call memory", "Policy-grounded responses"],
        "hub_badge": "Enterprise",
    },
    {
        "slug": "gemini",
        "name": "Gemini",
        "short": "Gemini",
        "region": "Google · Real-time",
        "tag": "Real-time",
        "logo": '<img src="https://cdn.simpleicons.org/google/4285F4" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/google/4285F4" alt="" width="32" height="32" loading="lazy" />',
        "title": "Gemini — EMAAVY",
        "h1": "Gemini Flash",
        "meta": "Google Gemini and EMAAVY — ultra-fast inference for live intent detection and real-time voice agent loops.",
        "lead": "Gemini Flash brings Google-scale infrastructure and millisecond-class inference to EMAAVY — perfect for intent detection, slot filling, and agent replies when latency beats raw reasoning depth.",
        "stats": [("Flash", "Low latency"), ("Multimodal", "Ready"), ("Google", "Cloud")],
        "about": [
            "Google Gemini is a family of multimodal models spanning ultra-fast Flash variants to larger Pro tiers. Flash models are optimized for high-throughput, low-latency workloads — exactly the profile live voice agents need on every conversational turn.",
            "Organizations already on Google Cloud can keep billing, VPC, and IAM patterns while EMAAVY orchestrates which Gemini variant handles classification versus response generation per call segment.",
        ],
        "emaavy": [
            ("Live intent scoring", "Classify buyer intent on every utterance without blocking TTS."),
            ("Flash for loops", "Default Flash models on high-QPS outbound campaigns."),
            ("Pro on escalation", "Swap to heavier Gemini when scripts require deeper reasoning."),
            ("Workspace synergy", "Optional hooks for Calendar, Docs, and internal knowledge bases."),
        ],
        "features": [
            ("Gemini Flash", "Optimized for real-time voice turn latency."),
            ("Intent classifiers", "Parallel scoring pipelines during active calls."),
            ("Multimodal future", "Room for visual context in advanced agent flows."),
            ("Google Cloud IAM", "Enterprise security and region pinning."),
            ("Cost efficiency", "Lower per-token cost on classification-heavy programs."),
            ("Streaming API", "Token streams aligned with EMAAVY voice pacing."),
        ],
        "uses": [
            ("High-QPS outbound", "Dialer campaigns needing fast turn-taking."),
            ("Intent routing", "Pre-qualify leads before expensive flagship model time."),
            ("Google-native stacks", "Teams standardized on GCP and Workspace."),
        ],
        "setup": [
            ("Enable Gemini API", "Connect Google Cloud project and API credentials."),
            ("Set Flash defaults", "Assign Flash to greeting and qualification agents."),
            ("Define escalation rules", "Promote to Pro/Ultra analogs on intent triggers."),
            ("Load test latency", "Benchmark turn time against SLA targets."),
        ],
        "hub_desc": "Ultra-fast inference for real-time intent detection and responsive voice agent loops.",
        "hub_points": ["Sub-second classification", "Flash-optimized voice turns", "GCP-native security"],
        "hub_badge": "Real-time",
    },
    {
        "slug": "qwen",
        "name": "Qwen",
        "short": "Qwen",
        "region": "Multilingual · APAC",
        "tag": "Multilingual",
        "logo": '<span class="brand-mark">QW</span>',
        "logo_sm": '<span class="brand-mark">QW</span>',
        "title": "Qwen — EMAAVY",
        "h1": "Qwen 3.6",
        "meta": "Qwen and EMAAVY — cost-efficient multilingual models for Hinglish, regional Indian dialects, and APAC voice programs.",
        "lead": "Qwen delivers strong multilingual performance at efficient price points — EMAAVY routes Hinglish, Tamil, Telugu, and other regional programs to Qwen when global models miss nuance or economics.",
        "stats": [("22+", "Language fit"), ("Cost", "Efficient"), ("Hinglish", "Native feel")],
        "about": [
            "Qwen is Alibaba Cloud's open-model family widely adopted for multilingual chat, code, and voice-agent backends across APAC. Recent versions improve Indic language handling, code-mixed Hinglish, and dialect robustness compared with generic Western-trained models.",
            "For Indian outbound and support at millions of minutes per month, Qwen often becomes the default reasoning layer — with EMAAVY handling telephony, STT, and CRM sync around it.",
        ],
        "emaavy": [
            ("Regional campaigns", "Dedicated Qwen agents per language and script variant."),
            ("Cost control", "Run qualification on Qwen; reserve GPT/Claude for closing tiers."),
            ("Dialect tuning", "Prompt packs tuned for city-specific vocabulary and honorifics."),
            ("Unified analytics", "Same intent and sentiment layer regardless of model vendor."),
        ],
        "features": [
            ("Hinglish fluency", "Natural code-mixed sales and support dialogue."),
            ("Regional languages", "Hindi, Tamil, Telugu, Bengali, and more."),
            ("Efficient tokens", "Lower cost per minute on scale outbound."),
            ("Open-weight options", "Deploy variants matching data residency needs."),
            ("Structured output", "JSON dispositions for Indian CRM ecosystems."),
            ("Fast inference", "Suitable for sub-2s voice turn targets on optimized hardware."),
        ],
        "uses": [
            ("India outbound", "D2C, fintech, and ed-tech dial programs."),
            ("Multilingual BPO", "Single platform across language queues."),
            ("Cost-sensitive pilots", "Prove ROI before upgrading select agents to flagship models."),
        ],
        "setup": [
            ("Connect Qwen endpoint", "API keys or self-hosted gateway in EMAAVY."),
            ("Language per agent", "Bind Qwen variants to agent language profiles."),
            ("Localize scripts", "Upload region-specific objection handlers."),
            ("A/B against GPT", "Measure conversion and CSAT by language cohort."),
        ],
        "hub_desc": "Cost-efficient multilingual model optimized for Hinglish and regional Indian dialects.",
        "hub_points": ["Hinglish and Indic languages", "Efficient at high minute volumes", "Regional script libraries"],
        "hub_badge": "Multilingual",
    },
    {
        "slug": "grok",
        "name": "Grok",
        "short": "Grok",
        "region": "xAI · Experimental",
        "tag": "Experimental",
        "logo": '<span class="brand-mark">GX</span>',
        "logo_sm": '<span class="brand-mark">GX</span>',
        "title": "Grok — EMAAVY",
        "h1": "Grok",
        "meta": "Grok and EMAAVY — experimental reasoning for creative outbound scripts and dynamic rebuttals.",
        "lead": "Grok from xAI offers a distinct reasoning style — bold, adaptive copy and dynamic rebuttals. EMAAVY lets innovation teams pilot Grok on select campaigns without destabilizing production defaults.",
        "stats": [("Pilot", "Programs"), ("Dynamic", "Scripts"), ("xAI", "Stack")],
        "about": [
            "Grok is xAI's conversational model family positioned for real-time knowledge and creative generation. While not every enterprise standardizes on Grok for regulated support, it shines in experimental outbound where fresh hooks and rapid rebuttal invention matter.",
            "EMAAVY treats Grok as a first-class routing target — sandbox agents, champion-challenger tests, and creative campaign variants can call Grok while core support lines stay on Claude or GPT.",
        ],
        "emaavy": [
            ("Creative outbound", "Generate variant openings and rebuttals per industry vertical."),
            ("Champion-challenger", "Run Grok on 5–10% traffic with automatic KPI comparison."),
            ("Sandbox agents", "Isolate experimental prompts from production knowledge bases."),
            ("Fast iteration", "Swap Grok prompts daily without redeploying telephony."),
        ],
        "features": [
            ("Dynamic scripts", "Less rigid templates; more adaptive banter within guardrails."),
            ("Rebuttal invention", "Respond to uncommon objections with novel angles."),
            ("Pilot isolation", "Separate API quotas and monitoring per experiment."),
            ("Real-time tone", "Conversational style suited for challenger brands."),
            ("Guardrail layer", "EMAAVY policy filters still apply before speech."),
            ("Easy rollback", "One-click revert to GPT/Claude defaults per agent."),
        ],
        "uses": [
            ("PLG outbound", "Startup campaigns testing edgy positioning."),
            ("Challenger brands", "Categories where differentiation beats safe scripts."),
            ("Innovation labs", "Internal teams exploring next-gen agent personalities."),
        ],
        "setup": [
            ("Enable Grok API", "Add xAI credentials to a sandbox workspace."),
            ("Clone production agent", "Fork an agent profile for Grok-only traffic."),
            ("Set traffic cap", "Limit dial percentage until KPIs validate."),
            ("Review compliance", "Legal approves sample calls before scale."),
        ],
        "hub_desc": "Experimental reasoning for creative outbound scripts and dynamic rebuttals on pilot campaigns.",
        "hub_points": ["Creative script variants", "Champion-challenger testing", "Sandboxed from production"],
        "hub_badge": "Experimental",
    },
]


def model_nav(current: str) -> str:
    links = []
    for m in MODELS:
        cls = ' class="is-current"' if m["slug"] == current else ""
        links.append(f'<a href="{m["slug"]}.html"{cls}>{m["short"]}</a>')
    links.append('<a href="llms.html">All LLMs</a>')
    return "\n          ".join(links)


def render_partner(m: dict) -> str:
    stats = "".join(
        f'<div class="llm-partner-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in m["stats"]
    )
    about = "".join(f"<p>{para}</p>" for para in m["about"])
    benefits = "".join(
        f'<li><div><strong>{t}</strong><span>{d}</span></div></li>'
        for t, d in m["emaavy"]
    )
    features = "".join(
        f'<article class="llm-feature-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in m["features"]
    )
    uses = "".join(
        f'<article class="llm-use-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in m["uses"]
    )
    setup = "".join(
        f'<li><div><strong>{t}</strong><p>{d}</p></div></li>'
        for t, d in m["setup"]
    )
    route = f"integration-{m['slug']}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{m['title']}</title>
  <meta name="description" content="{m['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{m['title']}" />
  <meta property="og:description" content="{m['meta']}" />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/llm-partner.css" />
</head>
<body data-base="../../" data-route="{route}">
  <div id="site-nav-root"></div>
  <main class="page-main llm-partner-page">
    <section class="llm-partner-hero">
      <div class="container llm-partner-hero-grid">
        <div class="llm-partner-hero-copy">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="../../index.html">Home</a>
            <span aria-hidden="true"> / </span>
            <a href="../../index.html#integrations">Integrations</a>
            <span aria-hidden="true"> / </span>
            <a href="llms.html">LLMs</a>
            <span aria-hidden="true"> / </span>
            <span>{m['short']}</span>
          </nav>
          <span class="llm-partner-kicker">LLMs · {m['tag']}</span>
          <h1>{m['h1']}</h1>
          <p class="llm-partner-lead">{m['lead']}</p>
          <div class="llm-partner-stats">{stats}</div>
          <div class="llm-partner-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Connect {m['short']}</a>
            <a href="llms.html" class="btn-outline">All models</a>
          </div>
        </div>
        <aside class="llm-partner-hero-card" aria-label="{m['name']} overview">
          <div class="llm-partner-hero-logo">{m['logo']}</div>
          <span class="llm-partner-hero-region">{m['region']}</span>
          <p>Powered through EMAAVY — per-agent routing, mid-call escalation, and live CRM extraction.</p>
        </aside>
      </div>
    </section>

    <section class="llm-partner-section">
      <div class="container">
        <header class="llm-partner-section-head">
          <h2>What {m['short']} is built for</h2>
          <p>Choosing the right model family shapes conversion, compliance, and cost on every call.</p>
        </header>
        <div class="llm-partner-prose">{about}</div>
      </div>
    </section>

    <section class="llm-partner-section alt">
      <div class="container llm-partner-split">
        <header class="llm-partner-section-head">
          <h2>How EMAAVY uses {m['short']}</h2>
          <p>One orchestration layer — swap models by agent, campaign, or intent without rebuilding voice infrastructure.</p>
        </header>
        <ul class="llm-partner-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="llm-partner-section">
      <div class="container">
        <header class="llm-partner-section-head">
          <h2>Key capabilities</h2>
          <p>What teams enable when {m['short']} drives EMAAVY voice agents.</p>
        </header>
        <div class="llm-feature-grid">{features}</div>
      </div>
    </section>

    <section class="llm-partner-section alt">
      <div class="container">
        <header class="llm-partner-section-head">
          <h2>Ideal use cases</h2>
          <p>Where {m['short']} and EMAAVY deliver the strongest combined outcomes.</p>
        </header>
        <div class="llm-use-grid">{uses}</div>
      </div>
    </section>

    <section class="llm-partner-section">
      <div class="container">
        <header class="llm-partner-section-head">
          <h2>Getting connected</h2>
          <p>From API credentials to production traffic on EMAAVY.</p>
        </header>
        <ol class="llm-setup-steps">{setup}</ol>
      </div>
    </section>

    <section class="llm-partner-section alt">
      <div class="container">
        <header class="llm-partner-section-head">
          <h2>Explore other models</h2>
          <p>Mix providers by campaign — EMAAVY keeps transcripts, scoring, and CRM sync consistent.</p>
        </header>
        <nav class="llm-partner-nav-strip" aria-label="LLM partners">
          {model_nav(m['slug'])}
        </nav>
      </div>
    </section>

    <section class="llm-partner-cta">
      <div class="container">
        <h2>Ready to connect {m['short']}?</h2>
        <p>Book a walkthrough — we will map model routing, extraction schemas, and a live agent demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="llms.html" class="btn-outline">LLM overview</a>
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


def card_html(m: dict) -> str:
    points = "".join(f"<li>{x}</li>" for x in m["hub_points"])
    featured = " llm-model-card--native" if m.get("featured") else ""
    cta = "Explore integration →" if not m.get("featured") else "View full integration →"
    badge = f'<span class="llm-model-badge">{m["hub_badge"]}</span>'
    return f"""          <a href="{m['slug']}.html" id="{m['slug']}" class="llm-model-card{featured}">
            <div class="llm-model-card-top">
              <div class="llm-model-card-logo">{m['logo_sm']}</div>
              {badge}
            </div>
            <h3>{m['name']}</h3>
            <p class="llm-model-card-desc">{m['hub_desc']}</p>
            <ul class="llm-model-card-points">{points}</ul>
            <span class="llm-model-card-cta">{cta}</span>
          </a>"""


def render_hub() -> str:
    cards = "\n".join(card_html(m) for m in MODELS)
    jumps = " ".join(f'<a href="#{m["slug"]}">{m["short"]}</a>' for m in MODELS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>LLMs — EMAAVY</title>
  <meta name="description" content="EMAAVY routes flagship reasoning, real-time inference, and multilingual models per agent, per intent, or mid-call — without losing context." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="LLMs — EMAAVY" />
  <meta property="og:description" content="Connect GPT, Claude, Gemini, Qwen, and Grok to EMAAVY voice agents with per-call orchestration." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/llm-hub.css" />
</head>
<body data-base="../../" data-route="integration-llms">
  <div id="site-nav-root"></div>
  <main class="page-main llm-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../index.html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../index.html#integrations">Integrations</a>
          <span aria-hidden="true"> / </span>
          <span>LLMs</span>
        </nav>
        <span class="page-kicker">Reasoning layer · LLMs</span>
        <h1>The reasoning engine behind every conversation</h1>
        <p class="telephony-hero-lead">EMAAVY routes flagship reasoning, real-time inference, and multilingual models per agent, per intent, or mid-call — without losing context. Engineering sets defaults once; operations swaps models by campaign without rebuilding agents.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>5</b><span>Model families</span></div>
          <div class="stat-box"><b>128K+</b><span>Max context</span></div>
          <div class="stat-box"><b>Per-turn</b><span>Routing</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#reasoning-layer">How EMAAVY orchestrates</a>
          <a href="#models">Model partners</a>
          <a href="#orchestration">Orchestration flow</a>
          {jumps}
        </div>
      </div>
    </section>

    <section id="reasoning-layer" class="llm-hub-reasoning">
      <div class="container">
        <article class="llm-hub-reasoning-card">
          <div class="llm-hub-reasoning-meta">
            <span class="llm-hub-reasoning-num">Layer 02</span>
            <span class="llm-hub-reasoning-tag">EMAAVY · LLMs</span>
            <h2>How EMAAVY orchestrates LLMs</h2>
            <p class="llm-hub-reasoning-lead">One conversation layer, many models. Pick flagship reasoning for closes, flash models for intent, and regional models for Hinglish — all on the same agent definitions.</p>
          </div>
          <div class="llm-hub-pill-grid">
            <div class="llm-hub-pill"><strong>Per-agent routing</strong><span>Assign GPT, Claude, Gemini, Qwen, or Grok per workflow.</span></div>
            <div class="llm-hub-pill"><strong>Mid-call switching</strong><span>Escalate to a heavier model when complexity spikes.</span></div>
            <div class="llm-hub-pill"><strong>Structured extraction</strong><span>JSON dispositions and scores from live transcripts.</span></div>
            <div class="llm-hub-pill"><strong>Cost control</strong><span>Flash for classification; flagship models for closing.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="models" class="llm-hub-models page-section alt">
      <div class="container">
        <header class="llm-hub-models-head">
          <h2>Model partners</h2>
          <p>Five families integrated today — each with a dedicated page on capabilities, EMAAVY orchestration, and rollout steps.</p>
        </header>
        <div class="llm-model-grid">
{cards}
        </div>
      </div>
    </section>

    <section id="orchestration" class="llm-hub-flow">
      <div class="container">
        <header class="llm-hub-flow-head">
          <h2>Live orchestration flow</h2>
          <p>How every conversational turn moves through EMAAVY — regardless of which LLM you select.</p>
        </header>
        <div class="llm-flow-track">
          <article class="llm-flow-step"><strong>Transcript in</strong><p>Live speech becomes text in the reasoning pipeline.</p></article>
          <article class="llm-flow-step"><strong>Model selected</strong><p>EMAAVY picks the model for intent, language, and SLA.</p></article>
          <article class="llm-flow-step"><strong>Intent scored</strong><p>Buyer signals update on every turn.</p></article>
          <article class="llm-flow-step"><strong>Data extracted</strong><p>Structured fields map to CRM and campaigns.</p></article>
          <article class="llm-flow-step"><strong>Agent speaks</strong><p>TTS delivers the model-backed reply.</p></article>
        </div>
      </div>
    </section>

    <section class="llm-hub-cta">
      <div class="container">
        <h2>Connect LLMs to EMAAVY</h2>
        <p>See live model routing, extraction, and agent handoff in a tailored demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="index.html" class="btn-outline">All integrations</a>
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


def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = ["      { id: 'llms', label: 'LLM layer', path: 'pages/integrations/llms.html' },"]
    for m in MODELS:
        label = m["name"]
        lines.append(
            f"      {{ id: '{m['slug']}', label: '{label}', path: 'pages/integrations/{m['slug']}.html' }},"
        )
    block = "    llm: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    llm: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "llms.html").write_text(render_hub(), encoding="utf-8")
    for m in MODELS:
        (INT / f"{m['slug']}.html").write_text(render_partner(m), encoding="utf-8")
    update_routes()
    print(f"OK: LLM hub + {len(MODELS)} model pages, routes.js updated")


if __name__ == "__main__":
    main()
