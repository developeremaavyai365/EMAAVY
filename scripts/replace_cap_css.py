from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
CSS = Path(__file__).resolve().parent / "cap_section.css"

START = "/* ═══ ELEGANT FEATURES — refined shell (HIW cards below) ═══ */"
END = "/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */"

def main():
    text = HTML.read_text(encoding="utf-8")
    start = text.find(START)
    end = text.find(END)
    if start < 0 or end < 0:
        raise SystemExit("markers not found")
    new_block = CSS.read_text(encoding="utf-8") + "\n"
    text = text[:start] + new_block + text[end:]

    # Head animation disable
    text = text.replace(
        "#features::before, #agents::before, #case-studies::before, #bento::before, #journey::before, #docs::before, .template-shell::before",
        ".cap-section::before, .template-shell::before",
    )
    text = text.replace(
        "#features::before, .template-shell::before",
        ".cap-section::before, .template-shell::before",
    )

    HTML.write_text(text, encoding="utf-8")
    print("replaced cap section CSS")


if __name__ == "__main__":
    main()
