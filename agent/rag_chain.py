from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from .llm_loader import load_llm
from .config import DB_DIR, EMBED_MODEL

def get_rag_chain():
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=DB_DIR, embedding_function=embedding)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    llm = load_llm()
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")
