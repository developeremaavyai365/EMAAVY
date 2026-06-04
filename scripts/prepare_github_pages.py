#!/usr/bin/env python3
"""Prepare static site for GitHub Pages (index.html as landing)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANDING = ROOT / "emaavy_white_blue (2).html"
INDEX = ROOT / "index.html"

REPLACEMENTS = [
    ("emaavy_white_blue%20(2).html", "index.html"),
    ("emaavy_white_blue (2).html", "index.html"),
]


def main():
    if not LANDING.exists():
        raise SystemExit(f"Missing landing file: {LANDING}")

    text = LANDING.read_text(encoding="utf-8")
    INDEX.write_text(text, encoding="utf-8")
    print(f"Wrote {INDEX.name} from landing ({len(text)} chars)")

    count = 0
    for path in list(ROOT.rglob("*.html")) + list(ROOT.rglob("*.js")):
        if path.name.startswith(".") or "node_modules" in path.parts:
            continue
        if path.resolve() == LANDING.resolve():
            continue
        raw = path.read_text(encoding="utf-8")
        updated = raw
        for old, new in REPLACEMENTS:
            updated = updated.replace(old, new)
        if updated != raw:
            path.write_text(updated, encoding="utf-8")
            count += 1
            print("patched", path.relative_to(ROOT))

    routes = ROOT / "assets" / "routes.js"
    r = routes.read_text(encoding="utf-8")
    r = r.replace("landingPage: 'emaavy_white_blue (2).html'", "landingPage: 'index.html'")
    r = r.replace("path: 'emaavy_white_blue (2).html#campaigns'", "path: 'index.html#campaigns'")
    routes.write_text(r, encoding="utf-8")
    print("patched assets/routes.js")
    print(f"Done. {count} files updated.")

if __name__ == "__main__":
    main()
