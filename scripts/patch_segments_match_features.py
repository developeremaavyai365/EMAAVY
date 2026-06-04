"""Match agents, case-studies, bento, journey, docs to #features (Platform Capabilities)."""
from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

CAP = "#features, #agents, #case-studies, #bento, #journey, #docs"

def card(n, detail, title, desc, tag):
    return (
        f'<article class="hiw-step reveal click-detail" data-detail="{detail}" tabindex="0">'
        f'<div class="hiw-step-num">{n}</div><span class="hiw-step-icon" aria-hidden="true"></span>'
        f"<h4>{title}</h4><p>{desc}</p>"
        f'<span class="hiw-step-tag">{tag}</span>'
        f'<span class="hiw-step-hint">Explore capability →</span></article>'
    )


def section(sid, kicker, h2, p, cards, stats):
    cards_html = " ".join(cards)
    return (
        f'<section id="{sid}"> <div class="features-head reveal"> '
        f'<span class="section-kicker">{kicker}</span> <h2>{h2}</h2> <p>{p}</p> </div> '
        f'<div class="hiw-steps"> {cards_html} </div> {stats} </section>'
    )


def stats(a, b, c):
    return (
        '<div class="platform-stats"> '
        f'<div class="platform-stat"><b>{a[0]}</b><span>{a[1]}</span></div> '
        f'<div class="platform-stat"><b>{b[0]}</b><span>{b[1]}</span></div> '
        f'<div class="platform-stat"><b>{c[0]}</b><span>{c[1]}</span></div> '
        "</div>"
    )


