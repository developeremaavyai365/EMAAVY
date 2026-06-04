from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
assert "ELEGANT SIGNAL" in text
snap = text.split('id="snapshots"')[1].split("<!-- HOW IT WORKS -->")[0]
assert "signal-band-glow" not in snap
assert "signal-chip-glow" not in snap
assert "signal-band-grid" not in snap
start = text.find("ELEGANT SIGNAL")
block = text[start:text.find("</style>", start)]
assert "0 0" not in block
print("Signal section OK")
print("Snapshot HTML preview:")
print(snap[:1200])
