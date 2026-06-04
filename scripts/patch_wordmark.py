from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

old = (
    '<a href="#top" class="logo-mega logo-mega--mark" id="logoMega" aria-label="EMAAVY home"> '
    '<img src="assets/emaavy-mark.png" srcset="assets/emaavy-mark.png 364w" '
    'sizes="44px" alt="" class="logo-mega-mark" width="364" height="364" '
    'decoding="async" fetchpriority="high" /> '
    '<span class="logo-tag">The Enterprise AI Operating System</span> </a>'
)

new = (
    '<a href="#top" class="logo-mega logo-mega--mark" id="logoMega" aria-label="EMAAVY home"> '
    '<span class="logo-mega-brand" aria-hidden="true">'
    '<img src="assets/emaavy-mark.png" srcset="assets/emaavy-mark.png 364w" '
    'sizes="40px" alt="" class="logo-mega-mark" width="364" height="364" '
    'decoding="async" fetchpriority="high" />'
    '<span class="logo-mega-maavy">MAAVY</span></span> '
    '<span class="logo-tag">The Enterprise AI Operating System</span> </a>'
)

if old not in text:
    raise SystemExit("logo block not found")
text = text.replace(old, new, 1)
HTML.write_text(text, encoding="utf-8")
print("Wordmark updated.")
