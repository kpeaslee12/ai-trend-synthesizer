# AI Trend Synthesizer CLI Tool (Enhanced)
# Gathers live headlines from DuckDuckGo and optionally from NewsAPI

import argparse
import requests
from bs4 import BeautifulSoup
import os

# Optional: Replace with your NewsAPI key if available
NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Or replace with your key directly

PREDEFINED_SUMMARIES = {
    "AutoGPT": {
        "summary": "AutoGPT is an emerging autonomous agent framework built on top of GPT models. It attempts to complete complex tasks by chaining prompts and using tools like web browsing and file access.",
        "use_cases": ["Customer service automation", "Research agents", "Task delegation in productivity workflows"],
        "risks": ["Inaccurate outputs", "Overreliance on automation", "Security concerns"]
    },
    "Claude": {
        "summary": "Claude is a conversational AI developed by Anthropic with a focus on safety, constitutional AI, and more controllable outputs. It’s often compared to ChatGPT and excels in long conversations.",
        "use_cases": ["Legal summarization", "Long-form customer support", "Safe enterprise chatbots"],
        "risks": ["Less open-source access", "Potential for subtle bias", "Requires thoughtful prompting"]
    }
}

def get_duckduckgo_headlines(query):
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("a", class_="result__a")
    headlines = [r.get_text() for r in results[:5]]
    return headlines

def get_newsapi_headlines(query):
    if not NEWS_API_KEY:
        return []
    url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&apiKey={NEWS_API_KEY}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        return [article['title'] for article in data.get('articles', [])]
    return []

def synthesize_trend(topic):
    topic_clean = topic.strip()
    print("\n=== AI Trend Summary ===")
    print(f"\nTopic: {topic_clean}")

    # Headlines (live search)
    print("\nTop Headlines (DuckDuckGo):")
    duckduck_headlines = get_duckduckgo_headlines(topic_clean)
    for h in duckduck_headlines:
        print(f"- {h}")

    if NEWS_API_KEY:
        print("\nTop Headlines (NewsAPI):")
        newsapi_headlines = get_newsapi_headlines(topic_clean)
        for h in newsapi_headlines:
            print(f"- {h}")

    # Predefined summary if available
    topic_data = PREDEFINED_SUMMARIES.get(topic_clean)
    if topic_data:
        print("\nSummary:")
        print(topic_data['summary'])

        print("\nKey Use Cases:")
        for u in topic_data['use_cases']:
            print(f"- {u}")

        print("\nRisks / Considerations:")
        for r in topic_data['risks']:
            print(f"- {r}")
    else:
        print("\nNo predefined summary available.")

if __name__ == "__main__":
    import sys
    if "get_ipython" in globals():
        synthesize_trend("AutoGPT")
    else:
        parser = argparse.ArgumentParser(description="AI Trend Synthesizer CLI Tool")
        parser.add_argument("topic", type=str, help="The AI topic to summarize (e.g., AutoGPT, Claude)")
        args, unknown = parser.parse_known_args()
        synthesize_trend(args.topic)

