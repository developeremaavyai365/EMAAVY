#!/usr/bin/env python3
"""Generate Call Lifecycle hub + per-stage detail pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LC_DIR = ROOT / "pages" / "call-lifecycle"

HEAD_COMMON = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/navbar-tokens.css" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/masthead-flex.css" />
  <link rel="stylesheet" href="../../assets/brand-logo.css" />
  <link rel="stylesheet" href="../../assets/navbar-typography.css" />
  <link rel="icon" href="../../assets/brand/emaavy-logo.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="../../assets/emaavy-type-tokens.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
  <link rel="stylesheet" href="../../assets/footer-premium.css" />
  <link rel="stylesheet" href="../../assets/emaavy-theme.css" />
  <link rel="stylesheet" href="../../assets/responsive-system.css" />
"""

STAGES = [
    {
        "slug": "ring",
        "step": "01",
        "name": "Call Connects",
        "short": "Ring",
        "route": "lifecycle-ring",
        "kicker": "Step 1 · Ring",
        "headline": "Ring — Call Connects",
        "region": "Ingest · Connect",
        "meta": "EMAAVY call lifecycle — Ring stage captures audio, metadata, and speaker context the moment a call connects.",
        "lead": "The lifecycle begins the moment the call connects. EMAAVY starts listening immediately — no warm-up delay, no dropped opening seconds, no intelligence lost before the first hello.",
        "stats": [("0ms", "Start delay"), ("100%", "Capture rate"), ("Instant", "Metadata")],
        "overview": [
            "Ring is the ingest stage. Whether inbound support, outbound campaign, or supervisor-monitored sales, EMAAVY attaches to the audio stream at connect and enriches it with caller ID, campaign tags, and consent state before transcription even starts.",
        ],
        "happens": [
            ("Audio capture", "Stream begins at answer — inbound or outbound."),
            ("Session metadata", "Caller ID, dialed number, and campaign ID logged."),
            ("Compliance flags", "Recording consent and regional rules applied."),
            ("Speaker context", "Diarization initialized for downstream stages."),
        ],
        "emaavy_steps": [
            ("Connect", "Telephony layer (Vobiz, SIP, or CPaaS) hands media to EMAAVY."),
            ("Tag", "Campaign, agent, and language hints attached to the session."),
            ("Record", "Optional encrypted recording with retention policy."),
            ("Stream", "Real-time audio forked to STT without batch delay."),
        ],
        "stack": ["Telephony", "SIP / CPaaS", "Session tagging", "Recording"],
        "outcomes": [
            ("100% pipeline entry", "Every answered call enters the intelligence pipeline."),
            ("Zero ring gap", "No delay between connect and first transcribed word."),
            ("Full attribution", "CRM and analytics receive complete session context."),
        ],
        "outcome_bullets": [
            "100% of answered calls enter the intelligence pipeline",
            "Zero gap between ring and first transcribed word",
            "Full attribution for downstream CRM and analytics",
        ],
        "hub_desc": "Outbound or inbound — audio, metadata, and speaker context from the first ring.",
        "hub_points": ["Instant capture at answer", "Campaign & consent tagging", "Live stream to STT"],
        "hub_badge": "Step 01 · Ring",
        "prev": None,
        "next": "transcribe",
    },
    {
        "slug": "transcribe",
        "step": "02",
        "name": "Every Word Captured",
        "short": "Transcribe",
        "route": "lifecycle-transcribe",
        "kicker": "Step 2 · Transcribe",
        "headline": "Transcribe — Every Word",
        "region": "STT · Streaming",
        "meta": "EMAAVY transcribe stage — sub-500ms streaming STT with Deepgram, Sarvam, and nine providers on the live wire.",
        "lead": "Transcription is not a post-call report. EMAAVY streams every word through your chosen STT stack — Deepgram for international accents, Sarvam for Indian languages — with sub-half-second word latency.",
        "stats": [("&lt;0.5s", "Word latency"), ("9+", "STT providers"), ("Streaming", "Architecture")],
        "overview": [
            "The transcribe stage turns speech into searchable text while the conversation is still happening. Supervisors, AI agents, and scoring models all consume the same live transcript — eliminating the batch-processing blind spot that plagues traditional call centers.",
        ],
        "happens": [
            ("Live partials", "Transcripts appear word-by-word in the intelligence layer."),
            ("Diarization", "Agent, customer, and AI voices separated."),
            ("Confidence scores", "Each token scored for QA review."),
            ("Keyword alerts", "Supervisor triggers on live phrase detection."),
        ],
        "emaavy_steps": [
            ("Route STT", "Per-language provider — Sarvam, Deepgram, Gladia, and more."),
            ("Enhance", "Telephony-optimized preprocessing for noisy lines."),
            ("Timestamp", "Word-level timing for playback and coaching sync."),
            ("Archive", "Full transcript stored for search, export, and compliance."),
        ],
        "stack": ["Deepgram", "Sarvam", "Gladia", "Streaming STT"],
        "outcomes": [
            ("Live coaching", "Supervisors act on what is being said, not was said."),
            ("AI context", "Voice agents respond with full conversational state."),
            ("QA automation", "Eliminate manual listen-and-type workflows."),
        ],
        "outcome_bullets": [
            "Supervisors coach on what is being said, not what was said",
            "AI agents respond with full conversational context",
            "QA teams eliminate manual listen-and-type workflows",
        ],
        "hub_desc": "Sub-500ms streaming STT — every word on the wire, not after hang-up.",
        "hub_points": ["9+ STT providers", "Word-level timestamps", "Live keyword detection"],
        "hub_badge": "Step 02 · Transcribe",
        "prev": "ring",
        "next": "analyze",
    },
    {
        "slug": "analyze",
        "step": "03",
        "name": "Score Live",
        "short": "Analyze",
        "route": "lifecycle-analyze",
        "kicker": "Step 3 · Analyze",
        "headline": "Analyze — Score Live",
        "region": "Intelligence · LLM",
        "meta": "EMAAVY analyze stage — per-turn sentiment, intent, objections, and compliance scoring before the caller hangs up.",
        "lead": "Analysis happens per conversational turn — not in a batch job overnight. Sentiment arcs, buyer intent, objection types, and compliance risk update live so teams can act before the caller hangs up.",
        "stats": [("Per-turn", "Scoring"), ("Live", "Alerts"), ("Multi-signal", "Intelligence")],
        "overview": [
            "The analyze stage is EMAAVY's reasoning layer. Your configured LLM stack interprets meaning, emotion, and risk on each turn, feeding the intelligence matrix dashboards and trigger engine simultaneously.",
        ],
        "happens": [
            ("Sentiment timeline", "Tone shifts green, amber, or red as the call evolves."),
            ("Intent classification", "Buy, explore, objection, or reject per turn."),
            ("Compliance flags", "Risky phrases flagged for regulated programs."),
            ("Objection tags", "Feed script coaching and funnel analytics."),
        ],
        "emaavy_steps": [
            ("Reason", "Route GPT, Claude, Gemini, Qwen, or Grok per workflow."),
            ("Score", "Sentiment, intent, and compliance models in parallel."),
            ("Alert", "Notify supervisors when thresholds breach."),
            ("Summarize", "Rolling call summary for handoff and CRM notes."),
        ],
        "stack": ["OpenAI", "Claude", "Gemini", "Intelligence Matrix"],
        "outcomes": [
            ("Live decisions", "Act on conversation state, not post-call guesswork."),
            ("In-call compliance", "Issues caught while the call is active."),
            ("Revenue signal", "Leaders see intent shift before deals slip."),
        ],
        "outcome_bullets": [
            "Decisions based on live conversation state, not post-call guesswork",
            "Compliance teams catch issues during the call",
            "Sales leaders see intent shift before deals slip away",
        ],
        "hub_desc": "Sentiment, intent, objections, and compliance scored on every turn.",
        "hub_points": ["Per-turn LLM reasoning", "Live supervisor alerts", "Rolling summaries"],
        "hub_badge": "Step 03 · Analyze",
        "prev": "transcribe",
        "next": "act",
    },
    {
        "slug": "act",
        "step": "04",
        "name": "Triggers Fire",
        "short": "Act",
        "route": "lifecycle-act",
        "kicker": "Step 4 · Act",
        "headline": "Act — Triggers Fire",
        "region": "Orchestration · Tools",
        "meta": "EMAAVY act stage — CRM, WhatsApp, calendar, webhooks, and coaching triggers fire from live call intelligence.",
        "lead": "Intelligence without action is noise. The Act stage fires CRM updates, WhatsApp confirmations, Cal.com bookings, coaching pings, and custom webhooks — automatically, from what was actually said on the call.",
        "stats": [("Zero", "Manual steps"), ("Instant", "Execution"), ("CRM + WA", "Connected")],
        "overview": [
            "Act is the orchestration layer. Business rules map conversation signals to downstream systems — so operations teams stop copying notes and developers stop polling for transcripts.",
        ],
        "happens": [
            ("CRM sync", "Dispositions and custom fields update mid-call or on end."),
            ("Follow-ups", "WhatsApp and email with personalized context."),
            ("Live booking", "Calendar events when the agent confirms a slot."),
            ("Coaching pings", "Supervisor alerts on negative sentiment shifts."),
        ],
        "emaavy_steps": [
            ("Match rules", "Intent thresholds, keywords, and sentiment gates."),
            ("Execute", "Native connectors and webhooks with retry logic."),
            ("Log", "Every trigger recorded in the audit trail."),
            ("Handoff", "Warm transfer to humans with full transcript."),
        ],
        "stack": ["Salesforce", "HubSpot", "WhatsApp", "Webhooks", "Cal.com"],
        "outcomes": [
            ("Continuity", "Customer journey continues after the voice call."),
            ("Revenue speed", "Meetings booked without manual CRM entry."),
            ("Evidence", "Support tickets include transcript attachments."),
        ],
        "outcome_bullets": [
            "Same-tab customer experience continues after the voice call",
            "Revenue teams see meetings booked without manual entry",
            "Support tickets created with transcript evidence attached",
        ],
        "hub_desc": "Webhooks, CRM updates, WhatsApp, and supervisor alerts — automatic.",
        "hub_points": ["Rule-based triggers", "Native CRM connectors", "Warm human handoff"],
        "hub_badge": "Step 04 · Act",
        "prev": "analyze",
        "next": "learn",
    },
    {
        "slug": "learn",
        "step": "05",
        "name": "Models Improve",
        "short": "Learn",
        "route": "lifecycle-learn",
        "kicker": "Step 5 · Learn",
        "headline": "Learn — Models Improve",
        "region": "Optimization · Loop",
        "meta": "EMAAVY learn stage — script A/B, model routing, and coaching patterns improve every campaign automatically.",
        "lead": "The lifecycle closes with learning. Every conversation feeds script A/B results, model routing refinements, and coaching patterns — so the next campaign performs better than the last.",
        "stats": [("Continuous", "Learning"), ("Auto", "Optimization"), ("A/B", "Scripts")],
        "overview": [
            "Learn turns operational data into compounding advantage. EMAAVY aggregates outcomes across campaigns to recommend script changes, STT/LLM routing tweaks, and agent coaching focus areas — without a separate data science team.",
        ],
        "happens": [
            ("Script ranking", "Variants scored by conversion and handle time."),
            ("Routing tuning", "STT and LLM paths adjusted per segment."),
            ("Coaching patterns", "Focus areas for under-performing agents."),
            ("Executive exports", "Funnel trends for leadership reviews."),
        ],
        "emaavy_steps": [
            ("Aggregate", "Roll up scores, outcomes, and durations."),
            ("Recommend", "Script and routing changes from win/loss patterns."),
            ("Loop", "Feed results into agent builder and campaign defaults."),
            ("Report", "Weekly intelligence summaries for leadership."),
        ],
        "stack": ["Analytics", "A/B scripts", "Agent builder", "Campaign defaults"],
        "outcomes": [
            ("Compounding conversion", "Rates improve quarter over quarter."),
            ("Lower cost", "Routing optimizes cost per outcome."),
            ("Data-led coaching", "QA moves from anecdote to metrics."),
        ],
        "outcome_bullets": [
            "Conversion rates improve quarter over quarter without new headcount",
            "Cost per outcome drops as routing optimizes automatically",
            "Coaching becomes data-led instead of anecdotal",
        ],
        "hub_desc": "Outcomes feed the next campaign — scripts, routing, and coaching improve.",
        "hub_points": ["Script A/B results", "Model routing refinements", "Ops dashboards"],
        "hub_badge": "Step 05 · Learn",
        "prev": "act",
        "next": "ring",
    },
]

