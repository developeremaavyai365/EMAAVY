#!/usr/bin/env python3
"""Generate Case Studies hub + per-client story pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CS_DIR = ROOT / "pages" / "case-studies"
HUB = ROOT / "pages" / "case-studies.html"

HEAD_COMMON = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{base}assets/nav.css" />
  <link rel="stylesheet" href="{base}assets/masthead-flex.css" />
  <link rel="stylesheet" href="{base}assets/site.css" />
  <link rel="stylesheet" href="{base}assets/emaavy-theme.css" />
"""

STUDIES = [
    {
        "slug": "mudita",
        "name": "Warehouse by Mudita",
        "short": "Mudita",
        "mark": "WA",
        "route": "case-study-mudita",
        "kicker": "Events · Outbound",
        "headline": "Exhibition Registration Campaign",
        "region": "Events · Luxury retail",
        "meta": "Warehouse by Mudita — 68% exhibition registration with EMAAVY bilingual outbound voice vs 12% email baseline across 5,000 prospects.",
        "lead": "Warehouse by Mudita needed to fill a luxury designer exhibition — not with cold email, but with warm, bilingual voice conversations that captured registrations in real time.",
        "stats": [("68%", "Registration rate"), ("5,000", "Contacts reached"), ("12%", "Email baseline")],
        "challenge": [
            "The marketing team had a list of 5,000 high-value prospects but email campaigns plateaued at a 12% registration rate. Manual calling was too slow for the exhibition timeline, and scripts in English alone missed a large Hindi-speaking audience.",
            "They needed measurable conversion before the event date — without hiring a temporary outbound floor or losing brand tone on every call.",
        ],
        "solution_lead": "EMAAVY deployed Priya, a campaign voice agent fluent in Hindi and English with natural code-switching. Every call captured intent, objections, and registration details live — then triggered WhatsApp confirmations automatically.",
        "solution_points": [
            ("Bilingual voice agent", "Hinglish fluency with Bulbul V3 and Sarvam STT for natural code-switching."),
            ("Live registration capture", "Structured fields written to CRM during the call — zero manual entry."),
            ("WhatsApp automation", "Confirmation and show-rate lift within 30 seconds of verbal yes."),
            ("Supervisor pacing", "Ops adjusted connect windows hourly from the EMAAVY dashboard."),
        ],
        "stack": ["Outbound Agent", "Sarvam STT", "Bulbul V3", "WhatsApp", "Webhooks"],
        "implementation": [
            ("Audience upload", "5,000 contacts segmented by city and language preference."),
            ("Agent configuration", "Priya outbound flow with exhibition details, pricing FAQ, and registration capture."),
            ("Live routing", "Sarvam STT for Hinglish, Bulbul V3 voice, and Qwen for cost-efficient dialogue."),
            ("Post-call automation", "WhatsApp ticket + calendar hold sent within 30 seconds of a yes."),
            ("Supervisor view", "Ops monitored conversion by hour and adjusted pacing in the dashboard."),
        ],
        "results_highlights": [
            ("5.6× email lift", "68% registration vs 12% email-only baseline."),
            ("3,400 attendees", "Confirmed with structured CRM fields from voice."),
            ("Sub-4 min AHT", "Average handle time with zero manual data entry."),
            ("+11% show-rate", "WhatsApp follow-up after verbal commitment."),
        ],
        "results_bullets": [
            "68% registration rate — 5.6× improvement over email alone",
            "3,400 confirmed attendees captured with structured CRM fields",
            "Average handle time under 4 minutes with zero manual data entry",
            "WhatsApp follow-up lifted show-rate by an additional 11%",
        ],
        "hub_desc": "5,000 bilingual outbound calls for a luxury designer exhibition — 68% registration vs 12% email.",
        "hub_points": ["68% registration rate", "Bilingual Hinglish agent", "WhatsApp confirmations"],
        "hub_badge": "Events · Outbound",
    },
    {
        "slug": "nextcall",
        "name": "NextCall BPO",
        "short": "NextCall",
        "mark": "NE",
        "route": "case-study-nextcall",
        "kicker": "BPO · Quality Assurance",
        "headline": "QA Automation at Scale",
        "region": "BPO · Quality assurance",
        "meta": "NextCall BPO — 100% call coverage and 61% faster QA with EMAAVY real-time transcription, sentiment, and compliance scoring.",
        "lead": "NextCall BPO replaced sample-based manual auditing with EMAAVY's real-time intelligence — every call scored for sentiment, compliance, and intent the moment it happens.",
        "stats": [("61%", "Faster QA"), ("100%", "Call coverage"), ("5%", "Prior manual sample")],
        "challenge": [
            "Quality teams could only audit about 5% of calls manually. Coaching was delayed, compliance gaps were discovered days later, and supervisors had no live signal when calls went off-script.",
            "Scaling headcount to review every conversation was economically impossible across their regulated client programs.",
        ],
        "solution_lead": "EMAAVY ingested the full call stream, transcribed in real time, and scored every turn for sentiment, compliance keywords, and buyer intent. Supervisors received coaching alerts during active calls instead of after batch reviews.",
        "solution_points": [
            ("100% call coverage", "Every conversation transcribed and scored — not a 5% sample."),
            ("Live supervisor feed", "Sentiment color coding and compliance flags during active calls."),
            ("Compliance lexicon", "Script deviations flagged within the call, not days later."),
            ("Webhook QA sync", "Scores and summaries pushed to internal QA tools automatically."),
        ],
        "stack": ["Deepgram STT", "Claude Sonnet", "Webhooks", "Exotel", "Call Intelligence"],
        "implementation": [
            ("Telephony connect", "Exotel numbers routed through EMAAVY with zero agent workflow change."),
            ("Scoring models", "Compliance lexicon + intent tiers tuned to NextCall's regulated scripts."),
            ("Supervisor console", "Live transcript feed with sentiment color coding per seat."),
            ("QA dashboards", "Per-agent compliance score, objection tags, and auto-generated summaries."),
            ("CRM sync", "Disposition and score pushed to internal QA tools via webhooks."),
        ],
        "results_highlights": [
            ("100% coverage", "Full call stream vs 5% manual audit sampling."),
            ("61% faster QA", "Reduction in time spent on review cycles."),
            ("In-call compliance", "Violations flagged while the conversation is live."),
            ("Real-time coaching", "Suggestions delivered to team leads during calls."),
        ],
        "results_bullets": [
            "100% call coverage vs 5% manual audit sampling",
            "61% reduction in time spent on QA review cycles",
            "Compliance violations flagged within the call, not days later",
            "Coaching suggestions delivered to team leads in real time",
        ],
        "hub_desc": "100% call coverage with real-time sentiment, compliance, and intent scoring.",
        "hub_points": ["61% faster QA cycles", "Live supervisor alerts", "Full call stream scoring"],
        "hub_badge": "BPO · QA",
    },
    {
        "slug": "fleetiq",
        "name": "FleetIQ Logistics",
        "short": "FleetIQ",
        "mark": "FL",
        "route": "case-study-fleetiq",
        "kicker": "Logistics · Customer Experience",
        "headline": "Driver Follow-Up Automation",
        "region": "Logistics · Post-delivery CX",
        "meta": "FleetIQ Logistics — 28% CSAT lift and 50K monthly follow-up calls with multilingual EMAAVY support agents and 60-second escalation.",
        "lead": "FleetIQ automated post-delivery follow-ups across eight Indian languages — unhappy customers reach a human specialist in under 60 seconds, while satisfied deliveries scale without adding headcount.",
        "stats": [("28%", "CSAT lift"), ("50K", "Calls / month"), ("60s", "Escalation SLA")],
        "challenge": [
            "Fifty thousand deliveries per month meant fifty thousand potential support calls. A small team could not staff every language, and delayed follow-ups hurt CSAT scores in regional markets.",
            "Negative experiences needed immediate human intervention — but manual outbound teams could not keep pace with delivery volume.",
        ],
        "solution_lead": "EMAAVY support-style agents placed outbound follow-up calls in the customer's preferred language, detected negative sentiment live, and warm-transferred frustrated callers to human agents with full transcript context.",
        "solution_points": [
            ("Eight-language routing", "Regional language auto-selected from delivery metadata."),
            ("Sentiment gates", "Negative shift triggers supervisor alert and human bridge in under 60s."),
            ("Script library", "Delivery confirmation, damage report, and reschedule branches."),
            ("Helpdesk ticketing", "Issues logged with full transcript attachment."),
        ],
        "stack": ["Support Agent", "Sarvam STT", "Sentiment scoring", "Webhooks", "Human handoff"],
        "implementation": [
            ("Language routing", "Eight regional languages auto-selected from delivery metadata."),
            ("Sentiment gates", "Negative shift triggers supervisor alert and human bridge in &lt;60s."),
            ("Script library", "Delivery confirmation, damage report, and reschedule branches."),
            ("Ticketing", "Issues logged to FleetIQ helpdesk with transcript attachment."),
            ("Monthly scale", "Campaign pacing handles 50K+ contacts with retry and timezone rules."),
        ],
        "results_highlights": [
            ("50K calls / month", "Automated follow-ups without proportional hiring."),
            ("28% CSAT lift", "Measured over 90 days post-launch."),
            ("60s escalation", "Negative-sentiment callers reach humans with context."),
            ("Full handoff brief", "Issue, language, and transcript summary for specialists."),
        ],
        "results_bullets": [
            "50,000 automated follow-up calls per month without proportional hiring",
            "28% CSAT improvement measured over 90 days post-launch",
            "60-second escalation SLA for negative-sentiment callers",
            "Human agents receive full context — issue, language, and transcript summary",
        ],
        "hub_desc": "50,000 multilingual post-delivery calls per month with smart escalation.",
        "hub_points": ["28% CSAT lift", "8 languages", "60s human escalation"],
        "hub_badge": "Logistics · CX",
    },
]


