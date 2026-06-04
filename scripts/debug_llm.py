import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
m = re.search(
    r'id="integration-llm">(.*?)id="integration-stt"',
    text,
    re.DOTALL,
)
if m:
    seg = m.group(1)
    print("segment length", len(seg))
    # check grid
    g = re.search(r'int-cards-grid"[^>]*>(.*?)</div>\s*<div class="llm-flow"', seg, re.DOTALL)
    if g:
        print("grid inner len", len(g.group(1)))
        print("articles", len(re.findall(r"<article", g.group(1))))
    else:
        print("grid not closed properly")
        print(seg[-800:])
    # div balance in segment
    opens = seg.count("<div")
    closes = seg.count("</div>")
    print("div opens", opens, "closes", closes)
