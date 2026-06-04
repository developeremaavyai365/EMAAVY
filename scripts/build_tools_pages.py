#!/usr/bin/env python3
"""Generate Tools & Workflow hub + per-tool integration pages."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

HEAD_COMMON = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/masthead-flex.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
  <link rel="stylesheet" href="../../assets/emaavy-theme.css" />
"""

TOOLS = [
    {
        "slug": "webhooks",
        "name": "Webhooks",
        "short": "Webhooks",
        "region": "Custom events · Any stack",
        "tag": "Events",
        "featured": True,
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


def tool_nav(current: str) -> str:
    links = []
    for t in TOOLS:
        cls = ' class="is-current"' if t["slug"] == current else ""
        links.append(f'<a href="{t["slug"]}.html"{cls}>{t["short"]}</a>')
    links.append('<a href="tools.html">All tools</a>')
    return "\n          ".join(links)


def render_partner(t: dict) -> str:
    stats = "".join(
        f'<div class="tools-partner-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in t["stats"]
    )
    about = "".join(f"<p>{para}</p>" for para in t["about"])
    benefits = "".join(
        f'<li><div><strong>{h}</strong><span>{d}</span></div></li>'
        for h, d in t["emaavy"]
    )
    features = "".join(
        f'<article class="tools-feature-card"><h3>{h}</h3><p>{d}</p></article>'
        for h, d in t["features"]
    )
    uses = "".join(
        f'<article class="tools-use-card"><h3>{h}</h3><p>{d}</p></article>'
        for h, d in t["uses"]
    )
    setup = "".join(
        f'<li><div><strong>{h}</strong><p>{d}</p></div></li>'
        for h, d in t["setup"]
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['title']}</title>
  <meta name="description" content="{t['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{t['title']}" />
  <meta property="og:description" content="{t['meta']}" />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/tools-partner.css" />
</head>
<body data-base="../../" data-route="{t['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main tools-partner-page">
    <section class="tools-partner-hero">
      <div class="container tools-partner-hero-grid">
        <div class="tools-partner-hero-copy">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="../../index.html">Home</a>
            <span aria-hidden="true"> / </span>
            <a href="../../index.html#integrations">Integrations</a>
            <span aria-hidden="true"> / </span>
            <a href="tools.html">Tools &amp; Workflow</a>
            <span aria-hidden="true"> / </span>
            <span>{t['short']}</span>
          </nav>
          <span class="tools-partner-kicker">Tools &amp; Workflow · {t['tag']}</span>
          <h1>{t['h1']}</h1>
          <p class="tools-partner-lead">{t['lead']}</p>
          <div class="tools-partner-stats">{stats}</div>
          <div class="tools-partner-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Connect {t['short']}</a>
            <a href="tools.html" class="btn-outline">All tools</a>
          </div>
        </div>
        <aside class="tools-partner-hero-card" aria-label="{t['name']} overview">
          <div class="tools-partner-hero-logo">{t['logo']}</div>
          <span class="tools-partner-hero-region">{t['region']}</span>
          <p>Triggered from EMAAVY — on call end or mid-call when your rules require action.</p>
        </aside>
      </div>
    </section>

    <section class="tools-partner-section">
      <div class="container">
        <header class="tools-partner-section-head">
          <h2>What {t['short']} does</h2>
          <p>How this tool fits into your post-call and in-call automation stack.</p>
        </header>
        <div class="tools-partner-prose">{about}</div>
      </div>
    </section>

    <section class="tools-partner-section alt">
      <div class="container tools-partner-split">
        <header class="tools-partner-section-head">
          <h2>How EMAAVY uses {t['short']}</h2>
          <p>Conversation intelligence becomes operational motion — without manual entry.</p>
        </header>
        <ul class="tools-partner-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="tools-partner-section">
      <div class="container">
        <header class="tools-partner-section-head">
          <h2>Key capabilities</h2>
          <p>What teams configure when {t['short']} is wired to EMAAVY programs.</p>
        </header>
        <div class="tools-feature-grid">{features}</div>
      </div>
    </section>

    <section class="tools-partner-section alt">
      <div class="container">
        <header class="tools-partner-section-head">
          <h2>Ideal use cases</h2>
          <p>Where {t['short']} and EMAAVY deliver the strongest combined outcomes.</p>
        </header>
        <div class="tools-use-grid">{uses}</div>
      </div>
    </section>

    <section class="tools-partner-section">
      <div class="container">
        <header class="tools-partner-section-head">
          <h2>Getting connected</h2>
          <p>From credentials to production automations on EMAAVY.</p>
        </header>
        <ol class="tools-setup-steps">{setup}</ol>
      </div>
    </section>

    <section class="tools-partner-section alt">
      <div class="container">
        <header class="tools-partner-section-head">
          <h2>Explore other tools</h2>
          <p>Combine CRM, scheduling, messaging, Slack, and webhooks — one EMAAVY action layer.</p>
        </header>
        <nav class="tools-partner-nav-strip" aria-label="Tools and workflow partners">
          {tool_nav(t['slug'])}
        </nav>
      </div>
    </section>

    <section class="tools-partner-cta">
      <div class="container">
        <h2>Ready to connect {t['short']}?</h2>
        <p>Book a walkthrough — map triggers, field sync, and live post-call automation on a real call.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="tools.html" class="btn-outline">Tools overview</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""


def card_html(t: dict) -> str:
    points = "".join(f"<li>{x}</li>" for x in t["hub_points"])
    featured = " tools-model-card--native" if t.get("featured") else ""
    cta = "Explore integration →" if not t.get("featured") else "View full integration →"
    badge = f'<span class="tools-model-badge">{t["hub_badge"]}</span>'
    return f"""          <a href="{t['slug']}.html" id="{t['slug']}" class="tools-model-card{featured}">
            <div class="tools-model-card-top">
              <div class="tools-model-card-logo">{t['logo_sm']}</div>
              {badge}
            </div>
            <h3>{t['name']}</h3>
            <p class="tools-model-card-desc">{t['hub_desc']}</p>
            <ul class="tools-model-card-points">{points}</ul>
            <span class="tools-model-card-cta">{cta}</span>
          </a>"""


def render_hub() -> str:
    cards = "\n".join(card_html(t) for t in TOOLS)
    jumps = " ".join(f'<a href="#{t["slug"]}">{t["short"]}</a>' for t in TOOLS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tools &amp; Workflow — EMAAVY</title>
  <meta name="description" content="CRM updates, calendar bookings, WhatsApp follow-ups, and custom webhooks — all fired from live EMAAVY call intelligence with zero manual entry." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Tools &amp; Workflow — EMAAVY" />
  <meta property="og:description" content="Connect Salesforce, HubSpot, Cal.com, Google Calendar, WhatsApp, Slack, and webhooks to EMAAVY voice programs." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/tools-hub.css" />
</head>
<body data-base="../../" data-route="integration-tools">
  <div id="site-nav-root"></div>
  <main class="page-main tools-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../index.html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../index.html#integrations">Integrations</a>
          <span aria-hidden="true"> / </span>
          <span>Tools &amp; Workflow</span>
        </nav>
        <span class="page-kicker">Action layer · Tools &amp; Workflow</span>
        <h1>Every call triggers the right action — instantly</h1>
        <p class="telephony-hero-lead">CRM updates, calendar bookings, WhatsApp follow-ups, and custom webhooks — all fired from what was actually said on the call. EMAAVY turns conversation intelligence into follow-through with zero manual entry.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>7</b><span>Connected tools</span></div>
          <div class="stat-box"><b>Zero</b><span>Manual entry</span></div>
          <div class="stat-box"><b>Real-time</b><span>Automation</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#action-layer">How EMAAVY automates</a>
          <a href="#providers">Connected tools</a>
          <a href="#automation">Post-call flow</a>
          {jumps}
        </div>
      </div>
    </section>

    <section id="action-layer" class="tools-hub-action">
      <div class="container">
        <article class="tools-hub-action-card">
          <div class="tools-hub-action-meta">
            <span class="tools-hub-action-num">Layer 05</span>
            <span class="tools-hub-action-tag">EMAAVY · Tools &amp; Workflow</span>
            <h2>How EMAAVY automates follow-through</h2>
            <p class="tools-hub-action-lead">Conversation intelligence becomes operational motion the moment a call ends — or mid-call when compliance and escalation rules require it.</p>
          </div>
          <div class="tools-hub-pill-grid">
            <div class="tools-hub-pill"><strong>CRM sync</strong><span>Salesforce and HubSpot updated from live dispositions.</span></div>
            <div class="tools-hub-pill"><strong>Scheduling</strong><span>Cal.com and Google Calendar bookings during calls.</span></div>
            <div class="tools-hub-pill"><strong>Messaging</strong><span>WhatsApp confirmations and links after hang-up.</span></div>
            <div class="tools-hub-pill"><strong>Custom logic</strong><span>Webhooks with full transcript and score payloads.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="providers" class="tools-hub-partners page-section alt">
      <div class="container">
        <header class="tools-hub-partners-head">
          <h2>Connected tools</h2>
          <p>Seven integrations today — each with a dedicated page on what the tool does, how EMAAVY triggers it, and how to roll out.</p>
        </header>
        <div class="tools-model-grid">
{cards}
        </div>
      </div>
    </section>

    <section id="automation" class="tools-hub-flow">
      <div class="container">
        <header class="tools-hub-flow-head">
          <h2>What fires when a call ends</h2>
          <p>The default post-call automation path on EMAAVY — mix and match tools per campaign.</p>
        </header>
        <div class="tools-flow-track">
          <article class="tools-flow-step"><strong>Call completes</strong><p>EMAAVY finalizes transcript, scores, and metadata.</p></article>
          <article class="tools-flow-step"><strong>Trigger matched</strong><p>Rules map intent and keywords to actions.</p></article>
          <article class="tools-flow-step"><strong>CRM updated</strong><p>Records, tasks, and deals sync automatically.</p></article>
          <article class="tools-flow-step"><strong>Meeting booked</strong><p>Calendar events created with invites.</p></article>
          <article class="tools-flow-step"><strong>Follow-up sent</strong><p>WhatsApp, Slack, or webhook payloads delivered.</p></article>
        </div>
      </div>
    </section>

    <section class="tools-hub-cta">
      <div class="container">
        <h2>Connect Tools &amp; Workflow to EMAAVY</h2>
        <p>See live CRM sync, scheduling, and webhook automation in a tailored demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="index.html" class="btn-outline">All integrations</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""


def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = ["      { id: 'tools', label: 'Tools layer', path: 'pages/integrations/tools.html' },"]
    for t in TOOLS:
        lines.append(
            f"      {{ id: '{t['slug']}', label: '{t['name']}', path: 'pages/integrations/{t['slug']}.html' }},"
        )
    block = "    tools: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    tools: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "tools.html").write_text(render_hub(), encoding="utf-8")
    for t in TOOLS:
        (INT / f"{t['slug']}.html").write_text(render_partner(t), encoding="utf-8")
    update_routes()
    print(f"OK: Tools hub + {len(TOOLS)} tool pages, routes.js updated")


if __name__ == "__main__":
    main()
