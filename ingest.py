from langchain_community.document_loaders import TextLoader, PyPDFLoader
from app.vectorstore.faiss_store import create_faiss_index

loader = PyPDFLoader("data/GoWafir_Official_Corporate_Profile.pdf")
documents = loader.load()

create_faiss_index(documents)
print("FAISS index created successfully")

