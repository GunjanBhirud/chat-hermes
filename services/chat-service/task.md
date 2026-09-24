# TASK.md

Progress tracker for Chat Service, derived from plan.md Section 23.
Legend: [ ] not started · [x] done

## Phase 1: Conversation CRUD and History State
- [x] Initialize Python FastAPI securely inside `services/chat-service/`.
- [x] Configure `requirements.txt` (FastAPI, pydantic, sqlalchemy, asyncpg, sse-starlette, httpx, alembic).
- [x] Scaffold Configuration fetching `DOCUMENT_SERVICE_URL`.
- [x] Create SQLAlchemy `Conversation` and `Message` relationship schema files.
- [x] Build Alembic migration.
- [x] Implement `POST /api/v1/conversations` inserting tracking metadata (closes FR-006, TC-006).
- [x] Implement CRUD tracking for GET and DELETE variants of discussions.

## Phase 2: RAG Contextualization & Document Service Connectors
- [x] Create `clients/document_service.py` with `httpx` helper to securely POST `query_embedding` arrays formatting correctly.
- [x] Develop `llm/base.py` generic embed adapter logic extracting local query text to arrays mapping prior to downstream push.
- [x] Build Prompt assembler wrapping contextual history into static context (closes FR-008). 
- [x] Mock downstream server connectivity logic to validate schema boundaries matching contract (closes TC-008).

## Phase 3: LLM Integration and SSE Streaming
- [x] Hook Ollama stream endpoints generating yield arrays inside `llm/ollama.py`.
- [x] Map SSE token outputs to `Server-Sent Events` mapping classes natively via Yield strings.
- [x] Create `POST /api/v1/conversations/{id}/messages` initiating chain logic routing to front end (closes FR-007, FR-009, TC-007).
- [x] Insert Message tracing `message_sources` DB items concurrently matching chunks to response output loops appropriately (closes FR-010).
