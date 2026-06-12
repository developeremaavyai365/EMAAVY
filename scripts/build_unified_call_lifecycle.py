"""
Replace home #journey (Call lifecycle) with unified EMAAVY promo.
Create pages/call-lifecycle/*.html with descriptive step pages.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
CLC_DIR = ROOT / "pages" / "call-lifecycle"
HUB = CLC_DIR / "index.html"
ROUTES = ROOT / "assets" / "routes.js"

CLC_CSS = """
/* ═══ CALL LIFECYCLE — unified landing promo ═══ */
.clc-promo-shell {
  padding: clamp(2rem, 4vw, 2.75rem) clamp(1.25rem, 4vw, 2.25rem) !important;
}
.clc-promo {
  display: grid !important;
  grid-template-columns: 1.05fr 0.95fr !important;
  gap: clamp(1.5rem, 4vw, 2.25rem) !important;
  align-items: start !important;
  text-align: left !important;
  margin-bottom: 1.75rem !important;
}
.clc-promo h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.5rem, 3.2vw, 2.1rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.12 !important;
  color: #0f172a !important;
  margin: 0 0 1rem !important;
  max-width: 22ch !important;
}
.clc-promo-lead {
  font-size: clamp(0.9rem, 1.45vw, 1.02rem) !important;
  line-height: 1.7 !important;
  color: #475569 !important;
  margin: 0 0 1.2rem !important;
  max-width: 54ch !important;
}
.clc-promo-highlights {
  list-style: none !important;
  margin: 0 0 1.6rem !important;
  padding: 0 !important;
  display: grid !important;
  gap: 0.5rem !important;
}
.clc-promo-highlights li {
  font-size: 0.86rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  padding: 0.32rem 0 0.32rem 0.85rem !important;
  border-left: 3px solid #4A658B !important;
}
.clc-promo-highlights strong { color: #0f172a !important; font-weight: 600 !important; }
.clc-promo-actions {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 0.7rem !important;
}
.btn-clc-explore {
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
.btn-clc-explore:hover { background: #18345D !important; transform: translateY(-1px) !important; }
.btn-clc-secondary {
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
.btn-clc-secondary:hover { border-color: #4A658B !important; background: #f8fafc !important; }
.clc-promo-panel {
  padding: 1.2rem 1rem !important;
  border-radius: 10px !important;
  background: linear-gradient(145deg, #f8fafc 0%, #f0f4f8 100%) !important;
  border: 1px solid #e2e8f0 !important;
  max-height: 26rem !important;
  overflow-y: auto !important;
}
.clc-promo-panel-head {
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
.clc-step-cards { display: grid !important; gap: 0.45rem !important; }
.clc-step-card {
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
.clc-step-card:hover {
  border-color: #4A658B !important;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06) !important;
}
.clc-step-card:hover .clc-step-explore { color: #18345D !important; }
.clc-step-label {
  grid-column: 1 !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.clc-step-card strong {
  grid-column: 1 !important;
  font-size: 0.88rem !important;
  color: #0f172a !important;
  font-weight: 600 !important;
}
.clc-step-snippet {
  grid-column: 1 / -1 !important;
  font-size: 0.72rem !important;
  line-height: 1.45 !important;
  color: #64748b !important;
  margin-top: 0.15rem !important;
}
.clc-step-meta {
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
.clc-step-explore {
  grid-column: 1 / -1 !important;
  font-size: 0.7rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  margin-top: 0.35rem !important;
}
.clc-promo-stats {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.65rem !important;
  padding-top: 0.25rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
.clc-promo-stats .int-stat {
  text-align: center !important;
  padding: 0.85rem 0.5rem !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
}
.clc-promo-stats .int-stat b {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.25rem !important;
  color: #4A658B !important;
  margin-bottom: 0.2rem !important;
}
@media (max-width: 900px) {
  .clc-promo { grid-template-columns: 1fr !important; }
  .clc-promo h3 { max-width: none !important; }
  .clc-promo-stats { grid-template-columns: repeat(2, 1fr) !important; }
  .clc-promo-panel { max-height: none !important; }
  .clc-step-meta { display: none !important; }
}
"""

STEPS = {
    "ring": {
        "route": "lifecycle-ring",
        "step_num": "01",
        "title": "Call Connects",
        "short_title": "Ring — Call Connects",
        "kicker": "Step 1 · Ring",
        "meta": "0ms delay",
        "snippet": "Capture audio, metadata, and speaker context from the first ring.",
        "hero_lead": "The lifecycle begins the moment the call connects. EMAAVY starts listening immediately — no warm-up delay, no dropped opening seconds, no intelligence lost before the first hello.",
        "stats": [("0ms", "Start delay"), ("100%", "Capture rate"), ("Instant", "Metadata")],
        "overview": "Ring is the ingest stage. Whether inbound support, outbound campaign, or supervisor-monitored sales, EMAAVY attaches to the audio stream at connect and enriches it with caller ID, campaign tags, and consent state before transcription even starts.",
        "what_happens": [
            "Audio stream capture begins at answer — inbound or outbound",
            "Caller ID, dialed number, and campaign ID logged to the session",
            "Recording consent and regional compliance flags applied",
            "Speaker context initialized for diarization downstream",
        ],
        "emaavy_does": [
            ("Connect", "Telephony layer (Vobiz, SIP, or CPaaS) hands media to EMAAVY."),
            ("Tag", "Campaign, agent, and language hints attached to the session."),
            ("Record", "Optional encrypted recording with retention policy."),
            ("Stream", "Real-time audio forked to STT without batch delay."),
        ],
        "outcomes": [
            "100% of answered calls enter the intelligence pipeline",
            "Zero gap between ring and first transcribed word",
            "Full attribution for downstream CRM and analytics",
        ],
        "related": "Transcribe",
    },
    "transcribe": {
        "route": "lifecycle-transcribe",
        "step_num": "02",
        "title": "Every Word Captured",
        "short_title": "Transcribe — Every Word",
        "kicker": "Step 2 · Transcribe",
        "meta": "<0.5s latency",
        "snippet": "Deepgram, Sarvam, and more stream every word in real time.",
        "hero_lead": "Transcription is not a post-call report. EMAAVY streams every word through your chosen STT stack — Deepgram for international accents, Sarvam for Indian languages — with sub-half-second word latency.",
        "stats": [("<0.5s", "Word latency"), ("9+", "STT providers"), ("Streaming", "Architecture")],
        "overview": "The transcribe stage turns speech into searchable text while the conversation is still happening. Supervisors, AI agents, and scoring models all consume the same live transcript — eliminating the batch-processing blind spot that plagues traditional call centers.",
        "what_happens": [
            "Partial transcripts appear word-by-word in the intelligence layer",
            "Speaker diarization separates agent, customer, and AI voices",
            "Confidence scores attach to each token for QA review",
            "Live keyword detection can trigger supervisor alerts mid-call",
        ],
        "emaavy_does": [
            ("Route STT", "Per-language provider selection — Sarvam, Deepgram, Gladia, etc."),
            ("Enhance", "Telephony-optimized audio preprocessing for noisy lines."),
            ("Timestamp", "Word-level timing for sync with playback and coaching."),
            ("Archive", "Full transcript stored for search, export, and compliance."),
        ],
        "outcomes": [
            "Supervisors coach on what is being said, not what was said",
            "AI agents respond with full conversational context",
            "QA teams eliminate manual listen-and-type workflows",
        ],
        "related": "Analyze",
    },
    "analyze": {
        "route": "lifecycle-analyze",
        "step_num": "03",
        "title": "Score Live",
        "short_title": "Analyze — Score Live",
        "kicker": "Step 3 · Analyze",
        "meta": "Per-turn scoring",
        "snippet": "Sentiment, intent, objections, and compliance scored on every turn.",
        "hero_lead": "Analysis happens per conversational turn — not in a batch job overnight. Sentiment arcs, buyer intent, objection types, and compliance risk update live so teams can act before the caller hangs up.",
        "stats": [("Per-turn", "Scoring"), ("Live", "Alerts"), ("Multi-signal", "Intelligence")],
        "overview": "The analyze stage is EMAAVY's reasoning layer. Your configured LLM stack interprets meaning, emotion, and risk on each turn, feeding the intelligence matrix dashboards and trigger engine simultaneously.",
        "what_happens": [
            "Sentiment timeline shifts green, amber, or red as tone changes",
            "Intent classified as buy, explore, objection, or reject per turn",
            "Compliance lexicon flags risky phrases for regulated industries",
            "Objection tags feed script coaching and funnel analytics",
        ],
        "emaavy_does": [
            ("Reason", "Route GPT, Claude, Gemini, Qwen, or Grok per workflow."),
            ("Score", "Apply sentiment, intent, and compliance models in parallel."),
            ("Alert", "Notify supervisors when thresholds breach."),
            ("Summarize", "Rolling call summary for handoff and CRM notes."),
        ],
        "outcomes": [
            "Decisions based on live conversation state, not post-call guesswork",
            "Compliance teams catch issues during the call",
            "Sales leaders see intent shift before deals slip away",
        ],
        "related": "Act",
    },
    "act": {
        "route": "lifecycle-act",
        "step_num": "04",
        "title": "Triggers Fire",
        "short_title": "Act — Triggers Fire",
        "kicker": "Step 4 · Act",
        "meta": "Zero manual steps",
        "snippet": "CRM, WhatsApp, calendar, and coaching alerts fire from call intelligence.",
        "hero_lead": "Intelligence without action is noise. The Act stage fires CRM updates, WhatsApp confirmations, Cal.com bookings, coaching pings, and custom webhooks — automatically, from what was actually said on the call.",
        "stats": [("Zero", "Manual steps"), ("Instant", "Execution"), ("CRM + WA", "Connected")],
        "overview": "Act is the orchestration layer. Business rules map conversation signals to downstream systems — so operations teams stop copying notes and developers stop polling for transcripts.",
        "what_happens": [
            "CRM disposition and custom fields update on call end or mid-call",
            "WhatsApp and email follow-ups send with personalized context",
            "Calendar events create when the agent books a slot live",
            "Supervisor coaching alerts fire on negative sentiment shifts",
        ],
        "emaavy_does": [
            ("Match rules", "Intent thresholds, keywords, and sentiment gates."),
            ("Execute", "Native connectors + webhooks with retry logic."),
            ("Log", "Every trigger recorded in the audit trail."),
            ("Handoff", "Warm transfer to humans with full transcript attached."),
        ],
        "outcomes": [
            "Same-tab customer experience continues after the voice call",
            "Revenue teams see meetings booked without manual entry",
            "Support tickets created with transcript evidence attached",
        ],
        "related": "Learn",
    },
    "learn": {
        "route": "lifecycle-learn",
        "step_num": "05",
        "title": "Models Improve",
        "short_title": "Learn — Models Improve",
        "kicker": "Step 5 · Learn",
        "meta": "Continuous",
        "snippet": "Every call feeds script tuning, routing, and coaching improvements.",
        "hero_lead": "The lifecycle closes with learning. Every conversation feeds script A/B results, model routing refinements, and coaching patterns — so the next campaign performs better than the last.",
        "stats": [("Continuous", "Learning"), ("Auto", "Optimization"), ("A/B", "Scripts")],
        "overview": "Learn turns operational data into compounding advantage. EMAAVY aggregates outcomes across campaigns to recommend script changes, STT/LLM routing tweaks, and agent coaching focus areas — without a separate data science team.",
        "what_happens": [
            "Script variants ranked by conversion and handle time",
            "Model routing adjusted for language and intent segments",
            "Coaching patterns surfaced for under-performing agents",
            "Funnel trends exported for executive and ops reviews",
        ],
        "emaavy_does": [
            ("Aggregate", "Roll up scores, outcomes, and durations across campaigns."),
            ("Recommend", "Suggest script and routing changes from win/loss patterns."),
            ("Loop", "Feed results into agent builder and campaign defaults."),
            ("Report", "Weekly intelligence summaries for leadership."),
        ],
        "outcomes": [
            "Conversion rates improve quarter over quarter without new headcount",
            "Cost per outcome drops as routing optimizes automatically",
            "Coaching becomes data-led instead of anecdotal",
        ],
        "related": "Ring",
    },
}


def card_html(slug, s, num):
    return f"""          <a href="pages/call-lifecycle/{slug}.html" class="clc-step-card">
            <span class="clc-step-label">Step {num} · {s['kicker'].split('·')[-1].strip()}</span>
            <strong>{s['title']}</strong>
            <span class="clc-step-meta">{s['meta']}</span>
            <span class="clc-step-snippet">{s['snippet']}</span>
            <span class="clc-step-explore">Explore step →</span>
          </a>"""


CLC_SECTION = """<!-- CALL LIFECYCLE HUB --> <section id="journey" class="cap-section">
 <div class="features-head reveal">
  <span class="section-kicker">Call lifecycle · End-to-end flow</span>
  <h2>The call journey — step by step</h2>
  <p class="int-hub-desc">From ring to learn — five stages, each on its own page. See how EMAAVY captures, transcribes, scores, acts, and improves on every call.</p>
 </div>
 <div class="int-showcase reveal clc-promo-wrap" id="call-lifecycle-emaavy">
  <div class="int-shell clc-promo-shell">
    <div class="clc-promo reveal">
      <div class="clc-promo-copy">
        <span class="section-kicker">Call lifecycle · EMAAVY</span>
        <h3>From ring to learn — fully automated</h3>
        <p class="clc-promo-lead">EMAAVY runs the complete call lifecycle without batch jobs or manual handoffs. Every stage — connect, transcribe, analyze, act, and learn — has dedicated documentation so your team knows exactly what happens on the wire.</p>
        <ul class="clc-promo-highlights" aria-label="Call lifecycle highlights">
          <li><strong>Five stages</strong> — ring, transcribe, analyze, act, and learn in sequence</li>
          <li><strong>Real-time pipeline</strong> — no waiting until after hang-up for intelligence</li>
          <li><strong>Closed loop</strong> — outcomes feed the next campaign and agent version</li>
          <li><strong>100% automated</strong> — triggers and learning without ops copy-paste</li>
        </ul>
        <div class="clc-promo-actions">
          <a href="pages/call-lifecycle/index.html" class="btn-clc-explore">Explore call lifecycle</a>
          <a href="book-demo.html" class="btn-clc-secondary">Book a demo</a>
        </div>
      </div>
      <div class="clc-promo-panel">
        <div class="clc-promo-panel-head">Lifecycle stages</div>
        <div class="clc-step-cards">
{cards}
        </div>
      </div>
    </div>
    <div class="clc-promo-stats">
      <div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>5</b><span>Lifecycle stages</span></div>
      <div class="int-stat"><b>&lt;0.5s</b><span>Transcription</span></div>
      <div class="int-stat"><b>100%</b><span>Automated</span></div>
      <div class="int-stat"><b>0</b><span>Manual handoffs</span></div>
    </div>
  </div>
 </div>
</section>"""


def step_page(slug, s):
    flow = "".join(
        f'<li><span class="telephony-flow-num">{i:02d}</span><strong>{t}</strong><p>{d}</p></li>'
        for i, (t, d) in enumerate(s["emaavy_does"], 1)
    )
    happens = "".join(f"<li>{x}</li>" for x in s["what_happens"])
    outcomes = "".join(f"<li>{x}</li>" for x in s["outcomes"])
    stats = "".join(f'<div class="stat-box"><b>{b}</b><span>{l}</span></div>' for b, l in s["stats"])
    pills = "".join(
        f'<a href="{k}.html" class="int-layer-pill">{STEPS[k]["title"]}</a>' for k in STEPS
    )
    next_slug = {
        "Ring": "transcribe",
        "Transcribe": "analyze",
        "Analyze": "act",
        "Act": "learn",
        "Learn": "ring",
    }[s["related"]]
    prev_map = {v: k for k, v in {
        "transcribe": "ring",
        "analyze": "transcribe",
        "act": "analyze",
        "learn": "act",
        "ring": "learn",
    }.items()}
    prev_slug = prev_map.get(slug, "ring")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{s['short_title']} — Call Lifecycle — EMAAVY</title>
  <meta name="description" content="{s['hero_lead'][:155]}…" />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="{s['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main int-category-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <span class="page-kicker">{s['kicker']}</span>
        <h1>{s['short_title']}</h1>
        <p class="telephony-hero-lead">{s['hero_lead']}</p>
        <div class="stat-row telephony-hero-stats">{stats}</div>
        <div class="capabilities-jump telephony-jump">
          <a href="#overview">Overview</a>
          <a href="#happens">What happens</a>
          <a href="#emaavy">EMAAVY layer</a>
          <a href="#outcomes">Outcomes</a>
        </div>
      </div>
    </section>

    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">{pills}</div>
        <div class="cta-row" style="margin-top:1rem">
          <a href="{prev_slug}.html" class="btn-outline">← Previous stage</a>
          <a href="{next_slug}.html" class="btn-outline">Next stage →</a>
        </div>
      </div>
    </section>

    <section id="overview" class="page-section alt">
      <div class="container">
        <article class="capability-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">{s['step_num']}</span>
              <span class="capability-tag">Call lifecycle · {s['title']}</span>
            </div>
            <div class="capability-content">
              <h2>Stage overview</h2>
              <p class="capability-lead">{s['overview']}</p>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="happens" class="page-section">
      <div class="container">
        <h2 class="section-title">What happens on the call</h2>
        <p class="section-desc">Signals and events your team sees during this stage.</p>
        <ul class="feature-list">{happens}</ul>
      </div>
    </section>

    <section id="emaavy" class="page-section alt">
      <div class="container">
        <h2 class="section-title">How EMAAVY powers this stage</h2>
        <div class="telephony-flow-panel">
          <ol class="telephony-flow-steps">{flow}</ol>
        </div>
      </div>
    </section>

    <section id="outcomes" class="page-section">
      <div class="container">
        <h2 class="section-title">Business outcomes</h2>
        <ul class="feature-list">{outcomes}</ul>
        <div class="cta-row" style="margin-top:1.5rem">
          <a href="../../book-demo.html" class="btn-primary">See the lifecycle live →</a>
          <a href="index.html" class="btn-outline">All lifecycle stages</a>
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
    for slug, s in STEPS.items():
        cards.append(f"""          <a href="{slug}.html" class="glow-card">
            <div class="card-icon"><span class="brand-mark">{s['step_num']}</span></div>
            <h3>{s['title']}</h3>
            <p>{s['snippet']}</p>
            <span class="card-tag">{s['kicker']}</span>
            <span class="clc-step-explore" style="display:block;margin-top:0.5rem">Explore step →</span>
          </a>""")
    grid = "\n".join(cards)
    pills = "".join(f'<a href="{k}.html" class="int-layer-pill">{STEPS[k]["title"]}</a>' for k in STEPS)
    flow_items = "".join(
        f'<li><span class="telephony-flow-num">{s["step_num"]}</span><strong>{s["title"]}</strong>'
        f'<p>{s["snippet"]} <a href="{slug}.html">Explore step →</a></p></li>'
        for slug, s in STEPS.items()
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Call Lifecycle — EMAAVY</title>
  <meta name="description" content="EMAAVY call lifecycle — ring, transcribe, analyze, act, and learn. Five automated stages from connect to continuous improvement." />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="call-lifecycle">
  <div id="site-nav-root"></div>
  <main class="page-main int-category-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <span class="page-kicker">End-to-end flow</span>
        <h1>The call journey — step by step</h1>
        <p class="telephony-hero-lead">From ring to learn — every stage is captured, scored, and turned into action automatically. Explore each step for full detail on what EMAAVY does and why it matters.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>5</b><span>Lifecycle stages</span></div>
          <div class="stat-box"><b>&lt;0.5s</b><span>Transcription</span></div>
          <div class="stat-box"><b>100%</b><span>Automated</span></div>
        </div>
      </div>
    </section>
    <section class="page-section alt">
      <div class="container">
        <h2 class="section-title">The five-stage pipeline</h2>
        <div class="telephony-flow-panel">
          <ol class="telephony-flow-steps">{flow_items}</ol>
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
    if "callLifecycle:" not in text:
        entries = ",\n".join(
            f"    {{ id: '{k}', label: '{STEPS[k]['title']}', path: 'pages/call-lifecycle/{k}.html' }}"
            for k in STEPS
        )
        block = f"  callLifecycle: [\n{entries},\n  ],\n\n"
        text = text.replace("  intelligenceMatrix: [", block + "  intelligenceMatrix: [")
    if "pages/call-lifecycle/" not in text:
        text = text.replace(
            "    if (path === 'pages/intelligence-matrix/index.html') return '#/intelligence-matrix';",
            "    if (path === 'pages/call-lifecycle/index.html') return '#/call-lifecycle';\n"
            "    if (path.startsWith('pages/call-lifecycle/')) {\n"
            "      const slug = path.replace('pages/call-lifecycle/', '').replace('.html', '');\n"
            "      return '#/call-lifecycle/' + slug;\n"
            "    }\n"
            "    if (path === 'pages/intelligence-matrix/index.html') return '#/intelligence-matrix';",
        )
    if "startsWith('lifecycle-')" not in text:
        text = text.replace(
            "    if (routeId.startsWith('matrix-')) return '#/intelligence-matrix/' + routeId.replace('matrix-', '');",
            "    if (routeId.startsWith('lifecycle-')) return '#/call-lifecycle/' + routeId.replace('lifecycle-', '');\n"
            "    if (routeId.startsWith('matrix-')) return '#/intelligence-matrix/' + routeId.replace('matrix-', '');",
        )
    if "startsWith('lifecycle-')" not in text.split("matchRoute", 1)[1]:
        text = text.replace(
            "    if (currentRoute.startsWith('matrix-')) return 'intelligence-matrix';",
            "    if (currentRoute.startsWith('lifecycle-')) return 'call-lifecycle';\n"
            "    if (currentRoute.startsWith('matrix-')) return 'intelligence-matrix';",
        )
    ROUTES.write_text(text, encoding="utf-8")


def main():
    CLC_DIR.mkdir(parents=True, exist_ok=True)
    order = list(STEPS.keys())
    cards = "\n".join(card_html(k, STEPS[k], i) for i, k in enumerate(order, 1))
    section = CLC_SECTION.format(cards=cards)

    text = HTML.read_text(encoding="utf-8")
    if "/* ═══ CALL LIFECYCLE — unified landing promo ═══ */" not in text:
        marker = "/* ═══ INTELLIGENCE MATRIX — unified landing promo ═══ */"
        if marker not in text:
            marker = "/* ═══ CASE STUDIES — unified landing promo ═══ */"
        end = text.find("/* ═══ TELEPHONY — landing promo", text.index(marker))
        insert_at = text.rfind("}", 0, end) + 1
        text = text[:insert_at] + CLC_CSS + text[insert_at:]

    for pat in [
        r"<!-- Journey / Call lifecycle -->.*?</section>\s*<!-- Pricing",
        r"<!-- CALL LIFECYCLE HUB -->.*?</section>\s*<!-- Pricing",
    ]:
        m = re.search(pat, text, re.DOTALL)
        if m:
            text = text[: m.start()] + section + "\n <!-- Pricing" + text[m.end() :]
            break
    else:
        raise SystemExit("journey section not found")

    HTML.write_text(text, encoding="utf-8")
    for slug, data in STEPS.items():
        (CLC_DIR / f"{slug}.html").write_text(step_page(slug, data), encoding="utf-8")
    HUB.write_text(hub_html(), encoding="utf-8")
    patch_routes()
    print("OK: call lifecycle promo,", len(STEPS), "step pages, hub index")


if __name__ == "__main__":
    main()
