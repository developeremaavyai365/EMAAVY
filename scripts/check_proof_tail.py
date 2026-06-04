from pathlib import Path
text = Path(__file__).resolve().parents[1].joinpath("emaavy_white_blue (2).html").read_text(encoding="utf-8")
proof_start = text.index('id="proof"')
proof_end = text.index('</section>', proof_start)
section = text[proof_start:proof_end+10]
# last 500 chars
print(section[-800:])
