#!/usr/bin/env python3
"""Apply professional theme: strip emojis from HTML and update detailData logos."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"

# Emoji ranges (common pictographs + symbols)
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\U00002700-\U000027BF"
    "\U0001F600-\U0001F64F"
    "\U00002600-\U000026FF"
    "]+",
    flags=re.UNICODE,
)

DETAIL_LOGO_MAP = {
    "vobiz": '<span class="detail-brand-mark">VZ</span>',
    "qwen": '<span class="detail-brand-mark">QW</span>',
    "grok": '<span class="detail-brand-mark">GX</span>',
    "assemblyai": '<span class="detail-brand-mark">AA</span>',
    "gladia": '<span class="detail-brand-mark">GL</span>',
    "sarvam": '<span class="detail-brand-mark">SV</span>',
    "smallest": '<span class="detail-brand-mark">SM</span>',
    "flash": '<img src="https://cdn.simpleicons.org/elevenlabs/0f172a" alt="Flash Bulbul" style="height:24px;width:auto"/>',
    "webhooks": '<span class="detail-brand-mark">WH</span>',
    "hiw-connect": '<span class="detail-brand-mark">01</span>',
    "hiw-transcribe": '<span class="detail-brand-mark">02</span>',
    "hiw-reason": '<span class="detail-brand-mark">03</span>',
    "hiw-act": '<span class="detail-brand-mark">04</span>',
    "feat-bulk": '<span class="detail-brand-mark">BC</span>',
    "feat-api": '<span class="detail-brand-mark">API</span>',
    "feat-stt": '<span class="detail-brand-mark">STT</span>',
    "feat-agents": '<span class="detail-brand-mark">AI</span>',
    "feat-intel": '<span class="detail-brand-mark">CI</span>',
    "feat-security": '<span class="detail-brand-mark">SEC</span>',
    "tpl-sales": '<span class="detail-brand-mark">SL</span>',
    "tpl-support": '<span class="detail-brand-mark">SP</span>',
    "tpl-leadership": '<span class="detail-brand-mark">EX</span>',
    "snap-speed": '<span class="detail-brand-mark">RT</span>',
    "snap-lang": '<span class="detail-brand-mark">LG</span>',
    "snap-intent": '<span class="detail-brand-mark">IN</span>',
    "snap-api": '<span class="detail-brand-mark">API</span>',
    "bento-volume": '<span class="detail-brand-mark">VOL</span>',
    "bento-realtime": '<span class="detail-brand-mark">LIVE</span>',
    "bento-intent": '<span class="detail-brand-mark">INT</span>',
    "bento-ops": '<span class="detail-brand-mark">OPS</span>',
    "bento-latency": '<span class="detail-brand-mark">LAT</span>',
    "bento-security": '<span class="detail-brand-mark">SEC</span>',
    "journey-1": '<span class="detail-brand-mark">01</span>',
    "journey-2": '<span class="detail-brand-mark">02</span>',
    "journey-3": '<span class="detail-brand-mark">03</span>',
    "journey-4": '<span class="detail-brand-mark">04</span>',
    "journey-5": '<span class="detail-brand-mark">05</span>',
    "cs-mudita": '<span class="detail-brand-mark">WM</span>',
    "cs-nextcall": '<span class="detail-brand-mark">NC</span>',
    "cs-fleetiq": '<span class="detail-brand-mark">FQ</span>',
    "gal-capture": '<span class="detail-brand-mark">REC</span>',
    "gal-transcribe": '<span class="detail-brand-mark">TR</span>',
    "gal-analytics": '<span class="detail-brand-mark">AN</span>',
    "gal-scale": '<span class="detail-brand-mark">SC</span>',
    "gal-agents": '<span class="detail-brand-mark">AG</span>',
    "wf-ingest": '<span class="detail-brand-mark">IN</span>',
    "wf-understand": '<span class="detail-brand-mark">UN</span>',
    "wf-orchestrate": '<span class="detail-brand-mark">OR</span>',
    "wf-optimize": '<span class="detail-brand-mark">OP</span>',
    "price-starter": '<span class="detail-brand-mark">ST</span>',
    "price-pro": '<span class="detail-brand-mark">PR</span>',
    "price-business": '<span class="detail-brand-mark">BU</span>',
    "price-enterprise": '<span class="detail-brand-mark">EN</span>',
    "docs-quickstart": '<span class="detail-brand-mark">QS</span>',
    "docs-api": '<span class="detail-brand-mark">API</span>',
    "docs-agents": '<span class="detail-brand-mark">AB</span>',
    "agent-sales": '<span class="detail-brand-mark">SA</span>',
    "agent-support": '<span class="detail-brand-mark">SU</span>',
    "agent-campaign": '<span class="detail-brand-mark">CA</span>',
    "agents-overview": '<span class="detail-brand-mark">CB</span>',
}

CARD_EMOJI_TO_MARK = {
    "💼": "SA", "🎧": "SU", "📣": "CA", "⚡": "CB",
    "🏛": "WM", "📋": "NC", "🚛": "FQ",
    "📈": "VOL", "🎙": "LIVE", "🧠": "INT", "👥": "OPS", "🔒": "SEC",
    "📞": "01", "🔄": "05",
    "🔗": "WH", "📅": "CAL", "💬": "WA",
    "Q": "QW", "G": "GX", "A": "AA", "S": "SV", "Sm": "SM",
    "V": "VZ",
}


def strip_emojis(text: str) -> str:
    return EMOJI_RE.sub("", text)


def replace_detail_logos(content: str) -> str:
    for key, logo in DETAIL_LOGO_MAP.items():
        # Match logo: '<span ...>emoji</span>' or similar for this key
        pattern = rf"('{key}':\s*{{[^}}]*?logo:\s*)'[^']*'"
        content = re.sub(pattern, rf"\1'{logo.replace(chr(39), chr(92)+chr(39))}'", content, count=1)
    return content


def replace_card_logos(content: str) -> str:
    for emoji, mark in CARD_EMOJI_TO_MARK.items():
        content = content.replace(
            f'<div class="int-card-logo"><span>{emoji}</span></div>',
            f'<div class="int-card-logo"><span class="brand-mark">{mark}</span></div>',
        )
        content = content.replace(
            f'<div class="int-card-logo"><span>{emoji}</span></div>'.replace(emoji, mark if len(mark)==1 else emoji),
            f'<div class="int-card-logo"><span class="brand-mark">{mark}</span></div>',
        )
    # Letter-only logos in int-card
    for letter, mark in [("Q", "QW"), ("G", "GX")]:
        content = content.replace(
            f'<div class="int-card-logo"><span>{letter}</span></div>',
            f'<div class="int-card-logo"><span class="brand-mark">{mark}</span></div>',
        )
    return content


def clean_html_emojis(content: str) -> str:
    # Preserve detailData block — handle separately
    start = content.find("const detailData = {")
    end = content.find("};", start) + 2 if start != -1 else -1
    if start != -1 and end > start:
        before = content[:start]
        data_block = content[start:end]
        after = content[end:]
        before = strip_emojis(before)
        after = strip_emojis(after)
        data_block = replace_detail_logos(data_block)
        content = before + data_block + after
    else:
        content = strip_emojis(content)

    content = replace_card_logos(content)

    # Clean int-cap: collapse double spaces after emoji removal (within tags only)
    content = re.sub(r'(<span class="int-cap">)\s+', r"\1", content)

    # Remove empty cap-icon spans
    content = re.sub(r'<span class="cap-icon" aria-hidden="true">\s*</span>\s*', "", content)

    # Nav dropdown titles — already stripped by emoji regex

    # int-card-metric: strip leading emoji remnants
    content = re.sub(
        r'(<span class="int-card-metric">)\s*',
        r"\1",
        content,
    )

    # FX hubs — replace emoji in em tags with step numbers / labels
    fx_replacements = [
        ('<div class="int-fx-neural-hub">🧠</div>', '<div class="int-fx-neural-hub"><span class="brand-mark sm">AI</span></div>'),
        ('<div class="int-fx-rings-core">🔊</div>', '<div class="int-fx-rings-core"><span class="brand-mark sm">TTS</span></div>'),
        ('<div class="int-fx-action-hub">⚡</div>', '<div class="int-fx-action-hub"><span class="brand-mark sm">ACT</span></div>'),
        ('<div class="int-fx-workforce-hub">🤖</div>', '<div class="int-fx-workforce-hub"><span class="brand-mark sm">AI</span></div>'),
        ('<div class="int-fx-success-hub">🏆</div>', '<div class="int-fx-success-hub"><span class="brand-mark sm">CS</span></div>'),
        ('<div class="int-fx-analytics-hub">📊</div>', '<div class="int-fx-analytics-hub"><span class="brand-mark sm">BI</span></div>'),
    ]
    for old, new in fx_replacements:
        content = content.replace(old, new)

    # Telephony nodes
    telephony_icons = [
        ('<div class="telephony-node-icon" aria-hidden="true">🔗</div>', 'CH'),
        ('<div class="telephony-node-icon" aria-hidden="true">📡</div>', 'VB'),
        ('<div class="telephony-node-icon" aria-hidden="true">🧠</div>', 'AI'),
    ]
    for old, mark in telephony_icons:
        content = content.replace(
            old,
            f'<div class="telephony-node-icon" aria-hidden="true"><span class="brand-mark xs">{mark}</span></div>',
        )

    # Feature/workflow/bento icons in older sections
    content = re.sub(
        r'<div class="bento-icon">[^<]*</div>',
        lambda m: '<div class="bento-icon"><span class="brand-mark sm">·</span></div>',
        content,
    )
    content = re.sub(
        r'<div class="feature-icon">[^<]*</div>',
        lambda m: '<div class="feature-icon"><span class="brand-mark sm">·</span></div>',
        content,
    )

    return content


def main():
    text = HTML.read_text(encoding="utf-8")
    text = clean_html_emojis(text)
    HTML.write_text(text, encoding="utf-8")
    print(f"Professionalized {HTML.name}")


if __name__ == "__main__":
    main()