def study_nav(current: str) -> str:
    links = []
    for s in STUDIES:
        cls = ' class="is-current"' if s["slug"] == current else ""
        links.append(f'<a href="{s["slug"]}.html"{cls}>{s["short"]}</a>')
    links.append('<a href="../case-studies.html">All case studies</a>')
    return "\n          ".join(links)


def render_study(s: dict) -> str:
    stats = "".join(
        f'<div class="cs-study-stat"><b>{a}</b><span>{b}</span></div>' for a, b in s["stats"]
    )
    challenge = "".join(f"<p>{p}</p>" for p in s["challenge"])
    benefits = "".join(
        f'<li><div><strong>{t}</strong><span>{d}</span></div></li>'
        for t, d in s["solution_points"]
    )
    stack = "".join(f'<span class="cs-stack-pill">{x}</span>' for x in s["stack"])
    impl = "".join(
        f'<li><div><strong>{t}</strong><p>{d}</p></div></li>'
        for t, d in s["implementation"]
    )
    highlights = "".join(
        f'<article class="cs-feature-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in s["results_highlights"]
    )
    bullets = "".join(f"<li>{b}</li>" for b in s["results_bullets"])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{s['name']} — Case Study — EMAAVY</title>
  <meta name="description" content="{s['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{s['name']} — Case Study — EMAAVY" />
  <meta property="og:description" content="{s['meta']}" />
  <meta property="og:type" content="article" />
{HEAD_COMMON.format(base="../../")}
  <link rel="stylesheet" href="../../assets/case-study-detail.css" />
