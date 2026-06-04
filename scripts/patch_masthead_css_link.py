from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSERT = '<link rel="stylesheet" href="{base}assets/masthead-flex.css" />\n'

for html in ROOT.rglob("*.html"):
    if "emaavy_white_blue" in html.name:
        continue
    text = html.read_text(encoding="utf-8")
    if "masthead-flex.css" in text:
        continue
    rel = html.parent.relative_to(ROOT)
    depth = len(rel.parts)
    base = "../" * depth if depth else ""
    needle = f'<link rel="stylesheet" href="{base}assets/nav.css" />'
    if needle not in text:
        continue
    text = text.replace(needle, needle + "\n" + INSERT.format(base=base), 1)
    html.write_text(text, encoding="utf-8")
    print("patched", html.relative_to(ROOT))
