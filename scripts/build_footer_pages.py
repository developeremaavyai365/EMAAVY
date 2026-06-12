#!/usr/bin/env python3
"""Generate EMAAVY footer subpages, llms.txt files, and patch routes + index."""
from __future__ import annotations

import re
from pathlib import Path

from footer_pages_catalog import API_BASE, FOOTER_LINKS, api_responses
from footer_pages_common import (
    api_endpoint_section,
    feature_list_section,
    hero,
    prose_section,
    related_links,
    shell,
)

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ROOT / "assets" / "routes.js"
INDEX = ROOT / "index.html"
BASE_SUB = "../../"


def crumbs_api(title: str) -> list[tuple[str, str | None]]:
    return [("Home", "index.html"), ("API Documentation", None), (title, None)]


def crumbs_product(title: str) -> list[tuple[str, str | None]]:
    return [("Home", "index.html"), ("Product Features", None), (title, None)]


def crumbs_company(title: str) -> list[tuple[str, str | None]]:
    return [("Home", "index.html"), ("Company & Resources", None), (title, None)]


def crumbs_legal(title: str) -> list[tuple[str, str | None]]:
    return [("Home", "index.html"), (title, None)]


def build_api_auth() -> str:
    lead = (
        "Authenticate every EMAAVY REST request with workspace-scoped API keys. "
        "Keys are issued per sub-account, rotate without downtime, and scope to granular "
        "permissions for agents, telephony, and knowledgebase operations."
    )
    h = hero("API Documentation", "API Authentication", lead, BASE_SUB, crumbs_api("API Authentication"),
             [("<50ms", "Token validation"), ("Sub-account", "Scoped keys")])
    s1 = prose_section(
        "overview", "01", "Overview", "Bearer tokens & workspace isolation",
        [
            "EMAAVY uses Bearer token authentication on all <code>/v1</code> endpoints. "
            "Generate keys from the dashboard under <strong>Settings → API Keys</strong> or via the "
            "<code>POST /v1/api-keys</code> endpoint using a parent admin key.",
            "Each key carries a <code>sub_account_id</code> claim. Requests made with a sub-account key "
            "can only access agents, numbers, campaigns, and knowledgebases owned by that tenant — "
            "enforcing multi-tenant isolation at the API gateway.",
        ],
    )
    api = api_endpoint_section(
        "create-key", "02", "Create an API key", "Issue a scoped key for programmatic access.",
        "POST", f"{API_BASE}/api-keys",
        f"""curl -X POST {API_BASE}/api-keys \\
  -H "Authorization: Bearer <EMAAVY_ADMIN_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "name": "production-outbound",
    "sub_account_id": "sub_acct_8f2k9",
    "scopes": ["agents:read", "calls:write", "knowledgebases:read"],
    "expires_in_days": 90
  }}'""",
        """{
  "name": "production-outbound",
  "sub_account_id": "sub_acct_8f2k9",
  "scopes": ["agents:read", "calls:write", "knowledgebases:read"],
  "expires_in_days": 90
}""",
        api_responses("200", "OK — key created (secret shown once)", """{
  "id": "key_7Qm2xP",
  "name": "production-outbound",
  "secret": "emaavy_sk_live_••••••••••••••••",
  "sub_account_id": "sub_acct_8f2k9",
  "scopes": ["agents:read", "calls:write", "knowledgebases:read"],
  "created_at": "2026-05-30T10:00:00Z"
}"""),
    )
    rel = related_links(BASE_SUB, [
        ("Using Agents APIs", "pages/api-docs/using-agents-apis.html"),
        ("Sub-account Isolation", "pages/api-docs/sub-account-isolation-apis.html"),
        ("Making Phone Calls", "pages/api-docs/making-phone-calls-apis.html"),
    ])
    return h + "\n" + s1 + "\n" + api + "\n" + rel


def build_using_agents() -> str:
    lead = "Create, version, and deploy production voice agents programmatically. Agent configs bundle LLM routing, STT/TTS providers, tool definitions, and telephony bindings."
    h = hero("API Documentation", "Using Agents APIs", lead, BASE_SUB, crumbs_api("Using Agents APIs"))
    s1 = prose_section("agents-overview", "01", "Concepts", "Agent lifecycle via API",
        ["An <strong>agent</strong> is an immutable configuration snapshot referenced by outbound campaigns and inbound number routes. "
         "Updates create a new <code>version</code> while preserving in-flight calls on the prior revision.",
         "Deploy agents to specific <code>sub_account_id</code> tenants. Tool schemas follow OpenAI function-calling format and execute in EMAAVY's secure sandbox with 250ms p95 latency."])
    api = api_endpoint_section(
        "create-agent", "02", "Create an agent", "Provision a voice agent with model and voice stack.",
        "POST", f"{API_BASE}/agents",
        f"""curl -X POST {API_BASE}/agents \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "name": "Outbound Sales — EN/HI",
    "sub_account_id": "sub_acct_8f2k9",
    "llm": {{ "provider": "openai", "model": "gpt-4.1" }},
    "stt": {{ "provider": "deepgram", "model": "nova-2" }},
    "tts": {{ "provider": "elevenlabs", "voice_id": "priya_sales_v3" }},
    "system_prompt": "You qualify B2B leads and book demos...",
    "tools": ["crm.lookup_contact", "calendar.book_slot"]
  }}'""",
        """{
  "name": "Outbound Sales — EN/HI",
  "sub_account_id": "sub_acct_8f2k9",
  "llm": { "provider": "openai", "model": "gpt-4.1" },
  "stt": { "provider": "deepgram", "model": "nova-2" },
  "tts": { "provider": "elevenlabs", "voice_id": "priya_sales_v3" },
  "system_prompt": "You qualify B2B leads and book demos...",
  "tools": ["crm.lookup_contact", "calendar.book_slot"]
}""",
        api_responses("200", "OK — agent created", """{
  "id": "agt_4kLm9",
  "version": 1,
  "status": "draft",
  "name": "Outbound Sales — EN/HI",
  "created_at": "2026-05-30T10:05:00Z"
}"""),
    )
    rel = related_links(BASE_SUB, [("Inbound Agents APIs", "pages/api-docs/inbound-agents-apis.html"), ("Function & Tool Calling", "pages/product/function-tool-calling.html")])
    return h + "\n" + s1 + "\n" + api + "\n" + rel