</head>
<body data-base="../../" data-route="{s['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main cs-study-page">
    <section class="cs-study-hero">
      <div class="container cs-study-hero-grid">
        <div class="cs-study-hero-copy">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="../../index.html">Home</a>
            <span aria-hidden="true"> / </span>
            <a href="../../index.html#case-studies">Case Studies</a>
            <span aria-hidden="true"> / </span>
            <a href="../case-studies.html">All stories</a>
            <span aria-hidden="true"> / </span>
            <span>{s['short']}</span>
          </nav>
          <span class="cs-study-kicker">Case Study · {s['kicker']}</span>
          <h1>{s['headline']}</h1>
          <p class="cs-study-lead">{s['lead']}</p>
          <div class="cs-study-stats">{stats}</div>
          <div class="cs-study-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Discuss a similar rollout</a>
            <a href="../case-studies.html" class="btn-outline">All case studies</a>
          </div>
        </div>
        <aside class="cs-study-hero-card" aria-label="{s['name']}">
          <div class="cs-study-hero-logo"><span class="brand-mark">{s['mark']}</span></div>
          <span class="cs-study-hero-region">{s['region']}</span>
          <p><strong>{s['name']}</strong> — client success on EMAAVY voice, intelligence, and integrations.</p>
        </aside>
      </div>
    </section>

    <section class="cs-study-section" id="challenge">
      <div class="container">
        <header class="cs-study-section-head">
          <h2>The challenge</h2>
          <p>What {s['name']} needed to solve before EMAAVY.</p>
        </header>
        <div class="cs-study-prose">{challenge}</div>
      </div>
    </section>

    <section class="cs-study-section alt" id="solution">
      <div class="container cs-study-split">
        <header class="cs-study-section-head">
          <h2>How EMAAVY delivered</h2>
          <p>{s['solution_lead']}</p>
          <div class="cs-stack-pills">{stack}</div>
        </header>
        <ul class="cs-study-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="cs-study-section" id="implementation">
      <div class="container">
        <header class="cs-study-section-head">
          <h2>Implementation on EMAAVY</h2>
          <p>Step-by-step rollout — from data ingest to live operations.</p>
        </header>
        <ol class="cs-impl-steps">{impl}</ol>
      </div>
    </section>

    <section class="cs-study-section alt" id="results">
      <div class="container">
        <header class="cs-study-section-head">
          <h2>Results &amp; impact</h2>
          <p>Outcomes measured after go-live — not projections.</p>
        </header>
        <div class="cs-feature-grid">{highlights}</div>
        <ul class="cs-results-list">{bullets}</ul>
      </div>
    </section>

    <section class="cs-study-section">
      <div class="container">
        <header class="cs-study-section-head">
          <h2>More client stories</h2>
          <p>Explore other industries and programs running on EMAAVY.</p>
        </header>
        <nav class="cs-study-nav-strip" aria-label="Case studies">
          {study_nav(s['slug'])}
        </nav>
      </div>
    </section>

    <section class="cs-study-cta">
      <div class="container">
        <h2>Ready for results like {s['short']}?</h2>
        <p>Book a walkthrough — review a live call, map your stack, and plan your first program.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="../case-studies.html" class="btn-outline">All case studies</a>
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
    return f"""          <a href="case-studies/{s['slug']}.html" id="{s['slug']}" class="cs-study-card">
            <div class="cs-study-card-top">
              <div class="cs-study-card-logo"><span class="brand-mark">{s['mark']}</span></div>
              <span class="cs-study-badge">{s['hub_badge']}</span>
            </div>
            <h3>{s['name']}</h3>
            <p class="cs-study-card-desc">{s['hub_desc']}</p>
            <ul class="cs-study-card-points">{points}</ul>
            <span class="cs-study-card-cta">Read case study →</span>
          </a>"""


