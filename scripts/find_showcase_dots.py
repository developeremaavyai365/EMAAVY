from pathlib import Path
s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
for term in [
    "hero-showcase-chrome",
    'class="hero-showcase-dot"',
    "hero-showcase-dot {",
    "hero-showcase-dot:nth",
]:
    idx = 0
    hits = []
    while True:
        i = s.find(term, idx)
        if i < 0:
            break
        hits.append(i)
        idx = i + 1
    print(term, len(hits), hits[:5])
