# company-chatbot
# 🤖 Company Chatbot – AI Agent (Full-Stack Implementation)

> A document-aware conversational AI system built using **LangChain, FastAPI, FAISS, Gemini, and Ollama**, following **AI Agent full-stack principles**.

---

## 🧠 AI Agent Architecture (Concept Applied)

User Query
↓
API Layer (FastAPI)
↓
Retriever Agent (FAISS)
↓
Embedding Engine
(Gemini → Ollama Fallback)
↓
LLM Reasoning (Gemini)
↓
Final Answer


✔ Agent decides **how to retrieve context**  
✔ Agent selects **embedding provider dynamically**  
✔ Agent produces **grounded, document-based responses**

---

## ⚙️ Tech Stack

- **Backend**: FastAPI (ASGI)
- **Agent Framework**: LangChain
- **LLM**: Gemini (Google Generative AI)
- **Embeddings**:
  - Primary: Gemini Embeddings
  - Fallback: Ollama (local)
- **Vector Store**: FAISS
- **Document Loader**: PDF Loader
- **Containerization**: Docker & Docker Compose

---

## 📂 Project Structure

company-chatbot/
├── app/
│ ├── main.py # FastAPI entry point
│ ├── config.py # Environment & model config
│ ├── chains/ # QA & agent chains
│ ├── embeddings/ # Embedding engines
│ └── vectorstore/ # FAISS store logic
├── ingest.py # Document ingestion
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── README.md


---

## 📄 Document Processing Pipeline

PDF Files
↓
Text Loader
↓
Recursive Text Splitter
↓
Embedding Generation
↓
FAISS Index Storage


✔ Optimized chunking  
✔ Semantic search ready  
✔ Persistent vector index

---

## 🔑 Environment Configuration

Create a .env file:

env
GEMINI_API_KEY=your_gemini_api_key 

## 📥 Ingest Company Documents

This step is required **before running the chatbot** or **whenever company documents are updated**.

### 📄 What Happens in This Step

PDF Documents
↓
Text Extraction
↓
Chunking (Recursive Splitter)
↓
Embedding Generation
↓
FAISS Vector Index


✔ Splits documents into semantic chunks  
✔ Generates embeddings (Gemini / Ollama)  
✔ Stores vectors locally using FAISS  

---

### ▶️ Command to Run Ingestion

```bash
python ingest.py

## 📁 Output Generated

After successful ingestion, the following artifacts are created:

### 🧠 Vector Store

- **FAISS Index Location**


- Contains:
- Embedded document chunks
- Metadata for semantic retrieval
- Optimized similarity search index

---

## 🔁 When to Re-Run Ingestion

Re-run the ingestion process **only when necessary**:

- ✅ New company documents are added
- ✅ Existing PDFs are modified or replaced
- ✅ Embedding model is changed (Gemini ↔ Ollama)
- ❌ Not required for normal API restarts

---

## 🚀 Running the API Server

Start the FastAPI application:

```bash
uvicorn app.api.main:app --host 0.0.0.0 --port 8000


## 🐳 Running with Docker

### 🔨 Build the Image

Build the Docker image for the chatbot API:

```bash
docker build -t company-chatbot .

docker run --env-file .env -p 8000:8000 company-chatbot



