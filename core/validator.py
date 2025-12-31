def validator_pipeline(raw, clean, chunks, summary, analysis):
    print("Step 1: Extraction...")
    if len(raw) < 100:
        raise ValueError("Extraction failed: Text too short")
    print("Step 1: Extraction passed!")

    print("Step 2: Cleaning...")
    if len(raw) == len(clean):
        raise ValueError("Cleaning failed: Cleaning had no effect")
    print("Step 2: Cleaning passed!")

    print("Step 2: Chunking...")
    if any(len(c) > 25000 for c in chunks):
        raise ValueError("Chunking failed: Chunk too large")
    print("Step 2: Chunking passed!")

    print("Step 4: Summary...")
    if not summary or len(summary.strip()) < 20:
        raise ValueError("Summary failed: Summary too short")
    print("Step 4: Summary passed!")

    print("Step 5: Sentiment/Topic...")
    if not analysis:
        raise ValueError("Analysis failed: empty list")

    for i, item in enumerate(analysis, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Analysis item {i} is not a dict")
        if "sentiment" not in item or "topics" not in item:
            raise ValueError(f"Analysis item {i} missing 'sentiment' or 'topics'")

    print("Step 5: Analysis passed!")

    print("✓ All checks passed!")
