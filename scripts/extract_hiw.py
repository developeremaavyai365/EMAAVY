from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
m = re.search(r'<section id="how-it-works"[^>]*>.*?</section>', s, re.DOTALL)
if m:
    Path(__file__).parent.joinpath("hiw_section.txt").write_text(m.group(0), encoding="utf-8")
    print("len", len(m.group(0)))
