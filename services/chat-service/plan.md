# PLAN.md

## 1. Overview
- **Project/feature name:** Chat Service (Microservice)
- **Problem statement:** Generative text AI requests are distinct from document ingestion; they need independent conversation context tracking, fast LLM streaming responses, and interaction logic.
- **Goal:** Manage chat histories, assemble prompts, trigger internal vector search over Document Service API, invoke an LLM for conversational responses with citation tracing, and deliver tokens back to the UI.
- **Non-goals:** Executing text chunking, document file storage management.
- **Success criteria:** Accurately routes text user questions > pgvector similarity search > prompt packaging > sequential text streaming back to frontend.

## 2. Requirements
### Functional Requirements
- FR-006: Create conversations linked to multi-document contexts (`POST /api/v1/conversations`).
- FR-007: Accept natural language inputs inside conversations (`POST /api/v1/conversations/{id}/messages`).
- FR-008: Retrieve relevant document subset context from Document Service.
- FR-009: Stream grounded LLM sequences to frontend via SSE (Server-Sent Events) including chunk ID references.
- FR-010: Retain historical message tracking within conversation contexts.

### User Stories & Complete Lifecycle Scenarios
- US-001 (Actor): As an authenticated user, I want to create a chat specific to a selected list of PDFs, so it remembers my ongoing discussion.
- US-002 (Actor): As an authenticated user, I want to stream text back incrementally so I don't suffer 20s blocks.
- US-003 (Actor): As the system, I want to retrieve document metadata and append citations securely ensuring the user does not request chunks outside their tenant permissions.

### Non-Functional Requirements
- **Performance:** Time-to-first-token < 1-2s. 
- **Scalability:** Stateless API containers running Asyncio loops matching IO requirements of network-bound LLM inferences.
- **Security:** Conversation access verification.
- **Observability:** Metric on generic LLM latency.

## 3. Scope
### In Scope
- FastAPI endpoints for conversations.
- Async SSE output stream.
- LLM interaction adapter.

### Out of Scope
- Local physical LLM running (outsourced to API/Ollama).

## 4. User / System Flows
- Flow: Ask Question > Auth Verify > Conversation State Loaded > LLM Prompt Array Config > Vector Search Query sent over REST > RAG Inject > LLM Async Generator > Server-Sent Events response to Client.

## 5. Architecture
- **Components:** FastAPI server (port 8002). PostgreSQL DB (conversations mapping).
- **Services:** Query Generator -> Internal Client -> Prompt Contextualizer -> LLM Provider Adapter.

### Project Directory Structure
- `services/chat-service/`
  - `app/`
    - `main.py`
    - `config.py`
    - `api/` (conversations.py, messages.py)
    - `models/` (conversation.py, message.py)
    - `schemas/`
    - `rag/` (query.py, retriever.py, context.py)
    - `llm/` (base.py, ollama.py)
    - `prompts/` (document_qa.py)
    - `clients/` (document_service.py)
    - `db/`
  - `tests/`
  - `requirements.txt`
  - `Dockerfile`

### Frontend Plan
N/A

## 6. Technology Decisions
- **Language:** Python 3 async.
- **Framework:** FastAPI / `sse-starlette`.
- **Database:** PostgreSQL.
- **Providers:** Langchain or direct `httpx` parsing to `ollama` natively given lazy requirement overrides.

## 7. API / Interface Contract
**Endpoints:**
- `POST /api/v1/conversations` (Title + doc IDs list)
- `GET /api/v1/conversations`
- `GET /api/v1/conversations/{id}`
- `DELETE /api/v1/conversations/{id}`
- `POST /api/v1/conversations/{id}/messages` (Ask question -> returns SSE)
- `GET /api/v1/conversations/{id}/messages`

## 8. Data Model
- **Entities:**
  - `conversations`: (id, owner_id, title, created_at, updated_at)
  - `conversation_documents`: (conversation_id, document_id)
  - `messages`: (id, conversation_id, role, content, created_at)
  - `message_sources`: (message_id, chunk_id, source_order)
- **JSON Constraint:** NO JSON/JSONB. Strictly typed relations tracking sources to message components.

## 9. Security
- System prompt stripping mechanism to intercept prompt injection attempts.
- HTTP internal requests validating tenant isolation across microservice boundaries.

## 10. Scalability
- Async generator streaming optimizes network buffers per thread.

## 11. Performance
- Minimize token processing by summarization logic inside context thresholds.

## 12. Error Handling & Resilience
- Timeouts to Document Service requests triggering 503 fallback messages.
- Disconnections catch graceful generator closures.

## 13. Observability
- SSE disconnect events tracked to gauge user bail rates during slow inferences.

## 14. Testing Strategy (Backend, Frontend, Contract, User Stories)
### Backend
#### Unit Tests
- Memory context injection logic (Prompt structures array limits).
#### Consumer-Driven Contract Tests
- `httpx` test asserting strict adherence to Document Service `POST /internal/retrieval/search` payload rules.

## 15. Test Cases & User Story Verification Matrix
| ID | Scenario | Expected Result | Type | Layer |
|----|----------|-----------------|------|-------|
| TC-006 | Start conversation securely | 200 payload with conversation UUID | Unit | Backend |
| TC-007 | Send question invoking SSE | Response format matches text/event-stream | API | Backend |
| TC-008 | Contract: Interal DS Search | Sends properly serialized request downstream | Contract | Backend |

## 16. Edge Cases
- Client closes SSE channel mid-generation. Response: Thread should cancel LLM generation safely to save tokens.

## 17. Deployment
- Docker container `services/chat-service/Dockerfile`.
- Env via `DOCUMENT_SERVICE_URL`, `CHAT_SERVICE_URL`.

## 18. CI/CD
- Pytest and Flake8 running locally.

## 19. Compatibility
- N/A

## 20. Migration / Upgrade Plan
- Schema changes via Alembic.

## 21. Risks & Trade-offs
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Memory inflation via chat history. | Medium | High | Prune passed history list on context boundary limits default. |

## 22. Open Questions
- None.

## 23. Implementation Plan
### Phase 1: Conversation CRUD and History State
### Phase 2: RAG Contextualization & Document Service Connectors
### Phase 3: LLM Integration and SSE Streaming

## 24. Definition of Done
- [ ] Requirements implemented
- [ ] Tests passing
- [ ] Security reviewed
- [ ] Observability added
- [ ] Documentation updated
- [ ] Deployment verified

## 25. Post-Implementation Verification
- Integration loop checking if a mock document ID receives an SSE sequence ending correctly.

## 26. Existing Codebase Analysis
N/A

## 27. Implementation Constraints
- Follow existing architecture standards of microservices defined.
- Native async requests required.

## 28. Acceptance Criteria
AC-002:
Given a list of verified Document IDs,
when sending text to the conversations message endpoint,
then the user receives token-by-token mapped SSE text answers based on specific text chunk context retrieved via downstream requests.
