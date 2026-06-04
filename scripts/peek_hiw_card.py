from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
m = re.search(r'class="hiw-step reveal click-detail"[^>]*>.*?</article>', s)
print(m.group(0)[:500] if m else "none")
m2 = re.search(r'id="how-it-works".*?class="hiw-step reveal', s, re.DOTALL)
if m2:
    i = s.find('class="hiw-step reveal', m2.start())
    print("--- HIW ---")
    print(s[i : i + 400])
