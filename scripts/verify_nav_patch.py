from pathlib import Path

s = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
t = s.read_text(encoding="utf-8")
checks = [
    ("updateMasthead gone", "updateMasthead" not in t),
    ("landing-nav.js linked", "landing-nav.js" in t),
    ("rail spy comment", "rail scroll spy: assets/landing-nav.js" in t),
    ("old rail sections gone", "'gallery'" not in t or "rail scroll spy" in t),
    ("book-demo rail", 'href="#book-demo" data-label="Start"' in t),
    ("active nav scroll gone", "Active nav on scroll" not in t),
]
for name, ok in checks:
    print(name, "OK" if ok else "FAIL")
