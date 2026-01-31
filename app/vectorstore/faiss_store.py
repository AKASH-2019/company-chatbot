import os
from langchain_community.vectorstores import FAISS
# from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import CHUNK_SIZE, CHUNK_OVERLAP, FAISS_INDEX_PATH
from app.embeddings.embedding_engine import get_embedding_engine

def create_faiss_index(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    texts = text_splitter.split_documents(documents)
    embeddings = get_embedding_engine()

    db = FAISS.from_documents(texts, embeddings)
    db.save_local(FAISS_INDEX_PATH)
    return db


def load_faiss_index():
    embeddings = get_embedding_engine()
    if not os.path.exists(FAISS_INDEX_PATH):
        raise ValueError("FAISS index not found. Create it first.")

    return FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )