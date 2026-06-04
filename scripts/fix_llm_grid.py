"""Fix nested int-cards-grid breaking LLM card layout."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

old = '<div class="int-cards-grid"><div class="int-cards-grid" aria-label="LLM partners">'
new = '<div class="int-cards-grid" aria-label="LLM partners">'
if old not in text:
    print("ERROR: nested grid not found")
else:
    text = text.replace(old, new, 1)
    print("Removed nested grid opener")

# Remove extra closing div before llm-flow (only in LLM section)
pat = re.compile(
    r'(</footer></article>)\s*</div>\s*</div>\s*(<div class="llm-flow")',
)
m = pat.search(text[text.find("integration-llm") :])
if m:
    start = text.find("integration-llm")
    chunk_start = start + m.start()
    chunk_end = start + m.end()
    fixed = m.group(1) + " </div> " + m.group(2)
    text = text[:chunk_start] + fixed + text[chunk_end:]
    print("Removed extra grid closer")
else:
    print("WARN: extra closer pattern not found")

# Safer grid: 3 columns desktop (5 cards = 3+2), not 5 skinny columns
text = text.replace(
    "#integration-llm .int-cards-grid {\n  display: grid !important;\n  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;",
    "#integration-llm .int-cards-grid {\n  display: grid !important;\n  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;",
    1,
)

HTML.write_text(text, encoding="utf-8")
# verify
t2 = HTML.read_text(encoding="utf-8")
seg = t2[t2.find('id="integration-llm"'): t2.find('id="integration-stt"')]
print("grid count after fix:", seg.count('class="int-cards-grid'))