def build_phone_calls() -> str:
    lead = "Initiate outbound calls and attach live agents. EMAAVY negotiates media streams with Twilio or Plivo, pipes audio through STT, and streams LLM responses back as ultra-low-latency TTS."
    h = hero("API Documentation", "Making Phone Calls APIs", lead, BASE_SUB, crumbs_api("Making Phone Calls APIs"))
    s1 = prose_section("calls-flow", "01", "Call flow", "Outbound session orchestration",
        ["<code>POST /v1/calls</code> reserves telephony capacity, selects the agent version, and returns a <code>call_id</code> before the callee's phone rings.",
         "Media is bridged over WebSocket to EMAAVY's realtime inference plane. Typical mouth-to-ear latency stays under 800ms on Twilio US routes with Deepgram + ElevenTurbo stacks."])
    api = api_endpoint_section(
        "place-call", "02", "Place an outbound call", "Dial a single contact with a deployed agent.",
        "POST", f"{API_BASE}/calls",
        f"""curl -X POST {API_BASE}/calls \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "agent_id": "agt_4kLm9",
    "to": "+14155550123",
    "from": "+14155550999",
    "telephony_provider": "twilio",
    "metadata": {{ "campaign_id": "cmp_holiday_2026", "lead_id": "ld_8821" }}
  }}'""",
        """{
  "agent_id": "agt_4kLm9",
  "to": "+14155550123",
  "from": "+14155550999",
  "telephony_provider": "twilio",
  "metadata": { "campaign_id": "cmp_holiday_2026", "lead_id": "ld_8821" }
}""",
        api_responses("200", "OK — call initiated", """{
  "call_id": "call_9xR2m",
  "status": "initiated",
  "agent_id": "agt_4kLm9",
  "to": "+14155550123",
  "from": "+14155550999",
  "websocket_media_url": "wss://stream.emaavy.com/v1/calls/call_9xR2m/media"
}"""),
    )
    rel = related_links(BASE_SUB, [("Get Call Data APIs", "pages/api-docs/get-call-data-apis.html"), ("Twilio Voice Integrations", "pages/product/twilio-voice-integrations.html")])
    return h + "\n" + s1 + "\n" + api + "\n" + rel


def build_get_call_data() -> str:
    lead = "Retrieve transcripts, tool execution logs, sentiment arcs, and recording URLs after or during a live session."
    h = hero("API Documentation", "Get Call Data APIs", lead, BASE_SUB, crumbs_api("Get Call Data APIs"))
    api = api_endpoint_section(
        "get-call", "01", "Fetch call details", "Pull structured intelligence for a completed or active call.",
        "GET", f"{API_BASE}/calls/{{call_id}}",
        f"""curl -X GET {API_BASE}/calls/call_9xR2m \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -H "Accept: application/json" """,
        None,
        api_responses("200", "OK — call record", """{
  "call_id": "call_9xR2m",
  "status": "completed",
  "duration_seconds": 187,
  "transcript": [
    { "speaker": "agent", "text": "Hi, this is Priya from EMAAVY...", "ts_ms": 0 },
    { "speaker": "user", "text": "Yes, we are evaluating voice AI.", "ts_ms": 4200 }
  ],
  "sentiment_score": 0.82,
  "intent": "qualified",
  "tools_invoked": [
    { "name": "calendar.book_slot", "result": "2026-06-02T15:00:00Z" }
  ],
  "recording_url": "https://recordings.emaavy.com/call_9xR2m.mp3"
}"""),
    )
    s2 = feature_list_section("webhooks", "02", "Events", "Realtime webhooks",
        "Subscribe to call lifecycle events instead of polling:",
        ["<code>call.started</code> — media stream attached", "<code>call.tool_invoked</code> — function execution audit trail",
         "<code>call.scored</code> — intent and sentiment available", "<code>call.ended</code> — full transcript payload"])
    rel = related_links(BASE_SUB, [("Making Phone Calls APIs", "pages/api-docs/making-phone-calls-apis.html"), ("Batch & Queue APIs", "pages/api-docs/batch-queue-apis.html")])
    return h + "\n" + api + "\n" + s2 + "\n" + rel


def build_phone_numbers() -> str:
    lead = "Search, purchase, and bind phone numbers to inbound agents or outbound caller-ID pools across Twilio and Plivo inventories."
    h = hero("API Documentation", "Phone Numbers APIs", lead, BASE_SUB, crumbs_api("Phone Numbers APIs"))
    api = api_endpoint_section(
        "search-numbers", "01", "Search available numbers", "Query DIDs by country, locality, and capability.",
        "GET", f"{API_BASE}/phone-numbers/search?country=US&area_code=415&provider=twilio",
        f"""curl -X GET "{API_BASE}/phone-numbers/search?country=US&area_code=415&provider=twilio" \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" """,
        None,
        api_responses("200", "OK — numbers found", """{
  "numbers": [
    { "e164": "+14155551234", "locality": "San Francisco, CA", "monthly_cost_usd": 1.15 },
    { "e164": "+14155559876", "locality": "San Francisco, CA", "monthly_cost_usd": 1.15 }
  ]
}"""),
    )
    api2 = api_endpoint_section(
        "bind-inbound", "02", "Bind number to inbound agent", "Route all calls on a DID to a deployed agent.",
        "POST", f"{API_BASE}/phone-numbers/{{e164}}/inbound",
        f"""curl -X POST {API_BASE}/phone-numbers/%2B14155551234/inbound \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{ "agent_id": "agt_support_en", "fallback_human_sip": "sip:queue@acme.pbx" }}'""",
        """{ "agent_id": "agt_support_en", "fallback_human_sip": "sip:queue@acme.pbx" }""",
        api_responses("200", "OK — inbound route configured", """{
  "e164": "+14155551234",
  "agent_id": "agt_support_en",
  "status": "active"
}"""),
    )
    rel = related_links(BASE_SUB, [("Inbound Agents APIs", "pages/api-docs/inbound-agents-apis.html"), ("Plivo Voice Integrations", "pages/product/plivo-voice-integrations.html")])
    return h + "\n" + api + "\n" + api2 + "\n" + rel


def build_inbound_agents() -> str:
    lead = "Configure how inbound calls are answered — greeting scripts, business-hour routing, RAG context injection, and human handoff thresholds."
    h = hero("API Documentation", "Inbound Agents APIs", lead, BASE_SUB, crumbs_api("Inbound Agents APIs"))
    s1 = prose_section("inbound-routing", "01", "Routing", "Answer policies",
        ["Inbound agents differ from outbound configs: they include <code>greeting_mode</code> (instant vs. ring-delay), "
         "<code>after_hours_agent_id</code>, and <code>handoff_sentiment_threshold</code> for live supervisor bridging.",
         "Knowledgebases attached to inbound agents are pre-warmed in vector memory so first-turn RAG retrieval stays under 120ms."])
    api = api_endpoint_section(
        "patch-inbound", "02", "Update inbound policy", "Set handoff rules and knowledgebase bindings.",
        "PATCH", f"{API_BASE}/agents/{{agent_id}}/inbound",
        f"""curl -X PATCH {API_BASE}/agents/agt_support_en/inbound \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "knowledgebase_ids": ["kb_product_faq", "kb_returns_policy"],
    "handoff_sentiment_threshold": 0.35,
    "max_turns_before_handoff": 12
  }}'""",
        """{
  "knowledgebase_ids": ["kb_product_faq", "kb_returns_policy"],
  "handoff_sentiment_threshold": 0.35,
  "max_turns_before_handoff": 12
}""",
        api_responses("200", "OK — inbound policy saved", """{
  "agent_id": "agt_support_en",
  "knowledgebase_ids": ["kb_product_faq", "kb_returns_policy"],
  "handoff_sentiment_threshold": 0.35
}"""),
    )
    rel = related_links(BASE_SUB, [("Knowledgebases APIs", "pages/api-docs/knowledgebases-apis.html"), ("PDFs, RAGs & Knowledge bases", "pages/product/pdfs-rags-knowledge-bases.html")])
    return h + "\n" + s1 + "\n" + api + "\n" + rel