STAGE_BY_SLUG = {s["slug"]: s for s in STAGES}


def stage_nav(current: str) -> str:
    links = []
    for s in STAGES:
        cls = ' class="is-current"' if s["slug"] == current else ""
        links.append(f'<a href="{s["slug"]}.html"{cls}>{s["short"]}</a>')
    links.append('<a href="index.html">Lifecycle overview</a>')
    return "\n          ".join(links)


def step_nav_buttons(s: dict) -> str:
    parts = []
    if s["prev"]:
        prev = STAGE_BY_SLUG[s["prev"]]
        parts.append(
            f'<a href="{prev["slug"]}.html" class="btn-outline">← {prev["short"]}</a>'
        )
    if s["next"]:
        nxt = STAGE_BY_SLUG[s["next"]]
        label = "Start cycle →" if s["slug"] == "learn" else f'{nxt["short"]} →'
        parts.append(f'<a href="{nxt["slug"]}.html" class="btn-outline">{label}</a>')
    return "\n            ".join(parts)


def render_stage(s: dict) -> str:
    stats = "".join(
        f'<div class="clc-stage-stat"><b>{a}</b><span>{b}</span></div>' for a, b in s["stats"]
    )
    overview = "".join(f"<p>{p}</p>" for p in s["overview"])
    happens = "".join(
        f'<article class="clc-feature-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in s["happens"]
    )
    benefits = "".join(
        f'<li><div><strong>{t}</strong><span>{d}</span></div></li>'
        for t, d in s["emaavy_steps"]
    )
    impl = "".join(
        f'<li><div><strong>{t}</strong><p>{d}</p></div></li>'
        for t, d in s["emaavy_steps"]
    )
    highlights = "".join(
        f'<article class="clc-feature-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in s["outcomes"]
    )
    bullets = "".join(f"<li>{b}</li>" for b in s["outcome_bullets"])
    stack = "".join(f'<span class="clc-stack-pill">{x}</span>' for x in s["stack"])
    nav_btns = step_nav_buttons(s)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{s['headline']} — Call Lifecycle — EMAAVY</title>
  <meta name="description" content="{s['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{s['headline']} — EMAAVY" />
  <meta property="og:description" content="{s['meta']}" />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/call-lifecycle-stage.css" />
