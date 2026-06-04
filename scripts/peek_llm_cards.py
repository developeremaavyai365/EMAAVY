import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
m = re.search(r'id="integration-llm">(.*?)id="integration-stt"', text, re.DOTALL)
seg = m.group(1)
for card in re.finditer(r'<article class="int-card[^"]*" data-detail="([^"]+)"[^>]*>(.*?)</article>', seg, re.DOTALL):
    pid = card.group(1)
    inner = card.group(2)
    h4 = re.search(r"<h4>([^<]+)</h4>", inner)
    p = re.search(r"<h4>[^<]+</h4>\s*<p>([^<]+)</p>", inner)
    logo = re.search(r'int-card-logo">(.*?)</div>', inner, re.DOTALL)
    print("---", pid, "---")
    print("title:", h4.group(1) if h4 else "?")
    print("desc:", p.group(1) if p else "?")
    print("logo:", (logo.group(1).strip()[:120] if logo else "?"))
