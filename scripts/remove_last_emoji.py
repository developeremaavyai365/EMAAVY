import re
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
t = p.read_text(encoding="utf-8")
em = re.findall(r"[\U0001F300-\U0001FAFF\U00002700-\U000027BF]+", t)
print("before", len(em), [hex(ord(c)) for e in em for c in e][:5])
t = re.sub(r"[\U0001F300-\U0001FAFF\U00002700-\U000027BF]+", "", t)
t = t.replace(
    "logo: '<span style=\"font-size:1.4rem\"></span>'",
    "logo: '<span class=\"detail-brand-mark\">WH</span>'",
)
t = t.replace(
    "logo: '<img src=\"https://cdn.simpleicons.org/elevenlabs/0f172a\" alt=\"Flash Bulbul\" style=\"height:24px\"/>'",
    "logo: '<img src=\"https://cdn.simpleicons.org/elevenlabs/0f172a\" alt=\"Flash Bulbul\" style=\"height:24px\"/>'",
)
# flash might still have emoji in logo field
t = re.sub(
    r"(flash: \{ tag: 'TTS'[^}]*?logo: ')[^']*(')",
    r"\1<img src=\"https://cdn.simpleicons.org/elevenlabs/0f172a\" alt=\"Flash Bulbul\" style=\"height:24px\"/>\2",
    t,
    count=1,
)
p.write_text(t, encoding="utf-8")
em2 = re.findall(r"[\U0001F300-\U0001FAFF\U00002700-\U000027BF]+", t)
print("after", len(em2))
