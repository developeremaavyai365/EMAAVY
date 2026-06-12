"""Agent role mission icons — local SVG assets, consistent rendering."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ICON_DIR = ROOT / "assets" / "logos" / "agents"

AGENT_ICONS: dict[str, dict] = {
    "sales-agent": {"file": "sales-agent.svg", "alt": "Sales Agent"},
    "support-agent": {"file": "support-agent.svg", "alt": "Support Agent"},
    "outbound-agent": {"file": "outbound-agent.svg", "alt": "Outbound Agent"},
    "inbound-agent": {"file": "inbound-agent.svg", "alt": "Inbound Agent"},
    "custom-builder": {"file": "custom-builder.svg", "alt": "Custom Agent Builder"},
}

ICON_SVGS: dict[str, str] = {
    "sales-agent.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Sales Agent">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <path d="M14 32V18l10-6 10 6v14" stroke="#18345d" stroke-width="2" fill="none" stroke-linejoin="round"/>
  <path d="M20 32v-8h8v8" stroke="#4a658b" stroke-width="2" fill="none"/>
  <circle cx="24" cy="22" r="3" fill="#4a658b"/>
</svg>""",
    "support-agent.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Support Agent">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <path d="M14 26c0-6 4-10 10-10s10 4 10 10v4H14v-4z" stroke="#18345d" stroke-width="2" fill="none"/>
  <path d="M18 34h12" stroke="#4a658b" stroke-width="2" stroke-linecap="round"/>
  <path d="M20 30h8" stroke="#4a658b" stroke-width="2" stroke-linecap="round"/>
</svg>""",
    "outbound-agent.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Outbound Agent">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <path d="M16 24h16M28 18l6 6-6 6" stroke="#18345d" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="14" cy="24" r="4" stroke="#4a658b" stroke-width="2" fill="none"/>
</svg>""",
    "inbound-agent.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Inbound Agent">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <path d="M32 24H16M20 18l-6 6 6 6" stroke="#18345d" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="34" cy="24" r="4" stroke="#4a658b" stroke-width="2" fill="none"/>
</svg>""",
    "custom-builder.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Custom Agent Builder">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <rect x="12" y="14" width="10" height="8" rx="2" stroke="#18345d" stroke-width="1.8" fill="none"/>
  <rect x="26" y="14" width="10" height="8" rx="2" stroke="#18345d" stroke-width="1.8" fill="none"/>
  <rect x="19" y="28" width="10" height="8" rx="2" stroke="#4a658b" stroke-width="1.8" fill="none"/>
  <path d="M17 22v3h6M31 22v3h-6M24 25v3" stroke="#4a658b" stroke-width="1.6" fill="none"/>
</svg>""",
}


def ensure_icons() -> None:
    ICON_DIR.mkdir(parents=True, exist_ok=True)
    for filename, svg in ICON_SVGS.items():
        (ICON_DIR / filename).write_text(svg.strip(), encoding="utf-8")


def icon_path(slug: str) -> str:
    entry = AGENT_ICONS[slug]
    return f"../../assets/logos/agents/{entry['file']}"


def icon_img(slug: str, *, size: str = "sm", alt: str | None = None) -> str:
    entry = AGENT_ICONS[slug]
    label = alt or entry["alt"]
    path = icon_path(slug)
    if size == "lg":
        w, h, cls = 64, 64, "int-logo-img int-logo-img--lg int-logo-img--neutral"
    else:
        w, h, cls = 40, 40, "int-logo-img int-logo-img--neutral"
    return (
        f'<img class="{cls}" src="{path}" alt="{label}" '
        f'width="{w}" height="{h}" loading="lazy" decoding="async" />'
    )


def apply_agent_icons(role: dict) -> None:
    slug = role["slug"]
    name = role.get("name", slug)
    role["logo_sm"] = icon_img(slug, size="sm", alt=name)
    role["logo"] = icon_img(slug, size="lg", alt=name)


def apply_agent_icons_all(roles: list) -> None:
    ensure_icons()
    for r in roles:
        apply_agent_icons(r)


def template_icon_html(icon: str, *, size: str = "sm", alt: str = "") -> str:
    cls = "agt-tpl-icon agt-tpl-icon--lg" if size == "lg" else "agt-tpl-icon"
    label = f' aria-label="{alt}"' if alt else ' aria-hidden="true"'
    return f"<span class=\"{cls}\"{label}>{icon}</span>"


def apply_template_icons(role: dict) -> None:
    icon = role.get("icon", "🤖")
    name = role.get("name", role.get("slug", "Agent"))
    role["logo_sm"] = template_icon_html(icon, size="sm")
    role["logo"] = template_icon_html(icon, size="lg", alt=name)


def apply_template_icons_all(roles: list) -> None:
    for r in roles:
        apply_template_icons(r)
