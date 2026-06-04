from pathlib import Path
import re
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
style_start = text.find("<style>")
style_end = text.rfind("</style>")
style = text[style_start:style_end]
rules = []
for chunk in style.split("}"):
    if ".hero" in chunk or "hero-" in chunk:
        rules.append(chunk.strip() + "}")
out = Path(__file__).resolve().parent / "hero_rules.txt"
out.write_text("\n\n".join(rules), encoding="utf-8")
print(len(rules), "hero rules")
# glow rules in hero context
glows = [r for r in rules if "0 0" in r or "glow" in r.lower() or "gradient" in r.lower() and "hero" in r]
Path(__file__).resolve().parent.joinpath("hero_glows.txt").write_text("\n---\n".join(glows[:50]), encoding="utf-8")
print(len(glows), "glow-ish rules")
# hero html
body = text.find('<section class="hero"')
if body < 0:
    body = text.find('class="hero"')
print("hero html at", body)
if body >= 0:
    Path(__file__).resolve().parent.joinpath("hero_html.txt").write_text(text[body:body+4000], encoding="utf-8")
