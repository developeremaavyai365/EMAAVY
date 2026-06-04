from pathlib import Path
import re
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
proof = text.split('id="proof"')[1].split("</section>")[0]
assert "partner-grid" in proof
assert "platform-constellation" not in proof
assert "platform-marquee-zone" not in proof
assert "ELEGANT PARTNERS" in text
names = re.findall(r'class="partner-name[^"]*">([^<]+)', proof)
print(len(names), "partners:", ", ".join(names))
assert "Cal.com" in names
assert "HubSpot" in names
assert "ElevenLabs" in names
print("OK")
