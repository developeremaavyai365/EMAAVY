"""
Replace home #case-studies inline cards with unified EMAAVY promo.
Create pages/case-studies/{mudita,nextcall,fleetiq}.html with full narratives.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
CS_DIR = ROOT / "pages" / "case-studies"
HUB = ROOT / "pages" / "case-studies.html"
ROUTES = ROOT / "assets" / "routes.js"

CS_CSS = """
/* ═══ CASE STUDIES — unified landing promo ═══ */
.cs-promo-shell {
  padding: clamp(2rem, 4vw, 2.75rem) clamp(1.25rem, 4vw, 2.25rem) !important;
}
.cs-promo {
  display: grid !important;
  grid-template-columns: 1.05fr 0.95fr !important;
  gap: clamp(1.5rem, 4vw, 2.25rem) !important;
  align-items: start !important;
  text-align: left !important;
  margin-bottom: 1.75rem !important;
}
.cs-promo h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.5rem, 3.2vw, 2.1rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.12 !important;
  color: #0f172a !important;
  margin: 0 0 1rem !important;
  max-width: 22ch !important;
}
.cs-promo-lead {
  font-size: clamp(0.9rem, 1.45vw, 1.02rem) !important;
  line-height: 1.7 !important;
  color: #475569 !important;
  margin: 0 0 1.2rem !important;
  max-width: 54ch !important;
}
.cs-promo-highlights {
  list-style: none !important;
  margin: 0 0 1.6rem !important;
  padding: 0 !important;
  display: grid !important;
  gap: 0.5rem !important;
}
.cs-promo-highlights li {
  font-size: 0.86rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  padding: 0.32rem 0 0.32rem 0.85rem !important;
  border-left: 3px solid #4A658B !important;
}
.cs-promo-highlights strong { color: #0f172a !important; font-weight: 600 !important; }
.cs-promo-actions {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 0.7rem !important;
}
.btn-cs-explore {
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
.btn-cs-explore:hover { background: #18345D !important; transform: translateY(-1px) !important; }
.btn-cs-secondary {
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
.btn-cs-secondary:hover { border-color: #4A658B !important; background: #f8fafc !important; }
.cs-promo-panel {
  padding: 1.2rem 1rem !important;
  border-radius: 10px !important;
  background: linear-gradient(145deg, #f8fafc 0%, #f0f4f8 100%) !important;
  border: 1px solid #e2e8f0 !important;
}
.cs-promo-panel-head {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.75rem !important;
}
.cs-study-cards { display: grid !important; gap: 0.45rem !important; }
.cs-study-card {
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
.cs-study-card:hover {
  border-color: #4A658B !important;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06) !important;
}
.cs-study-card:hover .cs-study-explore { color: #18345D !important; }
.cs-study-label {
  grid-column: 1 !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.cs-study-card strong {
  grid-column: 1 !important;
  font-size: 0.88rem !important;
  color: #0f172a !important;
  font-weight: 600 !important;
}
.cs-study-snippet {
  grid-column: 1 / -1 !important;
  font-size: 0.72rem !important;
  line-height: 1.45 !important;
  color: #64748b !important;
  margin-top: 0.15rem !important;
}
.cs-study-meta {
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
.cs-study-explore {
  grid-column: 1 / -1 !important;
  font-size: 0.7rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  margin-top: 0.35rem !important;
}
.cs-promo-stats {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.65rem !important;
  padding-top: 0.25rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
.cs-promo-stats .int-stat {
  text-align: center !important;
  padding: 0.85rem 0.5rem !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
}
.cs-promo-stats .int-stat b {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.25rem !important;
  color: #4A658B !important;
  margin-bottom: 0.2rem !important;
}
@media (max-width: 900px) {
  .cs-promo { grid-template-columns: 1fr !important; }
  .cs-promo h3 { max-width: none !important; }
  .cs-promo-stats { grid-template-columns: repeat(2, 1fr) !important; }
  .cs-study-meta { display: none !important; }
}
"""

STUDIES = {
    "mudita": {
        "route": "case-study-mudita",
        "title": "Warehouse by Mudita",
        "short": "Exhibition Registration Campaign",
        "kicker": "Events · Outbound",
        "meta": "68% registration",
        "snippet": "5,000 bilingual outbound calls for a luxury designer exhibition.",
        "hero_lead": "Warehouse by Mudita needed to fill a luxury designer exhibition — not with cold email, but with warm, bilingual voice conversations that captured registrations in real time.",
        "stats": [("68%", "Registration rate"), ("5,000", "Contacts reached"), ("12%", "Email baseline")],
        "challenge": "The marketing team had a list of 5,000 high-value prospects but email campaigns plateaued at a 12% registration rate. Manual calling was too slow for the exhibition timeline, and scripts in English alone missed a large Hindi-speaking audience.",
        "solution": "EMAAVY deployed Priya, a campaign voice agent fluent in Hindi and English with natural code-switching. Every call captured intent, objections, and registration details live — then triggered WhatsApp confirmations automatically.",
        "implementation": [
            ("Audience upload", "5,000 contacts segmented by city and language preference."),
            ("Agent configuration", "Priya outbound flow with exhibition details, pricing FAQ, and registration capture."),
            ("Live routing", "Sarvam STT for Hinglish, Bulbul V3 voice, and Qwen for cost-efficient dialogue."),
            ("Post-call automation", "WhatsApp ticket + calendar hold sent within 30 seconds of a yes."),
            ("Supervisor view", "Ops monitored conversion by hour and adjusted pacing in the dashboard."),
        ],
        "results": [
            "68% registration rate — 5.6× improvement over email alone",
            "3,400 confirmed attendees captured with structured CRM fields",
            "Average handle time under 4 minutes with zero manual data entry",
            "WhatsApp follow-up lifted show-rate by an additional 11%",
        ],
        "stack": ["Campaign Agent", "Sarvam STT", "Bulbul V3", "WhatsApp", "Webhooks"],
    },
    "nextcall": {
        "route": "case-study-nextcall",
        "title": "NextCall BPO",
        "short": "QA Automation at Scale",
        "kicker": "BPO · Quality Assurance",
        "meta": "61% faster QA",
        "snippet": "100% call coverage with real-time sentiment and compliance scoring.",
        "hero_lead": "NextCall BPO replaced sample-based manual auditing with EMAAVY's real-time intelligence — every call scored for sentiment, compliance, and intent the moment it happens.",
        "stats": [("61%", "Faster QA"), ("100%", "Call coverage"), ("5%", "Prior manual sample")],
        "challenge": "Quality teams could only audit about 5% of calls manually. Coaching was delayed, compliance gaps were discovered days later, and supervisors had no live signal when calls went off-script.",
        "solution": "EMAAVY ingested the full call stream, transcribed in real time, and scored every turn for sentiment, compliance keywords, and buyer intent. Supervisors received coaching alerts during active calls instead of after batch reviews.",
        "implementation": [
            ("Telephony connect", "Exotel numbers routed through EMAAVY with zero agent workflow change."),
            ("Scoring models", "Compliance lexicon + intent tiers tuned to NextCall's regulated scripts."),
            ("Supervisor console", "Live transcript feed with sentiment color coding per seat."),
            ("QA dashboards", "Per-agent compliance score, objection tags, and auto-generated summaries."),
            ("CRM sync", "Disposition and score pushed to internal QA tools via webhooks."),
        ],
        "results": [
            "100% call coverage vs 5% manual audit sampling",
            "61% reduction in time spent on QA review cycles",
            "Compliance violations flagged within the call, not days later",
            "Coaching suggestions delivered to team leads in real time",
        ],
        "stack": ["Deepgram STT", "Claude Sonnet", "Webhooks", "Exotel", "Call Intelligence"],
    },
    "fleetiq": {
        "route": "case-study-fleetiq",
        "title": "FleetIQ Logistics",
        "short": "Driver Follow-Up Automation",
        "kicker": "Logistics · Customer Experience",
        "meta": "28% CSAT lift",
        "snippet": "50,000 multilingual post-delivery calls per month with smart escalation.",
        "hero_lead": "FleetIQ automated post-delivery follow-ups across eight Indian languages — unhappy customers reach a human specialist in under 60 seconds, while satisfied deliveries scale without adding headcount.",
        "stats": [("28%", "CSAT lift"), ("50K", "Calls / month"), ("60s", "Escalation SLA")],
        "challenge": "Fifty thousand deliveries per month meant fifty thousand potential support calls. A small team could not staff every language, and delayed follow-ups hurt CSAT scores in regional markets.",
        "solution": "EMAAVY support-style agents placed outbound follow-up calls in the customer's preferred language, detected negative sentiment live, and warm-transferred frustrated callers to human agents with full transcript context.",
        "implementation": [
            ("Language routing", "Eight regional languages auto-selected from delivery metadata."),
            ("Sentiment gates", "Negative shift triggers supervisor alert and human bridge in &lt;60s."),
            ("Script library", "Delivery confirmation, damage report, and reschedule branches."),
            ("Ticketing", "Issues logged to FleetIQ helpdesk with transcript attachment."),
            ("Monthly scale", "Campaign pacing handles 50K+ contacts with retry and timezone rules."),
        ],
        "results": [
            "50,000 automated follow-up calls per month without proportional hiring",
            "28% CSAT improvement measured over 90 days post-launch",
            "60-second escalation SLA for negative-sentiment callers",
            "Human agents receive full context — issue, language, and transcript summary",
        ],
        "stack": ["Support Agent", "Sarvam STT", "Sentiment scoring", "Webhooks", "Human handoff"],
    },
}


def card_html(slug, s, num):
    return f"""          <a href="pages/case-studies/{slug}.html" class="cs-study-card">
            <span class="cs-study-label">{num:02d} · {s['kicker']}</span>
            <strong>{s['title']}</strong>
            <span class="cs-study-meta">{s['meta']}</span>
            <span class="cs-study-snippet">{s['snippet']}</span>
            <span class="cs-study-explore">Explore case study →</span>
          </a>"""


CS_SECTION = """<!-- CASE STUDIES HUB --> <section id="case-studies" class="cap-section">
 <div class="features-head reveal">
  <span class="section-kicker">Client Success · Case Studies</span>
  <h2>What we've built for our clients</h2>
  <p class="int-hub-desc">Real campaigns, measurable outcomes — each client story opens on its own page with full context, implementation detail, and results.</p>
 </div>
 <div class="int-showcase reveal cs-promo-wrap" id="case-studies-emaavy">
  <div class="int-shell cs-promo-shell">
    <div class="cs-promo reveal">
      <div class="cs-promo-copy">
        <span class="section-kicker">Client Success · EMAAVY</span>
        <h3>Proof from the field — not slide decks</h3>
        <p class="cs-promo-lead">EMAAVY powers exhibition registrations, BPO quality at scale, and multilingual logistics follow-ups. Explore each case study for the challenge, how we implemented voice AI, and the numbers that changed.</p>
        <ul class="cs-promo-highlights" aria-label="Case study highlights">
          <li><strong>Three industries</strong> — events, BPO, and logistics with dedicated deep dives</li>
          <li><strong>Full-funnel voice</strong> — outbound campaigns, live QA, and support automation</li>
          <li><strong>Measurable ROI</strong> — registration rates, QA speed, and CSAT lifts documented</li>
          <li><strong>Same-tab pages</strong> — open any story without losing your place on the site</li>
        </ul>
        <div class="cs-promo-actions">
          <a href="pages/case-studies.html" class="btn-cs-explore">Explore all case studies</a>
          <a href="book-demo.html" class="btn-cs-secondary">Book a demo</a>
        </div>
      </div>
      <div class="cs-promo-panel">
        <div class="cs-promo-panel-head">Featured client stories</div>
        <div class="cs-study-cards">
{cards}
        </div>
      </div>
    </div>
    <div class="cs-promo-stats">
      <div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>68%</b><span>Peak conversion</span></div>
      <div class="int-stat"><b>50K+</b><span>Calls / month</span></div>
      <div class="int-stat"><b>61%</b><span>Faster QA</span></div>
      <div class="int-stat"><b>28%</b><span>CSAT lift</span></div>
    </div>
  </div>
 </div>
</section>"""


def study_page(slug, s):
    impl = "".join(
        f'<li><span class="telephony-flow-num">{i:02d}</span><strong>{t}</strong><p>{d}</p></li>'
        for i, (t, d) in enumerate(s["implementation"], 1)
    )
    results = "".join(f"<li>{r}</li>" for r in s["results"])
    stats_hero = "".join(
        f'<div class="stat-box"><b>{b}</b><span>{l}</span></div>' for b, l in s["stats"]
    )
    stack = "".join(f'<span class="int-layer-pill">{x}</span>' for x in s["stack"])
    others = [k for k in STUDIES if k != slug]
    nav_pills = "".join(
        f'<a href="{k}.html" class="int-layer-pill">{STUDIES[k]["title"]}</a>' for k in STUDIES
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{s['title']} — Case Study — EMAAVY</title>
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
        <h1>{s['short']}</h1>
        <p class="telephony-hero-lead">{s['hero_lead']}</p>
        <div class="stat-row telephony-hero-stats">{stats_hero}</div>
        <div class="capabilities-jump telephony-jump">
          <a href="#challenge">Challenge</a>
          <a href="#solution">Solution</a>
          <a href="#implementation">Implementation</a>
          <a href="#results">Results</a>
        </div>
      </div>
    </section>

    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">{nav_pills}</div>
      </div>
    </section>

    <section id="challenge" class="page-section alt">
      <div class="container">
        <article class="capability-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">01</span>
              <span class="capability-tag">The challenge</span>
            </div>
            <div class="capability-content">
              <h2>What {s['title']} needed to solve</h2>
              <p class="capability-lead">{s['challenge']}</p>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="solution" class="page-section">
      <div class="container">
        <article class="capability-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">02</span>
              <span class="capability-tag">EMAAVY solution</span>
            </div>
            <div class="capability-content">
              <h2>How EMAAVY delivered</h2>
              <p class="capability-lead">{s['solution']}</p>
              <div class="int-layer-nav" style="margin-top:1rem">{stack}</div>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="implementation" class="page-section alt">
      <div class="container">
        <h2 class="section-title">Implementation on EMAAVY</h2>
        <p class="section-desc">Step-by-step rollout — from data ingest to live operations.</p>
        <div class="telephony-flow-panel">
          <ol class="telephony-flow-steps">{impl}</ol>
        </div>
      </div>
    </section>

    <section id="results" class="page-section">
      <div class="container">
        <h2 class="section-title">Results &amp; impact</h2>
        <p class="section-desc">Outcomes measured after go-live — not projections.</p>
        <div class="stat-row" style="margin-bottom:1.5rem">{stats_hero}</div>
        <ul class="feature-list">{results}</ul>
        <div class="cta-row" style="margin-top:1.5rem">
          <a href="../../book-demo.html" class="btn-primary">Discuss a similar rollout →</a>
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


def hub_html():
    cards = []
    for i, (slug, s) in enumerate(STUDIES.items(), 1):
        cards.append(f"""          <a href="case-studies/{slug}.html" class="glow-card cs-hub-card">
            <div class="card-icon"><span class="brand-mark">{s['title'][:2].upper()}</span></div>
            <h3>{s['title']}</h3>
            <p>{s['snippet']}</p>
            <span class="card-tag">{s['meta']}</span>
            <span class="cs-study-explore" style="display:block;margin-top:0.5rem">Explore case study →</span>
          </a>""")
    grid = "\n".join(cards)
    nav = "".join(
        f'<a href="case-studies/{k}.html" class="int-layer-pill">{STUDIES[k]["title"]}</a>'
        for k in STUDIES
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Case Studies — EMAAVY</title>
  <meta name="description" content="Real EMAAVY client results — exhibition campaigns, QA automation, and logistics follow-ups with measurable ROI." />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/nav.css" />
  <link rel="stylesheet" href="../assets/site.css" />
</head>
<body data-base="../" data-route="case-studies">
  <div id="site-nav-root"></div>
  <main class="page-main">
    <section class="page-hero telephony-hero">
      <div class="container">
        <span class="page-kicker">Client Success</span>
        <h1>What we've built for our clients</h1>
        <p class="telephony-hero-lead">Real results from real campaigns — each story has a dedicated page with challenge, implementation, and measured outcomes.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>68%</b><span>Peak conversion</span></div>
          <div class="stat-box"><b>50K+</b><span>Calls / month</span></div>
          <div class="stat-box"><b>61%</b><span>Faster QA</span></div>
        </div>
      </div>
    </section>
    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">{nav}</div>
        <div class="card-grid cols-2" style="margin-top:1.5rem">
{grid}
        </div>
        <div class="cta-row" style="margin-top:2rem">
          <a href="../book-demo.html" class="btn-primary">Book a demo</a>
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


def patch_routes():
    text = ROUTES.read_text(encoding="utf-8")
    if "caseStudies:" not in text:
        block = """  caseStudies: [
    { id: 'mudita', label: 'Warehouse by Mudita', path: 'pages/case-studies/mudita.html' },
    { id: 'nextcall', label: 'NextCall BPO', path: 'pages/case-studies/nextcall.html' },
    { id: 'fleetiq', label: 'FleetIQ Logistics', path: 'pages/case-studies/fleetiq.html' },
  ],

"""
        text = text.replace("  agents: [", block + "  agents: [")
    if "pages/case-studies/" not in text:
        text = text.replace(
            "    if (path.startsWith('pages/agents/')) {",
            "    if (path.startsWith('pages/case-studies/')) {\n"
            "      const slug = path.replace('pages/case-studies/', '').replace('.html', '');\n"
            "      return '#/case-studies/' + slug;\n"
            "    }\n"
            "    if (path.startsWith('pages/agents/')) {",
        )
    if "case-study-" not in text:
        text = text.replace(
            "    if (routeId.startsWith('agent-')) return '#/agents/' + routeId.replace('agent-', '');",
            "    if (routeId.startsWith('case-study-')) return '#/case-studies/' + routeId.replace('case-study-', '');\n"
            "    if (routeId.startsWith('agent-')) return '#/agents/' + routeId.replace('agent-', '');",
        )
    ROUTES.write_text(text, encoding="utf-8")


def main():
    CS_DIR.mkdir(parents=True, exist_ok=True)
    cards = "\n".join(card_html(k, s, i) for i, (k, s) in enumerate(STUDIES.items(), 1))
    section = CS_SECTION.format(cards=cards)

    text = HTML.read_text(encoding="utf-8")
    if "/* ═══ CASE STUDIES — unified landing promo ═══ */" not in text:
        marker = "/* ═══ AGENTS — unified landing promo ═══ */"
        end = text.find("/* ═══ TELEPHONY — landing promo", text.index(marker))
        insert_at = text.rfind("}", 0, end) + 1
        text = text[:insert_at] + CS_CSS + text[insert_at:]

    pattern = re.compile(
        r"<!-- CASE STUDIES -->.*?</section>\s*<!-- Bento",
        re.DOTALL,
    )
    if not pattern.search(text):
        pattern = re.compile(
            r"<!-- CASE STUDIES HUB -->.*?</section>\s*<!-- Bento",
            re.DOTALL,
        )
    if not pattern.search(text):
        raise SystemExit("case-studies section not found")
    text = pattern.sub(section + "\n <!-- Bento", text, count=1)
    HTML.write_text(text, encoding="utf-8")

    for slug, data in STUDIES.items():
        (CS_DIR / f"{slug}.html").write_text(study_page(slug, data), encoding="utf-8")
    HUB.write_text(hub_html(), encoding="utf-8")
    patch_routes()
    print("OK: case studies promo, hub, and", len(STUDIES), "detail pages")


if __name__ == "__main__":
    main()
