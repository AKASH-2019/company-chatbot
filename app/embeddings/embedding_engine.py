from langchain_community.embeddings import OllamaEmbeddings
from app.config import OLLAMA_EMBED_MODEL, OLLAMA_BASE_URL


def get_embedding_engine():
    return OllamaEmbeddings(
        model=OLLAMA_EMBED_MODEL,
        base_url=OLLAMA_BASE_URL
    )


# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from app.config import GEMINI_API_KEY, OLLAMA_EMBED_MODEL


# def get_embedding_engine():
#     """
#     Returns the embedding engine used by the vector store.
#     """
#     return GoogleGenerativeAIEmbeddings(
#         model="models/embedding-001",
#         google_api_key=GEMINI_API_KEY
#     )
