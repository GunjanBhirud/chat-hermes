# TASK.md

Progress tracker for Document Service, derived from plan.md Section 23.
Legend: [ ] not started · [x] done

## Phase 1: Database & File Storage Foundation
- [x] Initialize Python FastAPI project layout securely inside `services/document-service/`.
- [x] Incorporate dependencies in `requirements.txt` (FastAPI, pydantic, sqlalchemy, psycopg2/asyncpg, pgvector).
- [x] Initialize SQLAlchemy models for `documents` and `document_chunks`.
- [x] Generate Alembic migrations for base tables and `pgvector` extension setup.
- [x] Implement `storage/file_storage.py` layer to handle secure randomized file persistence locally.
- [x] Build `POST /api/v1/documents` endpoint schema validation.
- [x] Build `POST /api/v1/documents` upload pipeline saving to disk and appending `QUEUED` DB state (closes FR-001).
- [x] Add unit tests for upload rejections (closes TC-002).

## Phase 2: Parsers & Ingestion Pipelines
- [x] Construct background process ingestion trigger pipeline marking state `PROCESSING`.
- [x] Create PyMuPDF parser base logic retaining metadata context (`parsers/pdf.py`).
- [x] Create Document/Markdown/DocX parsed text extractors (`parsers/docx.py`, `parsers/markdown.py`).
- [x] Implement Langchain recursive chunking splitting strategies (`ingestion/chunker.py`).
- [x] Wrap Embedding Provider interface class (`embeddings/provider.py`).
- [x] Unit test parser failures catching reliably to flag document status `FAILED` (closes TC-003).

## Phase 3: Vector Storage & Internal Retrieval
- [x] Embed chunk pipeline sending extracted components iteratively to DB backend (`document_chunks` insertion) with specific embeddings.
- [x] Ensure background process marks document `READY`.
- [x] Create endpoint `GET /api/v1/documents` and `GET /api/v1/documents/{id}` mapping metadata without heavy payload.
- [x] Establish `GET /internal/documents/{id}` for Chat Service usage (closes FR-004).
- [x] Set up `POST /internal/retrieval/search` querying pgvector utilizing HNSW metrics filtered safely via tenant IDs (closes TC-004).
- [x] Construct HTTP testing mocking logic against Contract tests (closes TC-005).
- [x] Construct `DELETE /api/v1/documents/{id}` mapping cascade deletions targeting file removals (closes FR-005).
