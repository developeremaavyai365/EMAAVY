import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
for key in ["vobiz", "exotel", "knowlarity", "bandwidth", "elevenlabs", "flash"]:
    m = re.search(rf"{key}:\s*\{{.*?\}},\s*\w+:", text, re.DOTALL)
    if not m:
        m = re.search(rf"{key}:\s*\{{[^}}]+\}}", text)
    print("===", key, "===")
    print(m.group(0)[:350] if m else "NOT FOUND")
    print()
