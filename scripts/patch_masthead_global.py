from pathlib import Path

p = Path(__file__).resolve().parent.parent / "assets" / "masthead-flex.css"
text = p.read_text(encoding="utf-8")
text = text.replace(
    "/**\n * Home landing masthead — single aligned bar, scroll-compact, CTAs always visible.",
    "/**\n * EMAAVY masthead — same bar on landing and all subpages.",
)
text = text.replace("body[data-page=\"home\"] {", "body {", 1)
keep_home = (
    ".hero",
    "#how-it-works",
    "#integrations",
    "#agents",
    "#campaigns",
    "#features",
    "#case-studies",
    "#journey",
    "#faq",
    "#book-demo",
    ".hub-zone",
)
lines = []
for line in text.splitlines():
    if "body[data-page=\"home\"]" in line and not any(k in line for k in keep_home):
        line = line.replace("body[data-page=\"home\"]", "body")
    lines.append(line)
p.write_text("\n".join(lines) + "\n", encoding="utf-8")
left = sum(1 for l in lines if "body[data-page=\"home\"]" in l)
print(f"Patched masthead-flex.css ({left} home-only rules kept)")
