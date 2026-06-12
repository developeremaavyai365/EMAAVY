#!/usr/bin/env python3
"""Generate TTS hub + per-provider integration pages."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from integration_logos import apply_logos_all
from integration_pages_common import ensure_uses, render_hub, render_partner

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

PROVIDERS = [
    {
        "slug": "elevenlabs",
        "name": "ElevenLabs",
        "short": "ElevenLabs",
        "display": "ElevenTurbo v2",
        "region": "Expressive · Global",
        "tag": "Expressive",
        "route": "integration-elevenlabs",
        "logo": '<img src="../../assets/logos/elevenlabs.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/elevenlabs.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "ElevenLabs — EMAAVY",
        "h1": "ElevenTurbo v2",
        "meta": "ElevenLabs and EMAAVY — low-latency expressive voice synthesis for persuasive AI agents on live calls.",
        "lead": "ElevenLabs sets the bar for expressive, human-like TTS — on EMAAVY, ElevenTurbo v2 powers outbound agents that sound warm, credible, and fast enough for real conversation turn-taking.",
        "stats": [("<300ms", "Target latency"), ("Voice clone", "Profiles"), ("Global", "Locales")],
        "about": [
            "ElevenLabs pioneered high-quality neural text-to-speech for creators and enterprises — voice cloning, emotional range, and turbo models optimized for conversational latency. ElevenTurbo v2 targets agents that must sound persuasive, not robotic, on sales and premium support calls.",
            "Teams choose ElevenLabs when brand voice consistency matters globally — the same cloned profile can greet, handle objections, and close without studio re-records between script changes.",
        ],
        "emaavy": [
            ("Per-agent voice profiles", "Assign ElevenLabs voice IDs per campaign, language, or brand line."),
            ("Stage-aware tone", "EMAAVY adjusts stability and style hints for opener vs. close segments."),
            ("Streaming playback", "Audio chunks stream into the call as tokens arrive from the LLM."),
            ("STT + TTS option", "Pair ElevenLabs capture and speech on one key when desired."),
        ],
        "features": [
            ("ElevenTurbo v2", "Low-latency model built for dialogue agents."),
            ("Voice cloning", "Consistent brand voice from short samples."),
            ("Multilingual output", "Serve global programs from one voice platform."),
            ("Emotion & stability", "Fine-tune expressiveness per script type."),
            ("API streaming", "Chunked audio for natural barge-in and overlap."),
            ("Dashboard analytics", "Monitor character usage alongside EMAAVY call KPIs."),
        ],
        "uses": [
            ("Premium outbound", "High-touch sales where voice trust drives conversion."),
            ("English-global support", "Empathetic tone on cancellation saves and VIP care."),
            ("Brand campaigns", "Launches requiring one recognizable voice everywhere."),
        ],
        "setup": [
            ("Add ElevenLabs API key", "Configure in EMAAVY integrations with quota alerts."),
            ("Select voice profile", "Pick cloned or library voice per agent."),
            ("Tune turbo settings", "Set stability and similarity for your vertical."),
            ("Run live call test", "Validate turn latency with your STT + LLM stack."),
        ],
        "hub_desc": "Low-latency expressive synthesis for warm, persuasive outbound and support agents.",
        "hub_points": ["ElevenTurbo v2 for dialogue", "Voice cloning and profiles", "Sub-300ms voice targets"],
        "hub_badge": "Expressive",
    },
    {
        "slug": "flash-bulbul",
        "name": "Flash · Bulbul",
        "short": "Flash · Bulbul",
        "display": "Flash v2 · Bulbul V3",
        "region": "India native · Hinglish",
        "tag": "India native",
        "route": "integration-flash-bulbul",
        "logo": '<img src="../../assets/logos/flash-bulbul.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/flash-bulbul.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Flash · Bulbul — EMAAVY",
        "h1": "Flash v2 · Bulbul V3",
        "meta": "Flash and Bulbul TTS with EMAAVY — native Indian voices, natural Hinglish cadence, and low-latency synthesis for domestic programs.",
        "lead": "Flash v2 and Bulbul V3 are built for how India actually speaks — Hinglish, regional rhythm, and code-switching mid-sentence. EMAAVY routes Indian campaigns to Bulbul when Western TTS sounds foreign on the phone.",
        "stats": [("22+", "Indian contexts"), ("Hinglish", "Native cadence"), ("Fast", "Synthesis")],
        "about": [
            "Flash and Bulbul are native Indian voice models designed for telephony-grade outbound and support — not accented English pasted on Indian scripts. They handle honorifics, city slang, and mixed Hindi-English flows that global engines flatten.",
            "EMAAVY pairs Bulbul with Sarvam STT and Qwen or regional LLMs so listen-and-speak loops stay culturally coherent end to end.",
        ],
        "emaavy": [
            ("Language routing", "Auto-select Bulbul when agent language is Hindi or Hinglish."),
            ("Campaign voice packs", "Pre-approved tones for BPO, fintech, and D2C verticals."),
            ("Latency tier", "Optimized for high-QPS domestic dialers."),
            ("Brand trust", "Voices that sound local increase answer and stay rates."),
        ],
        "features": [
            ("Flash v2", "Fast synthesis for short-turn dialogs."),
            ("Bulbul V3", "Richer expressiveness for longer explanations."),
            ("Hinglish code-switch", "Natural mixed-language delivery."),
            ("Regional nuance", "Cadence tuned for Indian telephony audio."),
            ("Agent personas", "Male/female profiles per campaign type."),
            ("EMAAVY orchestration", "Mix with ElevenLabs on English-only queues."),
        ],
        "uses": [
            ("India outbound", "Sales, verification, and collections in Hinglish."),
            ("Domestic support", "Billing, logistics, and appointment calls."),
            ("Government & PSU", "Citizen outreach in familiar voices."),
        ],
        "setup": [
            ("Enable Bulbul credentials", "Add keys in EMAAVY integrations hub."),
            ("Map agent languages", "Bind Bulbul to Hindi and Hinglish profiles."),
            ("Upload script samples", "QA team approves tone on recorded calls."),
            ("Scale per queue", "Roll out one BPO client at a time."),
        ],
        "hub_desc": "Native Indian models with natural Hinglish cadence for sales and support at scale.",
        "hub_points": ["Flash v2 and Bulbul V3", "Hinglish code-switching", "Built for Indian telephony"],
        "hub_badge": "India native",
    },
]

USE_EXTRAS = [
    ("Appointment booking", "Confirm schedules with natural, low-latency voice."),
    ("Automated follow-ups", "Post-call voice messages and callbacks with brand tone."),
    ("Multi-agent operations", "Assign voice profiles per campaign without rebuilding agents."),
]

HUB_CFG = {
    "route": "integration-tts",
    "title": "Text-to-Speech — EMAAVY",
    "meta": "Natural, empathetic TTS on EMAAVY — ElevenLabs for expressive global voice, Flash · Bulbul for native Indian and Hinglish programs.",
    "og_title": "Text-to-Speech — EMAAVY",
    "og_description": "Premium TTS engines for live AI voice agents — sub-300ms synthesis with brand-consistent profiles.",
    "breadcrumb": "Text-to-Speech",
    "kicker": "Voice layer · Text-to-Speech",
    "h1": "Voices that sound human — not robotic",
    "lead": "Natural, empathetic synthesis in every language your customers speak. EMAAVY connects premium TTS engines built for live conversations — where tone, pace, and cultural cadence decide whether callers stay on the line.",
    "stats": [("2", "Premium engines"), ("<300ms", "Voice latency"), ("22+", "Languages")],
    "anchor_jumps": [
        ("synthesis-layer", "How EMAAVY speaks"),
        ("providers", "TTS engines"),
        ("pipeline", "Voice pipeline"),
    ],
    "layer_id": "synthesis-layer",
    "layer_num": "Layer 04",
    "layer_tag": "EMAAVY · Text-to-Speech",
    "layer_h2": "How EMAAVY delivers agent voice",
    "layer_lead": "Scripts become speech in milliseconds. Tone adapts per call stage — opener, objection, close — without manual audio editing or post-production.",
    "pills": [
        ("ElevenTurbo v2", "Expressive global voices for persuasive outbound."),
        ("Flash · Bulbul", "Native Indian cadence and Hinglish code-switching."),
        ("Low latency", "Sub-300ms targets for natural turn-taking."),
        ("Voice profiles", "Per-campaign cloning and persona consistency."),
    ],
    "partners_id": "providers",
    "partners_h2": "TTS engines",
    "partners_desc": "Two premium partners today — each with a dedicated page on capabilities, EMAAVY voice routing, and rollout steps.",
    "flow_id": "pipeline",
    "flow_h2": "How your agent finds its voice",
    "flow_desc": "From LLM text to caller audio on every turn — across ElevenLabs and Flash · Bulbul.",
    "flow_steps": [
        ("Script generated", "LLM produces the next spoken line for the agent."),
        ("TTS synthesizes", "EMAAVY calls your engine with tone and pace parameters."),
        ("Tone adjusted", "Warmth tuned for sales, support, or compliance context."),
        ("Audio streams", "Speech plays into the live call with minimal gap."),
    ],
    "cta_h2": "Connect Text-to-Speech to EMAAVY",
    "cta_desc": "Hear live voice profiles, compare engines, and map TTS routing in a tailored demo.",
}

HUB_FILE = "tts.html"
HUB_LABEL = "All TTS"
HUB_BREADCRUMB = "Text-to-Speech"
HUB_CTA = "TTS overview"


def prepare():
    for p in PROVIDERS:
        p.pop("featured", None)
        ensure_uses(p, USE_EXTRAS)
    apply_logos_all(PROVIDERS)


def write_partner(p: dict) -> str:
    route = p.get("route", f"integration-{p['slug']}")
    display = p.get("display", p["name"])
    partner = {**p, "name": display}
    return render_partner(
        partner,
        partners=PROVIDERS,
        route=route,
        segment_kicker=f"Text-to-Speech · {p['tag']}",
        hub_file=HUB_FILE,
        hub_label=HUB_LABEL,
        hub_breadcrumb=HUB_BREADCRUMB,
        hub_cta_label=HUB_CTA,
        nav_label_key="short",
        connect_name_key="name",
        explore_title="Explore other TTS engines",
        explore_desc="Route English-global programs to ElevenLabs and Indian languages to Flash · Bulbul — same agent platform.",
        nav_aria="TTS engines",
        overview_fit="your voice layer",
        cta_desc="Book a walkthrough — hear live agent voice, compare engines, and map profiles to campaigns.",
        segment_type="tts",
        hub_label_key="short",
    )



def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = ["      { id: 'tts', label: 'TTS layer', path: 'pages/integrations/tts.html' },"]
    for p in PROVIDERS:
        label = p["name"]
        lines.append(
            f"      {{ id: '{p['slug']}', label: '{label}', path: 'pages/integrations/{p['slug']}.html' }},"
        )
    block = "    tts: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    tts: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    prepare()
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "tts.html").write_text(
        render_hub(HUB_CFG, PROVIDERS, jump_label_key="short", hub_tile_label_key="short"), encoding="utf-8"
    )
    for p in PROVIDERS:
        (INT / f"{p['slug']}.html").write_text(write_partner(p), encoding="utf-8")
    update_routes()
    print(f"OK: tts.html + {len(PROVIDERS)} partner pages, routes.js updated")


if __name__ == "__main__":
    main()
