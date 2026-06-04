"""
Replace home #bento (Intelligence matrix) with unified EMAAVY promo.
Create pages/intelligence-matrix/*.html with descriptive module pages.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
IMX_DIR = ROOT / "pages" / "intelligence-matrix"
HUB = IMX_DIR / "index.html"
ROUTES = ROOT / "assets" / "routes.js"

IMX_CSS = """
/* ═══ INTELLIGENCE MATRIX — unified landing promo ═══ */
.imx-promo-shell {
  padding: clamp(2rem, 4vw, 2.75rem) clamp(1.25rem, 4vw, 2.25rem) !important;
}
.imx-promo {
  display: grid !important;
  grid-template-columns: 1.05fr 0.95fr !important;
  gap: clamp(1.5rem, 4vw, 2.25rem) !important;
  align-items: start !important;
  text-align: left !important;
  margin-bottom: 1.75rem !important;
}
.imx-promo h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.5rem, 3.2vw, 2.1rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.12 !important;
  color: #0f172a !important;
  margin: 0 0 1rem !important;
  max-width: 22ch !important;
}
.imx-promo-lead {
  font-size: clamp(0.9rem, 1.45vw, 1.02rem) !important;
  line-height: 1.7 !important;
  color: #475569 !important;
  margin: 0 0 1.2rem !important;
  max-width: 54ch !important;
}
.imx-promo-highlights {
  list-style: none !important;
  margin: 0 0 1.6rem !important;
  padding: 0 !important;
  display: grid !important;
  gap: 0.5rem !important;
}
.imx-promo-highlights li {
  font-size: 0.86rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  padding: 0.32rem 0 0.32rem 0.85rem !important;
  border-left: 3px solid #4A658B !important;
}
.imx-promo-highlights strong { color: #0f172a !important; font-weight: 600 !important; }
.imx-promo-actions {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 0.7rem !important;
}
.btn-imx-explore {
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
.btn-imx-explore:hover { background: #18345D !important; transform: translateY(-1px) !important; }
.btn-imx-secondary {
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
.btn-imx-secondary:hover { border-color: #4A658B !important; background: #f8fafc !important; }
.imx-promo-panel {
  padding: 1.2rem 1rem !important;
  border-radius: 10px !important;
  background: linear-gradient(145deg, #f8fafc 0%, #f0f4f8 100%) !important;
  border: 1px solid #e2e8f0 !important;
  max-height: 28rem !important;
  overflow-y: auto !important;
}
.imx-promo-panel-head {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.75rem !important;
  position: sticky !important;
  top: 0 !important;
  background: linear-gradient(145deg, #f8fafc 0%, #f0f4f8 100%) !important;
  padding-bottom: 0.35rem !important;
  z-index: 1 !important;
}
.imx-module-cards { display: grid !important; gap: 0.45rem !important; }
.imx-module-card {
  display: grid !important;
  grid-template-columns: 1fr auto !important;
  grid-template-rows: auto auto auto !important;
  gap: 0.1rem 0.5rem !important;
  padding: 0.65rem 0.75rem !important;
  border-radius: 8px !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  text-decoration: none !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.imx-module-card:hover {
  border-color: #4A658B !important;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06) !important;
}
.imx-module-card:hover .imx-module-explore { color: #18345D !important; }
.imx-module-label {
  grid-column: 1 !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.imx-module-card strong {
  grid-column: 1 !important;
  font-size: 0.88rem !important;
  color: #0f172a !important;
  font-weight: 600 !important;
}
.imx-module-snippet {
  grid-column: 1 / -1 !important;
  font-size: 0.72rem !important;
  line-height: 1.45 !important;
  color: #64748b !important;
  margin-top: 0.15rem !important;
}
.imx-module-meta {
  grid-column: 2 !important;
  grid-row: 1 / span 2 !important;
  align-self: center !important;
  font-size: 0.62rem !important;
  color: #4A658B !important;
  text-align: right !important;
  max-width: 11ch !important;
  line-height: 1.35 !important;
  font-weight: 600 !important;
}
.imx-module-explore {
  grid-column: 1 / -1 !important;
  font-size: 0.7rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  margin-top: 0.35rem !important;
}
.imx-promo-stats {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.65rem !important;
  padding-top: 0.25rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
.imx-promo-stats .int-stat {
  text-align: center !important;
  padding: 0.85rem 0.5rem !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
}
.imx-promo-stats .int-stat b {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.25rem !important;
  color: #4A658B !important;
  margin-bottom: 0.2rem !important;
}
@media (max-width: 900px) {
  .imx-promo { grid-template-columns: 1fr !important; }
  .imx-promo h3 { max-width: none !important; }
  .imx-promo-stats { grid-template-columns: repeat(2, 1fr) !important; }
  .imx-promo-panel { max-height: none !important; }
  .imx-module-meta { display: none !important; }
}
"""

MODULES = {
    "volume": {
        "route": "matrix-volume",
        "title": "Calls Processed",
        "kicker": "Volume · Analytics",
        "meta": "10M+ decoded",
        "snippet": "Total call volume with breakdown by language, agent, outcome, and time.",
        "hero_lead": "See every call your organization runs — live counters, historical trends, and dimensional breakdowns across campaigns, languages, and outcomes in one command center view.",
        "stats": [("10M+", "Calls processed"), ("Live", "Counter"), ("Multi-dim", "Breakdown")],
        "overview": "The Calls Processed module is the volume heartbeat of EMAAVY's intelligence matrix. Operations leaders see real-time throughput, compare campaigns side by side, and spot spikes or drop-offs before they impact revenue.",
        "what_you_see": [
            "Real-time volume dashboard updating as calls connect and complete",
            "Language distribution chart across Hindi, English, Hinglish, and regional mixes",
            "Peak hour heatmaps by day-of-week and timezone",
            "Campaign comparison view — conversion vs volume in one glance",
        ],
        "how_it_works": [
            ("Ingest", "Every connected call increments the live counter with metadata tags."),
            ("Classify", "EMAAVY tags language, agent type, campaign ID, and disposition."),
            ("Aggregate", "Rollups run per minute for dashboards and per day for exports."),
            ("Alert", "Optional thresholds notify ops when volume deviates from forecast."),
            ("Export", "CSV, JSON, or API pull for BI tools and executive reporting."),
        ],
        "use_cases": [
            "Capacity planning for outbound campaign launches",
            "Proving ROI on AI agent vs human seat mix",
            "Identifying under-performing language segments",
        ],
    },
    "realtime": {
        "route": "matrix-realtime",
        "title": "Real-Time Ears",
        "kicker": "Live stream · Analytics",
        "meta": "Live captions",
        "snippet": "Words as they're spoken — captions, sentiment, and supervisor intervention.",
        "hero_lead": "Supervisors don't wait for recordings. Real-Time Ears streams live transcripts, sentiment color coding, and one-click join — so coaching happens while the conversation is still winnable.",
        "stats": [("Live", "Stream"), ("Instant", "Intervene"), ("<0.5s", "Caption lag")],
        "overview": "Real-Time Ears is the supervisor console for active calls. Every seat appears on a map with transcript preview, sentiment indicator, and intervention controls — built for BPO floors and inside sales pods alike.",
        "what_you_see": [
            "Active call map view with campaign and agent attribution",
            "Live transcript preview scrolling word-by-word",
            "Sentiment color coding shifting green, amber, or red per turn",
            "One-click supervisor join or whisper-coach without dropping the AI agent",
        ],
        "how_it_works": [
            ("Stream", "STT pipelines push partial transcripts over WebSocket."),
            ("Score", "Sentiment model updates on each conversational turn."),
            ("Display", "Supervisor UI renders captions with speaker labels."),
            ("Intervene", "Authorized users bridge into the call with full context."),
            ("Archive", "Completed streams merge into the searchable call record."),
        ],
        "use_cases": [
            "Live QA on high-value sales calls",
            "Escalation before a frustrated customer churns",
            "Training new human agents with real examples",
        ],
    },
    "intent": {
        "route": "matrix-intent",
        "title": "Intent Mapping",
        "kicker": "Intent engine · Funnel",
        "meta": "Live funnel",
        "snippet": "Buyer intent visualized — buying, exploring, objecting, or slipping away.",
        "hero_lead": "Intent Mapping turns conversation into a live funnel. Know when prospects are buying, stalling, or slipping away — updated per turn across every campaign and agent on EMAAVY.",
        "stats": [("Per-turn", "Scoring"), ("Live", "Funnel"), ("Export", "Reports")],
        "overview": "Stop guessing from dispositions typed after the fact. Intent Mapping classifies every turn into buyer signals — high intent, exploring, objection, not interested — and visualizes distribution in real time.",
        "what_you_see": [
            "Intent funnel visualization with live stage counts",
            "Trend-over-time chart for campaign A/B comparisons",
            "Filters by agent, language, product line, or region",
            "Exportable snapshots for weekly business reviews",
        ],
        "how_it_works": [
            ("Transcribe", "Live text feeds the intent classifier each turn."),
            ("Classify", "LLM + rules score buy / hold / reject / objection types."),
            ("Aggregate", "Funnel buckets update without batch jobs."),
            ("Trigger", "Threshold crossings can fire webhooks or CRM updates."),
            ("Learn", "Misclassifications feed back into model tuning."),
        ],
        "use_cases": [
            "Prioritizing callbacks for high-intent leads",
            "Spotting script fatigue when objection rates spike",
            "Aligning marketing messaging with real buyer language",
        ],
    },
    "ops": {
        "route": "matrix-ops",
        "title": "Operator Performance",
        "kicker": "Operator view · Rankings",
        "meta": "Live leaderboard",
        "snippet": "Human and AI operator leaderboard — conversion, handle time, coaching score.",
        "hero_lead": "Operator Performance ranks every seat — human or AI — on conversion rate, average handle time, sentiment score, and coaching compliance. Leaders see who to coach, clone, or scale.",
        "stats": [("Leaderboard", "Live"), ("AI + Human", "Compared"), ("Coaching", "Score")],
        "overview": "The leaderboard is not vanity metrics. It ties talk patterns to outcomes so workforce planners know which agents to replicate, which scripts to fix, and where AI is outperforming manual dialing.",
        "what_you_see": [
            "Per-agent conversion rate with trend arrows",
            "Average handle time vs team median",
            "Coaching compliance score from script adherence",
            "Side-by-side AI vs human performance bands",
        ],
        "how_it_works": [
            ("Attribute", "Calls map to operator or AI agent IDs."),
            ("Score", "Outcomes, sentiment, and script tags roll into KPIs."),
            ("Rank", "Leaderboard refreshes on a configurable interval."),
            ("Coach", "AI-generated notes highlight specific improvement moments."),
            ("Export", "HR and ops teams pull period summaries for reviews."),
        ],
        "use_cases": [
            "Weekly team standups with objective rankings",
            "Deciding which AI voice to clone for new campaigns",
            "Compliance reviews tied to script adherence scores",
        ],
    },
    "latency": {
        "route": "matrix-latency",
        "title": "Sub-500ms Latency",
        "kicker": "System health · P99",
        "meta": "SLA alerts",
        "snippet": "End-to-end latency — STT, LLM, TTS, and triggers with SLA alerting.",
        "hero_lead": "Voice AI only works if the stack keeps up. Sub-500ms Latency monitors transcription, reasoning, synthesis, and trigger execution — with P50/P95/P99 charts and SLA breach alerts before customers feel the lag.",
        "stats": [("<500ms", "P99 STT"), ("P99", "Charts"), ("SLA", "Alerts")],
        "overview": "Latency is a product feature, not an afterthought. Engineering and ops share one pane for component-level timing, historical trends, and automated alerts when inference or media streams exceed thresholds.",
        "what_you_see": [
            "P50 / P95 / P99 latency charts per stack component",
            "Per-component breakdown: STT, LLM, TTS, webhook execution",
            "SLA breach alerting to Slack, email, or PagerDuty",
            "Historical trend analysis for capacity upgrades",
        ],
        "how_it_works": [
            ("Timestamp", "Each pipeline stage records millisecond markers."),
            ("Aggregate", "Histograms compute percentiles per region and provider."),
            ("Compare", "Routes across STT/LLM providers highlight slow paths."),
            ("Alert", "Policies fire when P99 crosses configured limits."),
            ("Report", "Weekly infra summaries for platform and customer success teams."),
        ],
        "use_cases": [
            "Choosing STT provider by language and latency SLA",
            "Proving enterprise SLA compliance to procurement",
            "Debugging sporadic lag during peak campaign hours",
        ],
    },
    "security": {
        "route": "matrix-security",
        "title": "Enterprise Secure",
        "kicker": "Compliance · SOC 2",
        "meta": "PII detection",
        "snippet": "Encryption, PII detection, flagged calls, and audit log export.",
        "hero_lead": "Enterprise Secure is the compliance layer of the intelligence matrix — SOC-aligned controls, PII detection, flagged call review, and exportable audit trails so regulated teams trust every conversation stored on EMAAVY.",
        "stats": [("SOC 2", "Aligned"), ("PII", "Detection"), ("Audit", "Export")],
        "overview": "Security and compliance cannot be bolted on after launch. This module gives legal, security, and ops teams visibility into encryption status, redaction events, retention policies, and investigation workflows.",
        "what_you_see": [
            "Compliance keyword flagging on live and recorded calls",
            "PII auto-redaction events with review queue",
            "Full audit log export for regulators and internal InfoSec",
            "Retention policy status per workspace and region",
        ],
        "how_it_works": [
            ("Encrypt", "Data in transit and at rest with enterprise key management."),
            ("Detect", "PII and compliance lexicons scan transcripts in real time."),
            ("Flag", "Risky calls enter a supervisor review queue."),
            ("Retain", "Policies enforce deletion schedules by data class."),
            ("Export", "Immutable audit logs for SOC and internal investigations."),
        ],
        "use_cases": [
            "BFSI and healthcare deployments with strict retention rules",
            "Internal investigations on flagged conversations",
            "Customer trust reviews during enterprise security questionnaires",
        ],
    },
}


def card_html(slug, m, num):
    return f"""          <a href="pages/intelligence-matrix/{slug}.html" class="imx-module-card">
            <span class="imx-module-label">{num:02d} · {m['kicker'].split('·')[0].strip()}</span>
            <strong>{m['title']}</strong>
            <span class="imx-module-meta">{m['meta']}</span>
            <span class="imx-module-snippet">{m['snippet']}</span>
            <span class="imx-module-explore">Explore module →</span>
          </a>"""


IMX_SECTION = """<!-- INTELLIGENCE MATRIX HUB --> <section id="bento" class="cap-section">
 <div class="features-head reveal">
  <span class="section-kicker">Intelligence matrix · Analytics engine</span>
  <h2>Your call intelligence command center</h2>
  <p class="int-hub-desc">Six analytics modules — volume, live feed, intent, operators, latency, and security — each with a dedicated page and full EMAAVY specs.</p>
 </div>
 <div class="int-showcase reveal imx-promo-wrap" id="intelligence-matrix-emaavy">
  <div class="int-shell imx-promo-shell">
    <div class="imx-promo reveal">
      <div class="imx-promo-copy">
        <span class="section-kicker">Intelligence matrix · EMAAVY</span>
        <h3>Every metric decoded in real time</h3>
        <p class="imx-promo-lead">EMAAVY's intelligence matrix is the unified dashboard layer — from live transcripts and intent funnels to operator leaderboards, latency SLAs, and compliance controls. Open any module for a deep dive on its own page.</p>
        <ul class="imx-promo-highlights" aria-label="Intelligence matrix highlights">
          <li><strong>Six modules</strong> — volume, real-time feed, intent, ops, latency, and security</li>
          <li><strong>Live + historical</strong> — real-time operations with exportable trends</li>
          <li><strong>Human + AI</strong> — compare operator and voice agent performance fairly</li>
          <li><strong>Enterprise ready</strong> — SOC-aligned security and audit built in</li>
        </ul>
        <div class="imx-promo-actions">
          <a href="pages/intelligence-matrix/index.html" class="btn-imx-explore">Explore intelligence matrix</a>
          <a href="book-demo.html" class="btn-imx-secondary">Book a demo</a>
        </div>
      </div>
      <div class="imx-promo-panel">
        <div class="imx-promo-panel-head">Analytics modules</div>
        <div class="imx-module-cards">
{cards}
        </div>
      </div>
    </div>
    <div class="imx-promo-stats">
      <div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>10M+</b><span>Calls processed</span></div>
      <div class="int-stat"><b>99%</b><span>Decode accuracy</span></div>
      <div class="int-stat"><b>&lt;0.5s</b><span>Live latency</span></div>
      <div class="int-stat"><b>6</b><span>Matrix modules</span></div>
    </div>
  </div>
 </div>
</section>"""


def module_page(slug, m):
    flow = "".join(
        f'<li><span class="telephony-flow-num">{i:02d}</span><strong>{t}</strong><p>{d}</p></li>'
        for i, (t, d) in enumerate(m["how_it_works"], 1)
    )
    sees = "".join(f"<li>{x}</li>" for x in m["what_you_see"])
    uses = "".join(f"<li>{x}</li>" for x in m["use_cases"])
    stats = "".join(f'<div class="stat-box"><b>{b}</b><span>{l}</span></div>' for b, l in m["stats"])
    pills = "".join(
        f'<a href="{k}.html" class="int-layer-pill">{MODULES[k]["title"]}</a>' for k in MODULES
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{m['title']} — Intelligence Matrix — EMAAVY</title>
  <meta name="description" content="{m['hero_lead'][:155]}…" />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="{m['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main int-category-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../emaavy_white_blue%20(2).html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../emaavy_white_blue%20(2).html#bento">Intelligence matrix</a>
          <span aria-hidden="true"> / </span>
          <span>{m['title']}</span>
        </nav>
        <span class="page-kicker">{m['kicker']}</span>
        <h1>{m['title']}</h1>
        <p class="telephony-hero-lead">{m['hero_lead']}</p>
        <div class="stat-row telephony-hero-stats">{stats}</div>
        <div class="capabilities-jump telephony-jump">
          <a href="#overview">Overview</a>
          <a href="#dashboard">What you see</a>
          <a href="#how">How it works</a>
          <a href="#use-cases">Use cases</a>
        </div>
      </div>
    </section>

    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">{pills}</div>
      </div>
    </section>

    <section id="overview" class="page-section alt">
      <div class="container">
        <article class="capability-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">—</span>
              <span class="capability-tag">EMAAVY · {m['title']}</span>
            </div>
            <div class="capability-content">
              <h2>Overview</h2>
              <p class="capability-lead">{m['overview']}</p>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="dashboard" class="page-section">
      <div class="container">
        <h2 class="section-title">What you see in the dashboard</h2>
        <p class="section-desc">Key views and signals available in this module.</p>
        <ul class="feature-list">{sees}</ul>
      </div>
    </section>

    <section id="how" class="page-section alt">
      <div class="container">
        <h2 class="section-title">How it works on EMAAVY</h2>
        <div class="telephony-flow-panel">
          <ol class="telephony-flow-steps">{flow}</ol>
        </div>
      </div>
    </section>

    <section id="use-cases" class="page-section">
      <div class="container">
        <h2 class="section-title">Typical use cases</h2>
        <ul class="feature-list">{uses}</ul>
        <div class="cta-row" style="margin-top:1.5rem">
          <a href="../../book-demo.html" class="btn-primary">See {m['title']} live →</a>
          <a href="index.html" class="btn-outline">All matrix modules</a>
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


def hub_html():
    cards = []
    for slug, m in MODULES.items():
        cards.append(f"""          <a href="{slug}.html" class="glow-card">
            <div class="card-icon"><span class="brand-mark">{m['title'][:2].upper()}</span></div>
            <h3>{m['title']}</h3>
            <p>{m['snippet']}</p>
            <span class="card-tag">{m['meta']}</span>
            <span class="imx-module-explore" style="display:block;margin-top:0.5rem">Explore module →</span>
          </a>""")
    grid = "\n".join(cards)
    pills = "".join(f'<a href="{k}.html" class="int-layer-pill">{MODULES[k]["title"]}</a>' for k in MODULES)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Intelligence Matrix — EMAAVY</title>
  <meta name="description" content="EMAAVY call intelligence command center — volume, live feed, intent, operators, latency, and enterprise security modules." />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="intelligence-matrix">
  <div id="site-nav-root"></div>
  <main class="page-main int-category-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../emaavy_white_blue%20(2).html">Home</a>
          <span aria-hidden="true"> / </span>
          <span>Intelligence matrix</span>
        </nav>
        <span class="page-kicker">Analytics engine</span>
        <h1>Your call intelligence command center</h1>
        <p class="telephony-hero-lead">Every metric, every insight — decoded in real time. From live transcripts to intent scoring, operator leaderboards, and compliance flags — explore each module on its own page.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>10M+</b><span>Calls processed</span></div>
          <div class="stat-box"><b>99%</b><span>Decode accuracy</span></div>
          <div class="stat-box"><b>&lt;0.5s</b><span>Live latency</span></div>
        </div>
      </div>
    </section>
    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">{pills}</div>
        <div class="card-grid cols-2" style="margin-top:1.5rem">
{grid}
        </div>
        <div class="cta-row" style="margin-top:2rem">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
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


def patch_routes():
    text = ROUTES.read_text(encoding="utf-8")
    if "intelligenceMatrix:" not in text:
        entries = ",\n".join(
            f"    {{ id: '{k}', label: '{MODULES[k]['title']}', path: 'pages/intelligence-matrix/{k}.html' }}"
            for k in MODULES
        )
        block = f"  intelligenceMatrix: [\n{entries},\n  ],\n\n"
        text = text.replace("  agents: [", block + "  agents: [")
    if "pages/intelligence-matrix/" not in text:
        text = text.replace(
            "    if (path.startsWith('pages/case-studies/')) {",
            "    if (path === 'pages/intelligence-matrix/index.html') return '#/intelligence-matrix';\n"
            "    if (path.startsWith('pages/intelligence-matrix/')) {\n"
            "      const slug = path.replace('pages/intelligence-matrix/', '').replace('.html', '');\n"
            "      return '#/intelligence-matrix/' + slug;\n"
            "    }\n"
            "    if (path.startsWith('pages/case-studies/')) {",
        )
    if "matrix-" not in text or "startsWith('matrix-')" not in text:
        if "startsWith('case-study-')" in text:
            text = text.replace(
                "    if (routeId.startsWith('case-study-')) return '#/case-studies/' + routeId.replace('case-study-', '');",
                "    if (routeId.startsWith('case-study-')) return '#/case-studies/' + routeId.replace('case-study-', '');\n"
                "    if (routeId.startsWith('matrix-')) return '#/intelligence-matrix/' + routeId.replace('matrix-', '');",
            )
    if "startsWith('matrix-')" not in text.split("matchRoute")[1] if "matchRoute" in text else "":
        text = text.replace(
            "    if (currentRoute.startsWith('agent-')) return 'agents';",
            "    if (currentRoute.startsWith('matrix-')) return 'intelligence-matrix';\n"
            "    if (currentRoute.startsWith('agent-')) return 'agents';",
        )
    ROUTES.write_text(text, encoding="utf-8")


def main():
    IMX_DIR.mkdir(parents=True, exist_ok=True)
    cards = "\n".join(card_html(k, m, i) for i, (k, m) in enumerate(MODULES.items(), 1))
    section = IMX_SECTION.format(cards=cards)

    text = HTML.read_text(encoding="utf-8")
    if "/* ═══ INTELLIGENCE MATRIX — unified landing promo ═══ */" not in text:
        marker = "/* ═══ CASE STUDIES — unified landing promo ═══ */"
        if marker not in text:
            marker = "/* ═══ AGENTS — unified landing promo ═══ */"
        end = text.find("/* ═══ TELEPHONY — landing promo", text.index(marker))
        insert_at = text.rfind("}", 0, end) + 1
        text = text[:insert_at] + IMX_CSS + text[insert_at:]

    for pat in [
        r"<!-- Bento / Analytics -->.*?</section>\s*<!-- Journey",
        r"<!-- INTELLIGENCE MATRIX HUB -->.*?</section>\s*<!-- Journey",
    ]:
        m = re.search(pat, text, re.DOTALL)
        if m:
            text = text[: m.start()] + section + "\n <!-- Journey" + text[m.end() :]
            break
    else:
        raise SystemExit("bento section not found")

    HTML.write_text(text, encoding="utf-8")
    for slug, data in MODULES.items():
        (IMX_DIR / f"{slug}.html").write_text(module_page(slug, data), encoding="utf-8")
    HUB.write_text(hub_html(), encoding="utf-8")
    patch_routes()
    print("OK: intelligence matrix promo,", len(MODULES), "module pages, hub index")


if __name__ == "__main__":
    main()
