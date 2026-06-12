"""Official integration logo catalog — local assets, consistent rendering."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGO_DIR = ROOT / "assets" / "logos" / "integrations"

# slug -> file (under integrations/), alt text, optional container tone for contrast
LOGO_CATALOG: dict[str, dict] = {
    # Telephony
    "vobiz": {"file": "vobiz.svg", "alt": "Vobiz", "bg": "neutral"},
    "twilio": {"file": "twilio.svg", "alt": "Twilio", "bg": "neutral"},
    "plivo": {"file": "plivo.svg", "alt": "Plivo", "bg": "light"},
    "vonage": {"file": "vonage.svg", "alt": "Vonage", "bg": "light"},
    "exotel": {"file": "exotel.svg", "alt": "Exotel", "bg": "neutral"},
    "knowlarity": {"file": "knowlarity.svg", "alt": "Knowlarity", "bg": "neutral"},
    "telnyx": {"file": "telnyx.svg", "alt": "Telnyx", "bg": "neutral"},
    "bandwidth": {"file": "bandwidth.svg", "alt": "Bandwidth", "bg": "neutral"},
    # LLMs
    "openai": {"file": "openai.svg", "alt": "OpenAI", "bg": "neutral"},
    "claude": {"file": "anthropic.svg", "alt": "Anthropic Claude", "bg": "light"},
    "gemini": {"file": "gemini.svg", "alt": "Google Gemini", "bg": "neutral"},
    "qwen": {"file": "qwen.svg", "alt": "Qwen", "bg": "neutral"},
    "grok": {"file": "grok.svg", "alt": "Grok", "bg": "neutral"},
    # STT
    "deepgram": {"file": "deepgram.svg", "alt": "Deepgram", "bg": "neutral"},
    "sarvam": {"file": "sarvam.svg", "alt": "Sarvam AI", "bg": "neutral"},
    "assemblyai": {"file": "assemblyai.svg", "alt": "AssemblyAI", "bg": "neutral"},
    "azure-stt": {"file": "azure.svg", "alt": "Microsoft Azure Speech", "bg": "neutral"},
    "google-stt": {"file": "google-cloud.svg", "alt": "Google Cloud Speech", "bg": "neutral"},
    "openai-stt": {"file": "openai.svg", "alt": "OpenAI Whisper", "bg": "neutral"},
    "elevenlabs-stt": {"file": "elevenlabs.svg", "alt": "ElevenLabs Scribe", "bg": "neutral"},
    "gladia": {"file": "gladia.svg", "alt": "Gladia", "bg": "neutral"},
    "smallest": {"file": "smallest.svg", "alt": "Smallest AI", "bg": "neutral"},
    # TTS
    "elevenlabs": {"file": "elevenlabs.svg", "alt": "ElevenLabs", "bg": "light"},
    "flash-bulbul": {"file": "flash-bulbul.svg", "alt": "Flash · Bulbul", "bg": "neutral"},
    # Tools
    "webhooks": {"file": "webhooks.svg", "alt": "Webhooks", "bg": "neutral"},
    "salesforce": {"file": "salesforce.svg", "alt": "Salesforce", "bg": "neutral"},
    "hubspot": {"file": "hubspot.svg", "alt": "HubSpot", "bg": "neutral"},
    "calcom": {"file": "calcom.svg", "alt": "Cal.com", "bg": "neutral"},
    "google-calendar": {"file": "google-calendar.svg", "alt": "Google Calendar", "bg": "neutral"},
    "whatsapp": {"file": "whatsapp.svg", "alt": "WhatsApp", "bg": "neutral"},
    "slack": {"file": "slack.svg", "alt": "Slack", "bg": "light"},
}

# Remote sources used by sync_integration_logos.py
LOGO_SOURCES: dict[str, str] = {
    "twilio.svg": "https://cdn.worldvectorlogo.com/logos/twilio-2.svg",
    "openai.svg": "https://cdn.worldvectorlogo.com/logos/openai-2.svg",
    "salesforce.svg": "https://cdn.worldvectorlogo.com/logos/salesforce-2.svg",
    "hubspot.svg": "https://cdn.worldvectorlogo.com/logos/hubspot-1.svg",
    "vonage.svg": "https://cdn.worldvectorlogo.com/logos/vonage-1.svg",
    "deepgram.svg": "https://cdn.simpleicons.org/deepgram/13EF93",
    "anthropic.svg": "https://cdn.simpleicons.org/anthropic/191919",
    "gemini.svg": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg",
    "google-cloud.svg": "https://cdn.simpleicons.org/googlecloud/4285F4",
    "google-calendar.svg": "https://cdn.simpleicons.org/googlecalendar/4285F4",
    "whatsapp.svg": "https://cdn.simpleicons.org/whatsapp/25D366",
    "calcom.svg": "https://cdn.simpleicons.org/caldotcom/292929",
    "elevenlabs.svg": "https://cdn.simpleicons.org/elevenlabs/000000",
}


def logo_path(slug: str) -> str:
    entry = LOGO_CATALOG[slug]
    return f"../../assets/logos/integrations/{entry['file']}"


def logo_img(slug: str, *, size: str = "sm", alt: str | None = None) -> str:
    """Render standardized logo <img> for integration tiles and hero."""
    if slug not in LOGO_CATALOG:
        return _fallback_mark(alt or slug, size=size)
    entry = LOGO_CATALOG[slug]
    label = alt or entry["alt"]
    path = logo_path(slug)
    bg = entry.get("bg", "neutral")
    if size == "lg":
        w, h, cls = 64, 64, f'int-logo-img int-logo-img--lg int-logo-img--{bg}'
    else:
        w, h, cls = 40, 40, f'int-logo-img int-logo-img--{bg}'
    return (
        f'<img class="{cls}" src="{path}" alt="{label}" '
        f'width="{w}" height="{h}" loading="lazy" decoding="async" />'
    )


def _fallback_mark(name: str, *, size: str = "sm") -> str:
    words = [w for w in name.replace("·", " ").split() if w]
    initials = (words[0][0] + words[1][0]).upper() if len(words) >= 2 else name[:2].upper()
    cls = "brand-mark brand-mark--lg" if size == "lg" else "brand-mark"
    return f'<span class="{cls}" aria-label="{name}">{initials}</span>'


def apply_logos(partner: dict) -> None:
    """Inject logo + logo_sm from catalog using partner slug."""
    slug = partner["slug"]
    name = partner.get("name", slug)
    partner["logo_sm"] = logo_img(slug, size="sm", alt=name)
    partner["logo"] = logo_img(slug, size="lg", alt=name)


def apply_logos_all(partners: list) -> None:
    for p in partners:
        apply_logos(p)
