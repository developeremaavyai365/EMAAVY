"""Patch telephony + TTS partner cards and detailData with local logos."""
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

REPLACEMENTS = [
    # telephony cards
    (
        '<div class="int-card-logo"><span class="brand-mark">Vobiz</span></div><h4>Vobiz</h4>',
        '<div class="int-card-logo"><img src="assets/logos/vobiz.svg" alt="Vobiz" loading="lazy" /></div><h4>Vobiz</h4>',
    ),
    (
        '<div class="int-card-logo"><span class="brand-mark">Exotel</span></div><h4>Exotel</h4>',
        '<div class="int-card-logo"><img src="assets/logos/exotel.png" alt="Exotel" loading="lazy" /></div><h4>Exotel</h4>',
    ),
    (
        '<div class="int-card-logo"><span class="brand-mark">Knowlarity</span></div><h4>Knowlarity</h4>',
        '<div class="int-card-logo"><img src="assets/logos/knowlarity.png" alt="Knowlarity" loading="lazy" /></div><h4>Knowlarity</h4>',
    ),
    (
        '<div class="int-card-logo"><span class="brand-mark">Bandwidth</span></div><h4>Bandwidth</h4>',
        '<div class="int-card-logo"><img src="assets/logos/bandwidth.png" alt="Bandwidth" loading="lazy" /></div><h4>Bandwidth</h4>',
    ),
    # TTS cards + detail drawer
    ("https://cdn.simpleicons.org/elevenlabs/000000", "assets/logos/elevenlabs.svg"),
    ("https://cdn.simpleicons.org/elevenlabs/0f172a", "assets/logos/elevenlabs.svg"),
    # flash card uses elevenlabs icon — point to sarvam wordmark
    (
        '<div class="int-card-logo"><img src="assets/logos/elevenlabs.svg" alt="Flash Bulbul" style="height:24px"/></div><h4>Flash v2',
        '<div class="int-card-logo"><img src="assets/logos/flash-bulbul.svg" alt="Flash Bulbul" loading="lazy" /></div><h4>Flash v2',
    ),
    # detailData telephony
    (
        "vobiz: { tag: 'Telephony', title: 'Vobiz', logo: '<span class=\"detail-brand-mark\">VZ</span>'",
        "vobiz: { tag: 'Telephony', title: 'Vobiz', logo: '<img src=\"assets/logos/vobiz.svg\" alt=\"Vobiz\" style=\"height:28px\"/>'",
    ),
    (
        "exotel: { tag: 'Telephony', title: 'Exotel', logo: '<span class=\"detail-brand-mark\">EX</span>'",
        "exotel: { tag: 'Telephony', title: 'Exotel', logo: '<img src=\"assets/logos/exotel.png\" alt=\"Exotel\" style=\"height:28px\"/>'",
    ),
    (
        "knowlarity: { tag: 'Telephony', title: 'Knowlarity', logo: '<span class=\"detail-brand-mark\">KL</span>'",
        "knowlarity: { tag: 'Telephony', title: 'Knowlarity', logo: '<img src=\"assets/logos/knowlarity.png\" alt=\"Knowlarity\" style=\"height:28px\"/>'",
    ),
    (
        "bandwidth: { tag: 'Telephony', title: 'Bandwidth', logo: '<span class=\"detail-brand-mark\">BW</span>'",
        "bandwidth: { tag: 'Telephony', title: 'Bandwidth', logo: '<img src=\"assets/logos/bandwidth.png\" alt=\"Bandwidth\" style=\"height:28px\"/>'",
    ),
    # flash detail drawer
    (
        'flash: { tag: \'TTS\', title: \'Flash v2',
        'flash: { tag: \'TTS\', title: \'Flash v2',  # placeholder - handle separately
    ),
]

text = HTML.read_text(encoding="utf-8")

# flash detailData logo
text = text.replace(
    'logo: \'<img src=\\"https://cdn.simpleicons.org/elevenlabs/0f172a\\" alt=\\"Flash Bulbul\\" style=\\"height:24px\\"/>\'',
    'logo: \'<img src=\\"assets/logos/flash-bulbul.svg\\" alt=\\"Flash Bulbul\\" style=\\"height:28px\\"/>\'',
)
text = text.replace(
    'logo: \'<img src=\\"assets/logos/elevenlabs.svg\\" alt=\\"Flash Bulbul\\" style=\\"height:24px\\"/>\'',
    'logo: \'<img src=\\"assets/logos/flash-bulbul.svg\\" alt=\\"Flash Bulbul\\" style=\\"height:28px\\"/>\'',
)

for old, new in REPLACEMENTS:
    if old == new:
        continue
    if old in text:
        text = text.replace(old, new)
        print("patched:", old[:65])
    else:
        print("skip:", old[:65])

HTML.write_text(text, encoding="utf-8")
print("Done")
