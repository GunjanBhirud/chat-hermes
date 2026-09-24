# PLAN.md

## 1. Overview
- **Project/feature name:** Document Service (Microservice)
- **Problem statement:** Large document processing (parsing, chunking, embedding) is resource-intensive and blocks core user flows if tied directly to user-facing API servers.
- **Goal:** Provide a resilient, isolated backend API dedicated to handling file uploads, validation, storage, asynchronous parsing for PDF/DOCX/Markdown, chunk vectorization via embeddings, and serving vector similarity search to internal consumers.
- **Non-goals:** LLM interaction, conversation tracking, UI rendering.
- **Success criteria:** Document lifecycle fully manages state correctly; Vector indexing successfully serves internal searches with <1s latency under normal load.

## 2. Requirements
### Functional Requirements
- FR-001: Accept multipart/form-data document uploads (PDF, DOCX, Markdown).
- FR-002: Track full document lifecycle across states (QUEUED, PROCESSING, FAILED, READY).
- FR-003: Perform asynchronous text extraction, chunking (overlap), and pgvector embedding storage.
- FR-004: Serve internal vector queries securely (`/internal/retrieval/search`).
- FR-005: Manage secure storage and deletion of physical files + vector associations on demand.

### User Stories & Complete Lifecycle Scenarios
- US-001 (Actor): As a front-end client, I want to upload a document so that it begins processing.
  - Scenario A (Happy Path): File is an allowed format. System accepts it, stores to disk, returns `QUEUED`.
  - Scenario B (Edge Path): File is blocked format (.exe). System rejects inline with HTTP 400.
- US-002 (Actor): As a chat service, I want to query vectors securely over a restricted subset of document IDs so that I retrieve only context my user is authorized for. 
  - Scenario A (Happy Path): Relevant context found in vector DB; results returned array.
  - Scenario B (Edge / Negative Path): Attempting to query non-existing chunks or unauthorized documents; returns empty array securely.
- US-003 (Actor): As a user, I want to delete a document so that my stored files and indexes are wiped.

### Non-Functional Requirements
- **Performance:** Sub-1-second vector matching (`top_k=5` under standard load).
- **Scalability:** Horizontal scaling via decoupled processing queues (Redis queue in future, background loops internally at MVP).
- **Availability:** API must recover synchronously for upload ingestion under heavy DB load.
- **Reliability:** Failed document processing isolates to the specific document ID without cascading.
- **Security:** Owner constraints strictly enforced down to vector level matching.
- **Observability:** `X-Request-ID` attached to all parsed logs.
- **Maintainability:** Modular architecture allowing pluggable embedding providers.

## 3. Scope
### In Scope
- FastAPI endpoints for public document management, internal Retrieval API.
- Parsers: PyMuPDF, markdown, docx.
- pgvector interactions.

### Out of Scope
- Session management (handled at gateway level & Chat).

## 4. User / System Flows
- Main flow: Upload -> ID returned -> Background processing -> Status polling -> Marked Ready.
- Error flow: Corrupt PDF -> Parse fails -> State marked FAILED -> Client prompts for retry/delete.
- State transitions: IDLE -> UPLOADED -> QUEUED -> PROCESSING -> (READY / FAILED) -> DELETING -> DELETED.

## 5. Architecture
- **Components:** FastAPI server (port 8001), PostgreSQL (`pgvector`), local storage (`/data/documents`), optional Redis worker.
- **Services:** Document extraction layer -> Text processing pipeline -> Embedding generator. 
- **Dependencies:** `PyMuPDF`, `python-docx`, `markdown`, `langchain-text-splitters` (or raw custom), `psycopg2`/`asyncpg`.
- **Data flow:** Binary -> disk -> Text Chunks -> pgvector. 
- **External integrations:** Embedding model provider via HTTP. 

### Project Directory Structure (required for every project)
- `services/document-service/`
  - `app/`
    - `main.py` (FastAPI entrypoint)
    - `config.py` (Environment handling)
    - `api/` (public and internal endpoints)
    - `models/` (SQLAlchemy/SQLModel classes)
    - `schemas/` (Pydantic I/O validations)
    - `parsers/` (pdf, docx, mkd raw parsers)
    - `ingestion/` (orchestration, splitting logic, chunkers)
    - `embeddings/` (provider adapters)
    - `retrieval/` (pgvector search execution)
    - `storage/` (local disk interface)
    - `workers/` (Asyncio task runners or RQ/Celery consumers)
    - `db/` (pg connection configuration)
  - `tests/`
  - `requirements.txt`
  - `Dockerfile`

### Frontend Plan (required whenever the project has a UI)
N/A - This is a backend-only microservice mapping.

## 6. Technology Decisions
- **Language:** Python 3 (Typing-driven for schemas).
- **Framework:** FastAPI (Async ecosystem matches LLM & IO scaling).
- **Database:** PostgreSQL with `pgvector` (Scalable standard embedding storage).
- **APIs:** REST JSON.

## 7. API / Interface Contract
**Public Endpoints:**
- `POST /api/v1/documents` -> `multipart/form-data` -> 202 `{document_id, status}`
- `GET /api/v1/documents` -> 200 list of documents
- `GET /api/v1/documents/{id}` -> 200 Document detail
- `DELETE /api/v1/documents/{id}` -> 204
- `POST /api/v1/documents/{id}/retry` -> 200 status shift
- `GET /api/v1/documents/{id}/status` -> polling endpoint

