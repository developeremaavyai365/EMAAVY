from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
out = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\scripts\segments_dump.txt")

ids = ["agents", "case-studies", "bento", "journey", "docs"]
lines = []
for sid in ids:
    m = re.search(rf'<section id="{sid}"[^>]*>(.*?)</section>', s, re.DOTALL)
    if m:
        lines.append(f"\n=== {sid} FULL ===\n")
        lines.append(m.group(0))
        lines.append("\n")

out.write_text("".join(lines), encoding="utf-8")
print("ok", out)
