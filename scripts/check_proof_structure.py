from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
proof = text.split('class="proof-wall"')[1].split("</section>")[0]
for tag in ["partner-grid", "platform-stats", "platform-marquee", "platform-constellation"]:
    print(tag, proof.find(tag))
