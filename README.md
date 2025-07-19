# LLM-CustomerAssistant

**LLM-CustomerAssistant** is an intelligent AI chatbot system for customer support and knowledge delivery. Built with OpenAI/LLaMA models, FastAPI, LangChain, and a RAG (Retrieval-Augmented Generation) pipeline, it enables natural, context-aware conversations with real-time access to internal knowledge bases.

---

## 🚀 Features

- 💬 Multi-turn conversational AI with memory
- 📚 RAG-based question answering from PDFs, URLs, and FAQs
- 🔍 Fast and accurate retrieval using vector databases ( Chroma)
- 📅 Meeting booking integration 
- 🌐 REST API backend with FastAPI
- 🧠 LLM integration (LLaMA via HuggingFace)

---

## 🧱 Tech Stack

- **Backend:** FastAPI
- **LLM Orchestration:** LangChain
- **Vector Store:**  Chroma 
- **Embedding Models:** HuggingFace Transformers
- **Deployment:** Docker, uvicorn, Gunicorn

---

## 📦 Setup Instructions

```bash
git clone https://github.com/your-username/LLM-CustomerAssistant.git
cd LLM-CustomerAssistant
pip install -r requirements.txt
uvicorn app.main:app --reload
