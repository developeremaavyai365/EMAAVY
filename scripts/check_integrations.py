import re
from pathlib import Path

t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
i = text.index('id="integrations"')
end = text.index("</section>", i + 500)
chunk = text[i:end]
ids = sorted(set(re.findall(r'id="(integration-[^"]+)"', chunk)))
print("Integration IDs:", ids)
print("Showcases:", len(re.findall(r'class="int-showcase', chunk)))
print("Glow remnants:", len(re.findall(r'int-glow|telephony-glow|int-card-glow', chunk)))
print("Visual panels:", len(re.findall(r'int-visual-panel', chunk)))
