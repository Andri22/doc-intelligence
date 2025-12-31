doc-intelligence-app/
│
├── app.py                     
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example               # ADD THIS (for API keys)
│
├── core/                       
│   ├── __init__.py
│   ├── ingest.py               
│   ├── cleaner.py              
│   ├── chunker.py              
│   ├── summarizer.py           
│   ├── analyzer.py
│   └── validator.py            # ADD THIS (checkpoint validation)
│
├── prompts/                    
│   ├── executive.txt
│   ├── bullet.txt
│   ├── detailed.txt
│   └── sentiment_topic.txt
│
├── utils/
│   ├── __init__.py
│   ├── groq_client.py          
│   └── helpers.py              
│
├── assets/                     
│
└── outputs/                    # For checkpoint validation
    ├── 1_extracted/            # ADD: raw extracted text
    ├── 2_cleaned/              # ADD: cleaned text
    ├── 3_chunks/               # ADD: text chunks
    ├── 4_summaries/            # ADD: summaries
    └── 5_analysis/             # ADD: final results