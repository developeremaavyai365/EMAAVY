#!/usr/bin/env python3
"""Generate Case Studies hub + per-client story pages."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from case_study_logos import apply_case_study_icons, ensure_icons
from case_studies_pages_common import render_hub, render_study

ROOT = Path(__file__).resolve().parents[1]
CS_DIR = ROOT / "pages" / "case-studies"
HUB = ROOT / "pages" / "case-studies.html"

STUDIES = [
    {
        "slug": "mudita",
        "name": "Warehouse by Mudita",
        "short": "Mudita",
        "mark": "WA",
        "route": "case-study-mudita",
        "kicker": "Events · Outbound",
        "headline": "Exhibition Registration Campaign",
        "region": "Events · Luxury retail",
        "meta": "Warehouse by Mudita — 68% exhibition registration with EMAAVY bilingual outbound voice vs 12% email baseline across 5,000 prospects.",
        "lead": "Warehouse by Mudita needed to fill a luxury designer exhibition — not with cold email, but with warm, bilingual voice conversations that captured registrations in real time.",
        "stats": [("68%", "Registration rate"), ("5,000", "Contacts reached"), ("12%", "Email baseline")],
        "challenge": [
            "The marketing team had a list of 5,000 high-value prospects but email campaigns plateaued at a 12% registration rate. Manual calling was too slow for the exhibition timeline, and scripts in English alone missed a large Hindi-speaking audience.",
            "They needed measurable conversion before the event date — without hiring a temporary outbound floor or losing brand tone on every call.",
        ],
        "solution_lead": "EMAAVY deployed Priya, a campaign voice agent fluent in Hindi and English with natural code-switching. Every call captured intent, objections, and registration details live — then triggered WhatsApp confirmations automatically.",
        "solution_points": [
            ("Bilingual voice agent", "Hinglish fluency with Bulbul V3 and Sarvam STT for natural code-switching."),
            ("Live registration capture", "Structured fields written to CRM during the call — zero manual entry."),
            ("WhatsApp automation", "Confirmation and show-rate lift within 30 seconds of verbal yes."),
            ("Supervisor pacing", "Ops adjusted connect windows hourly from the EMAAVY dashboard."),
        ],
        "stack": ["Outbound Agent", "Sarvam STT", "Bulbul V3", "WhatsApp", "Webhooks"],
        "implementation": [
            ("Audience upload", "5,000 contacts segmented by city and language preference."),
            ("Agent configuration", "Priya outbound flow with exhibition details, pricing FAQ, and registration capture."),
            ("Live routing", "Sarvam STT for Hinglish, Bulbul V3 voice, and Qwen for cost-efficient dialogue."),
            ("Post-call automation", "WhatsApp ticket + calendar hold sent within 30 seconds of a yes."),
            ("Supervisor view", "Ops monitored conversion by hour and adjusted pacing in the dashboard."),
        ],
        "results_highlights": [
            ("5.6× email lift", "68% registration vs 12% email-only baseline."),
            ("3,400 attendees", "Confirmed with structured CRM fields from voice."),
            ("Sub-4 min AHT", "Average handle time with zero manual data entry."),
            ("+11% show-rate", "WhatsApp follow-up after verbal commitment."),
        ],
        "results_bullets": [
            "68% registration rate — 5.6× improvement over email alone",
            "3,400 confirmed attendees captured with structured CRM fields",
            "Average handle time under 4 minutes with zero manual data entry",
            "WhatsApp follow-up lifted show-rate by an additional 11%",
        ],
        "hub_desc": "5,000 bilingual outbound calls for a luxury designer exhibition — 68% registration vs 12% email.",
        "hub_points": ["68% registration rate", "Bilingual Hinglish agent", "WhatsApp confirmations"],
        "hub_badge": "Events · Outbound",
    },
    {
        "slug": "nextcall",
        "name": "NextCall BPO",
        "short": "NextCall",
        "mark": "NE",
        "route": "case-study-nextcall",
        "kicker": "BPO · Quality Assurance",
        "headline": "QA Automation at Scale",
        "region": "BPO · Quality assurance",
        "meta": "NextCall BPO — 100% call coverage and 61% faster QA with EMAAVY real-time transcription, sentiment, and compliance scoring.",
        "lead": "NextCall BPO replaced sample-based manual auditing with EMAAVY's real-time intelligence — every call scored for sentiment, compliance, and intent the moment it happens.",
        "stats": [("61%", "Faster QA"), ("100%", "Call coverage"), ("5%", "Prior manual sample")],
        "challenge": [
            "Quality teams could only audit about 5% of calls manually. Coaching was delayed, compliance gaps were discovered days later, and supervisors had no live signal when calls went off-script.",
            "Scaling headcount to review every conversation was economically impossible across their regulated client programs.",
        ],
        "solution_lead": "EMAAVY ingested the full call stream, transcribed in real time, and scored every turn for sentiment, compliance keywords, and buyer intent. Supervisors received coaching alerts during active calls instead of after batch reviews.",
        "solution_points": [
            ("100% call coverage", "Every conversation transcribed and scored — not a 5% sample."),
            ("Live supervisor feed", "Sentiment color coding and compliance flags during active calls."),
            ("Compliance lexicon", "Script deviations flagged within the call, not days later."),
            ("Webhook QA sync", "Scores and summaries pushed to internal QA tools automatically."),
        ],
        "stack": ["Deepgram STT", "Claude Sonnet", "Webhooks", "Exotel", "Call Intelligence"],
        "implementation": [
            ("Telephony connect", "Exotel numbers routed through EMAAVY with zero agent workflow change."),
            ("Scoring models", "Compliance lexicon + intent tiers tuned to NextCall's regulated scripts."),
            ("Supervisor console", "Live transcript feed with sentiment color coding per seat."),
            ("QA dashboards", "Per-agent compliance score, objection tags, and auto-generated summaries."),
            ("CRM sync", "Disposition and score pushed to internal QA tools via webhooks."),
        ],
        "results_highlights": [
            ("100% coverage", "Full call stream vs 5% manual audit sampling."),
            ("61% faster QA", "Reduction in time spent on review cycles."),
            ("In-call compliance", "Violations flagged while the conversation is live."),
            ("Real-time coaching", "Suggestions delivered to team leads during calls."),
        ],
        "results_bullets": [
            "100% call coverage vs 5% manual audit sampling",
            "61% reduction in time spent on QA review cycles",
            "Compliance violations flagged within the call, not days later",
            "Coaching suggestions delivered to team leads in real time",
        ],
        "hub_desc": "100% call coverage with real-time sentiment, compliance, and intent scoring.",
        "hub_points": ["61% faster QA cycles", "Live supervisor alerts", "Full call stream scoring"],
        "hub_badge": "BPO · QA",
    },
    {
        "slug": "fleetiq",
        "name": "FleetIQ Logistics",
        "short": "FleetIQ",
        "mark": "FL",
        "route": "case-study-fleetiq",
        "kicker": "Logistics · Customer Experience",
        "headline": "Driver Follow-Up Automation",
        "region": "Logistics · Post-delivery CX",
        "meta": "FleetIQ Logistics — 28% CSAT lift and 50K monthly follow-up calls with multilingual EMAAVY support agents and 60-second escalation.",
        "lead": "FleetIQ automated post-delivery follow-ups across eight Indian languages — unhappy customers reach a human specialist in under 60 seconds, while satisfied deliveries scale without adding headcount.",
        "stats": [("28%", "CSAT lift"), ("50K", "Calls / month"), ("60s", "Escalation SLA")],
        "challenge": [
            "Fifty thousand deliveries per month meant fifty thousand potential support calls. A small team could not staff every language, and delayed follow-ups hurt CSAT scores in regional markets.",
            "Negative experiences needed immediate human intervention — but manual outbound teams could not keep pace with delivery volume.",
        ],
        "solution_lead": "EMAAVY support-style agents placed outbound follow-up calls in the customer's preferred language, detected negative sentiment live, and warm-transferred frustrated callers to human agents with full transcript context.",
        "solution_points": [
            ("Eight-language routing", "Regional language auto-selected from delivery metadata."),
            ("Sentiment gates", "Negative shift triggers supervisor alert and human bridge in under 60s."),
            ("Script library", "Delivery confirmation, damage report, and reschedule branches."),
            ("Helpdesk ticketing", "Issues logged with full transcript attachment."),
        ],
        "stack": ["Support Agent", "Sarvam STT", "Sentiment scoring", "Webhooks", "Human handoff"],
        "implementation": [
            ("Language routing", "Eight regional languages auto-selected from delivery metadata."),
            ("Sentiment gates", "Negative shift triggers supervisor alert and human bridge in &lt;60s."),
            ("Script library", "Delivery confirmation, damage report, and reschedule branches."),
            ("Ticketing", "Issues logged to FleetIQ helpdesk with transcript attachment."),
            ("Monthly scale", "Campaign pacing handles 50K+ contacts with retry and timezone rules."),
        ],
        "results_highlights": [
            ("50K calls / month", "Automated follow-ups without proportional hiring."),
            ("28% CSAT lift", "Measured over 90 days post-launch."),
            ("60s escalation", "Negative-sentiment callers reach humans with context."),
            ("Full handoff brief", "Issue, language, and transcript summary for specialists."),
        ],
        "results_bullets": [
            "50,000 automated follow-up calls per month without proportional hiring",
            "28% CSAT improvement measured over 90 days post-launch",
            "60-second escalation SLA for negative-sentiment callers",
            "Human agents receive full context — issue, language, and transcript summary",
        ],
        "hub_desc": "50,000 multilingual post-delivery calls per month with smart escalation.",
        "hub_points": ["28% CSAT lift", "8 languages", "60s human escalation"],
        "hub_badge": "Logistics · CX",
    },
]

HUB_CFG = {
    "route": "case-studies",
    "title": "Case Studies — EMAAVY",
    "meta": "Real EMAAVY client results — exhibition campaigns, BPO QA automation, and logistics follow-ups with measurable ROI.",
    "og_title": "Case Studies — EMAAVY",
    "og_description": "Client success stories with challenge, EMAAVY rollout, and measured outcomes.",
    "kicker": "Client Success · Proof",
    "h1": "Real results from client stories",
    "lead": "Exhibition campaigns, BPO quality programs, and logistics at scale — each story documents the challenge, EMAAVY implementation, and outcomes measured after go-live.",
    "stats": [("68%", "Peak conversion"), ("50K+", "Calls / month"), ("61%", "Faster QA")],
    "anchor_jumps": [],
    "layer_id": "proof-layer",
    "layer_num": "Client proof",
    "layer_tag": "EMAAVY · Case Studies",
    "layer_h2": "Why enterprises trust EMAAVY outcomes",
    "layer_lead": "Every story follows the same arc — a business constraint, an EMAAVY voice and intelligence rollout, and metrics captured in production. No vanity slides; only measured lift against prior baselines.",
    "pills": [
        ("Proven conversion", "Voice beats email and manual outreach on high-intent lists."),
        ("Full call coverage", "Score every conversation — not 5% spot checks."),
        ("Multilingual scale", "Regional programs without proportional hiring."),
        ("Fast escalation", "Humans join with transcript context when risk spikes."),
    ],
    "stories_id": "stories",
    "stories_h2": "Client stories",
    "stories_desc": "Three published case studies — each with a dedicated page covering challenge, solution, implementation, and results.",
    "flow_id": "rollout",
    "flow_h2": "From pilot to production proof",
    "flow_desc": "How teams typically move from first story to scaled programs on EMAAVY.",
    "flow_steps": [
        ("Align on KPI", "Pick conversion, CSAT, or QA coverage targets."),
        ("Design the program", "Agents, languages, and integration stack."),
        ("Pilot cohort", "Single campaign or queue before full traffic."),
        ("Measure live", "Dashboards vs email, manual, or sample QA baselines."),
        ("Scale", "Expand lists, languages, and supervisor playbooks."),
    ],
    "cta_h2": "Build your next success story on EMAAVY",
    "cta_desc": "See how voice programs perform in your industry — tailored demo with live calls and ROI framing.",
}


def prepare():
    for s in STUDIES:
        s["uses"] = list(s["results_highlights"])


def main():
    prepare()
    ensure_icons()
    hub_studies = []
    for s in STUDIES:
        hs = dict(s)
        apply_case_study_icons(hs, base="../")
        hub_studies.append(hs)
    for s in STUDIES:
        apply_case_study_icons(s, base="../../")
    CS_DIR.mkdir(parents=True, exist_ok=True)
    HUB.write_text(render_hub(HUB_CFG, hub_studies), encoding="utf-8")
    for s in STUDIES:
        (CS_DIR / f"{s['slug']}.html").write_text(render_study(s, studies=STUDIES), encoding="utf-8")
    print(f"OK: case-studies hub + {len(STUDIES)} detail pages")


if __name__ == "__main__":
    main()
