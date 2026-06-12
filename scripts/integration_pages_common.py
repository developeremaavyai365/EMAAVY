"""Shared integration hub + partner page rendering (telephony-grade treatment)."""
from __future__ import annotations

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

HUB_CSS = "../../assets/telephony-hub.css"
PARTNER_CSS = "../../assets/telephony-partner.css"
LOGO_3D_CSS = "../../assets/integration-logo-3d.css"
SECTION_HEADING_CSS = "../../assets/section-heading.css"
LOGO_3D_JS = "../../assets/integration-logo-3d.js"

BRAND_GLOW: dict[str, str] = {
    "twilio": "#F22F46",
    "exotel": "#E85D24",
    "knowlarity": "#E31937",
    "vobiz": "#4a658b",
    "plivo": "#122B39",
    "vonage": "#000000",
    "telnyx": "#00E3AA",
    "bandwidth": "#0047BB",
    "openai": "#10A37F",
    "claude": "#191919",
    "gemini": "#4285F4",
    "qwen": "#615EFF",
    "grok": "#000000",
    "deepgram": "#13EF93",
    "sarvam": "#4a658b",
    "assemblyai": "#2545D0",
    "azure-stt": "#0078D4",
    "google-stt": "#4285F4",
    "openai-stt": "#10A37F",
    "elevenlabs-stt": "#000000",
    "gladia": "#6366F1",
    "smallest": "#4a658b",
    "elevenlabs": "#000000",
    "flash-bulbul": "#FF6B35",
    "webhooks": "#4a658b",
    "calcom": "#292929",
    "google-calendar": "#4285F4",
    "whatsapp": "#25D366",
    "salesforce": "#00A1E0",
    "hubspot": "#FF7A59",
    "slack": "#4A154B",
}

WORKFLOW_STEPS: dict[str, list[tuple[str, str]]] = {
    "telephony": [
        ("Call connects", "Inbound or outbound session starts on your numbers."),
        ("EMAAVY routes", "Platform selects carrier, media path, and agent profile."),
        ("Provider handles", "Telephony partner delivers PSTN, SIP, or CPaaS voice."),
        ("Audio streams", "Live media feeds STT and reasoning pipelines."),
        ("Agent engages", "AI agent speaks and acts on real-time intelligence."),
    ],
    "llm": [
        ("Transcript arrives", "Speech becomes text in the reasoning layer."),
        ("EMAAVY routes", "Model picked by intent, language, and campaign rules."),
        ("LLM responds", "Provider returns structured reply and extractions."),
        ("Actions trigger", "CRM, tools, and agent script update mid-call."),
        ("Voice continues", "TTS delivers the model-backed next turn."),
    ],
    "stt": [
        ("Audio captured", "Live call media enters the transcription layer."),
        ("EMAAVY routes", "STT engine selected by language and latency tier."),
        ("Provider transcribes", "Words stream with sub-second turnaround."),
        ("Intent parsed", "LLM scores buyer signals from transcript."),
        ("Automations fire", "Coaching, CRM, and webhooks react in real time."),
    ],
    "tts": [
        ("Script ready", "LLM produces the next spoken agent line."),
        ("EMAAVY routes", "TTS engine chosen by language and voice profile."),
        ("Provider synthesizes", "Audio generated with tone and pace parameters."),
        ("Stream plays", "Speech delivered into the live call path."),
        ("Conversation continues", "Caller hears natural, on-brand voice."),
    ],
    "tools": [
        ("Call event", "Live or completed call triggers EMAAVY rules."),
        ("EMAAVY evaluates", "Intent, keywords, and scores match automations."),
        ("Tool invoked", "CRM, calendar, or messaging API is called."),
        ("Record syncs", "Contacts, tasks, and deals update automatically."),
        ("Team notified", "Slack, WhatsApp, or webhooks confirm completion."),
    ],
}


def brand_glow(slug: str) -> str:
    return BRAND_GLOW.get(slug, "#4a658b")