def build_knowledgebases() -> str:
    lead = "Upload PDFs, connect vector databases, and sync internal wikis. EMAAVY chunks, embeds, and serves context to agents mid-call with sub-200ms retrieval."
    h = hero("API Documentation", "Knowledgebases APIs", lead, BASE_SUB, crumbs_api("Knowledgebases APIs"))
    api = api_endpoint_section(
        "create-kb", "01", "Create a knowledgebase", "Register a RAG corpus for agent grounding.",
        "POST", f"{API_BASE}/knowledgebases",
        f"""curl -X POST {API_BASE}/knowledgebases \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "name": "Product FAQ — Q2 2026",
    "embedding_model": "text-embedding-3-large",
    "vector_store": {{ "type": "pinecone", "index": "emaavy-acme-prod" }},
    "chunk_size_tokens": 512
  }}'""",
        """{
  "name": "Product FAQ — Q2 2026",
  "embedding_model": "text-embedding-3-large",
  "vector_store": { "type": "pinecone", "index": "emaavy-acme-prod" },
  "chunk_size_tokens": 512
}""",
        api_responses("200", "OK — knowledgebase created", """{
  "id": "kb_product_faq",
  "status": "ready",
  "document_count": 0,
  "chunk_count": 0
}"""),
    )
    api2 = api_endpoint_section(
        "upload-pdf", "02", "Ingest a PDF", "Upload and asynchronously index a document.",
        "POST", f"{API_BASE}/knowledgebases/{{kb_id}}/documents",
        f"""curl -X POST {API_BASE}/knowledgebases/kb_product_faq/documents \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -F "file=@returns-policy.pdf" \\
  -F 'metadata={{\"department\":\"support\"}}' """,
        None,
        api_responses("200", "OK — document queued", """{
  "document_id": "doc_3f8a",
  "status": "processing",
  "estimated_chunks": 42
}"""),
    )
    rel = related_links(BASE_SUB, [("Using Agents APIs", "pages/api-docs/using-agents-apis.html"), ("PDFs, RAGs & Knowledge bases", "pages/product/pdfs-rags-knowledge-bases.html")])
    return h + "\n" + api + "\n" + api2 + "\n" + rel


def build_batch_queue() -> str:
    lead = "Enqueue thousands of outbound dials with intelligent pacing, timezone windows, retry policies, and per-sub-account rate limits."
    h = hero("API Documentation", "Batch & Queue APIs", lead, BASE_SUB, crumbs_api("Batch & Queue APIs"))
    api = api_endpoint_section(
        "create-batch", "01", "Create a batch job", "Upload contacts and schedule a campaign wave.",
        "POST", f"{API_BASE}/batches",
        f"""curl -X POST {API_BASE}/batches \\
  -H "Authorization: Bearer <EMAAVY_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "agent_id": "agt_4kLm9",
    "name": "June renewal reminders",
    "contacts": [
      {{ "to": "+919876543210", "vars": {{ "first_name": "Anita", "due_date": "2026-06-15" }} }}
    ],
    "pacing": {{ "max_concurrent": 40, "calls_per_minute": 120 }},
    "retry": {{ "no_answer": {{ "attempts": 2, "delay_minutes": 180 }} }}
  }}'""",
        """{
  "agent_id": "agt_4kLm9",
  "name": "June renewal reminders",
  "contacts": [{ "to": "+919876543210", "vars": { "first_name": "Anita", "due_date": "2026-06-15" } }],
  "pacing": { "max_concurrent": 40, "calls_per_minute": 120 },
  "retry": { "no_answer": { "attempts": 2, "delay_minutes": 180 } }
}""",
        api_responses("200", "OK — batch queued", """{
  "batch_id": "batch_7hK2",
  "status": "queued",
  "contact_count": 1,
  "estimated_start": "2026-05-30T11:00:00Z"
}"""),
    )
    rel = related_links(BASE_SUB, [("Bulk Calls & Campaigns", "pages/product/bulk-calls-campaigns.html"), ("Making Phone Calls APIs", "pages/api-docs/making-phone-calls-apis.html")])
    return h + "\n" + api + "\n" + rel


def build_sub_account() -> str:
    lead = "Provision isolated sub-accounts for agencies, portfolio companies, or business units — each with separate API keys, billing meters, and data residency controls."
    h = hero("API Documentation", "Sub-account Isolation APIs", lead, BASE_SUB, crumbs_api("Sub-account Isolation APIs"))
    s1 = prose_section("isolation", "01", "Model", "Hard tenant boundaries",
        ["Sub-accounts are first-class tenants. Agents, numbers, recordings, and vector indices are namespaced by "
         "<code>sub_account_id</code>. Cross-tenant reads return <code>404</code> — not <code>403</code> — to prevent enumeration.",
         "Parent accounts can impersonate sub-accounts using <code>X-EMAAVY-Act-As: sub_acct_8f2k9</code> for support workflows, audited in immutable logs."])
    api = api_endpoint_section(
        "create-sub", "02", "Create sub-account", "Spin up a child tenant under your organization.",
        "POST", f"{API_BASE}/sub-accounts",
        f"""curl -X POST {API_BASE}/sub-accounts \\
  -H "Authorization: Bearer <EMAAVY_PARENT_API_KEY>" \\
  -H "Content-Type: application/json" \\
  -d '{{
    "name": "Acme — APAC Sales",
    "billing_email": "finance@acme.com",
    "data_region": "ap-south-1"
  }}'""",
        """{
  "name": "Acme — APAC Sales",
  "billing_email": "finance@acme.com",
  "data_region": "ap-south-1"
}""",
        api_responses("200", "OK — sub-account created", """{
  "id": "sub_acct_8f2k9",
  "name": "Acme — APAC Sales",
  "data_region": "ap-south-1",
  "status": "active"
}"""),
    )
    rel = related_links(BASE_SUB, [("API Authentication", "pages/api-docs/api-authentication.html"), ("Pricing & Plans", "pages/pricing.html")])
    return h + "\n" + s1 + "\n" + api + "\n" + rel


# ─── Product pages ───

