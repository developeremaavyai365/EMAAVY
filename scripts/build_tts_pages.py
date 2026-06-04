#!/usr/bin/env python3
"""Generate TTS hub + per-provider integration pages."""
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

PROVIDERS = [
    {
        "slug": "elevenlabs",
        "name": "ElevenLabs",
        "short": "ElevenLabs",
        "display": "ElevenTurbo v2",
        "region": "Expressive · Global",
        "tag": "Expressive",
        "featured": True,
        "route": "integration-elevenlabs",
        "logo": '<img src="../../assets/logos/elevenlabs.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/elevenlabs.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "ElevenLabs — EMAAVY",
        "h1": "ElevenTurbo v2",
        "meta": "ElevenLabs and EMAAVY — low-latency expressive voice synthesis for persuasive AI agents on live calls.",
        "lead": "ElevenLabs sets the bar for expressive, human-like TTS — on EMAAVY, ElevenTurbo v2 powers outbound agents that sound warm, credible, and fast enough for real conversation turn-taking.",
        "stats": [("<300ms", "Target latency"), ("Voice clone", "Profiles"), ("Global", "Locales")],
        "about": [
            "ElevenLabs pioneered high-quality neural text-to-speech for creators and enterprises — voice cloning, emotional range, and turbo models optimized for conversational latency. ElevenTurbo v2 targets agents that must sound persuasive, not robotic, on sales and premium support calls.",
            "Teams choose ElevenLabs when brand voice consistency matters globally — the same cloned profile can greet, handle objections, and close without studio re-records between script changes.",
        ],
        "emaavy": [
            ("Per-agent voice profiles", "Assign ElevenLabs voice IDs per campaign, language, or brand line."),
            ("Stage-aware tone", "EMAAVY adjusts stability and style hints for opener vs. close segments."),
            ("Streaming playback", "Audio chunks stream into the call as tokens arrive from the LLM."),
            ("STT + TTS option", "Pair ElevenLabs capture and speech on one key when desired."),
        ],
        "features": [
            ("ElevenTurbo v2", "Low-latency model built for dialogue agents."),
            ("Voice cloning", "Consistent brand voice from short samples."),
            ("Multilingual output", "Serve global programs from one voice platform."),
            ("Emotion & stability", "Fine-tune expressiveness per script type."),
            ("API streaming", "Chunked audio for natural barge-in and overlap."),
            ("Dashboard analytics", "Monitor character usage alongside EMAAVY call KPIs."),
        ],
        "uses": [
            ("Premium outbound", "High-touch sales where voice trust drives conversion."),
            ("English-global support", "Empathetic tone on cancellation saves and VIP care."),
            ("Brand campaigns", "Launches requiring one recognizable voice everywhere."),
        ],
        "setup": [
            ("Add ElevenLabs API key", "Configure in EMAAVY integrations with quota alerts."),
            ("Select voice profile", "Pick cloned or library voice per agent."),
            ("Tune turbo settings", "Set stability and similarity for your vertical."),
            ("Run live call test", "Validate turn latency with your STT + LLM stack."),
        ],
        "hub_desc": "Low-latency expressive synthesis for warm, persuasive outbound and support agents.",
        "hub_points": ["ElevenTurbo v2 for dialogue", "Voice cloning and profiles", "Sub-300ms voice targets"],
        "hub_badge": "Expressive",
    },
    {
        "slug": "flash-bulbul",
        "name": "Flash · Bulbul",
        "short": "Flash · Bulbul",
        "display": "Flash v2 · Bulbul V3",
        "region": "India native · Hinglish",
        "tag": "India native",
        "route": "integration-flash-bulbul",
        "logo": '<img src="../../assets/logos/flash-bulbul.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/flash-bulbul.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Flash · Bulbul — EMAAVY",
        "h1": "Flash v2 · Bulbul V3",
        "meta": "Flash and Bulbul TTS with EMAAVY — native Indian voices, natural Hinglish cadence, and low-latency synthesis for domestic programs.",
        "lead": "Flash v2 and Bulbul V3 are built for how India actually speaks — Hinglish, regional rhythm, and code-switching mid-sentence. EMAAVY routes Indian campaigns to Bulbul when Western TTS sounds foreign on the phone.",
        "stats": [("22+", "Indian contexts"), ("Hinglish", "Native cadence"), ("Fast", "Synthesis")],
        "about": [
            "Flash and Bulbul are native Indian voice models designed for telephony-grade outbound and support — not accented English pasted on Indian scripts. They handle honorifics, city slang, and mixed Hindi-English flows that global engines flatten.",
            "EMAAVY pairs Bulbul with Sarvam STT and Qwen or regional LLMs so listen-and-speak loops stay culturally coherent end to end.",
        ],
        "emaavy": [
            ("Language routing", "Auto-select Bulbul when agent language is Hindi or Hinglish."),
            ("Campaign voice packs", "Pre-approved tones for BPO, fintech, and D2C verticals."),
            ("Latency tier", "Optimized for high-QPS domestic dialers."),
            ("Brand trust", "Voices that sound local increase answer and stay rates."),
        ],
        "features": [
            ("Flash v2", "Fast synthesis for short-turn dialogs."),
            ("Bulbul V3", "Richer expressiveness for longer explanations."),
            ("Hinglish code-switch", "Natural mixed-language delivery."),
            ("Regional nuance", "Cadence tuned for Indian telephony audio."),
            ("Agent personas", "Male/female profiles per campaign type."),
            ("EMAAVY orchestration", "Mix with ElevenLabs on English-only queues."),
        ],
        "uses": [
            ("India outbound", "Sales, verification, and collections in Hinglish."),
            ("Domestic support", "Billing, logistics, and appointment calls."),
            ("Government & PSU", "Citizen outreach in familiar voices."),
        ],
        "setup": [
            ("Enable Bulbul credentials", "Add keys in EMAAVY integrations hub."),
            ("Map agent languages", "Bind Bulbul to Hindi and Hinglish profiles."),
            ("Upload script samples", "QA team approves tone on recorded calls."),
            ("Scale per queue", "Roll out one BPO client at a time."),
        ],
        "hub_desc": "Native Indian models with natural Hinglish cadence for sales and support at scale.",
        "hub_points": ["Flash v2 and Bulbul V3", "Hinglish code-switching", "Built for Indian telephony"],
        "hub_badge": "India native",
    },
]


