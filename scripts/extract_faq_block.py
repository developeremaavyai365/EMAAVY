from pathlib import Path
import re

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
t = text.read_text(encoding="utf-8")
m = re.search(r"<!-- FAQ -->.*?</section>\s*<!-- CTA -->", t, re.DOTALL)
if m:
    block = m.group(0)
    Path(__file__).parent.joinpath("faq_block_snippet.txt").write_text(block[:8000], encoding="utf-8")
    items = re.findall(r'<span class="faq-num">(\d+)</span>([^<]+)<i>', block)
    for num, q in items:
        print(num, q.strip())