</head>
<body data-base="../../" data-route="{s['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main clc-stage-page">
    <section class="clc-stage-hero">
      <div class="container clc-stage-hero-grid">
        <div class="clc-stage-hero-copy">
          <span class="clc-stage-kicker">Call Lifecycle · {s['kicker']}</span>
          <h1>{s['headline']}</h1>
          <p class="clc-stage-lead">{s['lead']}</p>
          <div class="clc-stage-stats">{stats}</div>
          <div class="clc-stage-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">See the lifecycle live</a>
            {nav_btns}
          </div>
        </div>
        <aside class="clc-stage-hero-card" aria-label="Stage {s['step']}">
          <div class="clc-stage-hero-logo"><span class="clc-stage-num">{s['step']}</span></div>
          <span class="clc-stage-hero-region">{s['region']}</span>
          <p>Stage <strong>{s['step']}</strong> of 5 — {s['name']} on the EMAAVY voice intelligence pipeline.</p>
        </aside>
      </div>
    </section>

    <section class="clc-stage-section" id="overview">
      <div class="container">
        <header class="clc-stage-section-head">
          <h2>Stage overview</h2>
          <p>What happens during {s['name']} and why it matters.</p>
        </header>
        <div class="clc-stage-prose">{overview}</div>
      </div>
    </section>

    <section class="clc-stage-section alt" id="happens">
      <div class="container">
        <header class="clc-stage-section-head">
          <h2>What happens on the call</h2>
          <p>Signals and events your team sees during this stage.</p>
        </header>
        <div class="clc-feature-grid">{happens}</div>
      </div>
    </section>

    <section class="clc-stage-section" id="emaavy">
      <div class="container clc-stage-split">
        <header class="clc-stage-section-head">
          <h2>How EMAAVY powers this stage</h2>
          <p>Platform steps from connect through downstream action.</p>
          <div class="clc-stack-pills">{stack}</div>
        </header>
        <ul class="clc-stage-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="clc-stage-section alt" id="implementation">
      <div class="container">
        <header class="clc-stage-section-head">
          <h2>Implementation flow</h2>
          <p>Technical path EMAAVY executes for {s['short']}.</p>
        </header>
        <ol class="clc-impl-steps">{impl}</ol>
      </div>
    </section>

    <section class="clc-stage-section" id="outcomes">
      <div class="container">
        <header class="clc-stage-section-head">
          <h2>Business outcomes</h2>
          <p>Measurable impact when {s['name']} runs on EMAAVY.</p>
        </header>
        <div class="clc-feature-grid">{highlights}</div>
        <ul class="clc-outcomes-list">{bullets}</ul>
      </div>
    </section>

    <section class="clc-stage-section alt">
      <div class="container">
        <header class="clc-stage-section-head">
          <h2>Explore lifecycle stages</h2>
          <p>Five connected stages — from ring to continuous improvement.</p>
        </header>
        <nav class="clc-stage-nav-strip" aria-label="Lifecycle stages">
          {stage_nav(s['slug'])}
        </nav>
      </div>
    </section>

    <section class="clc-stage-cta">
      <div class="container">
        <h2>See {s['name']} on a live call</h2>
        <p>Book a demo — walk through ring, transcribe, analyze, act, and learn on your stack.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="index.html" class="btn-outline">Lifecycle overview</a>
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


