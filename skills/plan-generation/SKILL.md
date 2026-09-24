---
name: plan-generation
description: Use when generating or updating plan.md for a Hermes project (initial Step 2, or Step 9 diffs for new features/tech-stack changes). Contains the drafting rules and the exact plan.md template structure (28 sections).
---

## Step 2 — Generate `plan.md`

Use the exact template in **Appendix A** below. Do not omit sections — if a section doesn't apply, write "N/A" and say why, rather than deleting it.

**Rules while drafting plan.md:**
- `plan.md` is a **specification + constraints + verification contract** — not just an implementation checklist. Every Functional Requirement (Section 2) must map to at least one Test Case (Section 15). Every Non-Functional Requirement must map to a concrete, checkable target (not "should be fast" — a number).
- **Mandatory User Stories & Complete Lifecycle Scenarios (Section 2.1):** Every capability, entity, or feature introduced must be modeled as complete user journeys covering the entire functional lifecycle (creation, discovery/listing, detail inspection, modification, consumption, state transitions, edge cases, and failure modes). Never implement half-lifecycle features (e.g., if data or assets are stored/created, retrieval, viewing, consumption, and boundary limits must also be designed and supported).
- Apply **Loop Engineering** (Appendix B) while drafting: propose the full draft → self-check consistency (does every FR and User Story have a test case? does the architecture match the tech decisions? do edge cases in Section 16 appear as test cases in Section 15?) → fix gaps → repeat until consistent.
- Fill Section 26 (Existing Codebase Analysis) by actually scanning the current repo if one exists — don't assume a greenfield project.
- If the project includes a UI, Section 5's **Frontend Plan** subsection is mandatory, not optional — do not leave it blank or assume it's covered by the backend architecture. Section 14/15 must then include both Backend and Frontend test coverage (unit, integration, API/E2E, security/accessibility, performance/responsive, failure/error states) — a backend-only test plan is incomplete for any project with a UI.
- Section 5's **Project Directory Structure** subsection is mandatory for every project (greenfield or existing). Lay out the actual folder/file tree Hermes will create or is working within (down to the key files — entry points, config, routes/controllers, models, components, tests, docs), not just a description in prose. For an existing codebase, this must reflect Section 26's findings, not a generic template.
- Section 8 (Data Model) has a **strict constraint on JSON columns/fields**: Hermes must **not** introduce a JSON/JSONB (or equivalent schemaless blob) column or data type anywhere in the data model unless `prd.md` explicitly calls for one. Default to normalized, explicitly-typed columns/fields for every entity. If a JSON field would genuinely be the right fit, do not add it silently — list it as an Open Question (Section 22) and ask the human before including it in the schema.
- Section 28 (Acceptance Criteria) must be independently checkable by a human without reading the code (e.g., "user can log in and see their dashboard within 2s" — not "login works").


# APPENDIX A — plan.md Template

*(This is the exact structure Hermes must produce in Step 2. Fill every section based on prd.md; mark unknowns as Open Questions in Section 22 rather than guessing.)*

# PLAN.md

## 1. Overview
- Project / feature name
- Problem statement
- Goal
- Non-goals
- Success criteria

## 2. Requirements
### Functional Requirements
- FR-001:
- FR-002:
- FR-003:

### User Stories & Complete Lifecycle Scenarios
- US-001 (Actor): As a [role], I want to [action] so that [benefit].
  - Scenario A (Happy Path): [Given / When / Then]
  - Scenario B (Edge / Negative Path): [Given / When / Then]
- US-002 (Actor): ...

### Non-Functional Requirements
- Performance
- Scalability
- Availability
- Reliability
- Security
- Observability
- Maintainability

## 3. Scope
### In Scope
### Out of Scope

## 4. User / System Flows
- Main user flow
- Error flows
- Edge cases
- State transitions

## 5. Architecture
- Components
- Services
- Dependencies
- Data flow
- External integrations
- Architecture diagram

### Project Directory Structure (required for every project)
- The actual folder/file tree Hermes will create or is working within.
- Note key entry points, config files, and where each major piece lives.
- For an existing codebase, this must match what Section 26 found.
- New paths marked with (new).

### Frontend Plan (required whenever the project has a UI)
- Pages / screens / routes
- Component hierarchy
- State management approach
- Client-server data flow
- Styling approach
- Client-side routing and navigation guards
- Accessibility requirements
- Browser/device support
- Build/bundling tooling

## 6. Technology Decisions
- Language
- Framework
- Database
- Cache
- Queue
- APIs
- Libraries
- Why each technology is used

## 7. API / Interface Contract
- Endpoints
- Request/response schemas
- Authentication
- Authorization
- Error responses
- Versioning
- Idempotency

## 8. Data Model
- Entities
- Relationships
- Indexes
- Constraints
- Migrations
- Data retention
- Sensitive data
- **JSON/JSONB constraint:** No JSON, JSONB, or other schemaless blob column/field anywhere in this data model unless `prd.md` explicitly requires one.

## 9. Security
- Authentication
- Authorization / RBAC
- Input validation
- Secrets management
- Encryption
- OWASP considerations
- Injection prevention
- Rate limiting
- Audit logging
- Dependency security
- Tenant isolation

## 10. Scalability
- Expected users
- Expected request rate
- Data volume
- Concurrent operations
- Horizontal scaling
- Database scaling
- Caching strategy
- Queue/background jobs
- Bottlenecks

## 11. Performance
- Latency targets
- Throughput targets
- Resource limits
- Database query expectations
- Caching
- Timeout/retry policies