def build_dashboard_analytics() -> str:
    lead = "Monitor live call feeds, campaign conversion funnels, agent latency percentiles, and sub-account usage from a unified operations dashboard."
    h = hero("Product Features", "Dashboard & Analytics", lead, BASE_SUB, crumbs_product("Dashboard & Analytics"),
             [("Live", "Call map"), ("P99", "Latency charts")])
    s1 = feature_list_section("metrics", "01", "Metrics", "What you see in real time",
        "EMAAVY's dashboard streams telemetry from the inference plane and telephony edge:",
        ["<strong>Active calls map</strong> — live transcript preview and sentiment color coding per session",
         "<strong>Campaign funnel</strong> — connected, qualified, booked, and lost outcomes updated per dial",
         "<strong>Agent leaderboard</strong> — conversion rate, average handle time, tool success ratio",
         "<strong>System latency</strong> — STT, LLM, TTS, and tool execution P50/P95/P99 with SLA breach alerts"])
    s2 = prose_section("export", "02", "Reporting", "Export & BI hooks", [
        "Schedule daily CSV exports to S3 or push metrics to your warehouse via webhook. "
        "Every chart maps to a <code>GET /v1/analytics/*</code> endpoint for programmatic reporting."], alt=True)
    rel = related_links(BASE_SUB, [("Bulk Calls & Campaigns", "pages/product/bulk-calls-campaigns.html"), ("Get Call Data APIs", "pages/api-docs/get-call-data-apis.html")])
    return h + "\n" + s1 + "\n" + s2 + "\n" + rel


def build_tool_calling() -> str:
    lead = "Define OpenAI-compatible function schemas that agents invoke mid-call — CRM lookups, payment links, calendar bookings — executed in EMAAVY's audited sandbox with sub-250ms p95."
    h = hero("Product Features", "Function & Tool Calling", lead, BASE_SUB, crumbs_product("Function & Tool Calling"))
    s1 = prose_section("sandbox", "01", "Execution", "Secure tool runtime",
        ["Tools never run on the LLM provider's infrastructure. EMAAVY validates JSON arguments against your schema, "
         "executes HTTP webhooks or native integrations (Salesforce, HubSpot, Cal.com), and injects results back into the conversational context before the next TTS chunk synthesizes.",
         "Failed tools trigger graceful verbal fallbacks — agents apologize, retry once, or offer human handoff based on your policy."])
    s2 = feature_list_section("patterns", "02", "Patterns", "Common production tools", "Teams ship these tool bundles on day one:",
        ["<code>crm.lookup_contact</code> — hydrate caller context from Salesforce or HubSpot",
         "<code>calendar.book_slot</code> — real-time Cal.com availability check and booking",
         "<code>payments.send_link</code> — Razorpay/Stripe payment link over SMS post-call",
         "<code>kb.search</code> — vector retrieval against attached knowledgebases"], alt=True)
    rel = related_links(BASE_SUB, [("Using Agents APIs", "pages/api-docs/using-agents-apis.html"), ("Voice Agent Integrations Ecosystem", "pages/product/voice-agent-integrations-ecosystem.html")])
    return h + "\n" + s1 + "\n" + s2 + "\n" + rel


def build_rag_kb() -> str:
    lead = "Ground agents in PDFs, Notion exports, and custom vector DBs. Retrieval runs in parallel with STT so answers cite accurate policy language during live calls."
    h = hero("Product Features", "PDFs, RAGs & Knowledge bases", lead, BASE_SUB, crumbs_product("PDFs, RAGs & Knowledge bases"))
    s1 = prose_section("pipeline", "01", "Pipeline", "Mid-call RAG architecture",
        ["When a caller asks a product question, EMAAVY runs hybrid search (dense vectors + BM25) across attached knowledgebases. "
         "Top-k chunks are reranked by a cross-encoder, then compressed into a citation-aware context block fed to the LLM.",
         "Agents speak answers — they do not read URLs aloud. Source documents are logged per turn for compliance review."])
    s2 = feature_list_section("sources", "02", "Sources", "Supported knowledge sources", "Connect the systems you already use:",
        ["PDF, DOCX, and Markdown uploads with OCR for scanned pages",
         "Pinecone, Weaviate, Qdrant, and pgvector connectors",
         "Scheduled sync from Confluence, Notion, and Google Drive",
         "Per-agent knowledgebase bindings with version pinning"], alt=True)
    rel = related_links(BASE_SUB, [("Knowledgebases APIs", "pages/api-docs/knowledgebases-apis.html"), ("Inbound Agents APIs", "pages/api-docs/inbound-agents-apis.html")])
    return h + "\n" + s1 + "\n" + s2 + "\n" + rel


def build_twilio_product() -> str:
    lead = "EMAAVY connects directly to Twilio Programmable Voice — provision numbers, stream bidirectional media, and receive call status webhooks without managing TwiML yourself."
    h = hero("Product Features", "Twilio Voice Integrations", lead, BASE_SUB, crumbs_product("Twilio Voice Integrations"))
    s1 = prose_section("twilio", "01", "Integration", "How EMAAVY uses Twilio",
        ["Link your Twilio Account SID and Auth Token once. EMAAVY creates subaccounts per tenant, provisions numbers via API, "
         "and registers <code>&lt;Connect&gt;</code> streams that pipe μ-law audio into our inference cluster.",
         "Outbound calls use Twilio's REST API with EMAAVY-owned TwiML endpoints. Inbound calls hit the same media bridge — one integration path for both directions."])
    s2 = feature_list_section("capabilities", "02", "Capabilities", "Production-ready telephony",
        "Everything you need for AI voice at scale on Twilio:", [
        "Elastic SIP trunking for existing PBX estates",
        "Answering machine detection with configurable policies",
        "Call recording with dual-channel separation",
        "Geo-matched caller ID pools for local presence"], alt=True)
    rel = related_links(BASE_SUB, [("Twilio partner page", "pages/integrations/twilio.html"), ("Making Phone Calls APIs", "pages/api-docs/making-phone-calls-apis.html")])
    return h + "\n" + s1 + "\n" + s2 + "\n" + rel


def build_plivo_product() -> str:
    lead = "Route high-volume AI workloads through Plivo's direct-carrier network. EMAAVY manages XML endpoints, media streaming, and per-destination rate optimization."
    h = hero("Product Features", "Plivo Voice Integrations", lead, BASE_SUB, crumbs_product("Plivo Voice Integrations"))
    s1 = prose_section("plivo", "01", "Integration", "Plivo + EMAAVY architecture",
        ["Plivo excels at cost-efficient international termination. EMAAVY's Plivo adapter normalizes call events into the same "
         "<code>call_id</code> schema used for Twilio — swap providers per campaign without rewriting agent logic.",
         "Media streams use Plivo's AudioStream API with automatic codec negotiation and packet loss concealment tuned for LLM turn-taking."])
    rel = related_links(BASE_SUB, [("Plivo partner page", "pages/integrations/plivo.html"), ("Phone Numbers APIs", "pages/api-docs/phone-numbers-apis.html")])
    return h + "\n" + s1 + "\n" + rel