def card_html(s: dict) -> str:
    points = "".join(f"<li>{x}</li>" for x in s["hub_points"])
    return f"""          <a href="{s['slug']}.html" id="{s['slug']}" class="clc-stage-card">
            <div class="clc-stage-card-top">
              <div class="clc-stage-card-logo"><span class="clc-stage-num">{s['step']}</span></div>
              <span class="clc-stage-badge">{s['hub_badge']}</span>
            </div>
            <h3>{s['name']}</h3>
            <p class="clc-stage-card-desc">{s['hub_desc']}</p>
            <ul class="clc-stage-card-points">{points}</ul>
            <span class="clc-stage-card-cta">Explore stage →</span>
          </a>"""


def render_hub() -> str:
    cards = "\n".join(card_html(s) for s in STAGES)
    jumps = " ".join(f'<a href="#{s["slug"]}">{s["short"]}</a>' for s in STAGES)
    flow = "".join(
        f'<article class="clc-flow-step"><strong>{s["name"]}</strong><p>{s["hub_desc"][:70]}…</p></article>'
        for s in STAGES
    )
    # shorter flow desc
    flow = "".join(
        f'<article class="clc-flow-step"><strong>{s["name"]}</strong><p>Stage {s["step"]} — <a href="{s["slug"]}.html">Details</a></p></article>'
        for s in STAGES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Call Lifecycle — EMAAVY</title>
  <meta name="description" content="EMAAVY call lifecycle — ring, transcribe, analyze, act, and learn. Five automated stages from connect to continuous improvement." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Call Lifecycle — EMAAVY" />
  <meta property="og:description" content="Five-stage voice intelligence pipeline — connect, transcribe, score, act, and learn on every call." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/call-lifecycle-hub.css" />
</head>
<body data-base="../../" data-route="call-lifecycle">
  <div id="site-nav-root"></div>
  <main class="page-main clc-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <span class="page-kicker">End-to-end flow · Voice intelligence</span>
        <h1>The call journey — step by step</h1>
        <p class="telephony-hero-lead">From ring to learn — every stage is captured, scored, and turned into action automatically. Explore each step for full detail on what EMAAVY does and why it matters.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>5</b><span>Lifecycle stages</span></div>
          <div class="stat-box"><b>&lt;0.5s</b><span>Transcription</span></div>
          <div class="stat-box"><b>100%</b><span>Automated</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#pipeline-layer">How the pipeline works</a>
          <a href="#stages">Lifecycle stages</a>
          <a href="#flow">Full journey</a>
          {jumps}
        </div>
      </div>
    </section>

    <section id="pipeline-layer" class="clc-hub-workforce">
      <div class="container">
        <article class="clc-hub-workforce-card">
          <div class="clc-hub-workforce-meta">
            <span class="clc-hub-workforce-num">Call lifecycle</span>
            <span class="clc-hub-workforce-tag">EMAAVY · Voice pipeline</span>
            <h2>How the five-stage pipeline works</h2>
            <p class="clc-hub-workforce-lead">EMAAVY treats every call as a continuous intelligence loop — not a recording you analyze tomorrow. Audio enters at ring, becomes text in milliseconds, gets scored live, triggers your stack, and feeds the next program automatically.</p>
          </div>
          <div class="clc-hub-pill-grid">
            <div class="clc-hub-pill"><strong>Ring → Transcribe</strong><span>Zero-gap capture and streaming STT on the wire.</span></div>
            <div class="clc-hub-pill"><strong>Analyze live</strong><span>Sentiment, intent, and compliance per turn.</span></div>
            <div class="clc-hub-pill"><strong>Act instantly</strong><span>CRM, WhatsApp, and webhooks from real speech.</span></div>
            <div class="clc-hub-pill"><strong>Learn &amp; improve</strong><span>Scripts and routing refine every campaign.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="stages" class="clc-hub-roles page-section alt">
      <div class="container">
        <header class="clc-hub-roles-head">
          <h2>Lifecycle stages</h2>
          <p>Five steps — each with a dedicated page covering signals, EMAAVY orchestration, and business outcomes.</p>
        </header>
        <div class="clc-stage-grid clc-stage-grid--five">
{cards}
        </div>
      </div>
    </section>

    <section id="flow" class="clc-hub-flow">
      <div class="container">
        <header class="clc-hub-flow-head">
          <h2>End-to-end journey on one call</h2>
          <p>What happens from the first ring through continuous improvement.</p>
        </header>
        <div class="clc-flow-track">
{flow}
        </div>
      </div>
    </section>

    <section class="clc-hub-cta">
      <div class="container">
        <h2>See the full lifecycle on your calls</h2>
        <p>Book a walkthrough — live demo across all five stages on your telephony and CRM stack.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="../../index.html#journey" class="btn-outline">Back to overview</a>
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


def main():
    LC_DIR.mkdir(parents=True, exist_ok=True)
    (LC_DIR / "index.html").write_text(render_hub(), encoding="utf-8")
    for s in STAGES:
        (LC_DIR / f"{s['slug']}.html").write_text(render_stage(s), encoding="utf-8")
    print(f"OK: call-lifecycle hub + {len(STAGES)} stage pages")


if __name__ == "__main__":
    main()
