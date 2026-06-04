from pathlib import Path
import re

t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
for s in ["<!-- CONTACT", 'id="contact"', "#contact", "contact-grid"]:
    print(s, text.find(s))
m = re.search(r"<!-- CONTACT US -->.*?</section>\s*<footer>", text, re.DOTALL)
if m:
    print("len", len(m.group()))
    Path(__file__).parent.joinpath("contact_snippet.txt").write_text(m.group()[:4000], encoding="utf-8")
