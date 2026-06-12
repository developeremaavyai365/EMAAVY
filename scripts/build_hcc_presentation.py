#!/usr/bin/env python3
"""Inject presentation slides into hero command center."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

SLIDES = [
    {
        "id": "agents",
        "kicker": "01 — AI Agents",
        "headline": "AI Agents That Never Miss a Conversation",
        "desc": "Autonomous agents handle live conversations across voice and messaging — qualifying leads, resolving issues, and escalating with full context. Sales and support teams scale without adding headcount.",
        "visual": '''<div class="hcc-vis--agents"><div class="hcc-vis-chat"><span class="hcc-vis-bubble hcc-vis-bubble--in">Interested in enterprise pricing?</span><span class="hcc-vis-bubble hcc-vis-bubble--out">I can walk you through plans and book a demo.</span><span class="hcc-vis-bubble hcc-vis-bubble--in">Tomorrow at 3pm works.</span></div><div class="hcc-vis-reason"><div class="hcc-vis-step is-live"><i>1</i>Detect intent</div><div class="hcc-vis-step"><i>2</i>Qualify lead</div><div class="hcc-vis-step"><i>3</i>Book meeting</div></div></div>''',
        "outcomes": ["24/7 coverage", "Faster qualification", "Higher conversion", "Lower handle time"],
        "usecases": ["Inbound sales", "Support triage", "Appointment booking", "Lead follow-up"],
    },
    {
        "id": "telephony",
        "kicker": "02 — Communication",
        "headline": "Enterprise Telephony Built for Scale",
        "desc": "Route inbound and outbound calls through intelligent voice infrastructure. Emaavy connects carriers, AI agents, and human handoffs in one orchestrated layer built for high-volume operations.",
        "visual": '''<div class="hcc-vis--telephony"><div class="hcc-vis-route"><span class="hcc-vis-route-node hcc-vis-route-node--hub">Emaavy Core</span><span class="hcc-vis-route-line"></span><div class="hcc-vis-route-row"><span class="hcc-vis-route-node">Inbound</span><span class="hcc-vis-route-pulse"></span><span class="hcc-vis-route-node">AI Agent</span><span class="hcc-vis-route-node">Human</span></div><div class="hcc-vis-route-row"><span class="hcc-vis-route-node">Outbound</span><span class="hcc-vis-route-node">Campaign</span></div></div></div>''',
        "outcomes": ["Sub-second routing", "Zero dropped handoffs", "Global scale", "Live call intelligence"],
        "usecases": ["Inbound support", "Outbound sales", "Appointment scheduling", "Collections"],
    },
    {
        "id": "whatsapp",
        "kicker": "02 — Communication",
        "headline": "WhatsApp Engagement at Enterprise Scale",
        "desc": "Meet customers on their preferred channel with compliant, conversational WhatsApp flows — synced with CRM, agents, and campaigns so every message drives action.",
        "visual": '''<div class="hcc-vis--whatsapp"><span class="hcc-vis-wa-header">WhatsApp · Live thread</span><span class="hcc-vis-wa-msg">Hi — I need help with my order</span><span class="hcc-vis-wa-msg hcc-vis-wa-msg--brand">Found your account. Resolving now.</span><span class="hcc-vis-wa-msg">Thank you!</span></div>''',
        "outcomes": ["Higher open rates", "Faster resolution", "Unified context", "Campaign reach"],
        "usecases": ["Customer support", "Order updates", "Lead nurturing", "Payment reminders"],
    },
    {
        "id": "crm",
        "kicker": "03 — Customer Data",
        "headline": "CRM That Stays in Sync With Every Conversation",
        "desc": "Leads, contacts, and deals update automatically from calls, chats, and workflows. Revenue teams work from one live customer record — never stale data, never manual entry.",
        "visual": '''<div class="hcc-vis--crm"><div class="hcc-vis-pipe-col"><span class="hcc-vis-pipe-label">Lead</span><div class="hcc-vis-pipe-cards"><span class="hcc-vis-pipe-card"></span><span class="hcc-vis-pipe-card"></span></div></div><div class="hcc-vis-pipe-col"><span class="hcc-vis-pipe-label">Qualified</span><div class="hcc-vis-pipe-cards"><span class="hcc-vis-pipe-card"></span></div></div><div class="hcc-vis-pipe-col"><span class="hcc-vis-pipe-label">Opportunity</span><div class="hcc-vis-pipe-cards"><span class="hcc-vis-pipe-card"></span></div></div><div class="hcc-vis-pipe-col"><span class="hcc-vis-pipe-label">Customer</span><div class="hcc-vis-pipe-cards"><span class="hcc-vis-pipe-card"></span></div></div></div>''',
        "outcomes": ["Clean pipeline data", "Faster deal velocity", "Revenue visibility", "Zero duplicate entry"],
        "usecases": ["Lead sync", "Deal updates", "Account health", "Renewal tracking"],
    },
    {
        "id": "workflows",
        "kicker": "04 — Automation",
        "headline": "Workflows That Run Your Business Logic",
        "desc": "Design multi-step automations that connect agents, channels, and systems. Triggers fire on conversation events, schedule rules, or CRM changes — with full audit trails.",
        "visual": '''<div class="hcc-vis--workflows"><div class="hcc-vis-flow"><span class="hcc-vis-flow-node is-running">Trigger</span><span class="hcc-vis-flow-arrow"><span class="hcc-vis-flow-dot"></span></span><span class="hcc-vis-flow-node">Reason</span><span class="hcc-vis-flow-arrow"></span><span class="hcc-vis-flow-node">Act</span><span class="hcc-vis-flow-arrow"></span><span class="hcc-vis-flow-node">Sync</span></div></div>''',
        "outcomes": ["Less manual work", "Consistent processes", "Faster SLAs", "Audit-ready ops"],
        "usecases": ["Escalation rules", "Onboarding flows", "Approval chains", "Post-call actions"],
    },
    {
        "id": "campaigns",
        "kicker": "05 — Outreach",
        "headline": "Campaigns That Run Themselves",
        "desc": "Launch sequenced outreach across voice and messaging with intelligent timing, personalization, and automatic follow-ups — all orchestrated through Emaavy Core.",
        "visual": '''<div class="hcc-vis--campaigns"><div class="hcc-vis-timeline"><div class="hcc-vis-tl-step is-done"><span class="hcc-vis-tl-dot"></span><span class="hcc-vis-tl-label">Segment</span></div><div class="hcc-vis-tl-step is-done"><span class="hcc-vis-tl-dot"></span><span class="hcc-vis-tl-label">Send</span></div><div class="hcc-vis-tl-step is-active"><span class="hcc-vis-tl-dot"></span><span class="hcc-vis-tl-label">Follow-up</span></div><div class="hcc-vis-tl-step"><span class="hcc-vis-tl-dot"></span><span class="hcc-vis-tl-label">Convert</span></div></div></div>''',
        "outcomes": ["More touchpoints", "Higher reply rates", "Automated nurture", "Pipeline growth"],
        "usecases": ["Lead nurturing", "Re-engagement", "Event invites", "Renewal outreach"],
    },
    {
        "id": "integrations",
        "kicker": "06 — Ecosystem",
        "headline": "Integrations That Connect Your Entire Stack",
        "desc": "Plug telephony, LLMs, CRM, calendars, and custom tools into one API layer. Swap providers per workflow without rebuilding — your stack evolves, Emaavy orchestrates.",
        "visual": '''<div class="hcc-vis--integrations"><div class="hcc-vis-hub"><span class="hcc-vis-hub-core">Core</span><span class="hcc-vis-hub-spoke">CRM</span><span class="hcc-vis-hub-spoke">LLM</span><span class="hcc-vis-hub-spoke">Voice</span><span class="hcc-vis-hub-spoke">Calendar</span></div></div>''',
        "outcomes": ["Faster deployment", "Vendor flexibility", "Unified data flow", "Lower IT overhead"],
        "usecases": ["Salesforce sync", "HubSpot pipeline", "Calendar booking", "Custom webhooks"],
    },
    {
        "id": "analytics",
        "kicker": "07 — Intelligence",
        "headline": "Analytics That Turn Conversations Into Insight",
        "desc": "Live dashboards surface agent performance, conversion trends, and operational KPIs — so leaders see what is working and teams improve with data, not guesswork.",
        "visual": '''<div class="hcc-vis--analytics"><div class="hcc-vis-bars"><span class="hcc-vis-bar"></span><span class="hcc-vis-bar"></span><span class="hcc-vis-bar"></span><span class="hcc-vis-bar"></span><span class="hcc-vis-bar"></span></div><div class="hcc-vis-kpis"><div class="hcc-vis-kpi">Conversion <strong>+34%</strong> <span class="hcc-vis-kpi-trend">↑</span></div><div class="hcc-vis-kpi">Avg. handle <strong>−28%</strong> <span class="hcc-vis-kpi-trend">↓</span></div><div class="hcc-vis-kpi">CSAT <strong>4.8</strong> <span class="hcc-vis-kpi-trend">↑</span></div></div></div>''',
        "outcomes": ["Executive visibility", "Team coaching", "Trend detection", "ROI proof"],
        "usecases": ["Executive dashboards", "Agent scorecards", "Campaign ROI", "Capacity planning"],
    },
    {
        "id": "knowledge",
        "kicker": "08 — Enterprise Ops",
        "headline": "Knowledge Bases That Power Every Agent",
        "desc": "Centralize policies, product docs, and playbooks so AI agents and human teams answer with accuracy. Knowledge stays indexed, searchable, and synced across every conversation.",
        "visual": '''<div class="hcc-vis--knowledge"><div class="hcc-vis-docs"><span class="hcc-vis-doc is-indexed"></span><span class="hcc-vis-doc is-indexed"></span><span class="hcc-vis-doc"></span><span class="hcc-vis-doc is-indexed"></span></div><div class="hcc-vis-search"><span class="hcc-vis-search-bar">Refund policy for enterprise?</span><span class="hcc-vis-search-hit">3 sources matched · 98% confidence</span></div></div>''',
        "outcomes": ["Accurate answers", "Faster onboarding", "Consistent messaging", "Reduced escalations"],
        "usecases": ["Agent grounding", "Policy lookup", "Product Q&amp;A", "Compliance docs"],
    },
    {
        "id": "automation",
        "kicker": "08 — Enterprise Ops",
        "headline": "Automation That Eliminates Operational Friction",
        "desc": "Trigger actions from any signal — a keyword in a call, a CRM stage change, or a missed follow-up. Emaavy runs the logic so teams focus on high-value work.",
        "visual": '''<div class="hcc-vis--automation"><div class="hcc-vis-trigger"><span class="hcc-vis-trigger-tag">Call ended</span><span>→ evaluate outcome</span></div><div class="hcc-vis-auto-chain"><span class="hcc-vis-auto-block is-firing">Update CRM</span><span>→</span><span class="hcc-vis-auto-block">Send WhatsApp</span><span>→</span><span class="hcc-vis-auto-block">Notify manager</span></div></div>''',
        "outcomes": ["Reduced manual tasks", "Fewer errors", "Shorter cycles", "Predictable ops"],
        "usecases": ["Post-call sync", "SLA alerts", "Data enrichment", "Task routing"],
    },
    {
        "id": "support",
        "kicker": "08 — Enterprise Ops",
        "headline": "Customer Support Built for Enterprise Volume",
        "desc": "Route, prioritize, and resolve tickets across voice and messaging with AI-first triage and seamless human escalation — every customer gets the right response, fast.",
        "visual": '''<div class="hcc-vis--support"><div class="hcc-vis-ticket"><span class="hcc-vis-ticket-pri"></span><span>Billing inquiry · Priority</span><span class="hcc-vis-ticket-status">AI handling</span></div><div class="hcc-vis-ticket is-resolved"><span class="hcc-vis-ticket-pri"></span><span>Order status · Resolved</span><span class="hcc-vis-ticket-status">Closed</span></div><div class="hcc-vis-ticket"><span class="hcc-vis-ticket-pri"></span><span>Technical issue · Escalated</span><span class="hcc-vis-ticket-status">Human</span></div></div>''',
        "outcomes": ["Faster resolution", "Higher CSAT", "Lower cost per ticket", "Smart escalation"],
        "usecases": ["Tier-1 deflection", "Priority routing", "After-hours coverage", "CSAT recovery"],
    },
    {
        "id": "sales",
        "kicker": "08 — Enterprise AI OS",
        "headline": "Sales Operations Orchestrated End to End",
        "desc": "From first touch to closed deal — Emaavy connects prospecting, conversations, CRM, and analytics into one operating system. This is the complete Enterprise AI platform story.",
        "visual": '''<div class="hcc-vis--sales"><div class="hcc-vis-funnel"><span class="hcc-vis-funnel-stage"></span><span class="hcc-vis-funnel-stage"></span><span class="hcc-vis-funnel-stage"></span><span class="hcc-vis-funnel-stage"></span></div><div class="hcc-vis-sales-metrics"><div class="hcc-vis-sales-metric">Pipeline velocity<strong>+41%</strong></div><div class="hcc-vis-sales-metric">Meetings booked<strong>3.2×</strong></div></div></div>''',
        "outcomes": ["Revenue acceleration", "Rep productivity", "Forecast accuracy", "Unified GTM"],
        "usecases": ["Outbound prospecting", "Demo scheduling", "Deal coaching", "Revenue reporting"],
    },
]


def build_slide_html(s: dict, idx: int) -> str:
    outcomes = "".join(f'<span class="hcc-slide-outcome">{o}</span>' for o in s["outcomes"])
    cases = "".join(f"<li>{c}</li>" for c in s["usecases"])
    return (
        f'<article class="hcc-slide" data-slide="{s["id"]}" role="tabpanel" aria-hidden="true">'
        f'<span class="hcc-slide-kicker">{s["kicker"]}</span>'
        f'<h3 class="hcc-slide-headline">{s["headline"]}</h3>'
        f'<p class="hcc-slide-desc">{s["desc"]}</p>'
        f'<div class="hcc-slide-visual">{s["visual"]}</div>'
        f'<div class="hcc-slide-outcomes">{outcomes}</div>'
        f'<div class="hcc-slide-usecases"><span class="hcc-slide-usecases-label">Use cases</span>'
        f'<ul class="hcc-slide-usecase-list">{cases}</ul></div>'
        f"</article>"
    )


def build_presentation_html() -> str:
    slides = "".join(build_slide_html(s, i) for i, s in enumerate(SLIDES))
    return (
        '<div class="hcc-presentation" aria-label="Emaavy capability presentation">'
        '<div class="hcc-pres-toolbar">'
        '<button type="button" class="hcc-pres-back" aria-label="Return to orbit view">← Orbit</button>'
        '<span class="hcc-pres-progress" data-hcc-pres-progress><strong>1</strong> / 12</span>'
        '<div class="hcc-pres-nav-group">'
        '<button type="button" class="hcc-pres-nav hcc-pres-nav--prev" aria-label="Previous capability">←</button>'
        '<button type="button" class="hcc-pres-nav hcc-pres-nav--next" aria-label="Next capability">→</button>'
        '</div></div>'
        f'<div class="hcc-slides-viewport">{slides}</div>'
        "</div>"
    )


def main():
    text = INDEX.read_text(encoding="utf-8")

    # Wrap orbit content in hcc-orbit-layer if not already
    if "hcc-orbit-layer" not in text:
        text = text.replace(
            '<div class="hcc-stage"><div class="hcc-ambient"',
            '<div class="hcc-stage"><div class="hcc-orbit-layer"><div class="hcc-ambient"',
            1,
        )
        # Close orbit layer before presentation or before closing hcc-stage
        if "hcc-presentation" not in text:
            pres = build_presentation_html()
            text = text.replace(
                '<div class="hcc-status">',
                "</div>" + pres + '<div class="hcc-status">',
                1,
            )
        else:
            # insert closing div before presentation
            text = text.replace(
                '<div class="hcc-presentation"',
                "</div><div class=\"hcc-presentation\"",
                1,
            )
    else:
        # Replace presentation block
        pres = build_presentation_html()
        text = re.sub(
            r'<div class="hcc-presentation"[^>]*>.*?</div>(?=\s*<div class="hcc-status">)',
            pres,
            text,
            count=1,
            flags=re.DOTALL,
        )

    # Add slides CSS link if missing
    if "hero-command-center-slides.css" not in text:
        text = text.replace(
            '<link rel="stylesheet" href="assets/hero-command-center.css" />',
            '<link rel="stylesheet" href="assets/hero-command-center.css" />\n'
            '  <link rel="stylesheet" href="assets/hero-command-center-slides.css" />',
        )

    INDEX.write_text(text, encoding="utf-8")
    print("Presentation slides injected.")


if __name__ == "__main__":
    main()
