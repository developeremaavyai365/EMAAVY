from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
sec = re.search(r'<section id="features"[^>]*>.*?</section>', s, re.DOTALL)
print("feature-card in sec", "feature-card" in sec.group(0))
print("hiw-step in sec", sec.group(0).count("hiw-step"))
print("hiw-steps", "hiw-steps" in sec.group(0))
print("abbrev RT", "content: 'RT'" in s)
m = re.search(r'<article class="hiw-step reveal click-detail" data-detail="feat-[^"]*"[^>]*>.*?</article>', sec.group(0), re.DOTALL)
if m:
    Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\scripts\feat_sample.txt").write_text(m.group(0), encoding="utf-8")
    print("sample written")
