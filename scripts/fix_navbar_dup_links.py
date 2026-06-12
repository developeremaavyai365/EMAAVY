from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BAD = '  <link rel="stylesheet" href="assets/navbar-typography.css" />\n'

for path in ROOT.rglob("*.html"):
    if path.name == "index.html" and path.parent != ROOT:
        text = path.read_text(encoding="utf-8")
        if BAD in text:
            path.write_text(text.replace(BAD, ""), encoding="utf-8")
            print("fixed", path.relative_to(ROOT))
