from pathlib import Path
import re
s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
m = re.search(r'<section id="how-it-works".*?</section>', s, re.DOTALL)
print("blueprint" in m.group(0), "split" in m.group(0), "flow-card" in m.group(0))
print(m.group(0)[:800])
print("...")
print(len(m.group(0)))
