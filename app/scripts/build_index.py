from app.loaders.pdf_loader import load_documents
from app.vectorstore.faiss_store import create_faiss_index

if __name__ == "__main__":
    # Change this to your actual PDF or TXT file
    file_path = "data/GoWafir_Official_Corporate_Profile.pdf"

    print("Loading documents...")
    docs = load_documents(file_path)

    print("Creating FAISS index...")
    create_faiss_index(docs)

    print("FAISS index created successfully ✅")