def ensure_uses(partner: dict, extras: list[tuple[str, str]], minimum: int = 6) -> None:
    """Pad use cases to enterprise page standard without duplicating titles."""
    uses = list(partner.get("uses", []))
    seen = {t for t, _ in uses}
    for title, desc in extras:
        if len(uses) >= minimum:
            break
        if title not in seen:
            uses.append((title, desc))
            seen.add(title)
    partner["uses"] = uses


def cap_initials(title: str) -> str:
    words = [w for w in title.replace("&", " ").split() if w]
    if len(words) >= 2:
        return (words[0][0] + words[1][0]).upper()
    return title[:2].upper()


def partner_nav(
    partners: list,
    current_slug: str,
    hub_file: str,
    hub_link: str,
    label_key: str = "name",
) -> str:
    links = []
    for p in partners:
        cls = ' class="is-current"' if p["slug"] == current_slug else ""
        label = p.get(label_key, p["name"])
        links.append(f'<a href="{p["slug"]}.html"{cls}>{label}</a>')
    links.append(f'<a href="{hub_file}">{hub_link}</a>')
    return "\n          ".join(links)


def logo_tile_html(
    p: dict,
    *,
    label_key: str = "name",
    compact: bool = False,
    category: str | None = None,
    aria_suffix: str = "integration",
    href: str | None = None,
) -> str:
    label = p.get(label_key, p["name"])
    cat = category or p.get("hub_badge") or p.get("region") or ""
    cat_html = f'<span class="int-logo-tile__category">{cat}</span>' if cat else ""
    compact_cls = " int-logo-tile--compact" if compact else ""
    aria = f"{label} {aria_suffix}".strip()
    link = href or f"{p['slug']}.html"
    return f"""          <a href="{link}" id="{p['slug']}" class="int-logo-tile{compact_cls}" aria-label="{aria}">
            <div class="int-logo-tile__logo">{p['logo_sm']}</div>
            <div class="int-logo-tile__meta">
              <span class="int-logo-tile__name">{label}</span>
              {cat_html}
            </div>
          </a>"""


def card_html(p: dict, label_key: str = "name") -> str:
    return logo_tile_html(p, label_key=label_key)


def logo_hero_html(p: dict, display: str) -> str:
    return f"""        <aside class="tel-partner-hero-card int-logo-hero-wrap" aria-label="{display} logo">
          <div class="int-logo-hero-panel">{p['logo']}</div>
          <span class="tel-partner-hero-region">{p['region']}</span>
        </aside>"""


def workflow_viz_html(steps: list[tuple[str, str]]) -> str:
    items = "".join(
        f'<article class="tel-workflow-viz__step"><span class="tel-workflow-viz__icon" aria-hidden="true">{i:02d}</span><h3>{t}</h3><p>{d}</p></article>'
        for i, (t, d) in enumerate(steps, 1)
    )
    return f'<div class="tel-workflow-viz__track">{items}</div>'


def setup_grid_html(steps: list[tuple[str, str]]) -> str:
    items = "".join(
        f'<article class="tel-setup-step"><span class="tel-setup-label">{t}</span><p>{d}</p></article>'
        for t, d in steps
    )
    return f'<div class="tel-setup-grid">{items}</div>'


def explore_logos_html(
    partners: list,
    current_slug: str,
    label_key: str = "name",
) -> str:
    tiles = []
    for p in partners:
        if p["slug"] == current_slug:
            continue
        tiles.append(logo_tile_html(p, label_key=label_key, compact=True, category=p.get("hub_badge") or p.get("region")))
    return "\n".join(tiles)


