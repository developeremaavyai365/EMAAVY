from pathlib import Path
text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
t = text.read_text(encoding="utf-8")
i = t.find("unsplash")
Path(__file__).parent.joinpath("_unsplash_ctx.txt").write_text(t[i-2000:i+3000], encoding="utf-8")
# also search hero section in scripts
for m in ["hero-copy", "class=\"hero-visual\"", "hero-gallery"]:
    j = t.find(m)
    Path(__file__).parent.joinpath(f"_ctx_{m.replace(chr(34),'')[:20]}.txt").write_text(
        t[max(0,j-500):j+2500] if j>=0 else "not found", encoding="utf-8"
    )
