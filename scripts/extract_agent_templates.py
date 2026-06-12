"""One-off: build agent_templates.py from build_agt_showcase.py TEMPLATES block."""
import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "scripts" / "build_agt_showcase.py"
OUT = ROOT / "scripts" / "agent_templates.py"

text = SRC.read_text(encoding="utf-8")
mod = ast.parse(text)
templates_src = None
for node in mod.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "TEMPLATES":
                templates_src = ast.get_source_segment(text, node.value)
                break

header = '''"""Shared EMAAVY agent template catalog (homepage showcase + subpages)."""
from __future__ import annotations

CATEGORY_ORDER = [
    "Sales", "Scheduling", "Feedback", "Events", "HR", "Finance", "Support", "Retention",
]


def slugify_category(cat: str) -> str:
    return cat.lower().replace(" & ", "-").replace(" ", "-")


def _benefit_title(point: str) -> str:
    clean = point.strip()
    chunk = clean.split(",")[0].split("—")[0].strip()
    return chunk if len(chunk) <= 42 else " ".join(clean.split()[:4]).rstrip(",.")


def template_to_role(t: dict) -> dict:
    slug = t["id"]
    workflow = [
        (step, f"The agent executes the {step.lower()} stage of this template flow.")
        for step in t["flow"]
    ]
    workflow.append(("Sync and log", "Outcomes, scores, and CRM fields update automatically after the call."))
    features = [(o, o) for o in t["outcomes"]]
    for p in t["points"][:2]:
        features.append((_benefit_title(p), p))
    return {
        "slug": slug,
        "name": t["title"],
        "short": t["category"],
        "region": f"{t['category']} · {t['mode']}",
        "tag": f"{t['mode']} · {t['duration']}",
        "route": f"agent-{slug}",
        "icon": t["icon"],
        "duration": t["duration"],
        "mode": t["mode"],
        "category": t["category"],
        "title": f"{t['title']} — EMAAVY",
        "h1": t["title"],
        "meta": f"Deploy the EMAAVY {t['title']} voice agent template — {t['short']}",
        "lead": t["desc"],
        "stats": [(t["duration"], "Setup time"), (t["mode"], "Call type"), (t["category"], "Category")],
        "about": [t["desc"], t["detail"]],
        "emaavy": [(_benefit_title(p), p) for p in t["points"]],
        "features": features[:6],
        "uses": [(u, f"Run this template for {u.lower()} use cases.") for u in t["usecases"]],
        "setup": [
            ("Select template", f"Choose {t['title']} from the EMAAVY agent library."),
            ("Customize flow", "Adjust prompts, voice, language, and branching rules."),
            ("Connect stack", "Wire telephony, LLM, STT, TTS, CRM, and calendar integrations."),
            ("Launch", f"Go live on a campaign or DID — typically ready in {t['duration']}."),
        ],
        "workflow": workflow,
        "hub_desc": t["short"],
        "hub_points": t["points"],
        "hub_badge": f"{t['duration']} · {t['mode']}",
    }


def templates_to_roles(templates=None) -> list[dict]:
    return [template_to_role(t) for t in (templates or TEMPLATES)]


def group_by_category(roles: list[dict]) -> list[tuple[str, list[dict]]]:
    buckets: dict[str, list[dict]] = {c: [] for c in CATEGORY_ORDER}
    for r in roles:
        buckets.setdefault(r.get("category", "Templates"), []).append(r)
    return [(c, buckets[c]) for c in CATEGORY_ORDER if buckets.get(c)]


'''

OUT.write_text(header + "TEMPLATES = " + templates_src + "\n", encoding="utf-8")
print("Wrote", OUT)
