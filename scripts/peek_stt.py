import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
start = text.find('id="integration-stt"')
end = text.find('id="integration-tts"', start)
seg = text[start:end]
print("stt-cards", len(re.findall(r"stt-card", seg)))
print("grids", seg.count('class="int-cards-grid"'))
print("call-flow", "call-flow" in seg)
print("nested?", '<div class="int-cards-grid"><div class="int-cards-grid"' in seg)
