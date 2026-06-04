from pathlib import Path
import re

t = Path(r"c:\Users\DELL\Desktop\New folder (3)\emaavy\emaavy_white_blue (2).html").read_text(encoding="utf-8")

# snapshots gone
assert 'id="snapshots"' not in t
assert "Live · Processing" not in t
assert "signal-band {" not in t

# cap sections stats close properly
for sid in ["agents", "case-studies", "bento", "journey", "docs", "features"]:
    m = re.search(rf'<section id="{sid}"[^>]*>.*?</section>', t, re.DOTALL)
    if not m:
        print(sid, "MISSING")
        continue
    html = m.group(0)
    if "platform-stats" in html:
        if "</div> </div> </section>" not in html and "</div> </section>" in html:
            # check if missing stats wrapper close
            if html.rstrip().endswith("</div> </section>"):
                pass
            print(sid, "stats close OK" if " </div> </section>" in html[-80:] else "CHECK", html[-60:])

print("ok")
