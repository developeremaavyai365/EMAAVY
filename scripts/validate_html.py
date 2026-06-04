"""Quick HTML balance check for landing page."""
from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = p.read_text(encoding="utf-8")
body = text.split("<body", 1)[1].split("</body>", 1)[0]
body = re.sub(r"<script[\s\S]*?</script>", "", body, flags=re.I)

opens = len(re.findall(r"<div[\s>]", body, re.I))
closes = len(re.findall(r"</div>", body, re.I))
secs = re.findall(r'<section[^>]*id="([^"]+)"', body, re.I)
print("div open", opens, "close", closes, "delta", opens - closes)
print("sections:", ", ".join(secs))

for sid in ("features", "agents", "how-it-works"):
    m = re.search(rf'id="{sid}"[^>]*>([\s\S]*?)</section>', body, re.I)
    if not m:
        print(sid, ": section not found or unclosed")
        continue
    chunk = m.group(1)
    d = chunk.count("<div") - chunk.count("</div>")
    print(sid, "inner div delta:", d)
