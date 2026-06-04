from pathlib import Path
import re
t = Path("emaavy_white_blue (2).html").read_text(encoding="utf-8")
m = re.search(r'<section class="hero"[^>]*>.*?</section>', t, re.DOTALL)
print(m.group(0) if m else "not found")
