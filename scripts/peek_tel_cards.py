import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
cards = re.findall(r'class="int-card tel-card[^"]*"', text)
print("tel-cards", len(cards))
print("has tel-card-head", "tel-card-head" in text)
print("has grid css", "TELEPHONY CARDS" in text)
