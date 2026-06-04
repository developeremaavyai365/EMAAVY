from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
sec = re.search(r'id="integrations".*?</section>', s, re.DOTALL).group(0)
bad = ["tel-card", "llm-card", "stt-card", "int-cards-grid", "int-card reveal"]
for b in bad:
    print(b, sec.count(b))
cards = re.findall(r'class="hiw-step reveal click-detail" data-detail="([^"]*)"', sec)
print("cards", len(cards))
# structure check
sample = re.search(r'<article class="hiw-step reveal click-detail"[^>]*>.*?</article>', sec, re.DOTALL)
parts = ["hiw-step-num", "hiw-step-icon", "<h4>", "<p>", "hiw-step-tag", "hiw-step-hint"]
for p in parts:
    print(p, p in (sample.group(0) if sample else ""))
