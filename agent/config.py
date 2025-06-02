# Path configurations and constants

import os

DATA_DIR = "rag_agent_data"
DB_DIR = "rag_db"
LLM_PATH = "../../llm_models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
MODEL_CTX = 2048
EMBED_MODEL = "all-MiniLM-L6-v2"
TOPICS = [
    "credit risk",
    "Macroeconomic insights",
    "Fintech trends",
    "Agentic AI"
]
GOOGLE_NEWS_URL = "https://news.google.com/rss/search?q=credit+risk+OR+macroeconomics+OR+fintech&hl=en-US&gl=US&ceid=US:en"