SECTIONS = {
    "agents": section(
        "agents",
        "AI Workforce · Voice Agents",
        "Meet your AI workforce",
        "Agents that speak like humans, think faster, and never call in sick. Deploy in minutes — each with its own voice, flow, and mission — running 24/7 across every language you serve.",
        [
            card(
                1,
                "agent-sales",
                "Sales Agent",
                "Qualifies leads, handles objections, and books meetings — with natural Hinglish and regional language fluency.",
                "Voice · Sales",
            ),
            card(
                2,
                "agent-support",
                "Support Agent",
                "Resolves issues, de-escalates frustrated callers, and routes complex cases to humans with full context.",
                "Voice · Support",
            ),
            card(
                3,
                "agent-campaign",
                "Campaign Agent",
                "Runs high-volume outreach flows — registrations, follow-ups, and reminders across thousands of contacts.",
                "Outbound · Campaigns",
            ),
            card(
                4,
                "agents-overview",
                "Custom Agent Builder",
                "Design any voice flow in minutes — pick a voice, set prompts, branch logic, and deploy across languages.",
                "AI Agents · Builder",
            ),
        ],
        stats(("24/7", "Always on"), ("22", "Languages"), ("3,241", "Calls today")),
    ),
    "case-studies": section(
        "case-studies",
        "Client Success · Case Studies",
        "What we've built for our clients",
        "Real results from real campaigns — from exhibition registrations to enterprise QA automation and multilingual follow-ups at scale.",
        [
            card(
                1,
                "cs-mudita",
                "Exhibition Registration Campaign",
                "Deployed Priya as an outbound agent to call 5,000 potential attendees — personalised Hindi and English conversations with real-time registration capture.",
                "Warehouse by Mudita · 68%",
            ),
            card(
                2,
                "cs-nextcall",
                "QA Automation at Scale",
                "Replaced manual call auditing with EMAAVY's real-time intelligence — every call scored for sentiment, compliance, and intent automatically.",
                "NextCall BPO · 61% faster QA",
            ),
            card(
                3,
                "cs-fleetiq",
                "Driver Follow-Up Automation",
                "Automated post-delivery follow-up calls to 50,000 customers per month across 8 Indian languages — unhappy callers routed to humans in 60 seconds.",
                "FleetIQ · 28% CSAT lift",
            ),
        ],
        stats(("68%", "Peak conversion"), ("50K+", "Calls / month"), ("61%", "Faster QA")),
    ),
    "bento": section(
        "bento",
        "Intelligence matrix · Analytics engine",
        "Your call intelligence command center",
        "Every metric, every insight — decoded in real time. From live transcripts to intent scoring, operator leaderboards, and compliance flags — all in one unified dashboard.",
        [
            card(
                1,
                "bento-volume",
                "Calls Processed",
                "Total call volume across all campaigns — with breakdown by language, agent, outcome, and time of day.",
                "Volume · 10M+ decoded",
            ),
            card(
                2,
                "bento-realtime",
                "Real-Time Ears",
                "Words appear as they're spoken — live captions, sentiment indicators, and supervisor intervention for every seat.",
                "Live stream · Real-time",
            ),
            card(
                3,
                "bento-intent",
                "Intent Mapping",
                "Know when they're buying, stalling, or slipping away — visual funnel updated live across every campaign.",
                "Intent engine · Funnel",
            ),
            card(
                4,
                "bento-ops",
                "Operator Performance",
                "Agent and AI operator leaderboard — conversion rate, handle time, sentiment score, and coaching compliance.",
                "Operator view · Rankings",
            ),
            card(
                5,
                "bento-latency",
                "Sub-500ms Latency",
                "End-to-end latency monitoring — transcription, LLM inference, and trigger execution with SLA alerting.",
                "System health · P99",
            ),
            card(
                6,
                "bento-security",
                "Enterprise Secure",
                "SOC-ready encryption, PII detection, flagged call review, and full audit log export — your calls stay yours.",
                "Compliance · SOC 2",
            ),
        ],
        stats(("10M+", "Calls processed"), ("99%", "Decode accuracy"), ("&lt;0.5s", "Live latency")),
    ),
    "journey": section(
        "journey",
        "Call lifecycle · End-to-end flow",
        "The call journey — step by step",
        "From ring to learn — every stage is captured, scored, and turned into action automatically. No batch processing, no manual handoffs, no intelligence left on the table.",
        [
            card(
                1,
                "journey-1",
                "Call Connects",
                "The moment the call connects, EMAAVY begins listening — capturing audio, metadata, and speaker context instantly.",
                "Step 1 · Ring",
            ),
            card(
                2,
                "journey-2",
                "Every Word Captured",
                "Deepgram and Sarvam stream every word to the intelligence layer in real time — no batch processing delay.",
                "Step 2 · Transcribe",
            ),
            card(
                3,
                "journey-3",
                "Score Live",
                "Sentiment, intent, objections, and compliance risk scored on every conversational turn — not after the call ends.",
                "Step 3 · Analyze",
            ),
            card(
                4,
                "journey-4",
                "Triggers Fire",
                "CRM updates, WhatsApp messages, calendar bookings, and coaching alerts fire automatically from call intelligence.",
                "Step 4 · Act",
            ),
            card(
                5,
                "journey-5",
                "Models Improve",
                "Every call feeds back into model fine-tuning, script optimization, and coaching — the system gets sharper over time.",
                "Step 5 · Learn",
            ),
        ],
        stats(("5", "Lifecycle stages"), ("&lt;0.5s", "Transcription"), ("100%", "Automated")),
    ),
    "docs": section(
        "docs",
        "Documentation",
        "Build with EMAAVY",
        "Guides, API references, and quickstarts to get your first agent live in under an hour.",
        [
            card(
                1,
                "docs-quickstart",
                "Quickstart Guide",
                "Launch your first outbound campaign in 15 minutes — from signup to first call.",
                "Guides · Quickstart",
            ),
            card(
                2,
                "docs-api",
                "API Reference",
                "Webhooks, REST endpoints, and event schemas for custom integrations.",
                "API · Reference",
            ),
            card(
                3,
                "docs-agents",
                "Agent Builder",
                "Design voice flows, configure prompts, and deploy agents across languages.",
                "Agents · Builder",
            ),
        ],
        stats(("15 min", "To first call"), ("REST", "API surface"), ("22", "Languages")),
    ),
}


def patch_css(text: str) -> str:
    start = text.find("/* ═══ ELEGANT FEATURES — refined shell (HIW cards below) ═══ */")
    end = text.find("/* ═══ ELEGANT TEMPLATE — refined shell, cards preserved ═══ */")
    if start < 0 or end < 0:
        raise SystemExit("features CSS block not found")

    block = text[start:end]
    block = block.replace("#features", CAP)
    # ::before on multiple ids
    block = block.replace(
        f"{CAP}::before,\n.features-glow,",
        f"{CAP}::before,\n.features-glow,",
    )
    text = text[:start] + block + text[end:]

    # Animation kill list
    text = text.replace(
        "#features::before, .template-shell::before",
        f"{CAP}::before, .template-shell::before",
    )

    return text


def patch_html(text: str) -> str:
    for sid, new_html in SECTIONS.items():
        m = re.search(rf"<section id=\"{sid}\"[^>]*>.*?</section>", text, re.DOTALL)
        if not m:
            raise SystemExit(f"section {sid} not found")
        text = text[: m.start()] + new_html + text[m.end() :]
        print(f"patched {sid}")
    return text


def main():
    text = HTML.read_text(encoding="utf-8")
    text = patch_css(text)
    text = patch_html(text)
    HTML.write_text(text, encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
