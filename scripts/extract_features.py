from pathlib import Path
import re
text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
t = text.read_text(encoding="utf-8")
chunk = t.split("<!-- FEATURES -->")[1].split("<!-- INTEGRATIONS")[0]
for art in re.findall(r"<article[^>]+>(.*?)</article>", chunk, re.S):
    h4 = re.search(r"<h4>([^<]+)</h4>", art)
    p = re.search(r"<h4>[^<]+</h4><p>([^<]+)</p>", art)
    tag = re.search(r'hiw-step-tag">([^<]*)</span>', art)
    if h4:
        print(h4.group(1))
        print(" ", p.group(1) if p else "")
        print(" ", tag.group(1) if tag else "")
        print()
