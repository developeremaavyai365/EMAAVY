from pathlib import Path
import re
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
# extract nav-related rules
keywords = ["masthead", "nav-dropdown", "nav-integrations", "btn-nav", "site-nav", "site-header", "masthead-go", "masthead-login"]
style_start = text.find("<style>")
style_end = text.rfind("</style>")
style = text[style_start:style_end]
# split by } and filter
rules = []
for chunk in style.split("}"):
    if any(k in chunk for k in keywords):
        rules.append(chunk.strip() + "}")
out = Path(__file__).resolve().parent / "nav_all_rules.txt"
out.write_text("\n\n".join(rules), encoding="utf-8")
print(len(rules), "rules")
