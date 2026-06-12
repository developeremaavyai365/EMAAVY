"""Case study client icons — local SVG assets, consistent rendering."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ICON_DIR = ROOT / "assets" / "logos" / "case-studies"

CASE_STUDY_ICONS: dict[str, dict] = {
    "mudita": {"file": "mudita.svg", "alt": "Warehouse by Mudita"},
    "nextcall": {"file": "nextcall.svg", "alt": "NextCall BPO"},
    "fleetiq": {"file": "fleetiq.svg", "alt": "FleetIQ Logistics"},
}

ICON_SVGS: dict[str, str] = {
    "mudita.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="Warehouse by Mudita">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <path d="M12 32V20l12-8 12 8v12" stroke="#18345d" stroke-width="2" fill="none" stroke-linejoin="round"/>
  <path d="M18 32v-6h12v6" stroke="#4a658b" stroke-width="2" fill="none"/>
  <path d="M22 24h4M24 22v4" stroke="#4a658b" stroke-width="1.6" stroke-linecap="round"/>
</svg>""",
    "nextcall.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="NextCall BPO">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <path d="M16 28c0-5 3-9 8-9s8 4 8 9" stroke="#18345d" stroke-width="2" fill="none"/>
  <path d="M14 30h20" stroke="#4a658b" stroke-width="2" stroke-linecap="round"/>
  <path d="M30 18l4 4-4 4" stroke="#18345d" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="20" cy="24" r="2" fill="#4a658b"/>
</svg>""",
    "fleetiq.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" role="img" aria-label="FleetIQ Logistics">
  <rect width="48" height="48" rx="12" fill="#f1f5f9"/>
  <rect x="10" y="22" width="22" height="10" rx="2" stroke="#18345d" stroke-width="2" fill="none"/>
  <path d="M32 26h6l4 6v6H32V26z" stroke="#18345d" stroke-width="2" fill="none" stroke-linejoin="round"/>
  <circle cx="18" cy="36" r="3" stroke="#4a658b" stroke-width="2" fill="none"/>
  <circle cx="36" cy="36" r="3" stroke="#4a658b" stroke-width="2" fill="none"/>
</svg>""",
}


def ensure_icons() -> None:
    ICON_DIR.mkdir(parents=True, exist_ok=True)
    for filename, svg in ICON_SVGS.items():
        (ICON_DIR / filename).write_text(svg.strip(), encoding="utf-8")


def icon_img(slug: str, *, size: str = "sm", base: str = "../../", alt: str | None = None) -> str:
    entry = CASE_STUDY_ICONS[slug]
    label = alt or entry["alt"]
    path = f"{base}assets/logos/case-studies/{entry['file']}"
    if size == "lg":
        w, h, cls = 64, 64, "int-logo-img int-logo-img--lg int-logo-img--neutral"
    else:
        w, h, cls = 40, 40, "int-logo-img int-logo-img--neutral"
    return (
        f'<img class="{cls}" src="{path}" alt="{label}" '
        f'width="{w}" height="{h}" loading="lazy" decoding="async" />'
    )


def apply_case_study_icons(study: dict, *, base: str = "../../") -> None:
    slug = study["slug"]
    name = study.get("name", slug)
    study["logo_sm"] = icon_img(slug, size="sm", base=base, alt=name)
    study["logo"] = icon_img(slug, size="lg", base=base, alt=name)


def apply_case_study_icons_all(studies: list, *, base: str = "../../") -> None:
    ensure_icons()
    for s in studies:
        apply_case_study_icons(s, base=base)