def provider_nav(current: str) -> str:
    links = []
    for p in PROVIDERS:
        cls = ' class="is-current"' if p["slug"] == current else ""
        links.append(f'<a href="{p["slug"]}.html"{cls}>{p["short"]}</a>')
    links.append('<a href="tts.html">All TTS</a>')
    return "\n          ".join(links)


def render_partner(p: dict) -> str:
    stats = "".join(
        f'<div class="tts-partner-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in p["stats"]
    )
    about = "".join(f"<p>{para}</p>" for para in p["about"])
    benefits = "".join(
        f'<li><div><strong>{t}</strong><span>{d}</span></div></li>'
        for t, d in p["emaavy"]
    )
    features = "".join(
        f'<article class="tts-feature-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in p["features"]
    )
    uses = "".join(
        f'<article class="tts-use-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in p["uses"]
    )
    setup = "".join(
        f'<li><div><strong>{t}</strong><p>{d}</p></div></li>'
        for t, d in p["setup"]
    )

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
  <link rel="stylesheet" href="../../assets/tts-partner.css" />
</head>
<body data-base="../../" data-route="{p['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main tts-partner-page">
    <section class="tts-partner-hero">
      <div class="container tts-partner-hero-grid">
        <div class="tts-partner-hero-copy">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="../../index.html">Home</a>
            <span aria-hidden="true"> / </span>
            <a href="../../index.html#integrations">Integrations</a>
            <span aria-hidden="true"> / </span>
            <a href="tts.html">Text-to-Speech</a>
            <span aria-hidden="true"> / </span>
            <span>{p['short']}</span>
          </nav>
          <span class="tts-partner-kicker">Text-to-Speech · {p['tag']}</span>
          <h1>{p['h1']}</h1>
          <p class="tts-partner-lead">{p['lead']}</p>
          <div class="tts-partner-stats">{stats}</div>
          <div class="tts-partner-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Connect {p['short']}</a>
            <a href="tts.html" class="btn-outline">All TTS engines</a>
          </div>
        </div>
        <aside class="tts-partner-hero-card" aria-label="{p['name']} overview">
          <div class="tts-partner-hero-logo">{p['logo']}</div>
          <span class="tts-partner-hero-region">{p['region']}</span>
          <p>Synthesized live on EMAAVY — tone, pace, and voice profile per agent and campaign.</p>
        </aside>
      </div>
    </section>

    <section class="tts-partner-section">
      <div class="container">
        <header class="tts-partner-section-head">
          <h2>What {p['display']} delivers</h2>
          <p>Why this engine exists and when it wins on live voice programs.</p>
        </header>
        <div class="tts-partner-prose">{about}</div>
      </div>
    </section>

    <section class="tts-partner-section alt">
      <div class="container tts-partner-split">
        <header class="tts-partner-section-head">
          <h2>How EMAAVY uses {p['short']}</h2>
          <p>From LLM script to caller audio — one orchestration layer controls the full voice loop.</p>
        </header>
        <ul class="tts-partner-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="tts-partner-section">
      <div class="container">
        <header class="tts-partner-section-head">
          <h2>Key capabilities</h2>
          <p>What teams configure when {p['display']} powers agent speech on EMAAVY.</p>
        </header>
        <div class="tts-feature-grid">{features}</div>
      </div>
    </section>

    <section class="tts-partner-section alt">
      <div class="container">
        <header class="tts-partner-section-head">
          <h2>Ideal use cases</h2>
          <p>Where {p['short']} and EMAAVY deliver the strongest combined outcomes.</p>
        </header>
        <div class="tts-use-grid">{uses}</div>
      </div>
    </section>

    <section class="tts-partner-section">
      <div class="container">
        <header class="tts-partner-section-head">
          <h2>Getting connected</h2>
          <p>From API credentials to production calls on EMAAVY.</p>
        </header>
        <ol class="tts-setup-steps">{setup}</ol>
      </div>
    </section>

    <section class="tts-partner-section alt">
      <div class="container">
        <header class="tts-partner-section-head">
          <h2>Explore other TTS engines</h2>
          <p>Route English-global programs to ElevenLabs and Indian languages to Flash · Bulbul — same agent platform.</p>
        </header>
        <nav class="tts-partner-nav-strip" aria-label="TTS engines">
          {provider_nav(p['slug'])}
        </nav>
      </div>
    </section>

    <section class="tts-partner-cta">
      <div class="container">
        <h2>Ready to connect {p['short']}?</h2>
        <p>Book a walkthrough — hear live agent voice, compare engines, and map profiles to campaigns.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="tts.html" class="btn-outline">TTS overview</a>
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


