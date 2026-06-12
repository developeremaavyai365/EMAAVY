#!/usr/bin/env python3
"""Generate Tools & Workflow hub + per-tool integration pages."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from integration_logos import apply_logos_all
from integration_pages_common import ensure_uses, render_hub, render_partner

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

TOOLS = [
    {
        "slug": "webhooks",
        "name": "Webhooks",
        "short": "Webhooks",
        "region": "Custom events · Any stack",
        "tag": "Events",
        "route": "integration-webhooks",
        "logo": '<span class="brand-mark">WH</span>',
        "logo_sm": '<span class="brand-mark">WH</span>',
        "title": "Webhooks — EMAAVY",
        "h1": "Webhooks",
        "meta": "EMAAVY webhooks — push call events, transcripts, scores, and metadata to any endpoint in real time.",
        "lead": "Webhooks are the escape hatch that connects EMAAVY to everything else — your data warehouse, internal apps, Zapier, or bespoke ERP logic. Every call emits structured JSON the moment something meaningful happens.",
        "stats": [("Real-time", "Events"), ("Full", "Payloads"), ("HMAC", "Signing")],
        "about": [
            "Webhooks let EMAAVY notify your systems when calls start, turn, score, or complete — without polling APIs or batch CSV exports. Engineering teams define endpoints per environment and map events to internal queues.",
            "Unlike point CRM connectors alone, webhooks carry the full conversation intelligence layer: transcript snippets, intent scores, compliance flags, and agent metadata in one payload.",
        ],
        "emaavy": [
            ("Event catalog", "Subscribe to ring, answer, turn, disposition, and hangup events."),
            ("Signed deliveries", "Verify authenticity with shared secrets and replay protection."),
            ("Retry policy", "Automatic retries with backoff when your endpoint is briefly down."),
            ("Sandbox mode", "Test payloads in staging before production traffic."),
        ],
        "features": [
            ("call.started / ended", "Lifecycle hooks for orchestration."),
            ("turn.completed", "Per-utterance payloads for live dashboards."),
            ("disposition.extracted", "Structured CRM-ready fields."),
            ("Custom headers", "Auth tokens and trace IDs per request."),
            ("Payload filtering", "Send only fields your system needs."),
            ("OpenAPI docs", "Schema reference for engineering onboarding."),
        ],
        "uses": [
            ("Custom ERP sync", "Push dispositions into non-standard systems."),
            ("Data warehouse", "Stream events into Snowflake or BigQuery pipelines."),
            ("Automation hubs", "Trigger Zapier, Make, or internal workflow engines."),
        ],
        "setup": [
            ("Register endpoint URL", "HTTPS required for production environments."),
            ("Choose events", "Select which EMAAVY signals to forward."),
            ("Configure signing secret", "Validate payloads in your receiver."),
            ("Run test call", "Inspect payload in EMAAVY webhook debugger."),
        ],
        "hub_desc": "Push call events, transcripts, and scores to any HTTPS endpoint — your universal integration layer.",
        "hub_points": ["Real-time event stream", "Signed webhook deliveries", "Full transcript payloads"],
        "hub_badge": "Events",
    },
    {
        "slug": "salesforce",
        "name": "Salesforce",
        "short": "Salesforce",
        "region": "CRM · Enterprise",
        "tag": "CRM",
        "route": "integration-salesforce",
        "logo": '<img src="https://cdn.worldvectorlogo.com/logos/salesforce-2.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.worldvectorlogo.com/logos/salesforce-2.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Salesforce — EMAAVY",
        "h1": "Salesforce",
        "meta": "Salesforce and EMAAVY — auto-update leads, opportunities, tasks, and call dispositions from live voice intelligence.",
        "lead": "Salesforce is the system of record for most enterprise revenue teams — EMAAVY writes call outcomes, intent scores, and next steps into Salesforce objects so reps never re-key conversations after hang-up.",
        "stats": [("Leads & Opps", "Objects"), ("Tasks", "Auto-created"), ("Real-time", "Sync")],
        "about": [
            "Salesforce Sales Cloud stores contacts, leads, opportunities, and activities. Voice programs fail when dispositions stay in a dialer tab — EMAAVY closes the loop by mapping conversation intelligence to the right Salesforce fields on every call.",
            "Admins configure field mappings once; operations trusts that MEDDIC fields, stage changes, and follow-up tasks reflect what was actually said.",
        ],
        "emaavy": [
            ("Live disposition sync", "Update lead status and opportunity stage from extracted intent."),
            ("Task creation", "Schedule rep follow-ups when the agent books a callback."),
            ("Call logging", "Attach transcript summaries to activity timelines."),
            ("Campaign attribution", "Tie calls to Salesforce campaigns and UTMs."),
        ],
        "features": [
            ("Lead & Contact updates", "Write standard and custom fields."),
            ("Opportunity sync", "Move stages based on conversation outcomes."),
            ("Task & Event objects", "Create next-step work items automatically."),
            ("Custom object support", "Map to industry-specific Salesforce schemas."),
            ("OAuth security", "Enterprise-grade connected app flows."),
            ("Bulk-safe throttling", "Respect Salesforce API limits automatically."),
        ],
        "uses": [
            ("Enterprise sales", "Outbound SDR and AE programs on Salesforce."),
            ("Inside sales", "High-velocity teams needing zero manual CRM entry."),
            ("Revenue operations", "Governed field mapping across many campaigns."),
        ],
        "setup": [
            ("Connect Salesforce org", "OAuth via EMAAVY integrations console."),
            ("Map fields", "Align disposition codes to picklists and stages."),
            ("Test sandbox", "Run pilot calls in a Salesforce sandbox org."),
            ("Roll out per team", "Enable for one business unit before global default."),
        ],
        "hub_desc": "Update records, log dispositions, and push intent scores — no manual CRM entry after calls.",
        "hub_points": ["Lead and opportunity sync", "Automatic tasks", "Activity timeline logging"],
        "hub_badge": "CRM",
    },
    {
        "slug": "hubspot",
        "name": "HubSpot",
        "short": "HubSpot",
        "region": "CRM · Growth",
        "tag": "CRM",
        "route": "integration-hubspot",
        "logo": '<img src="https://cdn.simpleicons.org/hubspot/FF7A59" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/hubspot/FF7A59" alt="" width="32" height="32" loading="lazy" />',
        "title": "HubSpot — EMAAVY",
        "h1": "HubSpot",
        "meta": "HubSpot and EMAAVY — create deals, update contacts, and trigger workflows from live call intelligence.",
        "lead": "HubSpot powers growth teams from first touch to closed-won — EMAAVY feeds call transcripts, meeting outcomes, and lead scores into HubSpot so marketing automation and sales sequences stay accurate.",
        "stats": [("Contacts", "Updated"), ("Deals", "Created"), ("Workflows", "Triggered")],
        "about": [
            "HubSpot CRM combines contacts, companies, deals, and marketing workflows in one platform. PLG and mid-market teams rely on HubSpot timelines to see every buyer interaction — voice calls must appear there automatically.",
            "EMAAVY triggers HubSpot workflows when keywords, intents, or dispositions match — sending nurture emails, Slack alerts, or owner assignments without human middleware.",
        ],
        "emaavy": [
            ("Contact enrichment", "Write call notes and properties after every conversation."),
            ("Deal pipeline", "Create or advance deals from qualified calls."),
            ("Workflow triggers", "Fire HubSpot automations on intent thresholds."),
            ("Timeline events", "Log calls with summaries reps can skim in seconds."),
        ],
        "features": [
            ("Contact & company sync", "Keep CRM properties current."),
            ("Deal creation", "Open pipeline records from qualified calls."),
            ("Engagement logging", "Calls appear on contact timelines."),
            ("Workflow enrollment", "Add contacts to sequences based on outcomes."),
            ("Custom properties", "Map EMAAVY extraction to HubSpot fields."),
            ("API rate handling", "Batch updates respect HubSpot limits."),
        ],
        "uses": [
            ("PLG & mid-market", "Fast-moving teams on HubSpot Sales Hub."),
            ("Marketing + sales", "Align voice outcomes with email nurture."),
            ("Appointment setting", "Booked meetings advance deals automatically."),
        ],
        "setup": [
            ("Connect HubSpot app", "OAuth through EMAAVY integrations."),
            ("Define property map", "Match dispositions to HubSpot dropdowns."),
            ("Configure workflows", "Choose which intents trigger automations."),
            ("Pilot one pipeline", "Validate deal creation on a test segment."),
        ],
        "hub_desc": "Create deals, update contacts, and trigger HubSpot workflows from call intelligence.",
        "hub_points": ["Contact and deal sync", "Timeline call logging", "Workflow triggers"],
        "hub_badge": "CRM",
    },
    {
        "slug": "calcom",
        "name": "Cal.com",
        "short": "Cal.com",
        "region": "Scheduling · Open",
        "tag": "Scheduling",
        "route": "integration-calcom",
        "logo": '<img src="https://cdn.simpleicons.org/caldotcom/292929" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/caldotcom/292929" alt="" width="32" height="32" loading="lazy" />',
        "title": "Cal.com — EMAAVY",
        "h1": "Cal.com",
        "meta": "Cal.com and EMAAVY — book meetings live during AI voice calls with instant calendar holds.",
        "lead": "Cal.com is the open scheduling layer modern teams trust — on EMAAVY, voice agents check availability, propose slots, and confirm bookings while the caller is still on the line.",
        "stats": [("Live", "Booking"), ("Open", "Scheduling"), ("Instant", "Confirm")],
        "about": [
            "Cal.com provides embeddable scheduling with team round-robin, collective events, and API access for programmatic booking. Sales and success teams use it to remove back-and-forth email when setting demos.",
            "EMAAVY agents read live calendar availability through Cal.com APIs, negotiate time with the callee, and create confirmed events — reducing drop-off after verbal yes on the phone.",
        ],
        "emaavy": [
            ("In-call booking", "Agent offers slots from real availability."),
            ("Hold & confirm", "Reservation completes before hang-up."),
            ("Team routing", "Round-robin across AE calendars per campaign."),
            ("Timezone aware", "Caller local time surfaced correctly."),
        ],
        "features": [
            ("Availability API", "Fetch open slots programmatically."),
            ("Instant booking", "Create events with attendee details."),
            ("Event types", "Map campaigns to specific Cal.com event links."),
            ("Buffer times", "Respect prep and travel buffers automatically."),
            ("Reschedule flows", "Agent can move meetings per script."),
            ("Webhook confirmations", "Sync booking IDs back to EMAAVY analytics."),
        ],
        "uses": [
            ("SDR outbound", "Book demos directly from cold calls."),
            ("Renewal calls", "Schedule success reviews on positive intent."),
            ("Healthcare & services", "Appointment setting with compliance scripts."),
        ],
        "setup": [
            ("Connect Cal.com API", "API key and default event type in EMAAVY."),
            ("Link team calendars", "Assign round-robin pools per campaign."),
            ("Script booking flow", "Train agent prompts for slot negotiation."),
            ("Test timezone edge cases", "Validate international callers."),
        ],
        "hub_desc": "Book meetings live during calls — agents capture the slot and confirm instantly.",
        "hub_points": ["Live availability check", "Instant event creation", "Team round-robin"],
        "hub_badge": "Scheduling",
    },
    {
        "slug": "google-calendar",
        "name": "Google Calendar",
        "short": "Google Calendar",
        "region": "Google Workspace",
        "tag": "Calendar",
        "route": "integration-google-calendar",
        "logo": '<img src="https://cdn.simpleicons.org/googlecalendar/4285F4" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/googlecalendar/4285F4" alt="" width="32" height="32" loading="lazy" />',
        "title": "Google Calendar — EMAAVY",
        "h1": "Google Calendar",
        "meta": "Google Calendar and EMAAVY — sync confirmed appointments into shared calendars with invites and reminders.",
        "lead": "When teams live in Google Workspace, EMAAVY creates Calendar events with invites, Meet links, and reminders the moment an agent secures a meeting — no rep copy-paste from call notes.",
        "stats": [("Workspace", "Native"), ("Meet links", "Optional"), ("Shared", "Calendars")],
        "about": [
            "Google Calendar is the default scheduling surface for millions of businesses using Gmail and Meet. EMAAVY integrates via Google APIs to insert events on the right organizer calendar with attendee invites.",
            "Programs already using Google for identity and email often prefer Calendar over third-party schedulers — EMAAVY supports both Cal.com and native Google flows.",
        ],
        "emaavy": [
            ("Event creation", "Title, time, attendees from extracted call data."),
            ("Meet link generation", "Optional video conference attachment."),
            ("Shared resource calendars", "Book into team pools with permissions."),
            ("Reminder defaults", "Respect org notification policies."),
        ],
        "features": [
            ("OAuth to Google", "Secure Workspace consent flows."),
            ("Multi-calendar", "Target primary or shared team calendars."),
            ("Invite attendees", "Callee email from verified disposition."),
            ("Free/busy lookup", "Avoid double-booking during calls."),
            ("Timezone handling", "Correct offsets for global callers."),
            ("Audit trail", "Event IDs stored in EMAAVY call records."),
        ],
        "uses": [
            ("Workspace-native sales", "Teams on Gmail and Google Meet."),
            ("SMB appointment setting", "Local services booking over the phone."),
            ("Hybrid scheduling", "Cal.com for external + Google for internal holds."),
        ],
        "setup": [
            ("Connect Google Workspace", "Admin consent for Calendar scope."),
            ("Pick organizer calendars", "Map campaigns to calendar resources."),
            ("Define event templates", "Default titles and descriptions per campaign."),
            ("Pilot invites", "Confirm attendees receive correct ICS emails."),
        ],
        "hub_desc": "Sync confirmed appointments into shared Google Calendars with invites and reminders.",
        "hub_points": ["Live event creation", "Google Meet links", "Shared team calendars"],
        "hub_badge": "Calendar",
    },
    {
        "slug": "whatsapp",
        "name": "WhatsApp",
        "short": "WhatsApp",
        "region": "Messaging · Global",
        "tag": "Messaging",
        "route": "integration-whatsapp",
        "logo": '<img src="https://cdn.simpleicons.org/whatsapp/25D366" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/whatsapp/25D366" alt="" width="32" height="32" loading="lazy" />',
        "title": "WhatsApp — EMAAVY",
        "h1": "WhatsApp",
        "meta": "WhatsApp Business and EMAAVY — send confirmations, links, and follow-ups when calls conclude.",
        "lead": "WhatsApp is where customers actually read messages — EMAAVY sends templated follow-ups, payment links, and appointment confirmations right after the agent closes on the phone.",
        "stats": [("Post-call", "Messages"), ("Templates", "Approved"), ("Global", "Reach")],
        "about": [
            "WhatsApp Business Platform enables programmatic messaging with approved templates, session messages, and rich media. In India and APAC especially, a call plus WhatsApp confirmation dramatically improves show rates.",
            "EMAAVY triggers WhatsApp sends when dispositions match — booked, interested, send brochure — using variables extracted from the live transcript.",
        ],
        "emaavy": [
            ("Template automation", "Map outcomes to pre-approved WhatsApp templates."),
            ("Variable injection", "Names, dates, and links from call extraction."),
            ("Opt-in aware", "Respect consent captured during the call script."),
            ("Delivery tracking", "Message status visible in EMAAVY campaign analytics."),
        ],
        "features": [
            ("Template messages", "Compliant outbound after calls."),
            ("Session messages", "Reply within customer service windows."),
            ("Rich links", "Send trackable URLs and documents."),
            ("Multi-language", "Templates per locale and campaign."),
            ("Opt-in capture", "Store consent flags on contact records."),
            ("Webhook receipts", "Delivered/read status back to EMAAVY."),
        ],
        "uses": [
            ("India D2C", "Order and delivery confirmations after voice outreach."),
            ("Appointment reminders", "Reduce no-shows with WhatsApp nudges."),
            ("Collections", "Payment links after promise-to-pay calls."),
        ],
        "setup": [
            ("Connect WhatsApp Business API", "Via BSP credentials in EMAAVY."),
            ("Register templates", "Meta-approved message templates per use case."),
            ("Map dispositions", "Which outcomes trigger which template."),
            ("Compliance review", "Legal approves opt-in language on scripts."),
        ],
        "hub_desc": "Send confirmations, links, and follow-ups automatically when calls conclude.",
        "hub_points": ["Template-based messaging", "Transcript-driven variables", "Delivery tracking"],
        "hub_badge": "Messaging",
    },
    {
        "slug": "slack",
        "name": "Slack",
        "short": "Slack",
        "region": "Team alerts · Ops",
        "tag": "Alerts",
        "route": "integration-slack",
        "logo": '<img src="https://cdn.simpleicons.org/slack/4A154B" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/slack/4A154B" alt="" width="32" height="32" loading="lazy" />',
        "title": "Slack — EMAAVY",
        "h1": "Slack",
        "meta": "Slack and EMAAVY — route call intelligence, alerts, and coaching notifications to team channels.",
        "lead": "Slack is where operations teams already watch dashboards — EMAAVY posts live call alerts, compliance flags, and coaching snippets to the right channels when thresholds breach.",
        "stats": [("Channels", "Targeted"), ("Live", "Alerts"), ("Rich", "Blocks")],
        "about": [
            "Slack connects revenue, support, and engineering in real time. Instead of forcing supervisors to refresh a new UI, EMAAVY pushes actionable call intelligence into #sales-alerts or #qa-escalations with context and links back to recordings.",
            "Workflow builders can combine Slack notifications with human takeover rules when sentiment crashes or compliance keywords appear.",
        ],
        "emaavy": [
            ("Live escalations", "Notify managers on negative sentiment spikes."),
            ("Daily digests", "Campaign KPI summaries to leadership channels."),
            ("Coaching clips", "Link to flagged moments in transcripts."),
            ("Custom routing", "Different channels per brand or region."),
        ],
        "features": [
            ("Incoming webhooks", "Post to channels without complex OAuth."),
            ("Block Kit messages", "Structured alerts with buttons and fields."),
            ("Keyword alerts", "Instant posts on compliance phrase detection."),
            ("Supervisor mentions", "@user when human handoff required."),
            ("Thread replies", "Keep long transcripts in threaded detail."),
            ("Environment separation", "Staging vs. production channels."),
        ],
        "uses": [
            ("Sales floor ops", "Real-time listen for hot leads and escalations."),
            ("QA teams", "Compliance keyword alerts to reviewers."),
            ("Engineering", "Webhook failure or integration health notices."),
        ],
        "setup": [
            ("Create Slack webhook", "Per channel or use Slack app OAuth."),
            ("Map alert rules", "Which intents post to which channels."),
            ("Test message format", "Preview Block Kit layout in sandbox."),
            ("Tune noise", "Thresholds so channels stay actionable."),
        ],
        "hub_desc": "Route call intelligence, coaching alerts, and escalations to Slack channels in real time.",
        "hub_points": ["Live sentiment alerts", "Compliance keyword posts", "Campaign digest summaries"],
        "hub_badge": "Alerts",
    },
]

USE_EXTRAS = [
    ("Lead qualification", "Sync scores and dispositions to CRM during live calls."),
    ("Automated follow-ups", "Trigger messaging and tasks the moment calls end."),
    ("Multi-agent operations", "Standardize automations while scaling agent programs."),
]

HUB_CFG = {
    "route": "integration-tools",
    "title": "Tools & Workflow — EMAAVY",
    "meta": "CRM updates, calendar bookings, WhatsApp follow-ups, and custom webhooks — all fired from live EMAAVY call intelligence with zero manual entry.",
    "og_title": "Tools & Workflow — EMAAVY",
    "og_description": "Connect Salesforce, HubSpot, Cal.com, Google Calendar, WhatsApp, Slack, and webhooks to EMAAVY voice programs.",
    "breadcrumb": "Tools & Workflow",
    "kicker": "Action layer · Tools & Workflow",
    "h1": "Every call triggers the right action — instantly",
    "lead": "CRM updates, calendar bookings, WhatsApp follow-ups, and custom webhooks — all fired from what was actually said on the call. EMAAVY turns conversation intelligence into follow-through with zero manual entry.",
    "stats": [("7", "Connected tools"), ("Zero", "Manual entry"), ("Real-time", "Automation")],
    "anchor_jumps": [
        ("action-layer", "How EMAAVY automates"),
        ("providers", "Connected tools"),
        ("automation", "Post-call flow"),
    ],
    "layer_id": "action-layer",
    "layer_num": "Layer 05",
    "layer_tag": "EMAAVY · Tools & Workflow",
    "layer_h2": "How EMAAVY automates follow-through",
    "layer_lead": "Conversation intelligence becomes operational motion the moment a call ends — or mid-call when compliance and escalation rules require it.",
    "pills": [
        ("CRM sync", "Salesforce and HubSpot updated from live dispositions."),
        ("Scheduling", "Cal.com and Google Calendar bookings during calls."),
        ("Messaging", "WhatsApp confirmations and links after hang-up."),
        ("Custom logic", "Webhooks with full transcript and score payloads."),
    ],
    "partners_id": "providers",
    "partners_h2": "Connected tools",
    "partners_desc": "Seven integrations today — each with a dedicated page on what the tool does, how EMAAVY triggers it, and how to roll out.",
    "flow_id": "automation",
    "flow_h2": "What fires when a call ends",
    "flow_desc": "The default post-call automation path on EMAAVY — mix and match tools per campaign.",
    "flow_steps": [
        ("Call completes", "EMAAVY finalizes transcript, scores, and metadata."),
        ("Trigger matched", "Rules map intent and keywords to actions."),
        ("CRM updated", "Records, tasks, and deals sync automatically."),
        ("Meeting booked", "Calendar events created with invites."),
        ("Follow-up sent", "WhatsApp, Slack, or webhook payloads delivered."),
    ],
    "cta_h2": "Connect Tools & Workflow to EMAAVY",
    "cta_desc": "See live CRM sync, scheduling, and webhook automation in a tailored demo.",
}

HUB_FILE = "tools.html"
HUB_LABEL = "All tools"
HUB_BREADCRUMB = "Tools & Workflow"
HUB_CTA = "Tools overview"


def prepare():
    for t in TOOLS:
        t.pop("featured", None)
        ensure_uses(t, USE_EXTRAS)
    apply_logos_all(TOOLS)


def write_partner(t: dict) -> str:
    route = t.get("route", f"integration-{t['slug']}")
    return render_partner(
        t,
        partners=TOOLS,
        route=route,
        segment_kicker=f"Tools & Workflow · {t['tag']}",
        hub_file=HUB_FILE,
        hub_label=HUB_LABEL,
        hub_breadcrumb=HUB_BREADCRUMB,
        hub_cta_label=HUB_CTA,
        nav_label_key="short",
        connect_name_key="name",
        explore_title="Explore other tools",
        explore_desc="Mix CRM, scheduling, messaging, and webhooks per campaign — EMAAVY keeps automations consistent.",
        nav_aria="Workflow tools",
        overview_fit="your operations stack",
        cta_desc="Book a walkthrough — we will map triggers, CRM fields, and live automation on a sample call.",
        aside_note="Integrated with EMAAVY voice agents, campaigns, and post-call automation.",
        segment_type="tools",
        hub_label_key="short",
    )



def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = ["      { id: 'tools', label: 'Tools layer', path: 'pages/integrations/tools.html' },"]
    for t in TOOLS:
        label = t["name"]
        lines.append(
            f"      {{ id: '{t['slug']}', label: '{label}', path: 'pages/integrations/{t['slug']}.html' }},"
        )
    block = "    tools: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    tools: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    prepare()
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "tools.html").write_text(
        render_hub(HUB_CFG, TOOLS, jump_label_key="short", hub_tile_label_key="short"), encoding="utf-8"
    )
    for t in TOOLS:
        (INT / f"{t['slug']}.html").write_text(write_partner(t), encoding="utf-8")
    update_routes()
    print(f"OK: tools.html + {len(TOOLS)} partner pages, routes.js updated")


if __name__ == "__main__":
    main()
