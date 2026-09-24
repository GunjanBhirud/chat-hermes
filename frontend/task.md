# TASK.md

Progress tracker for Frontend Service, derived from plan.md Section 23.
Legend: [ ] not started · [x] done

## Phase 1: SPA Foundation and API Bridges
- [x] Execute `vite create` internally avoiding interactive walls.
- [x] Implement `api/documentClient` pointing to document endpoints. 
- [x] Implement `api/chatClient` handling generic JSON.

## Phase 2: Upload UI & Document List (Polling)
- [x] Create `DocumentDashboard.tsx`.
- [x] Install React Query to setup `/api/v1/documents` status mapping interval.
- [x] Implement visual progress representation.

## Phase 3: Chat UI and SSE Streaming Parser
- [x] Build Chat Container interacting with SSE endpoint natively through browser APIs.
- [x] Append letters recursively mapping array changes gracefully.
- [x] Style UI mapping tailwind cleanly.