## 12. Error Handling & Resilience
- Expected failures
- Retry strategy
- Timeouts
- Circuit breakers
- Graceful degradation
- Transaction rollback
- Recovery behavior

## 13. Observability
- Logs
- Metrics
- Traces
- Alerts
- Health checks
- Audit events
- Dashboards

## 14. Testing Strategy (Backend, Frontend, Contract, User Stories)

### Backend
#### Unit Tests
- Business logic functions, validation rules, utility/helper functions
#### Integration Tests
- Database read/write, transactions, migrations
- External service calls
- Message queue / background job processing
#### API Tests
- Every endpoint: valid request → expected response schema and status code
- Invalid/malformed request → correct 4xx response
- Auth required vs. not required, correct behavior per role
- Pagination, filtering, sorting where applicable
- Idempotency
#### Security Tests
- AuthZ enforced per role/permission
- Injection attempts rejected
- Rate limiting triggers correctly
- Secrets/tokens never appear in logs or responses
- Dependency vulnerability scan clean
#### Performance Tests
- Response latency under expected load
- Concurrency / race conditions on shared resources
- N+1 query detection
- Load test at expected peak request rate
#### Failure / Chaos Tests
- Database unavailable / connection dropped mid-request
- External dependency timeout or 5xx
- Partial failure — confirm rollback/consistency
- Retry and circuit-breaker behavior

### Frontend
#### Unit Tests
- Component logic, hooks, reducers/state transitions
- Utility/formatting functions
#### Integration Tests
- Component + API interaction (mocked API): loading → success → error
- Form submission flows
- State management
#### End-to-End Tests
- Critical user journeys end-to-end
- Multi-step flows completed successfully
- Navigation/routing: protected routes redirect correctly when unauthenticated
#### Accessibility Tests
- Keyboard-only navigation
- Screen-reader labels present
- Color contrast meets target
#### Responsive / Cross-Browser Tests
- Layout correct at defined breakpoints
- Renders correctly on the browser/device matrix from Section 19
#### Error & Loading State Tests
- Network failure shows correct error state
- Slow response shows loading indicator
- Empty-state UI renders correctly

## 15. Test Cases & User Story Verification Matrix
| ID | Scenario | Expected Result | Type | Layer |
|----|----------|-----------------|------|-------|
| TC-001 | Valid API request | 200 with correct response schema | Unit/API | Backend |
| TC-002 | Invalid input to API | 400 with clear validation error | API | Backend |
| TC-003 | Unauthorized request | 401/403, no data leaked | Security | Backend |
| TC-004 | Database unavailable | 5xx handled gracefully, no data corruption | Integration | Backend |
| TC-005 | Concurrent requests to same resource | No race condition, data remains consistent | Performance | Backend |
| TC-006 | SQL/NoSQL injection attempt | Input rejected/sanitized, no injection executed | Security | Backend |
| TC-007 | Repeated identical request (idempotency) | No duplicate side effects | API | Backend |
| TC-008 | Form submitted with valid data | Success state shown, data persisted | Integration | Frontend |
| TC-009 | Form submitted with invalid data | Inline validation errors shown, no submission sent | Unit/Integration | Frontend |
| TC-010 | API call fails (network error) | Error state shown to user, no silent failure | Integration | Frontend |
| TC-011 | API call is slow | Loading indicator shown, submit button disabled | Integration | Frontend |
| TC-012 | User navigates to protected route while logged out | Redirected to login, destination preserved | E2E | Frontend |
| TC-013 | Full critical user journey | Journey completes end-to-end without errors | E2E | Frontend |
| TC-014 | Keyboard-only navigation through a form | All fields/buttons reachable and operable | Accessibility | Frontend |
| TC-015 | Page rendered at mobile breakpoint | Layout adapts correctly, no overflow/broken elements | Responsive | Frontend |
| TC-016 | Empty data state | Correct empty-state UI shown, not blank/broken | Unit/Integration | Frontend |

## 16. Edge Cases
- Empty input
- Null values
- Duplicate requests
- Large payloads
- Concurrent requests
- Network failure
- Dependency failure
- Partial failure
- Timeout
- Invalid state transitions

## 17. Deployment
- Build process
- Environment variables
- Configuration
- Database migrations
- Deployment strategy
- Rollback strategy
- Health checks

## 18. CI/CD
- Lint
- Formatting
- Type checking
- Unit tests
- Integration tests
- Security scanning
- Build
- Deployment gates

## 19. Compatibility
- Supported OS
- Browser/client versions
- API compatibility
- Database versions
- Backward compatibility

## 20. Migration / Upgrade Plan
- Existing data migration
- Schema changes
- Backward compatibility
- Rollback

## 21. Risks & Trade-offs
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|

## 22. Open Questions
- Question 1
- Question 2

## 23. Implementation Plan
### Phase 1
### Phase 2
### Phase 3

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
- Smoke tests
- Health checks
- Metrics verification
- Log verification
- Regression tests
- Rollback verification

## 26. Existing Codebase Analysis
### Relevant Files
### Existing Patterns
### DO NOT Change
### Reuse

## 27. Implementation Constraints
- Follow existing project architecture.
- Do not introduce a new framework.
- Do not duplicate existing services.
- Do not modify public APIs without explicit approval.
- Do not add dependencies unless necessary.
- Do not hardcode credentials or secrets.
- Do not disable existing security controls.
- Prefer existing utilities over creating new ones.
- Keep changes backward compatible.

## 28. Acceptance Criteria
AC-001:
Given [context],
when [action],
then [observable outcome].
