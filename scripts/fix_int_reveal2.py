from pathlib import Path
import re

PATH = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
html = PATH.read_text(encoding="utf-8")
marker = "<!-- INTEGRATIONS HUB -->"
start = html.find(marker)
if start < 0:
    raise SystemExit("integrations marker not found")
m = re.search(
    r"<!-- INTEGRATIONS HUB --> <section id=\"integrations\"[^>]*>.*?</section>",
    html[start:],
    re.DOTALL,
)
if not m:
    raise SystemExit("integrations section not found")
chunk = m.group(0)
before_articles = len(re.findall(r'<article class="int-card reveal', chunk))
chunk2 = re.sub(
    r'<article class="int-card (?!reveal)',
    '<article class="int-card reveal',
    chunk,
)
chunk2 = chunk2.replace('int-card reveal reveal', 'int-card reveal')
chunk2 = chunk2.replace('<div class="call-flow" ', '<div class="call-flow reveal" ')
after_articles = len(re.findall(r'<article class="int-card reveal', chunk2))
html = html[:start] + chunk2 + html[start + len(m.group(0)) :]
PATH.write_text(html, encoding="utf-8")
print("reveal before", before_articles, "after", after_articles, "call-flow", chunk2.count("call-flow reveal"))
