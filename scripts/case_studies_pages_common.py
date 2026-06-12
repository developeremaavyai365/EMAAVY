"""Shared case study hub + detail page rendering (integration-grade treatment)."""
from __future__ import annotations

from integration_pages_common import (
    HUB_CSS,
    LOGO_3D_CSS,
    PARTNER_CSS,
    cap_initials,
    logo_hero_html,
    logo_tile_html,
    setup_grid_html,
    workflow_viz_html,
)

HEAD_HUB = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/navbar-tokens.css" />
  <link rel="stylesheet" href="../assets/nav.css" />
  <link rel="stylesheet" href="../assets/masthead-flex.css" />
  <link rel="stylesheet" href="../assets/brand-logo.css" />
  <link rel="stylesheet" href="../assets/navbar-typography.css" />
  <link rel="icon" href="../assets/brand/emaavy-logo.svg" type="image/svg+xml" />
  <link rel="stylesheet" href="../assets/emaavy-type-tokens.css" />
  <link rel="stylesheet" href="../assets/site.css" />
  <link rel="stylesheet" href="../assets/footer-premium.css" />
  <link rel="stylesheet" href="../assets/emaavy-theme.css" />
  <link rel="stylesheet" href="../assets/responsive-system.css" />
"""

HEAD_DETAIL = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
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

HUB_CSS_REL = "../assets/telephony-hub.css"
PARTNER_CSS_REL = "../../assets/telephony-partner.css"
LOGO_3D_CSS_HUB = "../assets/integration-logo-3d.css"
LOGO_3D_CSS_DETAIL = "../../assets/integration-logo-3d.css"
SECTION_HEADING_CSS_HUB = "../assets/section-heading.css"
SECTION_HEADING_CSS_DETAIL = "../../assets/section-heading.css"

WORKFLOW_STEPS: dict[str, list[tuple[str, str]]] = {
    "mudita": [
        ("Audience loaded", "5,000 prospects segmented by city and language."),
        ("Agent configured", "Priya outbound flow with exhibition FAQ and capture."),
        ("Calls placed", "Bilingual Hinglish voice reaches every contact."),
        ("Registrations captured", "Intent and details written to CRM live."),
        ("WhatsApp confirms", "Show-rate lift within 30 seconds of verbal yes."),
    ],
    "nextcall": [
        ("Calls stream in", "Exotel numbers route through EMAAVY unchanged."),
        ("Real-time STT", "Every conversation transcribed as it happens."),
        ("Scores applied", "Sentiment, compliance, and intent per turn."),
        ("Supervisors alerted", "Coaching signals during active calls."),
        ("QA systems sync", "Scores and summaries via webhooks."),
    ],
    "fleetiq": [
        ("Delivery completes", "Post-delivery trigger from FleetIQ systems."),
        ("Language routed", "Regional language selected from metadata."),
        ("Follow-up placed", "Support agent confirms delivery satisfaction."),
        ("Sentiment monitored", "Negative shift flags supervisor instantly."),
        ("Human handoff", "Specialist joins with full transcript in under 60s."),
    ],
}


def study_tile_html(
    s: dict,
    *,
    label_key: str = "name",
    category: str | None = None,
    compact: bool = False,
    href: str | None = None,
) -> str:
    return logo_tile_html(
        s,
        label_key=label_key,
        category=category or s.get("hub_badge"),
        compact=compact,
        aria_suffix="case study",
        href=href,
    )


def explore_studies_html(studies: list, current_slug: str, label_key: str = "short") -> str:
    tiles = []
    for s in studies:
        if s["slug"] == current_slug:
            continue
        tiles.append(
            study_tile_html(s, label_key=label_key, category=s.get("hub_badge"), compact=True)
        )
    return "\n".join(tiles)


def stack_pills_html(stack: list[str]) -> str:
    pills = "".join(f'<span class="int-layer-pill">{x}</span>' for x in stack)
    return f'<div class="int-layer-nav">{pills}</div>'


def render_study(s: dict, *, studies: list) -> str:
    display = s.get("short", s["name"])
    stats = "".join(
        f'<div class="tel-partner-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in s["stats"]
    )
    challenge = "".join(f"<p>{para}</p>" for para in s["challenge"])
    benefits = "".join(
        f'<li><div><span class="tel-why-title">{t}</span><span class="tel-why-desc">{d}</span></div></li>'
        for t, d in s["solution_points"]
    )
    features = "".join(
        f'<article class="tel-feature-card"><span class="tel-cap-icon" aria-hidden="true">{cap_initials(t)}</span><h3>{t}</h3><p>{d}</p></article>'
        for t, d in s["solution_points"]
    )
    uses = "".join(
        f'<article class="tel-use-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in s["uses"]
    )
    workflow = workflow_viz_html(s.get("workflow", WORKFLOW_STEPS.get(s["slug"], s["implementation"])))
    setup = setup_grid_html(s["implementation"])
    results = "".join(
        f'<article class="tel-feature-card"><span class="tel-cap-icon" aria-hidden="true">{cap_initials(t)}</span><h3>{t}</h3><p>{d}</p></article>'
        for t, d in s["results_highlights"]
    )
    result_bullets = "".join(
        f'<li><div><span class="tel-why-title">{b}</span></div></li>' for b in s["results_bullets"]
    )
    explore = explore_studies_html(studies, s["slug"])
    hero_icon = logo_hero_html(s, s["name"])
    stack = stack_pills_html(s["stack"])

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
{HEAD_DETAIL}
  <link rel="stylesheet" href="{PARTNER_CSS_REL}" />
  <link rel="stylesheet" href="{LOGO_3D_CSS_DETAIL}" />
  <link rel="stylesheet" href="{SECTION_HEADING_CSS_DETAIL}" />
</head>
<body data-base="../../" data-route="{s['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main tel-partner-page">
    <section class="tel-partner-hero">
      <div class="container tel-partner-hero-grid">
        <div class="tel-partner-hero-copy">
          <span class="tel-partner-kicker">Case Study · {s['kicker']}</span>
          <h1>{s['headline']}</h1>
          <p class="tel-partner-lead">{s['lead']}</p>
          <div class="tel-partner-stats">{stats}</div>
          <div class="tel-partner-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Discuss a similar rollout</a>
            <a href="../case-studies.html" class="btn-outline">All case studies</a>
          </div>
        </div>
{hero_icon}
      </div>
    </section>

    <section id="overview" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Overview</h2>
          <p>The challenge {s['name']} faced before deploying EMAAVY.</p>
        </header>
        <div class="tel-partner-prose">{challenge}</div>
      </div>
    </section>

    <section id="capabilities" class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Key capabilities</h2>
          <p>{s['solution_lead']}</p>
        </header>
        <div class="tel-feature-grid">{features}</div>
        {stack}
      </div>
    </section>

    <section id="use-cases" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Business use cases</h2>
          <p>Where this program delivered the strongest outcomes for {s['short']}.</p>
        </header>
        <div class="tel-use-grid">{uses}</div>
      </div>
    </section>

    <section id="program-workflow" class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Program workflow</h2>
          <p>How the {s['short']} rollout runs end-to-end on EMAAVY.</p>
        </header>
        {workflow}
      </div>
    </section>

    <section id="setup-process" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Setup process</h2>
          <p>Step-by-step implementation — from data ingest to live operations.</p>
        </header>
        {setup}
      </div>
    </section>

    <section id="results" class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Results &amp; impact</h2>
          <p>Outcomes measured after go-live — not projections.</p>
        </header>
        <div class="tel-feature-grid">{results}</div>
        <ul class="tel-partner-benefits" style="margin-top:1.5rem">{result_bullets}</ul>
      </div>
    </section>

    <section id="business-benefits" class="tel-partner-section">
      <div class="container tel-partner-split">
        <header class="tel-partner-section-head">
          <h2>Business benefits</h2>
          <p>How EMAAVY voice, intelligence, and integrations powered the {s['short']} program.</p>
        </header>
        <ul class="tel-partner-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>More client stories</h2>
          <p>Explore other industries and programs running on EMAAVY.</p>
        </header>
        <nav class="int-logo-ecosystem int-logo-ecosystem--compact" aria-label="Case studies">
{explore}
        </nav>
      </div>
    </section>

    <section class="tel-partner-cta">
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


def render_hub(cfg: dict, studies: list) -> str:
    cards = "\n".join(
        study_tile_html(s, label_key="name", href=f"case-studies/{s['slug']}.html")
        for s in studies
    )
    extra_jumps = " ".join(f'<a href="#{s["slug"]}">{s["short"]}</a>' for s in studies)
    anchor_jumps = " ".join(
        f'<a href="#{jid}">{label}</a>' for jid, label in cfg.get("anchor_jumps", [])
    )
    stats = "".join(
        f'<div class="stat-box"><b>{a}</b><span>{b}</span></div>' for a, b in cfg["stats"]
    )
    pills = "".join(
        f'<div class="tel-hub-pill"><span class="tel-hub-pill-title">{t}</span><span>{d}</span></div>'
        for t, d in cfg["pills"]
    )
    flow = "".join(
        f'<article class="tel-flow-step"><span class="tel-flow-label">{t}</span><p>{d}</p></article>'
        for t, d in cfg["flow_steps"]
    )
    nav_pills = "".join(
        f'<a href="#{s["slug"]}" class="int-category-pill">{s["short"]}</a>' for s in studies
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{cfg['title']}</title>
  <meta name="description" content="{cfg['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{cfg.get('og_title', cfg['title'])}" />
  <meta property="og:description" content="{cfg.get('og_description', cfg['meta'])}" />
  <meta property="og:type" content="website" />
{HEAD_HUB}
  <link rel="stylesheet" href="{HUB_CSS_REL}" />
  <link rel="stylesheet" href="{LOGO_3D_CSS_HUB}" />
  <link rel="stylesheet" href="{SECTION_HEADING_CSS_HUB}" />
</head>
<body data-base="../" data-route="{cfg['route']}" class="int-logo-page">
  <div id="site-nav-root"></div>
  <main class="page-main telephony-page">
    <section class="int-dir-hero">
      <div class="container">
        <span class="page-kicker">{cfg['kicker']}</span>
        <h1>{cfg['h1']}</h1>
        <p class="int-dir-hero-lead">{cfg['lead']}</p>
        <div class="stat-row telephony-hero-stats">{stats}</div>
        <nav class="int-category-nav" aria-label="Case study categories">
          <a href="#{cfg['layer_id']}" class="int-category-pill">Why EMAAVY wins</a>
          <a href="#{cfg['stories_id']}" class="int-category-pill">Client stories</a>
          <a href="#{cfg['flow_id']}" class="int-category-pill">Rollout path</a>
          {nav_pills}
        </nav>
      </div>
    </section>

    <section id="{cfg['layer_id']}" class="tel-hub-voice">
      <div class="container">
        <article class="tel-hub-voice-card">
          <div class="tel-hub-voice-meta">
            <span class="tel-hub-voice-num">{cfg['layer_num']}</span>
            <span class="tel-hub-voice-tag">{cfg['layer_tag']}</span>
            <h2>{cfg['layer_h2']}</h2>
            <p class="tel-hub-voice-lead">{cfg['layer_lead']}</p>
          </div>
          <div class="tel-hub-pill-grid">{pills}</div>
        </article>
      </div>
    </section>

    <section id="{cfg['stories_id']}" class="tel-hub-partners tel-hub-partners--logos page-section alt">
      <div class="container">
        <header class="tel-hub-partners-head">
          <h2>{cfg['stories_h2']}</h2>
          <p>{cfg.get('stories_desc', 'Click a story to open the full case study.')}</p>
        </header>
        <nav class="int-logo-ecosystem" aria-label="{cfg['stories_h2']}">
{cards}
        </nav>
      </div>
    </section>

    <section id="{cfg['flow_id']}" class="tel-hub-flow">
      <div class="container">
        <header class="tel-hub-flow-head">
          <h2>{cfg['flow_h2']}</h2>
          <p>{cfg['flow_desc']}</p>
        </header>
        <div class="tel-flow-track">{flow}</div>
      </div>
    </section>

    <section class="tel-hub-cta">
      <div class="container">
        <h2>{cfg['cta_h2']}</h2>
        <p>{cfg['cta_desc']}</p>
        <div class="cta-row">
          <a href="../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="../index.html#case-studies" class="btn-outline">Back to platform</a>
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
