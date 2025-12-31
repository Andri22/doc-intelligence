from core.ingest import extract_text
from core.cleaner import clean_text
from core.validator import validator_pipeline
from core.chunker import chunk_text
from core.summarizer import summary_text
from core.analyzer import analyze_sentiment_topics

data = "data.pdf"


def main():
    raw = extract_text(data)
    clean = clean_text(raw)
    chunk = chunk_text(clean)
    summa = summary_text("bullet", chunk)
    analyz = analyze_sentiment_topics(chunk)
    validator_pipeline(
        raw=raw, clean=clean, chunks=chunk, summary=summa, analysis=analyz
    )


if __name__ == "__main__":
    main()