def build_multilingual() -> str:
    lead = "Deploy agents that code-switch between English, Hindi, Hinglish, and 20+ Indian regional languages — with Sarvam STT, Bulbul TTS, and Qwen routing for native comprehension."
    h = hero("Product Features", "Multilingual Voice Support", lead, BASE_SUB, crumbs_product("Multilingual Voice Support"),
             [("22+", "Indian languages"), ("Auto", "Language detect")])
    s1 = feature_list_section("stack", "01", "Stack", "Language-aware routing",
        "EMAAVY selects STT, LLM, and TTS triples per detected language:",
        ["Hinglish outbound sales — Sarvam STT + Qwen 3.6 + Bulbul V3",
         "Tamil support — Sarvam STT + Gemini Flash + ElevenMultilingual",
         "US English enterprise — Deepgram Nova-2 + GPT-4.1 + ElevenTurbo",
         "Auto-detect switches mid-call when callers change language"])
    rel = related_links(BASE_SUB, [("Agent Library & Templates", "pages/product/agent-library-templates.html"), ("Top Voice Agents Use Cases", "pages/company/top-voice-agents-use-cases.html")])
    return h + "\n" + s1 + "\n" + rel


def build_bulk_campaigns() -> str:
    lead = "Launch outbound waves to millions of contacts with timezone-aware scheduling, DNC enforcement, dynamic script variables, and live pause/resume controls."
    h = hero("Product Features", "Bulk Calls & Campaigns", lead, BASE_SUB, crumbs_product("Bulk Calls & Campaigns"))
    s1 = prose_section("orchestration", "01", "Orchestration", "Campaign engine",
        ["Upload CSV or push contacts via API. EMAAVY's queue shards work across telephony regions, respecting "
         "<code>calls_per_minute</code> caps per sub-account and carrier feedback loops that throttle on high AMD or short-call rates.",
         "Personalization variables (<code>{{first_name}}</code>, <code>{{outstanding_balance}}</code>) hydrate agent prompts per dial without creating per-contact agent copies."])
    s2 = feature_list_section("controls", "02", "Controls", "Operator tooling", "Campaign managers get:",
        ["Live pause/resume without dropping in-flight calls",
         "A/B agent variants with statistical significance tracking",
         "Automatic retry windows per outcome (no-answer, busy, voicemail)",
         "Real-time connect rate and conversion dashboards"], alt=True)
    rel = related_links(BASE_SUB, [("Batch & Queue APIs", "pages/api-docs/batch-queue-apis.html"), ("Dashboard & Analytics", "pages/product/dashboard-analytics.html")])
    return h + "\n" + s1 + "\n" + s2 + "\n" + rel


def build_agent_library() -> str:
    lead = "Start from production-tested templates — sales qualification, appointment booking, payment reminders, NPS surveys — and customize flows in the visual builder."
    h = hero("Product Features", "Agent Library & Templates", lead, BASE_SUB, crumbs_product("Agent Library & Templates"))
    s1 = feature_list_section("templates", "01", "Templates", "Ship faster with proven flows",
        "Each template includes prompt chains, tool wiring, and voice presets:",
        ["<strong>Real Estate Lead Qualification</strong> — budget, timeline, and site-visit booking",
         "<strong>Appointment Reminder</strong> — contextual rescheduling with calendar tools",
         "<strong>Payment Check-in</strong> — empathetic collections with payment-link tool",
         "<strong>NPS Review</strong> — score capture and detractor escalation"])
    rel = related_links(BASE_SUB, [("Agent Directory", "pages/agents/index.html"), ("Using Agents APIs", "pages/api-docs/using-agents-apis.html")])
    return h + "\n" + s1 + "\n" + rel


def build_integrations_ecosystem() -> str:
    lead = "EMAAVY orchestrates a full voice AI stack — telephony, STT, LLM, TTS, CRM, calendars, and webhooks — with per-layer routing and failover."
    h = hero("Product Features", "Voice Agent Integrations Ecosystem", lead, BASE_SUB, crumbs_product("Voice Agent Integrations Ecosystem"))
    s1 = prose_section("layers", "01", "Layers", "Composable stack",
        ["Every layer is swappable per agent or campaign. Run Deepgram + OpenAI + ElevenLabs for US sales, "
         "Sarvam + Qwen + Bulbul for Indian support — without forking your integration code.",
         "The integration hub documents 40+ partners with connection guides, latency benchmarks, and recommended pairings."])
    rel = related_links(BASE_SUB, [("Integration hub", "pages/integrations/index.html"), ("Function & Tool Calling", "pages/product/function-tool-calling.html")])
    return h + "\n" + s1 + "\n" + rel


# ─── Company pages ───

def build_yc_profile() -> str:
    lead = "EMAAVY is building the developer-first control plane for production voice agents — YC-backed, telephony-native, and obsessed with sub-second conversational latency."
    h = hero("Company & Resources", "YC Launch Profile", lead, BASE_SUB, crumbs_company("YC Launch Profile"))
    s1 = prose_section("mission", "01", "Mission", "Why we exist",
        ["Voice is the highest-bandwidth interface between businesses and customers, yet most teams still wire together "
         "five vendors to ship a single agent. EMAAVY collapses telephony, realtime inference, RAG, and tool execution into one API — "
         "the way Bolna simplified orchestration, but with first-class Twilio/Plivo pipes and multi-tenant isolation for agencies.",
         "We process millions of minutes monthly for BPOs, fintech collections, healthcare scheduling, and event registration — "
         "verticals where latency and accent accuracy determine conversion."])
    s2 = prose_section("founders", "02", "Team", "Built by infra engineers",
        ["Founded by engineers who ran realtime ML infra at scale. We have shipped sub-200ms inference paths, "
         "carrier-grade SIP bridges, and vector search hot paths purpose-built for telephony audio — not chat widgets."], alt=True)
    rel = related_links(BASE_SUB, [("Schedule a Demo", "book-demo.html"), ("Engineering Blog", "pages/company/engineering-blog.html")])
    return h + "\n" + s1 + "\n" + s2 + "\n" + rel


def build_engineering_blog() -> str:
    lead = "Deep dives on realtime voice inference, telephony media bridging, RAG at conversational speed, and multi-tenant isolation patterns."
    h = hero("Company & Resources", "EMAAVY Engineering Blog", lead, BASE_SUB, crumbs_company("EMAAVY Engineering Blog"))
    s1 = feature_list_section("posts", "01", "Recent posts", "From the EMAAVY engineering team",
        "Technical essays on building production voice agents:",
        ["<strong>Sub-800ms mouth-to-ear on Twilio</strong> — STT chunking, LLM streaming, and TTS overlap strategies",
         "<strong>RAG during live calls</strong> — hybrid retrieval without blocking the conversational turn",
         "<strong>Tool sandbox isolation</strong> — how we execute customer webhooks without leaking network topology",
         "<strong>Sub-account sharding</strong> — tenancy boundaries from API gateway to vector index"])
    rel = related_links(BASE_SUB, [("Documentation", "pages/documentation.html"), ("API Authentication", "pages/api-docs/api-authentication.html")])
    return h + "\n" + s1 + "\n" + rel


