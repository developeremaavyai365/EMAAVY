from pathlib import Path
import re

s = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
html = s.read_text(encoding="utf-8")
start = html.find("<!-- INTEGRATIONS HUB -->")
print("start", start)
for needle in ['<section id="pricing"', "<footer class=", "</main>", "<!-- PRICING"]:
    i = html.find(needle, start + 50)
    print(needle, i)
# find section close
m = re.search(r'id="integrations"[^>]*>.*?</section>', html[start:], re.DOTALL)
if m:
    chunk = m.group(0)
    print("section len", len(chunk))
    print("articles", len(re.findall(r"<article", chunk)))
    print("llm-card", chunk.count("llm-card"))
    print("tel-card", chunk.count("tel-card"))
    print("int-card", chunk.count("int-card"))
    idx = chunk.find("<article")
    print("first article", chunk[idx:idx+120])
