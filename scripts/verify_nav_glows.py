from pathlib import Path
import re
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
# find glow in navbar override section
start = text.find("ELEGANT NAVBAR")
end = text.find("</style>", start)
block = text[start:end]
glows = re.findall(r'0 0 \d+px', block)
print("Glows in override block:", len(glows))
# find glows after override in masthead/nav selectors only - check if any rules AFTER override still have glow for nav
after = text[start:end+500]
# check masthead-go in full file after override
for pat in ["masthead-go:hover", "masthead-nav:has", "0 0 28px", "0 0 18px", "navDemoPulse", "demoPulse"]:
    idx = text.rfind(pat)
    print(f"Last {pat!r} at {idx}")