def card_html(p: dict) -> str:
    points = "".join(f"<li>{x}</li>" for x in p["hub_points"])
    featured = " tts-model-card--native" if p.get("featured") else ""
    cta = "Explore integration →" if not p.get("featured") else "View full integration →"
    badge = f'<span class="tts-model-badge">{p["hub_badge"]}</span>'
    title = p.get("display", p["name"])
    return f"""          <a href="{p['slug']}.html" id="{p['slug']}" class="tts-model-card{featured}">
            <div class="tts-model-card-top">
              <div class="tts-model-card-logo">{p['logo_sm']}</div>
              {badge}
            </div>
            <h3>{title}</h3>
            <p class="tts-model-card-desc">{p['hub_desc']}</p>
            <ul class="tts-model-card-points">{points}</ul>
            <span class="tts-model-card-cta">{cta}</span>
          </a>"""


def render_hub() -> str:
    cards = "\n".join(card_html(p) for p in PROVIDERS)
    jumps = " ".join(f'<a href="#{p["slug"]}">{p["short"]}</a>' for p in PROVIDERS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Text-to-Speech — EMAAVY</title>
  <meta name="description" content="Natural, empathetic TTS on EMAAVY — ElevenLabs for expressive global voice, Flash · Bulbul for native Indian and Hinglish programs." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Text-to-Speech — EMAAVY" />
  <meta property="og:description" content="Premium TTS engines for live AI voice agents — sub-300ms synthesis with brand-consistent profiles." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/tts-hub.css" />
</head>
<body data-base="../../" data-route="integration-tts">
  <div id="site-nav-root"></div>
  <main class="page-main tts-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../index.html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../index.html#integrations">Integrations</a>
          <span aria-hidden="true"> / </span>
          <span>Text-to-Speech</span>
        </nav>
        <span class="page-kicker">Voice layer · Text-to-Speech</span>
        <h1>Voices that sound human — not robotic</h1>
        <p class="telephony-hero-lead">Natural, empathetic synthesis in every language your customers speak. EMAAVY connects premium TTS engines built for live conversations — where tone, pace, and cultural cadence decide whether callers stay on the line.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>2</b><span>Premium engines</span></div>
          <div class="stat-box"><b>&lt;300ms</b><span>Voice latency</span></div>
          <div class="stat-box"><b>22+</b><span>Languages</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#synthesis-layer">How EMAAVY speaks</a>
          <a href="#providers">TTS engines</a>
          <a href="#pipeline">Voice pipeline</a>
          {jumps}
        </div>
      </div>
    </section>

    <section id="synthesis-layer" class="tts-hub-synthesis">
      <div class="container">
        <article class="tts-hub-synthesis-card">
          <div class="tts-hub-synthesis-meta">
            <span class="tts-hub-synthesis-num">Layer 04</span>
            <span class="tts-hub-synthesis-tag">EMAAVY · Text-to-Speech</span>
            <h2>How EMAAVY delivers agent voice</h2>
            <p class="tts-hub-synthesis-lead">Scripts become speech in milliseconds. Tone adapts per call stage — opener, objection, close — without manual audio editing or post-production.</p>
          </div>
          <div class="tts-hub-pill-grid">
            <div class="tts-hub-pill"><strong>ElevenTurbo v2</strong><span>Expressive global voices for persuasive outbound.</span></div>
            <div class="tts-hub-pill"><strong>Flash · Bulbul</strong><span>Native Indian cadence and Hinglish code-switching.</span></div>
            <div class="tts-hub-pill"><strong>Low latency</strong><span>Sub-300ms targets for natural turn-taking.</span></div>
            <div class="tts-hub-pill"><strong>Voice profiles</strong><span>Per-campaign cloning and persona consistency.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="providers" class="tts-hub-providers page-section alt">
      <div class="container">
        <header class="tts-hub-providers-head">
          <h2>TTS engines</h2>
          <p>Two premium partners today — each with a dedicated page on capabilities, EMAAVY voice routing, and rollout steps.</p>
        </header>
        <div class="tts-model-grid tts-model-grid--duo">
{cards}
        </div>
      </div>
    </section>

    <section id="pipeline" class="tts-hub-flow">
      <div class="container">
        <header class="tts-hub-flow-head">
          <h2>How your agent finds its voice</h2>
          <p>From LLM text to caller audio on every turn — across ElevenLabs and Flash · Bulbul.</p>
        </header>
        <div class="tts-flow-track">
          <article class="tts-flow-step"><strong>Script generated</strong><p>LLM produces the next spoken line for the agent.</p></article>
          <article class="tts-flow-step"><strong>TTS synthesizes</strong><p>EMAAVY calls your engine with tone and pace parameters.</p></article>
          <article class="tts-flow-step"><strong>Tone adjusted</strong><p>Warmth tuned for sales, support, or compliance context.</p></article>
          <article class="tts-flow-step"><strong>Audio streams</strong><p>Speech plays into the live call with minimal gap.</p></article>
        </div>
      </div>
    </section>

    <section class="tts-hub-cta">
      <div class="container">
        <h2>Connect Text-to-Speech to EMAAVY</h2>
        <p>Hear live voice profiles, compare engines, and map TTS routing in a tailored demo.</p>
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
    lines = ["      { id: 'tts', label: 'TTS layer', path: 'pages/integrations/tts.html' },"]
    for p in PROVIDERS:
        label = p["name"]
        lines.append(
            f"      {{ id: '{p['slug']}', label: '{label}', path: 'pages/integrations/{p['slug']}.html' }},"
        )
    block = "    tts: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    tts: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def patch_hub_css():
    path = ROOT / "assets" / "tts-hub.css"
    extra = """
/* Two-engine hub layout */
.tts-model-grid--duo {
  max-width: 820px;
  margin: 0 auto;
  grid-template-columns: repeat(2, 1fr);
}
@media (max-width: 720px) {
  .tts-model-grid--duo {
    grid-template-columns: 1fr;
  }
}
"""
    text = path.read_text(encoding="utf-8")
    if "tts-model-grid--duo" not in text:
        path.write_text(text + extra, encoding="utf-8")


def main():
    INT.mkdir(parents=True, exist_ok=True)
    patch_hub_css()
    (INT / "tts.html").write_text(render_hub(), encoding="utf-8")
    for p in PROVIDERS:
        (INT / f"{p['slug']}.html").write_text(render_partner(p), encoding="utf-8")
    update_routes()
    print(f"OK: TTS hub + {len(PROVIDERS)} engine pages, routes.js updated")


if __name__ == "__main__":
    main()
