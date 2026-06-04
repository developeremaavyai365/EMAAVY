import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")

# TTS section
m = re.search(
    r'id="integration-tts">(.*?)<div class="int-showcase reveal" id="integration-tools">',
    text,
    re.DOTALL,
)
if m:
    seg = m.group(1)
    print("TTS SEGMENT LENGTH", len(seg))
    for card in re.finditer(r'data-detail="([^"]+)".*?</article>', seg, re.DOTALL):
        chunk = card.group(0)
        logo = re.search(r'int-card-logo">(.*?)</div>', chunk, re.DOTALL)
        title = re.search(r"<h4>([^<]+)</h4>", chunk)
        print(card.group(1), "|", title.group(1) if title else "?", "|", (logo.group(1)[:120] if logo else "?"))

# detailData voice/tts keys
for key in ["flash", "elevenlabs", "sarvam", "bulbul"]:
    dm = re.search(rf"{key}:\s*\{{[^}}]+logo:[^,]+,", text)
    if dm:
        print("DATA", key, dm.group(0)[:200])
