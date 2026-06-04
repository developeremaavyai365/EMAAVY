import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
for m in re.finditer(r'int-cap-strip.*?</div>\s*</div>\s*</div>\s*<div class="int-showcase', text):
    print(m.group(0)[:500])
    print("---")