def build_news_updates() -> str:
    lead = "Product releases, integration launches, and platform improvements — what shipped this quarter on EMAAVY."
    h = hero("Company & Resources", "News & Product Updates", lead, BASE_SUB, crumbs_company("News & Product Updates"))
    s1 = feature_list_section("releases", "01", "2026 highlights", "Recent launches",
        "Platform updates for voice AI builders:",
        ["<strong>May 2026</strong> — Plivo media streaming GA with automatic failover to Twilio",
         "<strong>April 2026</strong> — Sub-account isolation APIs and per-tenant billing meters",
         "<strong>March 2026</strong> — Pinecone & Weaviate native connectors for knowledgebases",
         "<strong>February 2026</strong> — Bulk batch API v2 with timezone-aware pacing"])
    rel = related_links(BASE_SUB, [("System Status", "pages/company/system-status.html"), ("Pricing & Plans", "pages/pricing.html")])
    return h + "\n" + s1 + "\n" + rel


def build_llms_txt_page() -> str:
    lead = "Machine-readable site summary for LLM crawlers — endpoints, capabilities, and contact paths in llms.txt format."
    h = hero("Company & Resources", "LLMs.txt (AI Scraping Spec)", lead, BASE_SUB, crumbs_company("LLMs.txt"))
    body = """# EMAAVY — Voice AI Agent Platform

> Build, deploy, and manage production LLM-powered voice agents with Twilio/Plivo telephony, RAG knowledgebases, and developer APIs.

## Core capabilities
- Outbound and inbound AI voice agents
- Twilio and Plivo direct integrations
- Vector DB / PDF knowledgebases with mid-call RAG
- Function & tool calling (CRM, calendars, webhooks)
- Bulk campaigns and batch queue APIs
- Multi-tenant sub-account isolation

## API base
https://api.emaavy.com/v1

## Key pages
- Documentation: /pages/documentation.html
- API Authentication: /pages/api-docs/api-authentication.html
- Pricing: /pages/pricing.html
- Contact: /pages/contact.html
- Book demo: /book-demo.html

## Contact
- sales@emaavy.com
- support@emaavy.com
"""
    s1 = f"""    <section class="page-section">
      <div class="container">
        <article class="capability-block footer-doc-block">
          <div class="capability-content">
            <p>Raw <code>llms.txt</code> served at <a href="../../llms.txt">/llms.txt</a> for compliant AI indexing.</p>
            <pre class="footer-code-block footer-llms-pre"><code>{body.strip()}</code></pre>
          </div>
        </article>
      </div>
    </section>"""
    rel = related_links(BASE_SUB, [("Docs LLMs.txt", "pages/company/docs-llms-txt.html"), ("Documentation", "pages/documentation.html")])
    return h + "\n" + s1 + "\n" + rel


def build_docs_llms_txt_page() -> str:
    lead = "Developer-focused llms.txt subset — API surfaces, authentication, and integration references for coding agents."
    h = hero("Company & Resources", "Docs LLMs.txt", lead, BASE_SUB, crumbs_company("Docs LLMs.txt"))
    body = """# EMAAVY API Documentation Index

## Authentication
Authorization: Bearer <EMAAVY_API_KEY>
Docs: /pages/api-docs/api-authentication.html

## Agents
POST /v1/agents — create agent
GET /v1/agents/{id} — retrieve agent
Docs: /pages/api-docs/using-agents-apis.html

## Calls
POST /v1/calls — place outbound call
GET /v1/calls/{id} — transcript & scores
Docs: /pages/api-docs/making-phone-calls-apis.html

## Knowledgebases
POST /v1/knowledgebases — create corpus
Docs: /pages/api-docs/knowledgebases-apis.html

## Telephony
Providers: twilio, plivo
Docs: /pages/product/twilio-voice-integrations.html
"""
    s1 = f"""    <section class="page-section">
      <div class="container">
        <article class="capability-block footer-doc-block">
          <div class="capability-content">
            <p>Raw file at <a href="../../docs-llms.txt">/docs-llms.txt</a></p>
            <pre class="footer-code-block footer-llms-pre"><code>{body.strip()}</code></pre>
          </div>
        </article>
      </div>
    </section>"""
    rel = related_links(BASE_SUB, [("LLMs.txt", "pages/company/llms-txt.html"), ("API Reference", "pages/documentation.html")])
    return h + "\n" + s1 + "\n" + rel


def build_use_cases() -> str:
    lead = "Production voice agent patterns teams deploy on EMAAVY — from BPO QA to fintech collections and healthcare scheduling."
    h = hero("Company & Resources", "Top Voice Agents Use Cases", lead, BASE_SUB, crumbs_company("Top Voice Agents Use Cases"))
    s1 = feature_list_section("cases", "01", "Use cases", "Highest-ROI deployments",
        "Customers ship these agents in the first 30 days:",
        ["<strong>BPO quality & coaching</strong> — 100% call scoring with realtime supervisor alerts",
         "<strong>Lead qualification</strong> — bilingual outbound with CRM sync and meeting booking",
         "<strong>Payment reminders</strong> — empathetic collections with payment-link tools",
         "<strong>Patient scheduling</strong> — HIPAA-aligned inbound with calendar integration",
         "<strong>Event registration</strong> — high-volume outbound with WhatsApp confirmation"])
    rel = related_links(BASE_SUB, [("Case Studies", "pages/case-studies.html"), ("Agent Library", "pages/product/agent-library-templates.html")])
    return h + "\n" + s1 + "\n" + rel


def build_system_status() -> str:
    lead = "Realtime platform health — API gateway, inference plane, telephony edge, and webhook delivery."
    h = hero("Company & Resources", "System Status", lead, BASE_SUB, crumbs_company("System Status"))
    s1 = f"""    <section class="page-section">
      <div class="container">
        <article class="capability-block footer-doc-block">
          <div class="capability-content">
            <div class="footer-status-page"><span class="footer-status-dot" aria-hidden="true"></span> All systems operational</div>
            <p style="margin-top:1rem;color:#475569;">Last updated: 30 May 2026, 10:00 UTC. API P99 latency 142ms. Media bridge uptime 99.99% (30-day).</p>
            <ul class="footer-feature-list">
              <li><strong>API Gateway</strong> — Operational</li>
              <li><strong>Realtime Inference (STT/LLM/TTS)</strong> — Operational</li>
              <li><strong>Twilio Media Edge</strong> — Operational</li>
              <li><strong>Plivo Media Edge</strong> — Operational</li>
              <li><strong>Webhook Delivery</strong> — Operational</li>
              <li><strong>Knowledgebase Indexing</strong> — Operational</li>
            </ul>
          </div>
        </article>
      </div>
    </section>"""
    rel = related_links(BASE_SUB, [("News & Product Updates", "pages/company/news-product-updates.html"), ("Contact support", "pages/contact.html")])
    return h + "\n" + s1 + "\n" + rel


def build_terms() -> str:
    lead = "Terms governing use of the EMAAVY platform, APIs, and voice agent services."
    h = hero("Legal", "Terms of Use", lead, BASE_SUB, crumbs_legal("Terms of Use"))
    s1 = prose_section("terms", "01", "Agreement", "Using EMAAVY",
        ["By accessing EMAAVY's dashboard, APIs, or voice services, you agree to these Terms. You must comply with applicable telemarketing, recording consent, and data protection laws in every jurisdiction you dial or receive calls.",
         "You are responsible for prompt content, knowledgebase accuracy, and obtaining callee consent. EMAAVY provides infrastructure — not legal advice on campaign compliance."])
    s2 = prose_section("api", "02", "API usage", "Rate limits & acceptable use",
        ["API keys are non-transferable. Reverse engineering, circumventing rate limits, or reselling raw telephony minutes without authorization is prohibited.",
         "We may suspend accounts that generate abusive traffic patterns or violate carrier acceptable-use policies."], alt=True)
    return h + "\n" + s1 + "\n" + s2


