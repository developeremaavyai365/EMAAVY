"""Shared EMAAVY agent template catalog (homepage showcase + subpages)."""
from __future__ import annotations

CATEGORY_ORDER = [
    "Sales", "Scheduling", "Feedback", "Events", "HR", "Finance", "Support", "Retention",
]


def slugify_category(cat: str) -> str:
    return cat.lower().replace(" & ", "-").replace(" ", "-")


def _benefit_title(point: str) -> str:
    clean = point.strip()
    chunk = clean.split(",")[0].split("—")[0].strip()
    return chunk if len(chunk) <= 42 else " ".join(clean.split()[:4]).rstrip(",.")


def template_to_role(t: dict) -> dict:
    slug = t["id"]
    workflow = [
        (step, f"The agent executes the {step.lower()} stage of this template flow.")
        for step in t["flow"]
    ]
    workflow.append(("Sync and log", "Outcomes, scores, and CRM fields update automatically after the call."))
    features = [(o, o) for o in t["outcomes"]]
    for p in t["points"][:2]:
        features.append((_benefit_title(p), p))
    return {
        "slug": slug,
        "name": t["title"],
        "short": t["category"],
        "region": f"{t['category']} · {t['mode']}",
        "tag": f"{t['mode']} · {t['duration']}",
        "route": f"agent-{slug}",
        "icon": t["icon"],
        "duration": t["duration"],
        "mode": t["mode"],
        "category": t["category"],
        "title": f"{t['title']} — EMAAVY",
        "h1": t["title"],
        "meta": f"Deploy the EMAAVY {t['title']} voice agent template — {t['short']}",
        "lead": t["desc"],
        "stats": [(t["duration"], "Setup time"), (t["mode"], "Call type"), (t["category"], "Category")],
        "about": [t["desc"], t["detail"]],
        "emaavy": [(_benefit_title(p), p) for p in t["points"]],
        "features": features[:6],
        "uses": [(u, f"Run this template for {u.lower()} use cases.") for u in t["usecases"]],
        "setup": [
            ("Select template", f"Choose {t['title']} from the EMAAVY agent library."),
            ("Customize flow", "Adjust prompts, voice, language, and branching rules."),
            ("Connect stack", "Wire telephony, LLM, STT, TTS, CRM, and calendar integrations."),
            ("Launch", f"Go live on a campaign or DID — typically ready in {t['duration']}."),
        ],
        "workflow": workflow,
        "hub_desc": t["short"],
        "hub_points": t["points"],
        "hub_badge": f"{t['duration']} · {t['mode']}",
    }


def templates_to_roles(templates=None) -> list[dict]:
    return [template_to_role(t) for t in (templates or TEMPLATES)]


def group_by_category(roles: list[dict]) -> list[tuple[str, list[dict]]]:
    buckets: dict[str, list[dict]] = {c: [] for c in CATEGORY_ORDER}
    for r in roles:
        buckets.setdefault(r.get("category", "Templates"), []).append(r)
    return [(c, buckets[c]) for c in CATEGORY_ORDER if buckets.get(c)]