def render_partner(
    p: dict,
    *,
    segment_kicker: str,
    hub_file: str,
    hub_label: str,
    hub_breadcrumb: str,
    partners: list,
    route: str | None = None,
    nav_label_key: str = "name",
    connect_name_key: str = "name",
    explore_title: str = "Explore other partners",
    explore_desc: str = "EMAAVY unifies every partner below — mix providers by campaign without rebuilding agents.",
    nav_aria: str = "Integration partners",
    overview_fit: str = "your stack",
    cta_desc: str = "Book a walkthrough — we will map configuration, routing, and your first live workflow.",
    hub_overview_label: str = "overview",
    hub_cta_label: str = "Segment overview",
    aside_note: str = "Integrated with EMAAVY voice agents, campaigns, and live call intelligence.",
    segment_type: str = "tools",
    hub_label_key: str = "name",
) -> str:
    display = p.get(connect_name_key, p["name"])
    stats = "".join(
        f'<div class="tel-partner-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in p["stats"]
    )
    about = "".join(f"<p>{para}</p>" for para in p["about"])
    benefits = "".join(
        f'<li><div><span class="tel-why-title">{t}</span><span class="tel-why-desc">{d}</span></div></li>'
        for t, d in p["emaavy"]
    )
    features = "".join(
        f'<article class="tel-feature-card"><span class="tel-cap-icon" aria-hidden="true">{cap_initials(t)}</span><h3>{t}</h3><p>{d}</p></article>'
        for t, d in p["features"]
    )
    uses = "".join(
        f'<article class="tel-use-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in p["uses"]
    )
    workflow_steps = p.get("workflow", WORKFLOW_STEPS.get(segment_type, WORKFLOW_STEPS["tools"]))
    workflow = workflow_viz_html(workflow_steps)
    setup = setup_grid_html(p["setup"])
    explore = explore_logos_html(partners, p["slug"], label_key=hub_label_key)
    hero_logo = logo_hero_html(p, display)
    route_id = route or f"integration-{p['slug']}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['title']}</title>
  <meta name="description" content="{p['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{p['title']}" />
  <meta property="og:description" content="{p['meta']}" />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="{PARTNER_CSS}" />
  <link rel="stylesheet" href="{LOGO_3D_CSS}" />
  <link rel="stylesheet" href="{SECTION_HEADING_CSS}" />
</head>
<body data-base="../../" data-route="{route_id}">
  <div id="site-nav-root"></div>
  <main class="page-main tel-partner-page">
    <section class="tel-partner-hero">
      <div class="container tel-partner-hero-grid">
        <div class="tel-partner-hero-copy">
          <span class="tel-partner-kicker">{segment_kicker}</span>
          <h1>{p['h1']}</h1>
          <p class="tel-partner-lead">{p['lead']}</p>
          <div class="tel-partner-stats">{stats}</div>
          <div class="tel-partner-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Connect {display}</a>
            <a href="{hub_file}" class="btn-outline">{hub_label}</a>
          </div>
        </div>
{hero_logo}
      </div>
    </section>

    <section id="overview" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Overview</h2>
          <p>What {display} provides and how it fits into {overview_fit}.</p>
        </header>
        <div class="tel-partner-prose">{about}</div>
      </div>
    </section>

    <section id="capabilities" class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Key capabilities</h2>
          <p>Core features teams configure when {display} powers EMAAVY programs.</p>
        </header>
        <div class="tel-feature-grid">{features}</div>
      </div>
    </section>

    <section id="use-cases" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Business use cases</h2>
          <p>Real-world applications for {display} with EMAAVY agents and campaigns.</p>
        </header>
        <div class="tel-use-grid">{uses}</div>
      </div>
    </section>

    <section id="integration-workflow" class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Integration workflow</h2>
          <p>How {display} connects through EMAAVY — from live events to automated outcomes.</p>
        </header>
        {workflow}
      </div>
    </section>

    <section id="setup-process" class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Setup process</h2>
          <p>Connection steps to go from credentials to production traffic with {display}.</p>
        </header>
        {setup}
      </div>
    </section>

    <section id="business-benefits" class="tel-partner-section alt">
      <div class="container tel-partner-split">
        <header class="tel-partner-section-head">
          <h2>Business benefits</h2>
          <p>Efficiency, automation, scalability, and customer experience gains from connecting {display} to EMAAVY.</p>
        </header>
        <ul class="tel-partner-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>{explore_title}</h2>
          <p>{explore_desc}</p>
        </header>
        <nav class="int-logo-ecosystem int-logo-ecosystem--compact" aria-label="{nav_aria}">
{explore}
        </nav>
      </div>
    </section>

    <section class="tel-partner-cta">
      <div class="container">
        <h2>Ready to connect {display}?</h2>
        <p>{cta_desc}</p>
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


