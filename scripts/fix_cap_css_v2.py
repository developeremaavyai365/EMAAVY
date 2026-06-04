"""Fix capability section CSS via .cap-section class."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
IDS = ["features", "agents", "case-studies", "bento", "journey", "docs"]
MARKER = "#features, #agents, #case-studies, #bento, #journey, #docs"


def main():
    text = HTML.read_text(encoding="utf-8")

    start = text.find("/* ═══ ELEGANT FEATURES — refined shell (HIW cards below) ═══ */")
    end = text.find("/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */")
    block = text[start:end]

    block = re.sub(
        r"#features, #agents, #case-studies, #bento, #journey, #docs(?=\s*::|\s+[\.\{])",
        ".cap-section",
        block,
    )
    block = re.sub(
        r"^#features, #agents, #case-studies, #bento, #journey, #docs\s*\{",
        ".cap-section {",
        block,
        flags=re.M,
    )

    text = text[:start] + block + text[end:]

    bad_anim = (
        "#features, #agents, #case-studies, #bento, #journey, #docs::before, "
        ".template-shell::before"
    )
    good_anim = ".cap-section::before, .template-shell::before"
    text = text.replace(bad_anim, good_anim)

    for sid in IDS:
        text = text.replace(
            f'<section id="{sid}">',
            f'<section id="{sid}" class="cap-section">',
            1,
        )

    HTML.write_text(text, encoding="utf-8")
    print("cap-section CSS + HTML class applied")


if __name__ == "__main__":
    main()
