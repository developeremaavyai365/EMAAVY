from pathlib import Path
import re

s = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")
for sid in ["agents", "case-studies", "bento", "journey", "docs"]:
    m = re.search(rf'<section id="{sid}"[^>]*>(.*?)</section>', s, re.DOTALL)
    body = m.group(0) if m else "MISSING"
    ok = "cap-section" in body and "hiw-steps" in body and "int-showcase" not in body
    print(sid, "OK" if ok else "FAIL", "cap-section" in body, "hiw-steps" in body)
