from pathlib import Path
s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
for term in ["hero-showcase-dot", "hero-showcase-chrome", "hero-showcase-header", "heroVisual"]:
    i = s.find(term)
    print(term, i)
    if i >= 0:
        print(s[i : i + 500])
        print("---")
