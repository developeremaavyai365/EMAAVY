from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
m = re.search(r'<!-- INTEGRATIONS HUB -->.*?</section>', s, re.DOTALL)
chunk = m.group(0) if m else ""
for pat in ["tel-card", "llm-card", "stt-card", 'class="int-card reveal']:
    i = chunk.find(pat)
    if i >= 0:
        print("===", pat, "===")
        print(chunk[i : i + 450])
        print()
