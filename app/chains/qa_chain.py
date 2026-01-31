from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.vectorstore.faiss_store import load_faiss_index
from app.llms.gemini import get_gemini_llm


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_qa_chain():
    db = load_faiss_index()
    retriever = db.as_retriever(search_kwargs={"k": 4})
    llm = get_gemini_llm()

    prompt = ChatPromptTemplate.from_template(
        """
You are a professional company assistant.

Use ONLY the context below to answer the question.
If the answer is not in the context, say:
"I don’t have that information."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain