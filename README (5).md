# 🧠 AI Trend Synthesizer CLI Tool (Enhanced)

A lightweight command-line tool that summarizes AI topics like AutoGPT or Claude using **live headlines** from DuckDuckGo and optionally NewsAPI. It also includes predefined summaries, use cases, and risks to simulate what an analyst might present to a stakeholder.

## 🔧 Features

- ✅ Real-time headline extraction (DuckDuckGo)
- 📰 Optional integration with [NewsAPI.org](https://newsapi.org/)
- 📚 Built-in summaries for AutoGPT and Claude
- 🧠 Insight-ready formatting for content and strategy teams

## 🚀 How to Run

**Command line:**
```bash
python ai_trend_synthesizer.py Claude
```

**In a Jupyter Notebook:**
```python
from ai_trend_synthesizer import synthesize_trend
synthesize_trend("Claude")
```

## 🌐 Environment Variables

To use NewsAPI (optional), set an API key in your environment:
```bash
export NEWS_API_KEY=your_api_key_here
```

## 📦 Requirements

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## 🧪 Sample Output

```
=== AI Trend Summary ===

Topic: Claude

Top Headlines (DuckDuckGo):
- Claude outperforms GPT in multi-turn conversations
- Claude used in enterprise chatbot demos...

Summary:
Claude is a conversational AI developed by Anthropic...

Key Use Cases:
- Legal summarization
- Customer support

Risks / Considerations:
- Requires structured prompting
```
