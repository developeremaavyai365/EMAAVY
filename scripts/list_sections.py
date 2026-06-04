from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
for m in re.finditer(r'<section[^>]*id="([^"]+)"', s):
    print("section:", m.group(1))
print("--- kickers ---")
for m in re.finditer(r'<span class="section-kicker">([^<]+)</span>', s):
    print("kicker:", m.group(1).strip())
