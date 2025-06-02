from langchain.llms import LlamaCpp
from .config import LLM_PATH, MODEL_CTX

def load_llm():
    return LlamaCpp(
        model_path=LLM_PATH,
        n_ctx=MODEL_CTX,
        temperature=0.7,
        top_p=0.9,
        max_tokens=512,  # ⬅️ adjust to 512–1024 based on model support
        verbose=False
    )