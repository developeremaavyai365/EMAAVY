"""Remove duplicate scroll-spy from landing HTML; wire landing-nav.js."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / "emaavy_white_blue (2).html"
s = path.read_text(encoding="utf-8")

old_masthead = (
    "const masthead = document.getElementById('masthead'); function updateMasthead() "
    "{ const compact = window.scrollY > 60; masthead.classList.toggle('compact', compact); "
    "document.documentElement.style.setProperty('--masthead-h', compact ? '88px' : '120px'); } "
    "window.addEventListener('scroll', updateMasthead); updateMasthead();"
)
if old_masthead in s:
    s = s.replace(old_masthead, "/* masthead scroll: assets/landing-nav.js */")
else:
    print("WARN: masthead block not found")

rail_old = (
    "/* Rail nav active */ const sections = ['top', 'how-it-works', 'features', 'gallery', "
    "'templates', 'proof', 'integrations', 'agents', 'bento', 'journey', 'case-studies', 'faq', 'cta']; "
    "const dots = document.querySelectorAll('.rail-dots a'); window.addEventListener('scroll', () => { "
    "let current = 'top'; sections.forEach((id) => { const el = document.getElementById(id); "
    "if (el && window.scrollY >= el.offsetTop - 200) current = id; }); "
    "dots.forEach((d) => d.classList.toggle('active', d.getAttribute('href') === '#' + current)); "
    "}, { passive: true });"
)
if rail_old in s:
    s = s.replace(rail_old, "/* rail scroll spy: assets/landing-nav.js */")
    print("rail block removed")
else:
    print("WARN: rail block not found")

nav_old = (
    "/* Active nav on scroll */ const navSections = ['how-it-works', 'features', 'integrations', "
    "'agents', 'case-studies']; const navLinks = document.querySelectorAll('[data-nav-section]'); "
    "window.addEventListener('scroll', () => { const offset = "
    "(document.getElementById('masthead')?.offsetHeight || 80) + 40; let current = 'top'; "
    "navSections.forEach((id) => { const sec = document.getElementById(id); "
    "if (sec && window.scrollY >= sec.offsetTop - offset) { "
    "current = id.startsWith('integration-') ? 'integrations' : id; } }); "
    "navLinks.forEach((link) => { const s = link.getAttribute('data-nav-section'); "
    "link.classList.toggle('active', s === current || (s === 'integrations' && current === 'integrations')); "
    "}); }, { passive: true });"
)
if nav_old in s:
    s = s.replace(nav_old, "")
    print("nav scroll block removed")
else:
    print("WARN: nav scroll block not found")

if "landing-nav.js" not in s:
    s = s.replace(
        '<script src="assets/nav.js"></script>',
        '<script src="assets/nav.js"></script> <script src="assets/landing-nav.js" defer></script>',
        1,
    )

s = s.replace('href="#cta" data-label="Start"', 'href="#book-demo" data-label="Start"', 1)

s, n = re.subn(
    r"/\* Smooth anchor navigation \*/ document\.querySelectorAll\('a\[href\^=\"#\"\]'\)\.forEach\(\(a\) => \{.*?\}\); \}\);",
    "/* smooth anchors: assets/landing-nav.js */",
    s,
    count=1,
    flags=re.DOTALL,
)
print("smooth anchor blocks removed:", n)

path.write_text(s, encoding="utf-8")
print("Done")
