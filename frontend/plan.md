# PLAN.md

## 1. Overview
- **Project/feature name:** Document Chat Frontend
- **Problem statement:** Users need a graphical overlay strictly integrating the Document endpoints with the Chat SSE streams.
- **Goal:** Render a SPA utilizing Vite/React that allows document uploading, real-time status polling, and chat SSE ingestion tracking mapped citations.
- **Non-goals:** Implementing authentication systems generically (we use mock static JWTs to map endpoints).
- **Success criteria:** Document status correctly changes without full reloads. Chat streams sequence letters incrementally.

## 2. Requirements
### Functional Requirements
- FR-011: React dashboard uploading documents bridging specific API URLs (Document Service).
- FR-012: Periodic polling of indexing status until `READY`.
- FR-013: Interface to instantiate conversations mapped to checked documents.
- FR-014: Visual tracking of SSE response streams.

### User Stories & Complete Lifecycle Scenarios
- US-004 (Actor): As a user I want to drag and drop PDFs so that they enter the system and show a progress bar.
- US-005 (Actor): As a user I want to check a box next to my documents and click 'Start Chat'.

### Non-Functional Requirements
- **Maintainability:** Extract complex states out of React tree into Zustand.

## 3. Scope
### In Scope
- Web UI development for React SPA.

## 4. User / System Flows
- Home > Upload File > Monitor List > Select Document > Create Chat > Switch to Message List.

## 5. Architecture
- **Components:** React SPA.
- **Data flow:** Components trigger Zustand/React Query -> REST requests (Axios/fetch).

### Project Directory Structure
- `frontend/`
  - `src/`
    - `components/` (Upload, Chat, Layout)
    - `api/` (api clients wrapping `httpx/fetch`)
    - `store/` (Zustand configuration)

### Frontend Plan
- **State management:** Zustand for UI State, TanStack Query for remote status.
- **Styling approach:** Tailwind CSS mapped to HTML fragments.
- **Browser support:** Evergreen Chrome/Firefox.

## 6. Technology Decisions
- React + Vite.

## 7. API / Interface Contract
- Relies on port `8001` and `8002` externally assuming unified Gateway isn't active for dev.

## 8. Data Model
- N/A

## 9. Security
- Minimal JWT tracking. (Out of Scope for mock dev layer).

## 10. Scalability
- UI caches component remounts lazily.

## 11. Performance
- Component renders scoped via strict mode tracking.

## 12. Error Handling & Resilience
- Error boundaries covering components safely.

## 13. Observability
- N/A

## 14. Testing Strategy (Backend, Frontend, Contract, User Stories)
### Frontend
#### Unit Tests
- Simple jest verifications.

## 15. Test Cases & User Story Verification Matrix
| ID | Scenario | Expected Result | Type | Layer |
|----|----------|-----------------|------|-------|
| TC-018 | Render main frame | Layout mounts without error | Unit | Frontend |

## 16. Edge Cases
- Client disconnected while SSE parsing.
- Server returns 5xx down API.

## 17. Deployment
- Docker container `frontend/Dockerfile` targeting reverse proxy or local static dist.

## 18. CI/CD
- Node TS validations.

## 19. Compatibility
- N/A

## 20. Migration / Upgrade Plan
- N/A

## 21. Risks & Trade-offs
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Memory leaks in SSE rendering loop. | High | Medium | Explicit closed loops within useEffect disconnect logic. |

## 22. Open Questions
- None.

## 23. Implementation Plan
### Phase 1: SPA Foundation and API Bridges
### Phase 2: Upload UI & Document List (Polling)
### Phase 3: Chat UI and SSE Streaming Parser

## 24. Definition of Done
- [ ] Requirements implemented
- [ ] Tests passing
- [ ] UI rendered

## 25. Post-Implementation Verification
- Visual E2E test confirmation via headless browser or human equivalent.

## 26. Existing Codebase Analysis
N/A

## 27. Implementation Constraints
- Rely heavily on generic styling.

## 28. Acceptance Criteria
AC-003:
Given a frontend instance,
when loading the dashboard,
then the Upload and Chat interfaces exist and are interactable natively.