import os
from dotenv import load_dotenv

load_dotenv()
# # load_dotenv(dotenv_path=".env")
# load_dotenv(find_dotenv())

# =======================
# API KEYS
# =======================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# =======================
# MODEL CONFIG
# =======================
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# =======================
# VECTOR STORE
# =======================
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "faiss_index")

# =======================
# CHUNKING
# =======================
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 2000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))
