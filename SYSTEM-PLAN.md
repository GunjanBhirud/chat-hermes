# SYSTEM-PLAN.md

## 1. System Overview
- **What the overall system does:** A document-grounded question-answering platform where users upload PDF, DOCX, or Markdown documents and ask natural-language questions about the document content. Answers stream in sequentially and are strictly grounded in retrieved text passages with specific source citations.
- **Why it's split into services:** To isolate heavy backend data processing tasks (document ingestion, text extraction, intensive chunking, and embedding creation) within the **Document Service**, separate from the inference constraints, prompt management, and conversational iteration of the **Chat Service**. This prevents expensive file parsing operations from blocking concurrent chat iterations.

## 2. Service Inventory
| Service Name | Owner/Developer | Purpose | Repo/Folder |
|---|---|---|---|
| Document Service | To be determined | Ingestion, parsing, chunking, embedding, indexing, document lifecycle and file storage access. | `services/document-service/` |
| Chat Service | To be determined | Conversations, messages, prompt construction, retrieval integration, LLM streaming and text generation. | `services/chat-service/` |
| Frontend | To be determined | SPA Interface (React/TS), document UI, drag & drop uploads, chat visualization and streaming rendering. | `frontend/` |

## 3. Service Boundaries & Data Ownership
- **Document Service:** Owns the `documents` metadata table, the `document_chunks` table (pgvector), and binary file storage parameters. It must NOT manage chat histories.
- **Chat Service:** Owns the `conversations`, `messages`, and `message_sources` tables. Interacts directly with the generic `LLM Provider`. It must NOT manage document uploads or pgvector insertions.
- **Boundary rule:** The two backend services should share a PostgreSQL instance (for the MVP cost considerations) but use completely separate database tables. Vector retrieval is performed by calling an internal API of the Document Service, not by cross-querying `document_chunks`.

## 4. Communication Patterns
- **Gateway -> Internal Services:** External requests route through a proxy API gateway (`/api/documents/*` to Document Service, `/api/chat/*` to Chat Service).
- **Service to Service (Synchronous):** Chat Service queries the Document Service synchronously via REST APIs to pull document metadata and execute pgvector searches during generation loops.
- **Frontend Streaming:** Chat Service to Frontend employs Server-Sent Events (SSE) for token-by-token streaming of assistant responses.
- **Asynchronous Work:** Queue-based internal operations (e.g. `QUEUED` -> `PROCESSING`) handled within Document Service using background workers.

## 5. Inter-Service API Contracts
| Provider Service | Consumer Service(s) | Contract (endpoint/event) | Schema/Payload | Versioning Policy |
|---|---|---|---|---|
| Document Service | Chat Service | `POST /internal/retrieval/search` | Req: `document_ids`, `query_embedding`, `top_k`. Res: `results` | Internal Versioning |
| Document Service | Chat Service | `GET /internal/documents/{document_id}` | Req: ID. Res: `owner_id`, `status`, metadata | Internal Versioning |

## 6. Authentication & Authorization Between Services
- **External Client:** JWT-based authentications generating a stateless `user_id`.
- **Internal Gateway:** The system propagates the `user_id` inside API headers securely across service calls. No public route directly hits internal processing endpoints.
- **Internal Auth:** Both `Document Service` and `Chat Service` treat any request to `*/internal/*` as secured via internal service tokens or infrastructure firewall boundaries. 
- **Authorization Enforcement:** The Document Service validates `owner_id == user_id` before querying embeddings on behalf of the Chat Service.

## 7. Shared Standards
- **Error Responses:** All public errors implement a standard JSON wrapper: `{"error": {"code": "...", "message": "..."}}`. Non-public stack traces are suppressed.
- **Tracing / Logging:** A unified standard request attribute (`X-Request-ID`) guarantees correlation logic propagated down from the Frontend through Chat Service and into Document Service.
- **Formatting:** Absolute use of `/api/v1/` routes.

## 8. Deployment Topology
- **Containers:** Docker Compose configurations linking separate Dockerfiles. 
- **Datastores:** Single PostgreSQL instance with `pgvector` enabled mapped to both backing FastAPIs. Local `redis` as an optional add if background queues saturate. 
- **LLM Topology:** Separate `ollama` or generic container configured strictly.
- **Discovery:** Host names within the docker-compose network (e.g., `http://document-service:8001`, `http://chat-service:8002`).

## 9. Failure & Degradation Across Services
- **Service Isolation:** If the LLM provider crashes, the `Document Service` independently ingests files successfully up to indexing.
- **Graceful Fault Lines:** A failure in `Document Service` during search cancels the `Chat Service` streaming block with an internal failure, while older context chunks theoretically resolve error screens promptly.
- **Calls/Timeouts:** Internal HTTP invocations use a configurable timeout policy to avoid blocking concurrency logic.

## 10. Contract Change Process
- Any modification to the structure of `/internal/retrieval/search` or JSON source schemas must be documented back in `SYSTEM-PLAN.md` and approved by humanity.
- Upgrading `SYSTEM-PLAN.md` necessitates simultaneous integration into the `Consumer-Driven Contract Tests` present in the respective service's testing harness.

## 11. Open Questions
- None. Required features rigorously stipulated in business specifications.
