# Document Intelligence & Chat Platform

A microservices-based Retrieval-Augmented Generation (RAG) platform. Upload PDFs, Word documents, or Markdown files, index them efficiently via OpenRouter embeddings natively into PostgreSQL, and chat with them using Google Gemma-4.

## Architecture

- **Frontend (Vite):** React + Vite SPA using Tailwind and Zustand. Supports SSE streaming and polling.
- **Document Service (Port 8013):** FastAPI backend. Ingests docs, extracts text via PyMuPDF, chunks via Langchain, and commits vectors to `pgvector`.
- **Chat Service (Port 8014):** FastAPI backend. Orchestrates conversation history routing and streams LLM generative tokens natively via OpenRouter.
- **PostgreSQL (`pgvector` on Port 5433):** Backing storage isolating `documents_chat` and `chat_db`.

## Setup & Running

### 1. Database
Start the containerized Postgres database initialized with `pgvector` mapping to port 5433:
```bash
docker compose up -d
```

### 2. Services Configuration
Generate your keys from [OpenRouter](https://openrouter.ai/) for `nvidia/nemotron` and `google/gemma-4`. Drop them into local configurations:
```bash
cp services/document-service/.env.sample services/document-service/.env
cp services/chat-service/.env.sample services/chat-service/.env
# Edit the variables inside these two files to mount your keys.
```

### 3. Start Backend Services
Activate each environment and boot the servers in separate terminals:
```bash
# Document Service
cd services/document-service
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --port 8013
```
```bash
# Chat Service
cd services/chat-service
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --port 8014
```

### 4. Start Frontend
```bash
cd frontend
cp .env.development .env
npm install
npm run dev
```

Browse to your local host URL to upload and chat!
