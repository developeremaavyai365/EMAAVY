#!/usr/bin/env python3
"""Generate agent template hub + per-template pages from shared catalog."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from agent_logos import apply_template_icons_all
from agent_templates import CATEGORY_ORDER, TEMPLATES, group_by_category, templates_to_roles
from agents_pages_common import ensure_uses, render_agents_index, render_role, render_workforce

ROOT = Path(__file__).resolve().parents[1]
AGENTS = ROOT / "pages" / "agents"

LEGACY_REDIRECTS = {
    "sales-agent": "real-estate.html",
    "support-agent": "support-playbook.html",
    "outbound-agent": "event-agent.html",
    "inbound-agent": "appointment-booking.html",
}

USE_EXTRAS = [
    ("Per-campaign assignment", "Assign the same template to multiple outbound or inbound programs."),
    ("Live supervisor handoff", "Humans join with full transcript when escalation rules fire."),
    ("22 languages", "Regional voices and Hinglish via ElevenLabs and Flash Bulbul."),
]

HUB_CFG = {
    "route": "agents-workforce",
    "title": "AI Agent Templates — EMAAVY",
    "meta": "Fourteen enterprise-ready EMAAVY voice agent templates — sales, support, HR, finance, events, and more. Deploy in 10–12 minutes.",
    "og_title": "AI Agent Templates — EMAAVY",
    "og_description": "Start from a template — real estate, scheduling, NPS, events, recruiting, collections, and support flows pre-built for voice.",
    "breadcrumb": "Agent Templates",
    "kicker": "Agent Templates · Voice AI",
    "h1": "Start from a template",
    "lead": "Fourteen enterprise-ready voice agent templates — pick one to pre-fill your canvas, customize voice and flows, and deploy on outbound or inbound campaigns in as little as 10 minutes.",
    "stats": [("14", "Templates"), ("10–12 min", "Typical setup"), ("22", "Languages")],
    "anchor_jumps": [
        ("workforce-layer", "How templates work"),
        ("templates", "All templates"),
        ("builder", "Custom builder"),
        ("deploy", "Deploy flow"),
    ],
    "layer_id": "workforce-layer",
    "layer_num": "Templates",
    "layer_tag": "EMAAVY · Agent Library",
    "layer_h2": "How EMAAVY agent templates work",
    "layer_lead": "Each template is a production-ready voice flow — prompts, branching, integrations, and disposition logic included. Clone, customize, and assign to campaigns without rebuilding from scratch.",
    "pills": [
        ("Pre-built flows", "Qualification, booking, NPS, events, HR, finance, and support patterns."),
        ("Fast customization", "Edit prompts, voice, language, and triggers in the visual builder."),
        ("Full stack wired", "Telephony, LLM, STT, TTS, CRM, and calendar layers connect once."),
        ("Campaign-ready", "Outbound lists and inbound DIDs go live from the same template."),
    ],
    "roles_id": "templates",
    "roles_h2": "All agent templates",
    "roles_desc_short": "Browse by category — click any template for full specs and setup steps.",
    "builder_h2": "Custom Agent Builder",
    "builder_lead": "Start from any template or a blank canvas — design branching voice flows, pick voices, and deploy across languages without code.",
    "builder_pills": [
        ("Clone any template", "Fork Real Estate, Support Playbook, Event Agent, or any of the 14 presets."),
        ("Sandbox calls", "Simulate conversations before attaching live DIDs or contact lists."),
        ("Version control", "Publish prompt updates without taking agents offline."),
        ("Multi-campaign", "One template definition, unlimited campaign assignments."),
    ],
    "flow_id": "deploy",
    "flow_h2": "From template to live calls",
    "flow_desc": "Typical path from library template to production traffic.",
    "flow_steps": [
        ("Pick a template", "Choose from 14 pre-built flows by category and call type."),
        ("Customize", "Voice, prompts, languages, integrations, and escalation rules."),
        ("Connect stack", "Telephony, LLM, STT, TTS, CRM, and tools in one console."),
        ("Launch", "Outbound campaign or inbound DID — live in 10–12 minutes."),
        ("Optimize", "Transcripts and scores feed coaching and flow improvements."),
    ],
    "cta_h2": "Deploy your first agent template",
    "cta_desc": "Hear a live template call, review scripts, and map your first campaign in a tailored demo.",
}


def builder_tile_html() -> str:
    return """          <a href="workforce.html#builder" class="int-logo-tile" aria-label="Custom Agent Builder">
            <div class="int-logo-tile__logo"><span class="agt-tpl-icon" aria-hidden="true">⚙️</span></div>
            <div class="int-logo-tile__meta">
              <span class="int-logo-tile__name">Custom Agent Builder</span>
              <span class="int-logo-tile__category">Visual flows</span>
            </div>
          </a>"""


def prepare(roles: list) -> None:
    for r in roles:
        ensure_uses(r, USE_EXTRAS)
    apply_template_icons_all(roles)


def _nav_label(name: str, max_len: int = 40) -> str:
    if len(name) <= max_len:
        return name
    return name[: max_len - 1].rstrip() + "…"


def update_routes(roles: list) -> None:
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = [
        "    { id: 'workforce', label: 'Agent Templates', path: 'pages/agents/workforce.html' },",
        "    { id: 'agents-index', label: 'Agent Directory', path: 'pages/agents/index.html' },",
    ]
    for r in roles:
        label = _nav_label(r["name"])
        lines.append(
            f"    {{ id: '{r['slug']}', label: '{label}', path: 'pages/agents/{r['slug']}.html' }},"
        )
    block = "  agents: [\n" + "\n".join(lines) + "\n  ],"
    text = re.sub(r"  agents: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def write_legacy_redirects() -> None:
    """Keep old agent URLs working after the 14-template migration."""
    for slug, target in LEGACY_REDIRECTS.items():
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url={target}" />
  <link rel="canonical" href="{target}" />
  <title>Redirecting to updated agent template…</title>
  <script>location.replace("{target}");</script>
</head>
<body>
  <p>This agent page has moved to our template library.
    <a href="{target}">Continue to the updated template</a> or
    <a href="index.html">browse all templates</a>.</p>
</body>
</html>
"""
        (AGENTS / f"{slug}.html").write_text(html, encoding="utf-8")


def main():
    roles = templates_to_roles()
    prepare(roles)
    AGENTS.mkdir(parents=True, exist_ok=True)
    write_legacy_redirects()
    (AGENTS / "workforce.html").write_text(
        render_workforce(HUB_CFG, roles, grouped=True), encoding="utf-8"
    )
    (AGENTS / "index.html").write_text(
        render_agents_index(roles, builder_tile_html(), grouped=True), encoding="utf-8"
    )
    for r in roles:
        (AGENTS / f"{r['slug']}.html").write_text(
            render_role(
                r,
                roles=roles,
                hub_breadcrumb="Agent Templates",
                hub_label="All templates",
                hub_cta_label="Template library",
            ),
            encoding="utf-8",
        )
    update_routes(roles)
    print(
        f"OK: workforce + index + {len(roles)} template pages "
        f"({len(CATEGORY_ORDER)} categories) + {len(LEGACY_REDIRECTS)} legacy redirects"
    )


if __name__ == "__main__":
    main()