TEMPLATES = [
    {
        "id": "real-estate",
        "icon": "🏠",
        "title": "Real Estate Lead Qualification",
        "duration": "12 min",
        "mode": "Outbound",
        "category": "Sales",
        "short": "Outbound call flow for qualifying real estate leads and scheduling site visits.",
        "desc": "An outbound voice agent that qualifies property inquiries, captures budget and timeline, handles objections, and books site visits — turning cold leads into showroom appointments without human dialers.",
        "detail": "Pre-built prompts cover new launches, resale, and rental programs. The agent scores intent in real time, routes hot leads to sales reps, and syncs disposition data to your CRM after every call.",
        "points": [
            "Qualifies budget, location preference, and purchase timeline on live calls",
            "Handles common objections and schedules site visits automatically",
            "Syncs lead scores and visit slots to CRM without manual entry",
        ],
        "outcomes": ["Higher show rates", "Faster qualification", "CRM auto-sync", "12 min setup"],
        "usecases": ["New project launches", "Resale inventory", "Rental programs", "Broker partnerships"],
        "flow": ["Greet", "Qualify", "Book visit"],
    },
    {
        "id": "appointment-reminder",
        "icon": "📅",
        "title": "Contextual Appointment Reminder",
        "duration": "12 min",
        "mode": "Outbound",
        "category": "Scheduling",
        "short": "Flexible outbound flow for appointment reminders with smart handling for lates and snoozing.",
        "desc": "A reminder agent that confirms upcoming appointments, offers reschedule options when callers are running late, and snoozes follow-ups — reducing no-shows without sounding robotic.",
        "detail": "Context-aware branching detects lateness, cancellations, and confirmation intent. Calendar integrations update slots live while supervisors see reminder outcomes in the campaign dashboard.",
        "points": [
            "Confirms, reschedules, or cancels appointments in one natural conversation",
            "Snooze and callback paths for callers who need more time",
            "Reduces no-shows with empathetic, context-driven reminders",
        ],
        "outcomes": ["Fewer no-shows", "Live rescheduling", "Snooze paths", "Calendar sync"],
        "usecases": ["Clinic reminders", "Sales demos", "Field visits", "Service calls"],
        "flow": ["Confirm", "Reschedule", "Snooze"],
    },
    {
        "id": "appointment-booking",
        "icon": "📋",
        "title": "Appointment Booking",
        "duration": "12 min",
        "mode": "Inbound",
        "category": "Scheduling",
        "short": "Book, reschedule, or cancel appointments with callers.",
        "desc": "An inbound scheduling agent that checks availability, books slots, sends confirmations, and handles reschedule or cancellation requests — 24/7 without front-desk bottlenecks.",
        "detail": "Connects to Cal.com or Google Calendar for live availability. Callers receive SMS or WhatsApp confirmations while your team sees every booking logged against the right contact record.",
        "points": [
            "Checks real-time calendar availability during the call",
            "Books, reschedules, and cancels with natural dialogue",
            "Sends cross-channel confirmations automatically",
        ],
        "outcomes": ["24/7 booking", "Zero hold time", "Auto confirmations", "CRM logging"],
        "usecases": ["Healthcare intake", "Consultation booking", "Salon & spa", "Professional services"],
        "flow": ["Intent", "Availability", "Confirm"],
    },
    {
        "id": "nps-review",
        "icon": "⭐",
        "title": "Insightful NPS Review",
        "duration": "10 min",
        "mode": "Outbound",
        "category": "Feedback",
        "short": "Transform the standard survey into a conversational feedback loop that answers detractors and amplifies promoters.",
        "desc": "Replace one-way NPS surveys with a voice conversation that probes detractor concerns, captures promoter stories, and routes urgent issues to human teams before churn spreads.",
        "detail": "Sentiment scoring flags at-risk customers mid-call. Promoters can be invited to leave public reviews while detractors receive follow-up tasks for recovery specialists.",
        "points": [
            "Conversational NPS that adapts to promoter and detractor signals",
            "Real-time escalation for urgent satisfaction issues",
            "Structured scores synced to analytics and CRM",
        ],
        "outcomes": ["Richer feedback", "Churn prevention", "Promoter capture", "10 min deploy"],
        "usecases": ["Post-purchase CSAT", "Service recovery", "Product launches", "Renewal programs"],
        "flow": ["Score", "Probe", "Route"],
    },
    {
        "id": "event-agent",
        "icon": "🎟️",
        "title": "High-Conversion Event Agent",
        "duration": "12 min",
        "mode": "Outbound",
        "category": "Events",
        "short": "Transform event invites into curiosity-driven conversations that maximize registrations and nurture interest.",
        "desc": "An outbound event invitation agent that personalizes invites, answers FAQs, handles objections, and secures registrations — turning invite lists into confirmed attendees.",
        "detail": "Dynamic scripts reference event details, speaker highlights, and VIP tiers. Waitlist and reminder sequences fire automatically for interested but undecided contacts.",
        "points": [
            "Personalized invites with natural FAQ handling",
            "VIP tier upsell and early-access positioning",
            "Registration confirmation with follow-up nurture",
        ],
        "outcomes": ["More registrations", "VIP upsell", "FAQ deflection", "Nurture sequences"],
        "usecases": ["Conferences", "Product launches", "Retail events", "Webinar drives"],
        "flow": ["Invite", "FAQ", "Register"],
    },
    {
        "id": "recruiter-outreach",
        "icon": "💼",
        "title": "Recruiter-grade Outreach",
        "duration": "12 min",
        "mode": "Outbound",
        "category": "HR",
        "short": "Engage candidates with a call-first approach, conversational screening, and a proactive path to interviews.",
        "desc": "A recruiting agent that introduces roles, runs conversational screening, answers candidate questions, and books interview slots — accelerating hiring pipelines without recruiter burnout.",
        "detail": "Screening rubrics score skills and availability in real time. Qualified candidates land on recruiter calendars while others receive polite nurture or referral paths.",
        "points": [
            "Call-first outreach with role-specific screening questions",
            "Answers compensation and role FAQs naturally",
            "Books interviews and syncs outcomes to ATS or CRM",
        ],
        "outcomes": ["Faster screening", "Interview booking", "ATS sync", "Scale hiring"],
        "usecases": ["Volume hiring", "Campus drives", "Niche roles", "Contract staffing"],
        "flow": ["Intro", "Screen", "Interview"],
    },
    {
        "id": "payment-checkin",
        "icon": "😊",
        "title": "Friendly Payment Check-in",
        "duration": "10 min",
        "mode": "Outbound",
        "category": "Finance",
        "short": "Empathetic outbound flow for payment reminders and collections.",
        "desc": "A collections agent that reminds customers of upcoming or overdue payments with an empathetic tone, offers payment plans, and escalates disputes — improving recovery rates without damaging relationships.",
        "detail": "Compliance-friendly scripts adapt to payment status and customer history. Successful commitments trigger WhatsApp payment links while disputes route to human specialists.",
        "points": [
            "Empathetic reminders with payment-plan options",
            "Handles disputes and hardship cases with escalation paths",
            "Logs commitments and outcomes for audit-ready collections",
        ],
        "outcomes": ["Higher recovery", "Empathetic tone", "Plan offers", "Audit trails"],
        "usecases": ["EMI reminders", "Subscription renewals", "B2B invoices", "Utility bills"],
        "flow": ["Remind", "Negotiate", "Confirm"],
    },
    {
        "id": "support-playbook",
        "icon": "🎧",
        "title": "Intelligent Support Playbook",
        "duration": "12 min",
        "mode": "Inbound",
        "category": "Support",
        "short": "A high-conversion support flow with specialized playbooks for interest, login, payment, and complaints.",
        "desc": "An inbound support agent with intent-specific playbooks — login issues, billing questions, product interest, and complaints each get tailored flows with smart escalation to humans.",
        "detail": "Intent classification routes callers to the right playbook in seconds. Resolution steps pull from your knowledge base while supervisors monitor CSAT risk on live dashboards.",
        "points": [
            "Dedicated playbooks for login, billing, interest, and complaints",
            "Knowledge-grounded answers with human escalation when needed",
            "Live intent routing reduces transfers and handle time",
        ],
        "outcomes": ["Tier-1 deflection", "Smart routing", "Lower AHT", "CSAT uplift"],
        "usecases": ["SaaS support", "Fintech helpdesk", "E-commerce care", "Telecom support"],
        "flow": ["Triage", "Playbook", "Resolve"],
    },
    {
        "id": "order-returns",
        "icon": "📦",
        "title": "Order, Refund & Returns",
        "duration": "12 min",
        "mode": "Inbound",
        "category": "Support",
        "short": "Full lifecycle support for orders: status, cancellations, refunds, and conversational returns/exchanges.",
        "desc": "A commerce support agent that tracks orders, processes cancellations, initiates refunds, and handles returns or exchanges conversationally — reducing ticket volume and chat queues.",
        "detail": "Integrates with OMS and CRM to pull live order status. Return eligibility, refund timelines, and exchange options are explained clearly with automated follow-up messages post-call.",
        "points": [
            "Live order status and delivery updates on voice calls",
            "Refund, cancellation, and return flows with policy guardrails",
            "Exchange recommendations that protect margin and CSAT",
        ],
        "outcomes": ["Fewer tickets", "Faster refunds", "Policy-safe", "OMS sync"],
        "usecases": ["D2C brands", "Marketplace sellers", "Subscription boxes", "B2B fulfillment"],
        "flow": ["Lookup", "Policy", "Action"],
    },
    {
        "id": "financial-assistant",
        "icon": "🏦",
        "title": "Financial Assistant (Loan & EMI)",
        "duration": "12 min",
        "mode": "Inbound",
        "category": "Finance",
        "short": "A human-centric loan concierge that handles payments, early closure, and stress cases with an advisory tone.",
        "desc": "A finance voice agent for loan and EMI programs — payment assistance, early closure quotes, hardship support, and product FAQs delivered with an advisory, trust-building tone.",
        "detail": "Built for regulated conversations with disclaimers, consent capture, and explainable outputs. Stress scenarios route to licensed advisors while routine queries resolve automatically.",
        "points": [
            "Payment, foreclosure, and EMI schedule assistance",
            "Advisory tone with compliance-ready disclaimers",
            "Escalation paths for hardship and dispute cases",
        ],
        "outcomes": ["Trust-led tone", "Compliance ready", "Self-serve EMI", "Advisor handoff"],
        "usecases": ["NBFC programs", "Banking EMIs", "BNPL support", "Mortgage servicing"],
        "flow": ["Verify", "Advise", "Act"],
    },
    {
        "id": "customer-reactivation",
        "icon": "🔄",
        "title": "High-Conversion Customer Reactivation",
        "duration": "10 min",
        "mode": "Outbound",
        "category": "Retention",
        "short": "Re-engage churned users by identifying the real reason they left and rebuilding value before offering a discount.",
        "desc": "A win-back agent that discovers why customers churned, rebuilds product value conversationally, and only then presents targeted offers — improving reactivation ROI versus blanket discounts.",
        "detail": "Churn-reason taxonomy powers personalized responses. High-intent returners get fast paths to purchase while researchers receive nurture sequences across voice and WhatsApp.",
        "points": [
            "Discovers churn drivers before pitching offers",
            "Value-first scripts that protect margin and brand",
            "Targeted incentives synced to CRM segments",
        ],
        "outcomes": ["Better ROI", "Value-first", "Segment offers", "10 min launch"],
        "usecases": ["SaaS churn", "Subscription lapse", "Dormant wallets", "Loyalty win-back"],
        "flow": ["Discover", "Rebuild", "Offer"],
    },
    {
        "id": "job-applicant",
        "icon": "🎓",
        "title": "Job Applicant Concierge",
        "duration": "12 min",
        "mode": "Inbound",
        "category": "HR",
        "short": "Transform status checks into proactive talent experiences that reduce anxiety and keep candidates engaged.",
        "desc": "An inbound candidate concierge that answers application status, next steps, and interview prep — keeping applicants informed and engaged instead of waiting on email black holes.",
        "detail": "Pulls ATS stage data live during calls. Proactive updates and prep tips reduce drop-off while recruiters receive summaries of high-anxiety or at-risk candidates.",
        "points": [
            "Live application status from ATS or spreadsheet integrations",
            "Interview prep and document checklist guidance",
            "Reduces candidate anxiety and ghosting rates",
        ],
        "outcomes": ["Candidate NPS", "Less ghosting", "ATS sync", "Recruiter alerts"],
        "usecases": ["Campus hiring", "High-volume roles", "Graduate programs", "Staffing firms"],
        "flow": ["Status", "Guide", "Engage"],
    },
    {
        "id": "distributor-collection",
        "icon": "🚚",
        "title": "Distributor Payment Collection",
        "duration": "12 min",
        "mode": "Outbound",
        "category": "Finance",
        "short": "Outbound flow for distributors chasing overdue bills from dealers — handles full payment, partial plans, PDCs, disputes, and escalations.",
        "desc": "A B2B collections agent for distributor-dealer programs — negotiates full payment, partial schedules, PDC commitments, and dispute resolution with a natural, relationship-preserving tone.",
        "detail": "Branching logic covers overdue tiers, stock commitments, and regional payment customs. Manager escalations fire when deals stall while every commitment is logged for finance teams.",
        "points": [
            "Full, partial, and PDC payment negotiation paths",
            "Dispute capture with documentation requests",
            "Relationship-safe tone for long-term dealer partnerships",
        ],
        "outcomes": ["Dealer retention", "PDC capture", "Dispute routing", "Finance logs"],
        "usecases": ["FMCG distribution", "Pharma supply", "Auto parts", "Agri inputs"],
        "flow": ["Remind", "Negotiate", "Commit"],
    },
    {
        "id": "fashion-event",
        "icon": "👗",
        "title": "Fashion Event Registration Call",
        "duration": "12 min",
        "mode": "Outbound",
        "category": "Events",
        "short": "Outbound invitation flow for exclusive retail events — personalized invite, VIP hour upsell, and natural FAQ handling.",
        "desc": "A retail event invitation agent that delivers personalized invites, highlights designers and collections, upsells VIP preview hours, and handles FAQs — driving footfall for exclusive sales.",
        "detail": "Scripts reference customer purchase history and preferred categories when available. VIP upsell, parking, and timing FAQs resolve on-call while registrations sync to event management tools.",
        "points": [
            "Personalized invites with designer and collection highlights",
            "VIP early-access upsell during the conversation",
            "Natural FAQ handling for timing, parking, and entry rules",
        ],
        "outcomes": ["VIP upsell", "Personalized", "FAQ deflection", "RSVP sync"],
        "usecases": ["Preview sales", "Designer launches", "Warehouse events", "Loyalty exclusives"],
        "flow": ["Invite", "VIP upsell", "RSVP"],
    },
]
