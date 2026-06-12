#!/usr/bin/env python3
"""Generate main integrations directory (logo-first discovery)."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
INT = ROOT / "pages" / "integrations"

sys.path.insert(0, str(SCRIPTS))
from integration_logos import apply_logos_all
from integration_pages_common import render_integrations_index


def _load(name: str, attr: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    partners = getattr(mod, attr)
    apply_logos_all(partners)
    return partners


def main():
    categories = [
        {
            "id": "telephony",
            "title": "Telephony",
            "hub": "telephony.html",
            "label_key": "name",
            "partners": _load("build_telephony_pages", "PARTNERS"),
        },
        {
            "id": "llms",
            "title": "LLMs",
            "hub": "llms.html",
            "label_key": "short",
            "partners": _load("build_llm_pages", "MODELS"),
        },
        {
            "id": "stt",
            "title": "Speech-to-Text",
            "hub": "stt.html",
            "label_key": "short",
            "partners": _load("build_stt_pages", "PROVIDERS"),
        },
        {
            "id": "tts",
            "title": "Text-to-Speech",
            "hub": "tts.html",
            "label_key": "short",
            "partners": _load("build_tts_pages", "PROVIDERS"),
        },
        {
            "id": "tools",
            "title": "Tools & Workflow",
            "hub": "tools.html",
            "label_key": "short",
            "partners": _load("build_tools_pages", "TOOLS"),
        },
    ]
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "index.html").write_text(render_integrations_index(categories), encoding="utf-8")
    total = sum(len(c["partners"]) for c in categories)
    print(f"OK: integrations/index.html — {total} logo tiles across {len(categories)} categories")


if __name__ == "__main__":
    main()
