from utils.groq_client import call_groq_llm
from utils.helpers import call_llm, save_text
import json
import re


def extract_json_block(text: str):
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    return {"sentiment": None, "topics": []}


def analyze_sentiment_topics(chunks, debug_save=True):
    """
    Analyze sentiment and topics for a list of text chunks.
    Returns a list of dictionaries.
    """
    client = call_groq_llm()
    analysis_results = []

    for chunk in chunks:
        prompt = f"""
Analyze the following text for sentiment and main topics:

Text:
"{chunk}"

Output format:
{{
  "sentiment": "Positive | Neutral | Negative",
  "topics": ["topic1", "topic2", ...]
}}
"""
        result = call_llm(client, prompt)

        try:
            structured = extract_json_block(result)
        except json.JSONDecodeError:
            structured = {"sentiment": None, "topics": []}

        analysis_results.append(structured)

    if debug_save:
        save_text(
            "./outputs/5_analysis/output.json", json.dumps(analysis_results, indent=2)
        )

    return analysis_results
