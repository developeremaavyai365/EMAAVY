from pathlib import Path
import re
t = Path("index.html").read_text(encoding="utf-8")
m = re.search(r'<div class="hero-copy">(.{0,3500})', t, re.DOTALL)
print(m.group(1)[:3500] if m else "not found")
