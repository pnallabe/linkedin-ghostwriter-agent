import os
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from .config import DATA_DIR, DB_DIR, EMBED_MODEL

def build_vectorstore():
    docs = []
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    for file in os.listdir(DATA_DIR):
        loader = TextLoader(os.path.join(DATA_DIR, file))
        docs.extend(splitter.split_documents(loader.load()))
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(docs, embedding, persist_directory=DB_DIR)
    vectordb.persist()