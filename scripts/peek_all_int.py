import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")

for layer in ["integration-telephony", "integration-llm", "integration-stt", "integration-tts", "integration-tools"]:
    m = re.search(
        rf'id="{layer}">(.*?)<div class="int-showcase reveal" id="integration-',
        text,
        re.DOTALL,
    )
    if not m and layer == "integration-tools":
        m = re.search(rf'id="{layer}">(.*?)<!-- END INTEGRATIONS', text, re.DOTALL)
    if not m:
        m = re.search(rf'id="{layer}">(.*?)<section', text, re.DOTALL)
    if not m:
        print("MISSING", layer)
        continue
    seg = m.group(1)
    kicker = re.search(r'section-kicker">([^<]+)', seg)
    print("\n===", layer, kicker.group(1) if kicker else "", "===")
    for card in re.finditer(r'data-detail="([^"]+)".*?</article>', seg, re.DOTALL):
        chunk = card.group(0)
        has_img = "<img" in chunk
        has_mark = "brand-mark" in chunk
        title = re.search(r"<h4>([^<]+)</h4>", chunk)
        src = re.search(r'src="([^"]+)"', chunk)
        print(
            card.group(1),
            "|",
            title.group(1) if title else "?",
            "|",
            "img:" + (src.group(1)[:60] if src else "none"),
            "|",
            "mark" if has_mark else "",
        )
