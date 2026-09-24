# Chat Service

Tracks multi-document conversation scopes and handles token streaming using SSE and pgvector search queries routed via the internal Document Service API.

### Setup
1. Define Postgres instance.
2. Ensure Document Service is running on `:8001`.
3. Set `LLM_PROVIDER` and `LLM_MODEL`.
4. Run `uvicorn app.main:app --port 8002`.

### APIs
Public: `/api/v1/conversations/{id}/messages`

### Architecture
RAG pipeline integrates vector fetching through REST connectors before compiling templated constraints into provider generators. 
