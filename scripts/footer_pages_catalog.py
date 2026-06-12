"""Page definitions for EMAAVY audited footer subpages."""
from __future__ import annotations

API_BASE = "https://api.emaavy.com/v1"

STANDARD_ERRORS = [
    (
        "400",
        "Bad Request",
        """{
  "error": {
    "code": "invalid_request",
    "message": "Missing required field or malformed JSON body.",
    "field": "agent_id"
  }
}""",
    ),
    (
        "401",
        "Unauthorized",
        """{
  "error": {
    "code": "unauthorized",
    "message": "Invalid or missing Authorization header. Use Bearer <EMAAVY_API_KEY>."
  }
}""",
    ),
    (
        "501",
        "Not Implemented",
        """{
  "error": {
    "code": "not_implemented",
    "message": "This endpoint is not enabled for your workspace tier. Contact sales@emaavy.com."
  }
}""",
    ),
]


def api_responses(ok_status: str, ok_label: str, ok_body: str) -> list[tuple[str, str, str]]:
    return [(ok_status, ok_label, ok_body)] + list(STANDARD_ERRORS)


# slug, route_id, folder, filename, title, description, kicker, category for crumbs
FOOTER_LINKS = {
    "apiDocs": [
        ("api-authentication", "footer-api-authentication", "api-docs", "API Authentication"),
        ("using-agents-apis", "footer-using-agents-apis", "api-docs", "Using Agents APIs"),
        ("making-phone-calls-apis", "footer-making-phone-calls-apis", "api-docs", "Making Phone Calls APIs"),
        ("get-call-data-apis", "footer-get-call-data-apis", "api-docs", "Get Call Data APIs"),
        ("phone-numbers-apis", "footer-phone-numbers-apis", "api-docs", "Phone Numbers APIs"),
        ("inbound-agents-apis", "footer-inbound-agents-apis", "api-docs", "Inbound Agents APIs"),
        ("knowledgebases-apis", "footer-knowledgebases-apis", "api-docs", "Knowledgebases APIs"),
        ("batch-queue-apis", "footer-batch-queue-apis", "api-docs", "Batch & Queue APIs"),
        ("sub-account-isolation-apis", "footer-sub-account-isolation-apis", "api-docs", "Sub-account Isolation APIs"),
    ],
    "productFeatures": [
        ("dashboard-analytics", "footer-dashboard-analytics", "product", "Dashboard & Analytics"),
        ("function-tool-calling", "footer-function-tool-calling", "product", "Function & Tool Calling"),
        ("pdfs-rags-knowledge-bases", "footer-pdfs-rags-knowledge-bases", "product", "PDFs, RAGs & Knowledge bases"),
        ("twilio-voice-integrations", "footer-twilio-voice-integrations", "product", "Twilio Voice Integrations"),
        ("plivo-voice-integrations", "footer-plivo-voice-integrations", "product", "Plivo Voice Integrations"),
        ("multilingual-voice-support", "footer-multilingual-voice-support", "product", "Multilingual Voice Support"),
        ("bulk-calls-campaigns", "footer-bulk-calls-campaigns", "product", "Bulk Calls & Campaigns"),
        ("agent-library-templates", "footer-agent-library-templates", "product", "Agent Library & Templates"),
        ("voice-agent-integrations-ecosystem", "footer-voice-agent-integrations-ecosystem", "product", "Voice Agent Integrations Ecosystem"),
    ],
    "companyResources": [
        ("yc-launch-profile", "footer-yc-launch-profile", "company", "YC Launch Profile"),
        ("contact-us", None, None, "Contact Us", "pages/contact.html"),
        ("schedule-demo-call", None, None, "Schedule a Demo Call", "book-demo.html"),
        ("pricing-plans", None, None, "Pricing & Plans", "pages/pricing.html"),
        ("engineering-blog", "footer-engineering-blog", "company", "EMAAVY Engineering Blog"),
        ("news-product-updates", "footer-news-product-updates", "company", "News & Product Updates"),
        ("llms-txt", "footer-llms-txt", "company", "LLMs.txt (AI Scraping Spec)"),
        ("docs-llms-txt", "footer-docs-llms-txt", "company", "Docs LLMs.txt"),
        ("top-voice-agents-use-cases", "footer-top-voice-agents-use-cases", "company", "Top Voice Agents Use Cases"),
        ("system-status", "footer-system-status", "company", "System Status Indicator"),
    ],
    "legal": [
        ("terms-of-use", "footer-terms-of-use", "legal", "Terms of Use"),
        ("privacy-policy", "footer-privacy-policy", "legal", "Privacy Policy"),
    ],
}
