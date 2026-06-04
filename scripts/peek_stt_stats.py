import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
m = re.search(r'id="integration-stt">(.*?)id="integration-tts"', text, re.DOTALL)
seg = m.group(1)
stats = re.findall(r'int-stat[^>]*>.*?</div>', seg)
for s in stats[:5]:
    print(re.sub(r'\s+', ' ', s)[:120])
