# Document Service

Ingests, chunks, embeds, and stores documents. Provides vector retrieval internal API.

### Environment & Setup
1. Define Postgres with pgvector in `docker-compose.yml` or externally.
2. `pip install -r requirements.txt`.
3. Set `DATABASE_URL` in `.env`.
4. Run `uvicorn app.main:app`.

### APIs
Public: `/api/v1/documents`
Internal: `/internal/retrieval/search`

### Phase Log
Phase 1: DB & Uploads - Unit tested and functioning.
Phase 2: Extraction logic - PyMuPDF & Markdown splitters enabled.
Phase 3: pgvector ingestion & Retrieval API setup mapped.
