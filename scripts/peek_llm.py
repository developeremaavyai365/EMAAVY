import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
m = re.search(
    r'id="integration-llm">(.*?)<div class="int-showcase reveal" id="integration-stt">',
    text,
    re.DOTALL,
)
if m:
    seg = m.group(1)
    print("LEN", len(seg))
    cards = re.findall(r'data-detail="([^"]+)"', seg)
    print("partners", cards)
    cap = re.search(r'int-cap-strip.*', seg)
    print("cap", cap.group(0)[:200] if cap else "none")
