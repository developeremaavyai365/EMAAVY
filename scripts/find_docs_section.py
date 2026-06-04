from pathlib import Path
import re

t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
for s in ["<!-- DOCS -->", 'id="docs"', "#docs", "docs-quickstart", "Build with EMAAVY"]:
    print(s, text.find(s))

m = re.search(r"<!-- DOCS -->.*?</section>\s*<!--", text, re.DOTALL)
if m:
    print("docs block len", len(m.group()))
    print("ends with", repr(m.group()[-80:]))
else:
    # try without next comment
    m2 = re.search(r'<!-- DOCS -->.*?</section>', text, re.DOTALL)
    print("alt match", len(m2.group()) if m2 else None)
    if m2:
        end = m2.end()
        print("after section:", repr(text[end : end + 80]))