def render_hub(
    cfg: dict,
    partners: list,
    jump_label_key: str = "name",
    hub_tile_label_key: str = "name",
) -> str:
    cards = "\n".join(logo_tile_html(p, label_key=hub_tile_label_key) for p in partners)
    extra_jumps = " ".join(
        f'<a href="#{p["slug"]}">{p.get(jump_label_key, p["name"])}</a>' for p in partners
    )
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
</head>
<body data-base="../../" data-route="{cfg['route']}" class="int-logo-page">
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

    <section id="{cfg['partners_id']}" class="tel-hub-partners tel-hub-partners--logos page-section alt">
      <div class="container">
        <header class="tel-hub-partners-head">
          <h2>{cfg['partners_h2']}</h2>
          <p>{cfg.get('partners_desc_short', 'Click a logo to open the integration page.')}</p>
        </header>
        <nav class="int-logo-ecosystem" aria-label="{cfg['partners_h2']}">
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


def render_integrations_index(categories: list[dict]) -> str:
    """Main integrations directory — logo-first discovery by category."""
    nav_pills = "".join(
        f'<a href="#{c["id"]}" class="int-category-pill">{c["title"]}</a>'
        for c in categories
    )
    sections = []
    for i, cat in enumerate(categories):
        alt = " alt" if i % 2 else ""
        tiles = "\n".join(
            logo_tile_html(
                p,
                label_key=cat.get("label_key", "name"),
                category=cat["title"],
            )
            for p in cat["partners"]
        )
        sections.append(f"""    <section id="{cat['id']}" class="int-category-block{alt}">
      <div class="container">
        <header class="int-category-head">
          <h2>{cat['title']}</h2>
          <a href="{cat['hub']}">View {cat['title'].lower()} layer →</a>
        </header>
        <nav class="int-logo-ecosystem" aria-label="{cat['title']} integrations">
{tiles}
        </nav>
      </div>
    </section>""")
    body_sections = "\n".join(sections)
    total = sum(len(c["partners"]) for c in categories)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Integrations — EMAAVY</title>
  <meta name="description" content="Discover {total}+ EMAAVY integrations — telephony, LLMs, speech, voice, and workflow tools through premium interactive brand logos." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Integrations — EMAAVY" />
  <meta property="og:description" content="Explore EMAAVY's full integration ecosystem — click any logo to open the provider page." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="{HUB_CSS}" />
  <link rel="stylesheet" href="{LOGO_3D_CSS}" />
  <link rel="stylesheet" href="{SECTION_HEADING_CSS}" />
</head>
<body data-base="../../" data-route="integrations" class="int-logo-page">
  <div id="site-nav-root"></div>
  <main class="page-main telephony-page">
    <section class="int-dir-hero">
      <div class="container">
        <span class="page-kicker">Integrations directory</span>
        <h1>Your entire AI stack — connected</h1>
        <p class="int-dir-hero-lead">Browse every partner in a clean, organized directory. Select a category, click an integration, and open the full provider page.</p>
        <nav class="int-category-nav" aria-label="Integration categories">
          {nav_pills}
        </nav>
      </div>
    </section>
{body_sections}
    <section class="tel-hub-cta">
      <div class="container">
        <h2>Ready to connect your stack?</h2>
        <p>Book a walkthrough — we will map providers, routing, and your first live workflow.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="../../index.html#integrations" class="btn-outline">Back to platform</a>
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
