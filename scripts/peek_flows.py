import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
for name in ["call-flow", "llm-flow"]:
    m = re.search(rf'<div class="{name}"[^>]*>.*?</div></div></div>\s*<div class="int-showcase', text)
    if not m:
        m = re.search(rf'<div class="{name}"[^>]*>.*?</ol></div>', text)
    if m:
        print("===", name, "===")
        print(m.group(0)[:900])
        print()
