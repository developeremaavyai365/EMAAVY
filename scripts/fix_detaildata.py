"""Fix broken detailData that causes blank landing page."""
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"

# Restored LLM entries removed by bad telephony patch regex
LLM_RESTORE = """gpt: { tag: 'LLM', title: 'GPT-5.5 / GPT-5.4', logo: '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="OpenAI" style="height:28px"/>', desc: 'OpenAI\\'s flagship models power complex multi-turn sales conversations, objection handling chains, and structured data extraction from live calls.', stats: [['128K','Context window'],['Top tier','Reasoning']], list: ['Multi-step objection handling flows', 'Structured JSON extraction from speech', 'Dynamic script adaptation mid-call', 'Best for high-value enterprise sales'] }, claude: { tag: 'LLM', title: 'Claude Opus · Sonnet · Haiku', logo: '<img src="https://cdn.simpleicons.org/anthropic/0f172a" alt="Anthropic" style="height:28px"/>', desc: 'Anthropic Claude models excel at nuanced comprehension — ideal for compliance-sensitive industries and emotionally complex customer conversations.', stats: [['3 tiers','Opus/Sonnet/Haiku'],['Best','Comprehension']], list: ['Opus for deep reasoning on complex calls', 'Sonnet for balanced speed + quality', 'Haiku for ultra-fast intent classification', 'Strong safety & compliance alignment'] }, gemini: { tag: 'LLM', title: 'Gemini Flash Preview', logo: '<img src="https://cdn.simpleicons.org/google/0f172a" alt="Google" style="height:28px"/>', desc: 'Google Gemini Flash delivers ultra-low-latency inference — perfect for real-time intent detection and live agent assist during active calls.', stats: [['<200ms','Inference'],['Live','Intent scoring']], list: ['Real-time intent classification', 'Live keyword & topic detection', 'Streaming-compatible architecture', 'Cost-efficient at high volume'] }, """

def main():
    text = HTML.read_text(encoding="utf-8")
    broken = "}, , qwen:"
    if broken not in text:
        if "gpt:" in text and "claude:" in text:
            print("detailData already OK")
            return
        print("ERROR: expected broken pattern not found")
        return

    text = text.replace(broken, "}, " + LLM_RESTORE + "qwen:", 1)
    HTML.write_text(text, encoding="utf-8")
    print("Fixed detailData: restored gpt/claude/gemini and removed syntax error")

if __name__ == "__main__":
    main()
