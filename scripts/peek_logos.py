import re
from pathlib import Path

t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
for pid in ["plivo", "telnyx", "twilio"]:
    m = re.search(rf'data-detail="{pid}"[^>]*>.*?</article>', text)
    print("CARD", pid, ":", m.group(0)[:350] if m else "NOT FOUND")
    dm = re.search(rf"{pid}:\s*\{{[^}}]+\}}", text)
    print("DATA", pid, ":", dm.group(0)[:500] if dm else "NOT FOUND")
    print()