**Internal Contracts (Cross-Service):**
- `POST /internal/retrieval/search` -> `{document_ids, query_embedding, top_k}` -> `{"results": [...]}`
- `GET /internal/documents/{id}` -> returns full status bypassing standard client payload shapes.

**Errors:**
- Implement unified pattern `{"error": {"code": "...", "message": "..."}}`.

## 8. Data Model
- **Entities:**
  - `documents`: (id, owner_id [UUID], name, original_filename, mime_type, file_size, storage_key, status, error_code, error_message, page_count, chunk_count, embedding_model, created_at, processed_at)
  - `document_chunks`: (id, document_id, owner_id, chunk_index, content [TEXT], embedding [VECTOR], page_start, page_end, heading_path_text, source_metadata_text, created_at)
- **Constraints:** `owner_id` isolated queries. On-delete cascade for chunks.
- **JSON/JSONB constraint:** NO JSON/JSONB usage for the model. Fields requiring array storage like `heading_path` are text arrays or flattened formats. Metadata is structured tables if needed, or excluded. We have explicitly bypassed JSONB to follow constraints, utilizing `heading_path_text` (Stringified/path format).

## 9. Security
- API Authentication via validated JSON Web Token (JWT) in proxy layer, extracting `user_id` to pass to service. 
- Input validation utilizing Pydantic. 
- File security: Save with random UUID hashes as `storage_key`. Restrict extensions to defined list. Size limit (50MB) enforced before parsing. 
- Path traversal block via UUID naming conventions. 
- Content bounds: We assume content isn't executable payload, but is considered untrusted string data during rendering.

## 10. Scalability
- **Volume:** Minimal chunk threshold expected per query (`top_k` clamped at default scaling).
- **Job tracking:** A future transition from async background tasks to Redis queues is documented for when parallel file ingestion creates resource contention. 

## 11. Performance
- Storage IO buffers read streams.
- Postgres utilizes an HNSW index on the vector col.

## 12. Error Handling & Resilience
- Graceful degradation: A parse failure on file marks file `FAILED`. Doesn't crash node.
- Retry: Endpoint available to force queue processing again.

## 13. Observability
- Logging captures `document_id` processing intervals (time-to-parse).
- Internal search latency injected to telemetry.

## 14. Testing Strategy (Backend, Frontend, Contract, User Stories)
### Backend
#### Unit Tests
- Validations, parsing (mocked files), chunk splitting logic.
#### Integration Tests
- In-memory database storing pseudo-vectors and tracking retrieval thresholds.
#### Consumer-Driven Contract Tests
- `Chat Service` dependency mocks tests matching `/internal/retrieval/search` signature.
- Test `GET /internal/documents/{id}` endpoint behaves identically to what Chat expects.

## 15. Test Cases & User Story Verification Matrix
| ID | Scenario | Expected Result | Type | Layer |
|----|----------|-----------------|------|-------|
| TC-001 | Valid upload request | 200 with schema matching Document | Integration | Backend |
| TC-002 | Invalid file format uploaded | HTTP 400 error rejection | API | Backend |
| TC-003 | Parse failure catches gracefully | DB state shifts to `FAILED` | Unit | Backend |
| TC-004 | Internal vector search across tenant boundary | Attempt retrieves 0 records | Security | Backend |
| TC-005 | Contract validity of internal search | Returns correctly shaped results array | Contract | Backend |

## 16. Edge Cases
- Massive files (1000+ pages) clogging RAM (stream logic requirement).
- Encrypted PDFs bypassing PyMuPDF extraction (detect and fail fast).

## 17. Deployment
- Docker container `services/document-service/Dockerfile`.
- Env via `DOCUMENT_SERVICE_URL`, `DATABASE_URL`. SQLAlchemy Alembic utilized for migrations.

## 18. CI/CD
- Pytest and Flake8 running locally prior to merges.
- Migration verification via Alembic head alignment.

## 19. Compatibility
- Compatible with generic LLM dimensional arrays (config driven dimensions).

## 20. Migration / Upgrade Plan
- Schema changes driven completely via Alembic.

## 21. Risks & Trade-offs
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Memory spiking on large inputs | High | Medium | Implement chunked reading logic for large pdfs. |

## 22. Open Questions
- None.

## 23. Implementation Plan
### Phase 1: Database & File Storage Foundation
### Phase 2: Parsers & Ingestion Pipelines
### Phase 3: Vector Storage & Internal Retrieval

## 24. Definition of Done
- [ ] Requirements implemented
- [ ] Tests passing
- [ ] Security reviewed
- [ ] Performance validated
- [ ] Observability added
- [ ] Documentation updated
- [ ] CI passing
- [ ] Deployment verified

## 25. Post-Implementation Verification
- Smoke tests of uploading basic markdown and successfully generating embeddings.

## 26. Existing Codebase Analysis
### Relevant Files
Greenfield initialization.
### Existing Patterns
N/A.
### DO NOT Change
N/A
### Reuse
N/A

## 27. Implementation Constraints
- Follow existing project architecture.
- Do not add dependencies unless necessary.
- Do not duplicate existing services.

## 28. Acceptance Criteria
AC-001:
Given a valid user token and a PDF,
when sent to `POST /api/v1/documents`,
then the system accepts it, queues processing, and can accurately serve a search request based on the contents.