def render_hub() -> str:
    cards = "\n".join(card_html(s) for s in STUDIES)
    jumps = " ".join(f'<a href="#{s["slug"]}">{s["short"]}</a>' for s in STUDIES)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Case Studies — EMAAVY</title>
  <meta name="description" content="Real EMAAVY client results — exhibition campaigns, BPO QA automation, and logistics follow-ups with measurable ROI." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Case Studies — EMAAVY" />
  <meta property="og:description" content="Client success stories with challenge, EMAAVY rollout, and measured outcomes." />
  <meta property="og:type" content="website" />
{HEAD_COMMON.format(base="../")}
  <link rel="stylesheet" href="../assets/case-studies-hub.css" />
</head>
<body data-base="../" data-route="case-studies">
  <div id="site-nav-root"></div>
  <main class="page-main cs-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../index.html">Home</a>
          <span aria-hidden="true"> / </span>
          <span>Case Studies</span>
        </nav>
        <span class="page-kicker">Client Success · Proof</span>
        <h1>Real results from client stories</h1>
        <p class="telephony-hero-lead">Exhibition campaigns, BPO quality programs, and logistics at scale — each story documents the challenge, EMAAVY implementation, and outcomes measured after go-live.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>68%</b><span>Peak conversion</span></div>
          <div class="stat-box"><b>50K+</b><span>Calls / month</span></div>
          <div class="stat-box"><b>61%</b><span>Faster QA</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#proof-layer">Why EMAAVY wins</a>
          <a href="#stories">Client stories</a>
          <a href="#rollout">Rollout path</a>
          {jumps}
        </div>
      </div>
    </section>

    <section id="proof-layer" class="cs-hub-workforce">
      <div class="container">
        <article class="cs-hub-workforce-card">
          <div class="cs-hub-workforce-meta">
            <span class="cs-hub-workforce-num">Client proof</span>
            <span class="cs-hub-workforce-tag">EMAAVY · Case Studies</span>
            <h2>Why enterprises trust EMAAVY outcomes</h2>
            <p class="cs-hub-workforce-lead">Every story follows the same arc — a business constraint, an EMAAVY voice and intelligence rollout, and metrics captured in production. No vanity slides; only measured lift against prior baselines.</p>
          </div>
          <div class="cs-hub-pill-grid">
            <div class="cs-hub-pill"><strong>Proven conversion</strong><span>Voice beats email and manual outreach on high-intent lists.</span></div>
            <div class="cs-hub-pill"><strong>Full call coverage</strong><span>Score every conversation — not 5% spot checks.</span></div>
            <div class="cs-hub-pill"><strong>Multilingual scale</strong><span>Regional programs without proportional hiring.</span></div>
            <div class="cs-hub-pill"><strong>Fast escalation</strong><span>Humans join with transcript context when risk spikes.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="stories" class="cs-hub-roles page-section alt">
      <div class="container">
        <header class="cs-hub-roles-head">
          <h2>Client stories</h2>
          <p>Three published case studies — each with a dedicated page covering challenge, solution, implementation, and results.</p>
        </header>
        <div class="cs-study-grid cs-study-grid--trio">
{cards}
        </div>
      </div>
    </section>

    <section id="rollout" class="cs-hub-flow">
      <div class="container">
        <header class="cs-hub-flow-head">
          <h2>From pilot to production proof</h2>
          <p>How teams typically move from first story to scaled programs on EMAAVY.</p>
        </header>
        <div class="cs-flow-track">
          <article class="cs-flow-step"><strong>Align on KPI</strong><p>Pick conversion, CSAT, or QA coverage targets.</p></article>
          <article class="cs-flow-step"><strong>Design the program</strong><p>Agents, languages, and integration stack.</p></article>
          <article class="cs-flow-step"><strong>Pilot cohort</strong><p>Single campaign or queue before full traffic.</p></article>
          <article class="cs-flow-step"><strong>Measure live</strong><p>Dashboards vs email, manual, or sample QA baselines.</p></article>
          <article class="cs-flow-step"><strong>Scale</strong><p>Expand lists, languages, and supervisor playbooks.</p></article>
        </div>
      </div>
    </section>

    <section class="cs-hub-cta">
      <div class="container">
        <h2>Build your next success story on EMAAVY</h2>
        <p>See how voice programs perform in your industry — tailored demo with live calls and ROI framing.</p>
        <div class="cta-row">
          <a href="../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="../index.html#case-studies" class="btn-outline">Back to overview</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../assets/routes.js"></script>
  <script src="../assets/components.js"></script>
  <script src="../assets/nav.js"></script>
</body>
</html>
"""


def main():
    CS_DIR.mkdir(parents=True, exist_ok=True)
    HUB.write_text(render_hub(), encoding="utf-8")
    for s in STUDIES:
        (CS_DIR / f"{s['slug']}.html").write_text(render_study(s), encoding="utf-8")
    print(f"OK: case-studies hub + {len(STUDIES)} detail pages")


if __name__ == "__main__":
    main()
