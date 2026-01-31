from fastapi import FastAPI
from pydantic import BaseModel
from app.chains.qa_chain import get_qa_chain

app = FastAPI(
    title="Company AI Chatbot",
    version="1.0.0"
)

qa_chain = get_qa_chain()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: ChatRequest):
    answer = qa_chain.invoke(request.question)

    return {
        "answer": answer
    }