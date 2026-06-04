from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
t = p.read_text(encoding="utf-8")

for sid in ["agents", "case-studies", "bento", "journey", "docs"]:
    m = re.search(rf'<section id="{sid}"[^>]*>.*?</section>', t, re.DOTALL)
    if not m:
        continue
    html = m.group(0)
    if "platform-stats" not in html:
        continue
    if "</div> </div> </section>" in html[-120:]:
        print(sid, "ok")
        continue
    new = re.sub(r"</div>\s*</section>\s*$", "</div> </div> </section>", html)
    t = t[: m.start()] + new + t[m.end() :]
    print(sid, "fixed")

p.write_text(t, encoding="utf-8")
