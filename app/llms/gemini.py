from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GEMINI_API_KEY, GEMINI_MODEL

def get_gemini_llm():
    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        temperature=0,
        api_key=GEMINI_API_KEY,
        max_retries=2,
    )