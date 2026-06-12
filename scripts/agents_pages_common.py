"""Shared agent hub + role page rendering (integration-grade treatment)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from agent_templates import group_by_category, slugify_category

from integration_pages_common import (
    HEAD_COMMON,
    HUB_CSS,
    LOGO_3D_CSS,
    PARTNER_CSS,
    SECTION_HEADING_CSS,
    cap_initials,
    ensure_uses,
    logo_hero_html,
    logo_tile_html,
    setup_grid_html,
    workflow_viz_html,
)

AGENTS_TEMPLATES_CSS = "../../assets/agents-templates.css"

WORKFLOW_STEPS: dict[str, list[tuple[str, str]]] = {
    "sales-agent": [
        ("Lead connects", "Outbound or inbound call reaches the Sales Agent."),
        ("EMAAVY qualifies", "LLM scores intent and runs discovery questions."),
        ("Objections handled", "Playbook-grounded responses on every turn."),
        ("Meeting booked", "Calendar event created during the conversation."),
        ("CRM updated", "Disposition and fields sync to Salesforce or HubSpot."),
    ],
    "support-agent": [
        ("Caller connects", "Support line answered without queue delay."),
        ("Issue understood", "STT + LLM classify intent and sentiment."),
        ("FAQ or action", "Knowledge base answer or account lookup via tools."),
        ("Escalation if needed", "Warm transfer with full transcript context."),
        ("Ticket closed", "Webhook or CRM records resolution automatically."),
    ],
    "outbound-agent": [
        ("List loaded", "Campaign contacts assigned to Outbound Agent."),
        ("Dial placed", "Telephony layer initiates proactive call."),
        ("Script adapts", "Personalized opener and live objection handling."),
        ("Disposition captured", "Outcome scored and logged in real time."),
        ("Follow-up fires", "WhatsApp or retry rules run post-call."),
    ],
    "inbound-agent": [
        ("Call rings", "Inbound DID answered on first ring."),
        ("Intent detected", "Natural language replaces legacy IVR menus."),
        ("Tier-1 resolved", "FAQ, status, or booking handled by agent."),
        ("Routed or transferred", "Sales, support, or specialist queue with context."),
        ("Analytics updated", "Volume and resolution metrics refresh live."),
    ],
}


def role_tile_html(
    r: dict,
    *,
    label_key: str = "short",
    category: str | None = None,
    compact: bool = False,
) -> str:
    return logo_tile_html(
        r,
        label_key=label_key,
        category=category or r.get("hub_badge"),
        compact=compact,
        aria_suffix="agent template",
    )


def explore_roles_html(roles: list, current_slug: str, label_key: str = "short") -> str:
    tiles = []
    for r in roles:
        if r["slug"] == current_slug:
            continue
        tiles.append(role_tile_html(r, label_key=label_key, category=r.get("hub_badge"), compact=True))
    return "\n".join(tiles)


def render_role(
    r: dict,
    *,
    roles: list,
    hub_file: str = "workforce.html",
    hub_label: str = "All agent roles",
    hub_breadcrumb: str = "AI Workforce",
    hub_cta_label: str = "Workforce overview",
) -> str:
    stats = "".join(
        f'<div class="tel-partner-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in r["stats"]
    )
    about = "".join(f"<p>{para}</p>" for para in r["about"])
    benefits = "".join(
        f'<li><div><span class="tel-why-title">{t}</span><span class="tel-why-desc">{d}</span></div></li>'
        for t, d in r["emaavy"]
    )
    features = "".join(
        f'<article class="tel-feature-card"><span class="tel-cap-icon" aria-hidden="true">{cap_initials(t)}</span><h3>{t}</h3><p>{d}</p></article>'
        for t, d in r["features"]
    )
    uses = "".join(
        f'<article class="tel-use-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in r["uses"]
    )
    workflow = workflow_viz_html(
        r.get("workflow", WORKFLOW_STEPS.get(r["slug"], WORKFLOW_STEPS.get("sales-agent", [])))
    )
    setup = setup_grid_html(r["setup"])
    explore = explore_roles_html(roles, r["slug"], label_key="name")
    hero_icon = logo_hero_html(r, r["name"])
    route_id = r.get("route", f"agent-{r['slug']}")
    campaigns_id = ""
    display = r["name"]

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
  <link rel="stylesheet" href="{PARTNER_CSS}" />
  <link rel="stylesheet" href="{LOGO_3D_CSS}" />
  <link rel="stylesheet" href="{SECTION_HEADING_CSS}" />
  <link rel="stylesheet" href="{AGENTS_TEMPLATES_CSS}" />
</head>
<body data-base="../../" data-route="{route_id}">
  <div id="site-nav-root"></div>
  <main class="page-main tel-partner-page">
    <section class="tel-partner-hero">
      <div class="container tel-partner-hero-grid">
        <div class="tel-partner-hero-copy">
          <span class="tel-partner-kicker">Agent Template · {r['tag']}</span>
          <h1>{r['h1']}</h1>
          <p class="tel-partner-lead">{r['lead']}</p>
          <div class="tel-partner-stats">{stats}</div>
          <div class="tel-partner-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Use this template</a>
            <a href="{hub_file}" class="btn-outline">{hub_label}</a>
          </div>
        </div>
{hero_icon}
      </div>
    </section>

    <section id="overview" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Overview</h2>
          <p>What the {r['name']} does and when to deploy it on EMAAVY.</p>
        </header>
        <div class="tel-partner-prose">{about}</div>
      </div>
    </section>

    <section id="capabilities" class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Key capabilities</h2>
          <p>Core features teams enable when the {r['name']} is live.</p>
        </header>
        <div class="tel-feature-grid">{features}</div>
      </div>
    </section>

    <section id="use-cases" class="tel-partner-section{campaigns_id}">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Business use cases</h2>
          <p>Where the {r['name']} delivers the strongest outcomes.</p>
        </header>
        <div class="tel-use-grid">{uses}</div>
      </div>
    </section>

    <section id="agent-workflow" class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Agent workflow</h2>
          <p>How the {r['name']} runs through EMAAVY on a typical call.</p>
        </header>
        {workflow}
      </div>
    </section>

    <section id="setup-process" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Setup process</h2>
          <p>From template to production calls with the {r['name']}.</p>
        </header>
        {setup}
      </div>
    </section>

    <section id="business-benefits" class="tel-partner-section alt">
      <div class="container tel-partner-split">
        <header class="tel-partner-section-head">
          <h2>Business benefits</h2>
          <p>How EMAAVY orchestrates voice, intelligence, and tools for the {r['name']}.</p>
        </header>
        <ul class="tel-partner-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Explore other templates</h2>
          <p>Browse all 14 pre-built flows — sales, scheduling, support, HR, finance, events, and more.</p>
        </header>
        <nav class="int-logo-ecosystem int-logo-ecosystem--compact" aria-label="Agent roles">
{explore}
        </nav>
      </div>
    </section>

    <section class="tel-partner-cta">
      <div class="container">
        <h2>Ready to deploy the {r['name']}?</h2>
        <p>Book a walkthrough — hear a live call, review scripts, and map your first campaign.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="{hub_file}" class="btn-outline">{hub_cta_label}</a>
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


def _category_tiles_html(roles: list, *, compact: bool = False) -> str:
    if not roles:
        return ""
    groups = group_by_category(roles)
    chunks = []
    for cat, items in groups:
        tiles = "\n".join(
            role_tile_html(r, label_key="name", category=r.get("hub_badge"), compact=compact)
            for r in items
        )
        chunks.append(
            f"""        <div class="agt-category-group" id="{slugify_category(cat)}">
          <h3 class="agt-category-title">{cat}</h3>
          <nav class="int-logo-ecosystem{" int-logo-ecosystem--compact" if compact else ""}" aria-label="{cat} templates">
{tiles}
          </nav>
        </div>"""
        )
    return "\n".join(chunks)


def render_workforce(cfg: dict, roles: list, *, grouped: bool = False) -> str:
    if grouped:
        cards = _category_tiles_html(roles)
    else:
        cards = "\n".join(role_tile_html(r, label_key="name") for r in roles)
    extra_jumps = " ".join(
        f'<a href="#{slugify_category(r["category"])}">{r["category"]}</a>'
        for r in roles
        if r.get("category")
    )
    extra_jumps = ""
    seen = set()
    for r in roles:
        cat = r.get("category")
        if cat and cat not in seen:
            seen.add(cat)
            extra_jumps += f' <a href="#{slugify_category(cat)}">{cat}</a>'
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
    builder_pills = "".join(
        f'<div class="tel-hub-pill"><span class="tel-hub-pill-title">{t}</span><span>{d}</span></div>'
        for t, d in cfg.get("builder_pills", [])
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
{HEAD_COMMON}
  <link rel="stylesheet" href="{HUB_CSS}" />
  <link rel="stylesheet" href="{LOGO_3D_CSS}" />
  <link rel="stylesheet" href="{SECTION_HEADING_CSS}" />
  <link rel="stylesheet" href="{AGENTS_TEMPLATES_CSS}" />
</head>
<body data-base="../../" data-route="{cfg['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main telephony-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <span class="page-kicker">{cfg['kicker']}</span>
        <h1>{cfg['h1']}</h1>
        <p class="telephony-hero-lead">{cfg['lead']}</p>
        <div class="stat-row telephony-hero-stats">{stats}</div>
        <div class="capabilities-jump telephony-jump">
          {anchor_jumps}
          {extra_jumps}
        </div>
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

    <section id="{cfg['roles_id']}" class="tel-hub-partners tel-hub-partners--logos page-section alt">
      <div class="container">
        <header class="tel-hub-partners-head">
          <h2>{cfg['roles_h2']}</h2>
          <p>{cfg.get('roles_desc_short', 'Click a role to open the full agent page.')}</p>
        </header>
        <div class="agt-template-groups" aria-label="{cfg['roles_h2']}">
{cards}
        </div>
      </div>
    </section>

    <section id="builder" class="tel-hub-voice">
      <div class="container">
        <article class="tel-hub-voice-card">
          <div class="tel-hub-voice-meta">
            <span class="tel-hub-voice-num">Custom</span>
            <span class="tel-hub-voice-tag">EMAAVY · Agent Builder</span>
            <h2>{cfg['builder_h2']}</h2>
            <p class="tel-hub-voice-lead">{cfg['builder_lead']}</p>
            <div class="cta-row" style="margin-top:1rem">
              <a href="../../book-demo.html" class="btn-primary">Build your agent</a>
              <a href="../../pages/documentation.html" class="btn-outline">Agent builder docs</a>
            </div>
          </div>
          <div class="tel-hub-pill-grid">{builder_pills}</div>
        </article>
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


def render_agents_index(roles: list, builder_tile: str, *, grouped: bool = False) -> str:
    seen = set()
    nav_pills = '<a href="workforce.html" class="int-category-pill">Full overview</a>'
    for r in roles:
        cat = r.get("category")
        if cat and cat not in seen:
            seen.add(cat)
            nav_pills += f'<a href="#{slugify_category(cat)}" class="int-category-pill">{cat}</a>'
    nav_pills += '<a href="workforce.html#builder" class="int-category-pill">Builder</a>'

    if grouped:
        role_sections = _category_tiles_html(roles)
        role_sections += f"\n        <div class=\"agt-category-group\" id=\"builder\">\n          <h3 class=\"agt-category-title\">Custom</h3>\n          <nav class=\"int-logo-ecosystem\" aria-label=\"Custom builder\">\n{builder_tile}\n          </nav>\n        </div>"
    else:
        role_tiles = "\n".join(
            role_tile_html(r, label_key="name", category=r.get("hub_badge")) for r in roles
        )
        role_sections = f"""        <nav class="int-logo-ecosystem" aria-label="Agent templates">
{role_tiles}
{builder_tile}
        </nav>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Agent Templates — EMAAVY</title>
  <meta name="description" content="Fourteen EMAAVY voice agent templates — sales, scheduling, support, HR, finance, events, and more. Deploy in 10–12 minutes." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="AI Agent Templates — EMAAVY" />
  <meta property="og:description" content="Start from a template — browse 14 enterprise-ready voice agent flows and deploy in minutes." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="{HUB_CSS}" />
  <link rel="stylesheet" href="{LOGO_3D_CSS}" />
  <link rel="stylesheet" href="{SECTION_HEADING_CSS}" />
  <link rel="stylesheet" href="{AGENTS_TEMPLATES_CSS}" />
</head>
<body data-base="../../" data-route="agents" class="int-logo-page">
  <div id="site-nav-root"></div>
  <main class="page-main telephony-page">
    <section class="int-dir-hero">
      <div class="container">
        <span class="page-kicker">Agent template directory</span>
        <h1>Start from a template</h1>
        <p class="int-dir-hero-lead">Fourteen enterprise-ready voice agent templates — pick one to pre-fill your canvas, customize everything after, and deploy on outbound or inbound campaigns.</p>
        <nav class="int-category-nav" aria-label="Template categories">
          {nav_pills}
        </nav>
      </div>
    </section>

    <section id="templates" class="int-category-block">
      <div class="container">
        <header class="int-category-head">
          <h2>All templates</h2>
          <a href="workforce.html">View template library →</a>
        </header>
        <div class="agt-template-groups" aria-label="Agent templates">
{role_sections}
        </div>
      </div>
    </section>

    <section class="tel-hub-cta">
      <div class="container">
        <h2>Deploy your first agent template</h2>
        <p>Hear a live template call and map your first campaign in a tailored demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="../../index.html#agents" class="btn-outline">Back to platform</a>
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
