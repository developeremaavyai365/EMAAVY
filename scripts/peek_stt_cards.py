import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
m = re.search(r'id="integration-stt">(.*?)id="integration-tts"', text, re.DOTALL)
seg = m.group(1)
head = re.search(r"<h3>([^<]+)</h3>\s*<p>([^<]+)</p>", seg)
print("HEAD:", head.group(1) if head else "?")
print("DESC:", head.group(2)[:120] if head else "?")
for card in re.finditer(r'data-detail="([^"]+)"[^>]*>(.*?)</article>', seg, re.DOTALL):
    pid = card.group(1)
    inner = card.group(2)
    h4 = re.search(r"<h4>([^<]+)</h4>", inner)
    p = re.search(r"<h4>[^<]+</h4>\s*<p>([^<]+)</p>", inner)
    logo = re.search(r'int-card-logo">(.*?)</div>', inner, re.DOTALL)
    print("---", pid)
    print("  title:", h4.group(1) if h4 else "?")
    print("  desc:", (p.group(1) if p else "?")[:100])
    print("  logo:", (logo.group(1).strip()[:100] if logo else "?"))

cap = re.search(r'int-cap-label">([^<]+)', seg)
if cap:
    print("CAP:", cap.group(1))
    row = re.findall(r'<span class="int-cap">([^<]+)</span>', seg)
    print("STEPS:", row)