def build_privacy() -> str:
    lead = "How EMAAVY collects, processes, and protects call audio, transcripts, and account data."
    h = hero("Legal", "Privacy Policy", lead, BASE_SUB, crumbs_legal("Privacy Policy"))
    s1 = prose_section("data", "01", "Data we process", "Call and account data",
        ["We process call audio, transcripts, metadata, and tool execution logs to deliver voice agent services. "
         "Customers control retention windows per sub-account — default 90 days for recordings, configurable to zero-storage modes.",
         "Vector embeddings derived from your knowledgebases remain in your chosen region. EMAAVY does not train foundation models on customer call content without explicit opt-in."])
    s2 = prose_section("rights", "02", "Your rights", "Access & deletion",
        ["Submit data access or deletion requests to privacy@emaavy.com. Enterprise customers receive DPA and SCC packages with designated security contacts."], alt=True)
    return h + "\n" + s1 + "\n" + s2


BUILDERS: dict[str, tuple[str, str, str, callable]] = {
    # slug -> (route, title, description, builder)
    "api-authentication": ("footer-api-authentication", "API Authentication",
        "Authenticate EMAAVY REST requests with Bearer API keys, sub-account scoping, and granular permissions.", build_api_auth),
    "using-agents-apis": ("footer-using-agents-apis", "Using Agents APIs",
        "Create, version, and deploy production voice agents via REST with LLM, STT, TTS, and tool configurations.", build_using_agents),
    "making-phone-calls-apis": ("footer-making-phone-calls-apis", "Making Phone Calls APIs",
        "Initiate outbound calls over Twilio or Plivo with live agent media streaming and sub-second inference.", build_phone_calls),
    "get-call-data-apis": ("footer-get-call-data-apis", "Get Call Data APIs",
        "Retrieve transcripts, sentiment scores, tool logs, and recordings for active and completed calls.", build_get_call_data),
    "phone-numbers-apis": ("footer-phone-numbers-apis", "Phone Numbers APIs",
        "Search, purchase, and bind phone numbers to inbound agents and outbound caller-ID pools.", build_phone_numbers),
    "inbound-agents-apis": ("footer-inbound-agents-apis", "Inbound Agents APIs",
        "Configure inbound greeting, RAG knowledgebases, business-hour routing, and human handoff policies.", build_inbound_agents),
    "knowledgebases-apis": ("footer-knowledgebases-apis", "Knowledgebases APIs",
        "Create vector knowledgebases, ingest PDFs, and ground agents with mid-call RAG retrieval.", build_knowledgebases),
    "batch-queue-apis": ("footer-batch-queue-apis", "Batch & Queue APIs",
        "Enqueue bulk outbound campaigns with pacing, retries, and timezone-aware scheduling.", build_batch_queue),
    "sub-account-isolation-apis": ("footer-sub-account-isolation-apis", "Sub-account Isolation APIs",
        "Provision isolated sub-accounts with separate API keys, billing, and data residency.", build_sub_account),
    "dashboard-analytics": ("footer-dashboard-analytics", "Dashboard & Analytics",
        "Live call monitoring, campaign funnels, latency percentiles, and exportable analytics.", build_dashboard_analytics),
    "function-tool-calling": ("footer-function-tool-calling", "Function & Tool Calling",
        "Secure mid-call tool execution for CRM, calendars, payments, and custom webhooks.", build_tool_calling),
    "pdfs-rags-knowledge-bases": ("footer-pdfs-rags-knowledge-bases", "PDFs, RAGs & Knowledge bases",
        "Ground voice agents in PDFs and vector DBs with hybrid retrieval during live calls.", build_rag_kb),
    "twilio-voice-integrations": ("footer-twilio-voice-integrations", "Twilio Voice Integrations",
        "Direct Twilio Programmable Voice integration with media streaming and number management.", build_twilio_product),
    "plivo-voice-integrations": ("footer-plivo-voice-integrations", "Plivo Voice Integrations",
        "High-volume voice through Plivo direct-carrier routes with unified EMAAVY call schema.", build_plivo_product),
    "multilingual-voice-support": ("footer-multilingual-voice-support", "Multilingual Voice Support",
        "22+ Indian languages, Hinglish code-switching, and per-language STT/LLM/TTS routing.", build_multilingual),
    "bulk-calls-campaigns": ("footer-bulk-calls-campaigns", "Bulk Calls & Campaigns",
        "Million-contact outbound campaigns with pacing, DNC, personalization, and live controls.", build_bulk_campaigns),
    "agent-library-templates": ("footer-agent-library-templates", "Agent Library & Templates",
        "Production-tested agent templates for sales, support, collections, and surveys.", build_agent_library),
    "voice-agent-integrations-ecosystem": ("footer-voice-agent-integrations-ecosystem", "Voice Agent Integrations Ecosystem",
        "Composable telephony, STT, LLM, TTS, and CRM layers with per-agent routing.", build_integrations_ecosystem),
    "yc-launch-profile": ("footer-yc-launch-profile", "YC Launch Profile",
        "EMAAVY company profile — developer-first voice AI platform, YC-backed, telephony-native.", build_yc_profile),
    "engineering-blog": ("footer-engineering-blog", "EMAAVY Engineering Blog",
        "Engineering deep dives on realtime voice inference, RAG, and telephony media bridging.", build_engineering_blog),
    "news-product-updates": ("footer-news-product-updates", "News & Product Updates",
        "EMAAVY product releases, integration launches, and platform improvements.", build_news_updates),
    "llms-txt": ("footer-llms-txt", "LLMs.txt (AI Scraping Spec)",
        "Machine-readable EMAAVY site summary for LLM crawlers and AI indexing.", build_llms_txt_page),
    "docs-llms-txt": ("footer-docs-llms-txt", "Docs LLMs.txt",
        "Developer-focused llms.txt with API surfaces and documentation links.", build_docs_llms_txt_page),
    "top-voice-agents-use-cases": ("footer-top-voice-agents-use-cases", "Top Voice Agents Use Cases",
        "Highest-ROI voice agent deployments on EMAAVY across industries.", build_use_cases),
    "system-status": ("footer-system-status", "System Status",
        "EMAAVY platform health — API, inference, telephony, and webhooks.", build_system_status),
    "terms-of-use": ("footer-terms-of-use", "Terms of Use",
        "Terms governing use of EMAAVY platform, APIs, and voice services.", build_terms),
    "privacy-policy": ("footer-privacy-policy", "Privacy Policy",
        "How EMAAVY handles call audio, transcripts, and account data.", build_privacy),
}

