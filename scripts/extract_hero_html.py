import re
from pathlib import Path
t = Path("index.html").read_text(encoding="utf-8")
# Find hero-showcase block
idx = t.find('class="hero-showcase"')
if idx < 0:
    idx = t.find('id="heroVisual"')
print("start", idx)
if idx > 0:
    snippet = t[idx-200:idx+6000]
    Path("scripts/_hero_showcase_html.txt").write_text(snippet, encoding="utf-8")
    print("written", len(snippet))