FOLDER_MAP = {
    "api-authentication": "api-docs", "using-agents-apis": "api-docs", "making-phone-calls-apis": "api-docs",
    "get-call-data-apis": "api-docs", "phone-numbers-apis": "api-docs", "inbound-agents-apis": "api-docs",
    "knowledgebases-apis": "api-docs", "batch-queue-apis": "api-docs", "sub-account-isolation-apis": "api-docs",
    "dashboard-analytics": "product", "function-tool-calling": "product", "pdfs-rags-knowledge-bases": "product",
    "twilio-voice-integrations": "product", "plivo-voice-integrations": "product", "multilingual-voice-support": "product",
    "bulk-calls-campaigns": "product", "agent-library-templates": "product", "voice-agent-integrations-ecosystem": "product",
    "yc-launch-profile": "company", "engineering-blog": "company", "news-product-updates": "company",
    "llms-txt": "company", "docs-llms-txt": "company", "top-voice-agents-use-cases": "company", "system-status": "company",
    "terms-of-use": "legal", "privacy-policy": "legal",
}


def write_llms_files():
    llms = """# EMAAVY — Voice AI Agent Platform

> Build, deploy, and manage production LLM-powered voice agents with Twilio/Plivo telephony, RAG knowledgebases, and developer APIs.

## Core capabilities
- Outbound and inbound AI voice agents
- Twilio and Plivo direct integrations
- Vector DB / PDF knowledgebases with mid-call RAG
- Function & tool calling (CRM, calendars, webhooks)
- Bulk campaigns and batch queue APIs
- Multi-tenant sub-account isolation

## API base
https://api.emaavy.com/v1

## Key pages
- Documentation: /pages/documentation.html
- API Authentication: /pages/api-docs/api-authentication.html
- Pricing: /pages/pricing.html
- Contact: /pages/contact.html
- Book demo: /book-demo.html

## Contact
- sales@emaavy.com
- support@emaavy.com
"""
    docs = """# EMAAVY API Documentation Index

## Authentication
Authorization: Bearer <EMAAVY_API_KEY>
Docs: /pages/api-docs/api-authentication.html

## Agents
POST /v1/agents — create agent
GET /v1/agents/{id} — retrieve agent
Docs: /pages/api-docs/using-agents-apis.html

## Calls
POST /v1/calls — place outbound call
GET /v1/calls/{id} — transcript & scores
Docs: /pages/api-docs/making-phone-calls-apis.html

## Knowledgebases
POST /v1/knowledgebases — create corpus
Docs: /pages/api-docs/knowledgebases-apis.html

## Telephony
Providers: twilio, plivo
Docs: /pages/product/twilio-voice-integrations.html
"""
    (ROOT / "llms.txt").write_text(llms, encoding="utf-8")
    (ROOT / "docs-llms.txt").write_text(docs, encoding="utf-8")


def generate_pages():
    for slug, (route, title, desc, builder) in BUILDERS.items():
        folder = FOLDER_MAP[slug]
        out_dir = ROOT / "pages" / folder
        out_dir.mkdir(parents=True, exist_ok=True)
        content = builder()
        html = shell(title, desc, route, BASE_SUB, content)
        (out_dir / f"{slug}.html").write_text(html, encoding="utf-8")
        print(f"  wrote pages/{folder}/{slug}.html")


def patch_routes():
    text = ROUTES.read_text(encoding="utf-8")
    if "footerNav:" in text:
        text = re.sub(r"  footerNav: \{[\s\S]*?\},\n\n", "", text)

    def link_entry(slug: str, label: str, path: str) -> str:
        rid = slug.replace("-", "_")
        if path.endswith(".txt"):
            rid = slug.replace("-", "_")
        route_id = f"footer-{slug}" if not path.startswith("pages/") and not path.endswith(".html") and path not in ("book-demo.html",) else None
        if slug in BUILDERS:
            route_id = BUILDERS[slug][0]
        if path in ("pages/contact.html", "book-demo.html", "pages/pricing.html"):
            route_id = f"footer-{slug}"
        entry = f"    {{ id: '{slug}', label: '{label}', path: '{path}'"
        if route_id:
            entry += f", route: '{route_id}'"
        return entry + " },"

    api_lines = []
    for item in FOOTER_LINKS["apiDocs"]:
        slug, route, folder, label = item[:4]
        api_lines.append(f"    {{ id: '{slug}', label: '{label}', path: 'pages/api-docs/{slug}.html', route: '{route}' }},")

    prod_lines = []
    for item in FOOTER_LINKS["productFeatures"]:
        slug, route, folder, label = item[:4]
        prod_lines.append(f"    {{ id: '{slug}', label: '{label}', path: 'pages/product/{slug}.html', route: '{route}' }},")

    co_lines = []
    for item in FOOTER_LINKS["companyResources"]:
        if len(item) == 5:
            slug, _, _, label, path = item
            co_lines.append(link_entry(slug, label, path))
        else:
            slug, route, folder, label = item[:4]
            co_lines.append(f"    {{ id: '{slug}', label: '{label}', path: 'pages/company/{slug}.html', route: '{route}' }},")

    legal_lines = [
        "    { id: 'terms-of-use', label: 'Terms of Use', path: 'pages/legal/terms-of-use.html', route: 'footer-terms-of-use' },",
        "    { id: 'privacy-policy', label: 'Privacy Policy', path: 'pages/legal/privacy-policy.html', route: 'footer-privacy-policy' },",
    ]

    block = f"""  footerNav: {{
    apiDocs: [
{chr(10).join(api_lines)}
    ],
    productFeatures: [
{chr(10).join(prod_lines)}
    ],
    companyResources: [
{chr(10).join(co_lines)}
    ],
    legal: [
{chr(10).join(legal_lines)}
    ],
    social: [
      {{ id: 'x', label: 'X (Twitter)', url: 'https://x.com/emaavy' }},
      {{ id: 'linkedin', label: 'LinkedIn', url: 'https://linkedin.com/company/emaavy' }},
      {{ id: 'youtube', label: 'YouTube', url: 'https://youtube.com/@emaavy' }},
    ],
  }},

"""
    text = text.replace("  integrationGroups: [", block + "  integrationGroups: [")
    ROUTES.write_text(text, encoding="utf-8")
    print("patched routes.js")


def patch_index():
    text = INDEX.read_text(encoding="utf-8")
    if "site-footer-root" not in text:
        text = re.sub(r"<footer>.*?</footer>", '<div id="site-footer-root"></div>', text, count=1, flags=re.DOTALL)
    if "footer-premium.css" not in text:
        text = text.replace(
            '<link rel="stylesheet" href="assets/showcase-layer-cards.css" />',
            '<link rel="stylesheet" href="assets/showcase-layer-cards.css" />\n  <link rel="stylesheet" href="assets/footer-premium.css" />',
        )
    INDEX.write_text(text, encoding="utf-8")
    print("patched index.html")


def main():
    print("Generating footer subpages...")
    write_llms_files()
    generate_pages()
    patch_routes()
    patch_index()
    print("Done.")


if __name__ == "__main__":
    main()
