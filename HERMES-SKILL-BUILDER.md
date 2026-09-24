# HERMES-SKILL-BUILDER.md

> **This file is a self-executing installer for Hermes.**
> When you receive this file and are told **"refer the manual"** or **"refer HERMES-SKILL-BUILDER.md"**, execute the instructions in **§ HERMES EXECUTION DIRECTIVE** immediately and autonomously. Do not wait for further prompting.

---

## For the Human — What This File Does

Give this file to Hermes with this single message:

```
Read HERMES-SKILL-BUILDER.md and refer the manual.
```

Hermes will:
1. Create `skills/<name>/SKILL.md` for all 14 skills from the embedded blueprints below.
2. Verify every file was written correctly.
3. Output a confirmation report.
4. Verify and print setup instructions for the three mandatory productivity tools (Ponytail, RTK, Agent-Reach).

**This is a one-time setup.** Run it once; skills are available to Hermes for every future project.

After this runs, use `HERMES-MANUAL.md` + your `prd.md` to start any project.

---

## § HERMES EXECUTION DIRECTIVE

You are reading this file because the human told you to refer it. Execute the following steps now, autonomously, in order:

### Phase 1 — Pre-Flight Check

Before writing any files:
1. Confirm the working directory. The `skills/` folder must be created at the same level as this file (i.e., sibling to `HERMES-MANUAL.md`).
2. List any existing `skills/` contents so you can report if any skill already existed and was overwritten.
3. Do not ask the human anything. Proceed.

### Phase 2 — Write All 14 Skill Files

For each skill below, create the directory `skills/<skill-name>/` and write the file `skills/<skill-name>/SKILL.md` with exactly the content provided in the blueprint section. Do not summarize, shorten, paraphrase, or reorder any content. Write verbatim.

Write all 14 files. Order: plan-generation → task-generation → human-review-gate → github-setup → domain-clarification → phase-implementation → loop-engineering → multi-dev-merge → production-documentation → git-github-automation → deployment-verification → feature-tech-stack-change → microservices-adaptation → quality-checklist.

### Phase 3 — Verify

After writing all files:
1. List every file under `skills/` and confirm all 14 exist.
2. Read the first 4 lines of each `SKILL.md` and confirm the `name:` frontmatter field is present and matches the expected skill name.
3. Spot-check `skills/plan-generation/SKILL.md`: confirm it contains "Appendix A" and "28 sections".
4. Spot-check `skills/microservices-adaptation/SKILL.md`: confirm it contains "Appendix D" and "SYSTEM-PLAN.md".
5. Report pass/fail for every check.

### Phase 4 — Output Confirmation Report

Print a report in this format:
```
HERMES SKILL BUILDER — INSTALLATION REPORT
==========================================
Skills written: 14/14
Verification: PASS / FAIL (list any failures)

Installed skills:
  ✓ plan-generation
  ✓ task-generation
  ✓ human-review-gate
  ✓ github-setup
  ✓ domain-clarification
  ✓ phase-implementation
  ✓ loop-engineering
  ✓ multi-dev-merge
  ✓ production-documentation
  ✓ git-github-automation
  ✓ deployment-verification
  ✓ feature-tech-stack-change
  ✓ microservices-adaptation
  ✓ quality-checklist

SETUP COMPLETE. You may now use HERMES-MANUAL.md + prd.md to start any project.
```

### Phase 5 — Mandatory Tool Setup

After the report, print the following tool setup section exactly as written:

---

## Mandatory Productivity Tools

> ⚠️ **Installation note:** After installing each tool, run `hermes doctor` to confirm configuration health.

### Tool 1 — Ponytail (Always-On Coding Discipline)
**Repo:** https://github.com/dietrichgebert/ponytail
**What it does:** Enforces a 7-step "smallest correct diff" Decision Ladder before every code-write. Reduces over-engineering and token cost while never cutting security, validation, or accessibility. Native Hermes plugin.
**Install:**
```
Install and enable the ponytail plugin from github.com/dietrichgebert/ponytail,
then confirm it's active and show me what /ponytail-help lists.
```
After install: run `hermes doctor` and ask Hermes to summarize what the plugin installed.

---

### Tool 2 — RTK (Token Reduction, Always-On)
**Repo:** https://github.com/rtk-ai/rtk
**What it does:** CLI proxy that compresses `git`, `gh`, `mypy`, test runner output by 60–90% before it enters the context window. Explicit Hermes support via `rtk init --agent hermes`.
**Install:**
```
Install RTK from github.com/rtk-ai/rtk and initialize it for Hermes
(rtk init --agent hermes), then show me the savings dashboard (rtk gain)
so I can confirm it's working.
```
After install: run `hermes doctor` and ask Hermes to summarize what RTK installed and configured.

---

### Tool 3 — Agent-Reach (Conditional — Internet Access for Research)
**Repo:** https://github.com/Panniantong/Agent-Reach
**What it does:** Gives Hermes reliable read-only access to Twitter/X, Reddit, YouTube, GitHub, and 12+ other platforms — routing each request to the best available backend (CLI, API, or MCP tool). Activates automatically when `prd.md` references external integrations or when Hermes needs live documentation during debugging.
**Install:**
```
Set up Agent-Reach from github.com/Panniantong/Agent-Reach so I can search and
read content across platforms like Twitter, Reddit, and YouTube. Check first
whether it's confirmed compatible with Hermes, and tell me if anything about
the setup needs my review before it's enabled.
```
After install: run `hermes doctor` and ask Hermes to summarize what Agent-Reach installed and what permissions it uses.

---

All three tools are mandatory. Once installed, `HERMES-MANUAL.md` enforces them at the correct pipeline steps automatically.

---

## § SKILL BLUEPRINTS (Verbatim — Do Not Edit)

> These are the exact file contents Hermes writes in Phase 2. They are embedded here so this file is fully self-contained and requires no external sources.

---

### BLUEPRINT 1 — `skills/plan-generation/SKILL.md`

```markdown
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
```

---

### BLUEPRINT 2 — `skills/task-generation/SKILL.md`

```markdown
---
name: task-generation
description: Use immediately after plan.md is drafted, to generate or extend task.md (Step 2.1, or Step 9 when new phases are appended). Contains the drafting rules and the exact task.md template structure.
---

## Step 2.1 — Generate `task.md`

Immediately after `plan.md` is drafted (and before presenting either file at the Step 3 review gate), Hermes must also generate `task.md` — a flat, checkable task list derived from `plan.md` Section 23 (Implementation Plan).

**Rules for `task.md`:**
- One checkbox per concrete, completable task, grouped under its phase (matching Section 23's phases exactly).
- Each task must be small enough to be unambiguously either done or not done — not "build backend" but the individual steps that make it up (e.g., "create User model", "implement POST /login endpoint", "write TC-001 test").
- Derive tasks so that, taken together, they cover every Functional Requirement, every User Story Scenario, every Test Case (Section 15), and every Definition of Done item (Section 24) — nothing in the plan should exist with no corresponding task.
- Use GitHub-flavored checkboxes (`- [ ]` / `- [x]`) so progress is visible directly in the rendered file.
- Present `task.md` alongside `plan.md` at the Step 3 Human Review Gate — both are reviewed and approved together, and both are revised together if changes are requested.
- Use the exact structure in **Appendix E**.

**Keeping `task.md` current (applies from Step 4 onward):**
- The moment a task is completed and its validation passes (per the Loop Engineering cycle), Hermes marks it `- [x]` in `task.md` before moving to the next task. Do not batch updates until the end of a phase.
- If Step 9 (new feature) or a tech-stack change adds work, append the new tasks under a new or existing phase heading in `task.md` — do not create a second task file.
- `task.md` is a live progress record, not a one-time artifact — it should always reflect the true current state of implementation.

# APPENDIX E — task.md Template

# TASK.md

Progress tracker for <project/feature name>, derived from plan.md Section 23.
Legend: [ ] not started · [x] done

## Phase 1 — <phase name>
- [ ] Task: <short description> (covers FR-00X / TC-00X)
- [ ] Task: <short description>
- [ ] Task: <short description>

## Phase 2 — <phase name>
- [ ] Task: <short description>
- [ ] Task: <short description>

## Phase 3 — <phase name>
- [ ] Task: <short description>

## New Feature — <added via Step 9, if applicable>
- [ ] Task: <short description>

**Notes:**
- Group tasks under the same phase headings used in `plan.md` Section 23, in the same order.
- Where practical, note which Functional Requirement or Test Case ID a task closes out.
- New phases added later get appended as new headings — this file is never recreated from scratch, only extended and checked off.
```

---

### BLUEPRINT 3 — `skills/human-review-gate/SKILL.md`

```markdown
---
name: human-review-gate
description: Use before writing any implementation code, to run the mandatory blocking human review gate over plan.md and task.md (Step 3).
---

## Step 3 — Human Review Gate (MANDATORY, BLOCKING)

- **STOP. Do not write, generate, or scaffold any implementation code yet.**
- Present the full `plan.md` **and** the accompanying `task.md` to the human together.
- Explicitly ask: *"Please review plan.md and task.md. Reply 'approved' to proceed, or list changes needed."*
- If changes are requested: revise the relevant sections of `plan.md` and the corresponding tasks in `task.md`, re-present both, and ask again.
- Repeat until you receive an explicit approval. **No phase of Step 4 begins without this.**
```

---

### BLUEPRINT 4 — `skills/github-setup/SKILL.md`

```markdown
---
name: github-setup
description: Use right after plan.md/task.md are approved and before any code is scaffolded, to set up GitHub repo access and local git (Step 3.1).
---

## Step 3.1 — GitHub Setup & Authentication Gate (MANDATORY)

Immediately after receiving approval in Step 3 and before scaffolding any implementation code:
1. **Request GitHub Target & Credentials:**
   Prompt the human:
   ```
   Please provide the target GitHub repository (<owner>/<repo>) and ensure
   your fine-grained GITHUB_TOKEN is exported as an environment variable in your session.
   ```
2. **Repository Existence & Metadata Setup:**
   - Verify if the repository exists via GitHub API (`GET /repos/<owner>/<repo>`).
   - If not found, create it via GitHub API (`POST /user/repos`).
   - Populate the repository **Description** (`PATCH /repos/<owner>/<repo>`) with a clear summary of the project.
   - Set relevant repository **Topics** (`PUT /repos/<owner>/<repo>/topics`) representing the application's technologies and domain.
3. **Local Git Setup:**
   - Initialize git, configure user name/email, create a standard `.gitignore`, and set `origin` to the target repository URL using token authentication.
```

---

### BLUEPRINT 5 — `skills/domain-clarification/SKILL.md`

```markdown
---
name: domain-clarification
description: Use immediately before implementation starts, to surface domain-specific thresholds, retention rules, caps, or policy defaults not stated in prd.md and get them clarified by the human (Step 3.2).
---

## Step 3.2 — Domain & Operational Parameters Clarification Gate (MANDATORY)

Immediately prior to starting Step 4 implementation, Hermes must inspect the planned system entities and operational features to identify any domain-specific business thresholds, retention rules, resource caps, or policy defaults that were not explicitly stated in `prd.md`.

- **Proactive Clarification:** Present these specific domain choices to the human in a single, structured question list (e.g. data retention horizons, operational thresholds, capacity/resource limits, default system timeouts, or policy constants relevant to the application domain).
- **Incorporate Answers:** Apply the human's specified operational parameters across configuration files, environment variables, validation schemas, and database default constraints before writing core feature code.
```

---

### BLUEPRINT 6 — `skills/phase-implementation/SKILL.md`

```markdown
---
name: phase-implementation
description: Use to implement each phase of plan.md Section 23 in order, applying the Loop Engineering cycle and keeping task.md current (Step 4).
---

## Step 4 — Implementation, Phase by Phase

- Follow the phases listed in plan.md Section 23 (Implementation Plan), in order.
- For each phase, apply the **Loop Engineering cycle** (Appendix B):
  1. Build the phase's scope.
  2. Validate — run every test type relevant to that phase (unit, integration, API, security, performance, edge cases, and end-to-end user story walkthroughs — pull the specific cases from Section 15/16 that apply to this phase).
  3. If anything fails: read the exact failure, fix it, re-run the same check.
  4. Repeat up to 5 times. If still failing, stop and report the specific blocker to the human instead of guessing further.
- A phase is only "done" when its relevant tests pass **and** its slice of the Section 24 Definition of Done is met.
- As each individual task in that phase passes validation, mark it `- [x]` in `task.md` right away (see Step 2.1) — do not wait until the whole phase finishes to update it.
- Do not move to the next phase until the current one is done and `task.md` reflects that every task in it is checked off.
```

---

### BLUEPRINT 7 — `skills/loop-engineering/SKILL.md`

```markdown
---
name: loop-engineering
description: Use during any build/test/fix cycle anywhere in the project — drafting plan.md, implementing a phase, fixing a failing test. Defines the propose-validate-diagnose-refine-converge cycle and its 5-iteration cap (Appendix B).
---

# APPENDIX B — Loop Engineering (Reference)

**Definition:** every build/test/fix cycle follows **propose → validate → diagnose → refine → converge**, never a single one-shot attempt.

- **Propose** — produce the artifact (code, test, fix, root-cause guess, plan.md draft).
- **Validate** — check it with something independent of the agent itself: a test suite, linter, security scanner, or human judgment.
- **Diagnose & Refine** — if validation fails, feed the *exact* failure (error text, failing assertion, reviewer comment) back, and fix specifically that.
- **Converge** — only exit the loop when validation passes.
- **Cap iterations at 5** per phase/task. If not converging by then, stop and report the blocker to the human instead of continuing to guess.
- Never treat the agent's own claim ("this should work now," "this is secure") as validation — always re-run the actual check.
```

---

### BLUEPRINT 8 — `skills/multi-dev-merge/SKILL.md`

```markdown
---
name: multi-dev-merge
description: Use when more than one developer/Hermes session works on the same application, to keep plan.md as the shared contract and run the merge-readiness loop before any branch merges (Step 5).
---

## Step 5 — Multi-Developer Collaboration & Merge Handling

When more than one developer (each possibly running their own Hermes session) works on the same application:

1. **`plan.md` is the shared contract.** Both developers' Hermes sessions read the same `plan.md`. Sections 5–8 (Architecture, Tech Decisions, API Contract, Data Model) are binding — if a developer's work requires deviating from them, `plan.md` must be updated and re-approved by the human **before** implementation continues, so the two branches don't silently diverge.
2. **Branch isolation.** Each developer works on their own branch (`feature/<name>-<task>`), never directly on `main`.
3. **Before merging a branch, run a Merge-Readiness Loop:**
   - Pull the latest `main` into the feature branch (merge or rebase).
   - Re-run the **full test suite** against the merged result — not just the feature branch's own tests. A feature can pass alone and still break the combined codebase.
   - **Classify any conflicts:**
     - *Textual, non-overlapping logic* → Hermes resolves automatically, re-runs tests to confirm, and logs the resolution.
     - *Semantic conflicts* (both developers changed the same function, the same API contract, or overlapping logic) → Hermes does **not** auto-resolve. It presents both versions side by side, explains what each does, and asks a human to decide. Implementation does not continue until a decision is made.
   - Only after tests pass on the merged result does the branch become mergeable.
4. **Merge via Pull Request, not direct push to `main`** (see Step 7 for exact merge policy).
5. After any merge, create a `docs/MERGE_<date>_<branches>.md` log: which branches were merged, what conflicts were found, how each was resolved, and the post-merge test results.
```

---

### BLUEPRINT 9 — `skills/production-documentation/SKILL.md`

```markdown
---
name: production-documentation
description: Use after each phase or merge, to create/update the mandatory README.md, docs/APPLICATION_DOCUMENTATION.md, and docs/PHASE_*.md or docs/MERGE_*.md files (Step 6).
---

## Step 6 — Industry-Grade Production Documentation (MANDATORY)

Every project MUST produce and maintain the following documentation artifacts:

1. **Root `README.md`:**
   - System architecture diagram (ASCII or Mermaid) illustrating services, components, databases, and network flows.
   - Component & Port Inventory table.
   - User Roles & Access Control matrix.
   - Quickstart Guide via container orchestration (`docker compose up -d --build` or equivalent).
   - Local Development Setup Guide (environment variables, dependency installation, running services locally).
   - Test execution commands and test suite coverage summary.
   - Links to all phase documentation files.

2. **`docs/APPLICATION_DOCUMENTATION.md` (Comprehensive Technical & Operational Spec):**
   - Detailed architectural boundary rules, data isolation, and inter-service protocols.
   - Complete API endpoint reference with request/response schemas, status codes, and authentication requirements.
   - Domain Data Models, field specifications, indices, constraints, and relational mappings.
   - State transition diagrams and lifecycle rules.
   - Background tasks, queues, scheduler intervals, and event-driven workflows.
   - Error handling policies, failure modes, and graceful degradation strategies.

3. **`docs/PHASE_<number>_<short-name>.md` (and `docs/MERGE_<date>_<branches>.md` for merges):**
   - Created after finishing each phase (Step 4) or each merge (Step 5).
   - **What was implemented** in this phase (or what was merged).
   - **Loop Engineering log** — every fix attempted, what failed, what changed, how many iterations it took.
   - **Tests run and results** — broken out by type: unit, integration, API, security, performance, edge case, and user stories — referencing the Test Case IDs (`TC-xxx`) from `plan.md` Section 15.
   - **Any conflicts and resolutions** (merge docs only).
```

---

### BLUEPRINT 10 — `skills/git-github-automation/SKILL.md`

```markdown
---
name: git-github-automation
description: Use for ongoing git/GitHub operations after initial setup — credential handling, branch policy, PR/merge policy, and commit conventions (Step 7).
---

## Step 7 — Version Control & GitHub Automation

### 7.0 — GitHub Authentication: When and How

- **When to give credentials:** right after `plan.md` is approved in Step 3 and configured via Step 3.1 before Step 4 implementation begins. Hermes doesn't need repo write access while the plan is still being drafted or reviewed — there's nothing to commit yet.
- **How:** use a fine-grained, repo-scoped GitHub Personal Access Token (or a GitHub App installation) limited to this one repository, with only the scopes actually needed — `Contents` (read/write), `Pull requests` (read/write), and `Workflows` (only if Hermes needs to add/edit CI files). Do not grant org-wide or admin scope. Set an expiration on the token.
- **Never paste the token directly into chat.** Set it as an environment variable (e.g., `GITHUB_TOKEN`) in the shell/session Hermes runs in. Hermes must never print, log, or commit the token anywhere, and must treat it as a secret per the same rules as any other credential.
- Before starting implementation, confirm authentication with a test call or push (e.g., a test push to a throwaway branch) so auth problems surface before real work is at stake.

**Prompt to Use — Granting GitHub Access:**
```
I'm giving you GitHub push access for this project.
Repo: <owner/repo>
I've set the token as an environment variable named GITHUB_TOKEN — don't
ask me to paste it in chat, and never print it, log it, or commit it
anywhere.

Use it only to: create branches, push commits, open PRs, and merge only
per the policy below (PR + green CI required; autonomous merge only if
I've explicitly enabled it).

Confirm you can authenticate — push a commit to a throwaway test branch
and confirm it appears on GitHub — before starting real implementation.
```

### 7.1 — Automation Policy

Default policy (recommended — adjust only with explicit human instruction):

- Hermes may push freely to `feature/*` branches and open Pull Requests automatically.
- `main` is protected: merges require (a) CI fully green — lint, unit, integration, security scan, and (b) either explicit human approval on the PR, or, only if the human has explicitly set `autonomous-merge: true` for this project, Hermes may self-merge once CI is fully green — but must still write the merge doc from Step 5.5 and must never do this for changes touching auth, payments, secrets, or data-deletion logic without a human review regardless of the setting.
- Hermes never force-pushes to `main`, never deletes a branch with unmerged commits without confirming with the human first, and never rewrites merged history.
- Push all completed code, tests, and documentation to the remote repository on `main` / feature branch at the end of every phase.
- Every commit message should reference the phase or feature it implements (e.g., `feat(phase-2): add user auth endpoints`).
```

---

### BLUEPRINT 11 — `skills/deployment-verification/SKILL.md`

```markdown
---
name: deployment-verification
description: Use to deploy a phase and verify it, including mandatory automated Playwright/E2E browser verification whenever the project has a UI, and on-demand visual browsing when the human asks (Step 8 and 8.1).
---

## Step 8 — Deployment & Verification

- Deploy per `plan.md` Section 17 (Deployment).
- Run the Post-Implementation Verification checks from Section 25 (smoke tests, health checks, metrics/log verification, regression tests) before declaring the deployment done.
- Give the human the **live URL** to verify directly, along with a short summary of what was just deployed and which phase docs cover it.
- If any post-deployment check fails, do not consider the phase complete — treat it as a failure and re-enter the Loop Engineering cycle (Step 4) before re-announcing readiness.

### 8.1 — Frontend Browser Verification & User Story Testing

#### Automated Verification (Mandatory when UI is present):
- When the project includes a user interface, Hermes MUST execute automated end-to-end browser verification against the running application using Playwright (or `@playwright/test` / Vitest Browser Mode) and live user-story automation scripts.
- Automated tests must cover all user journeys and every possible scenario:
  1. Authentication & registration flows and session persistence.
  2. Route protection and unauthenticated redirect behaviors.
  3. Complete feature lifecycles (creation, discovery, detail inspection, editing, deletion, interaction, resource consumption, state transitions).
  4. Role-gated controls and permission views across all user roles.
  5. Negative scenarios (validation failures, forbidden actions, offline service graceful degradation).
  6. Absence of unhandled browser console errors or broken network requests.
- Report observed browser test and user story results in the phase documentation.

#### On-Demand Visual Browsing (Explicit Opt-In Only):
- Outside of automated CI/test suites, Hermes must **not** spontaneously launch an interactive browser session to visually inspect pages unless the human explicitly requests it — e.g., "open the URL and check the frontend," "verify the deployed page looks right," "browse to `<url>` and confirm X is visible."
- This applies each time — a prior request to browse does not carry forward to future phases; ask again if needed.

**Prompt to Use — Requesting a Playwright Check:**
```
Open <url> using Playwright and verify: <what to check — e.g., "the login
page renders correctly, the submit button is clickable, no console
errors, the dashboard loads after login">.
Take a screenshot and report exactly what you observed.
Do not repeat this automatically for future phases unless I ask again.
```
```

---

### BLUEPRINT 12 — `skills/feature-tech-stack-change/SKILL.md`

```markdown
---
name: feature-tech-stack-change
description: Use whenever the human requests a new feature or a technology-stack change after the initial build — recognized from plain language, no special template needed (Step 9).
---

## Step 9 — Adding a New Feature Later

When the human wants to add a feature after the initial build:

1. **Update `plan.md`, not a separate file** — add new Functional Requirements (Section 2), User Stories & Complete Lifecycle Scenarios (Section 2.1), new Test Cases (Section 15), new Edge Cases (Section 16), and update Architecture/Data Model/API Contract (Sections 5, 7, 8) if the feature touches them. Add a new phase under Section 23.
2. **Re-run the Human Review Gate (Step 3)** for just the new/changed sections — don't re-approve the whole document, but the human must explicitly approve the addition before implementation starts.
3. **Implement the new phase** using the same Loop Engineering cycle (Step 4).
4. **Run full regression** — not just tests for the new feature. Run both backend test suite and Playwright browser / user story E2E tests. Every existing test case in Section 15 must still pass, since new code can silently break old behavior.
5. **Update documentation** (`APPLICATION_DOCUMENTATION.md`, `README.md`, and create `docs/PHASE_*.md` for the new feature, same format as before).
6. **Branch, PR, merge** following the same policy as Step 7 (and the multi-developer merge process in Step 5 if others are actively working on other branches).
7. **Deploy and re-verify** (Step 8) — give the human the updated URL and confirm the regression suite passed.

### Prompt to Use — Adding a New Feature

```
I want to add a new feature: <feature name>.

Description: <what it should do>
Why: <problem it solves / user need>
Constraints: <any limits — performance, compatibility, etc., if known>

Follow Step 9 of HERMES-MANUAL.md exactly:
1. Update plan.md — add new FRs, new test cases, new edge cases, and update
   Architecture/Data Model/API Contract only if this feature touches them.
2. Present the diff to me for approval before implementing anything.
3. Once approved, implement using the Loop Engineering cycle.
4. Run the FULL regression suite, not just tests for this feature.
5. Create the phase doc.
6. Open a PR following the branch/merge policy in Step 7.
7. Deploy and give me the URL to verify.
```

### Prompt to Use — Adding / Changing a Tech Stack Component

```
I want to add/change a technology in this project: <e.g. "add Redis for caching",
"replace REST with GraphQL", "swap PostgreSQL for MongoDB">.

Reason: <why this change is needed>
Scope: <does this replace something existing, or is it additive?>

Before making any code changes:
1. Update plan.md Section 6 (Technology Decisions) — state what's changing, why,
   and what alternatives were considered.
2. Update plan.md Section 26 (Existing Codebase Analysis) — identify every place
   in the current code that this change touches, and anything in the "DO NOT
   Change" list that might conflict with this.
3. Update plan.md Section 27 (Implementation Constraints) if this changes what's
   allowed (e.g., a new dependency being added).
4. Update plan.md Section 21 (Risks & Trade-offs) — a tech stack change carries
   migration risk, so list it explicitly with mitigation (e.g., feature flag,
   parallel run, rollback plan).
5. Present the full diff to me for approval — do NOT implement anything yet.
6. Once approved, implement behind a feature flag or on an isolated branch where
   possible, so it can be rolled back without affecting the rest of the app.
7. Run the FULL regression suite plus any migration-specific tests.
8. Create the phase doc, including a migration/rollback section.
9. Open a PR — tech stack changes should NOT use autonomous merge even if it's
   enabled for this project; require explicit human approval on the PR.
10. Deploy to staging first, verify, then production — give me both URLs.
```
```

---

### BLUEPRINT 13 — `skills/microservices-adaptation/SKILL.md`

```markdown
---
name: microservices-adaptation
description: Use instead of the single-plan.md flow when the application is split into multiple independently-owned services. Contains the SYSTEM-PLAN.md template and per-service binding/contract-testing/deployment rules (Step 10).
---

## Step 10 — Microservices Adaptation

Use this instead of the single-`plan.md` flow when the application is split into multiple services, each owned by a different developer (and possibly a different Hermes session).

**Folder structure:**
```
project-root/
  SYSTEM-PLAN.md
  service-<name-a>/
    prd.md
    plan.md
    docs/
  service-<name-b>/
    prd.md
    plan.md
    docs/
```

### 10.1 Create `SYSTEM-PLAN.md` First (before any service-level work)

Before any developer starts on an individual service, generate `SYSTEM-PLAN.md` using the template in **Appendix D** — which is located further down in **this same file** (`skills/microservices-adaptation/SKILL.md`), under the heading `# APPENDIX D — SYSTEM-PLAN.md Template (Microservices)`. Read the entire file to reach it. The template has 11 numbered sections: System Overview, Service Inventory, Service Boundaries & Data Ownership, Communication Patterns, Inter-Service API Contracts, Authentication & Authorization Between Services, Shared Standards, Deployment Topology, Failure & Degradation Across Services, Contract Change Process, and Open Questions.

This is the cross-service equivalent of `plan.md` Sections 5–8 — it defines what each service owns, how they communicate, and what contracts they must not silently break.

`SYSTEM-PLAN.md` goes through the **same Human Review Gate as Step 3** — do not let any service's `plan.md` be written until `SYSTEM-PLAN.md` is approved.

### 10.2 Each Service's `plan.md` Is Bound to `SYSTEM-PLAN.md`

- Each service still gets its own full `plan.md` (Appendix A), generated and approved via Steps 1–3, scoped to that service's `prd.md`.
- Section 7 (API Contract) of a service's `plan.md` **must match** what `SYSTEM-PLAN.md` says that service is allowed to expose and consume.
- If implementing a service reveals a need to change a shared interface: **stop**, update `SYSTEM-PLAN.md` first, get it re-approved by the human, then update the affected services' `plan.md` files. Never change a cross-service contract quietly from inside one service's own plan.

### 10.3 Contract Testing (mandatory addition to Section 14)

For every service, add a **Consumer-Driven Contract Tests** category to `plan.md` Section 14:
- The service tests its own implementation against the contract `SYSTEM-PLAN.md` says it must expose (as a provider).
- The service tests against a mock of each dependency's published contract (as a consumer).
- Add corresponding test cases to Section 15 with `Type = Contract` and note which other service the contract is with.

### 10.4 Git/CI/CD, Per Service

- Each service keeps its own repo or its own top-level folder in a monorepo, with its own branch protection and CI pipeline (Step 7's policy applies per-service).
- Add one extra CI job per service: run its contract tests against the **currently deployed** version of the services it depends on, before promoting that service to production.

### 10.5 Multi-Developer Merge Within a Service

Step 5's merge-readiness loop still applies **within a single service** if more than one person works on it. Across services, coordination happens through `SYSTEM-PLAN.md`, not through git merges.

### 10.6 Deployment & Verification, Per Service

- Each service deploys independently (Step 8), but its post-deployment verification must also include a **contract check against live dependent services**.
- Give the human the URL/endpoint for each service deployed, plus a one-line summary of which contracts were verified against which dependencies.

### Prompt to Use — Starting a Microservices Project

```
This project is a microservices application with the following services:
<list service names and one-line purpose for each>

Before any service-level work:
1. Create SYSTEM-PLAN.md using Appendix D of HERMES-MANUAL.md.
2. Present it to me for approval — do not start any service's plan.md yet.

Once SYSTEM-PLAN.md is approved, for each service:
3. Create <service-folder>/plan.md per Appendix A.
4. Add Consumer-Driven Contract Tests to that service's Section 14/15.
5. Present each service's plan.md to me for approval before implementing it.

If at any point building one service requires changing an interface another
service depends on, stop and tell me — update SYSTEM-PLAN.md and get my
approval before changing any service's plan.md.
```

# APPENDIX D — SYSTEM-PLAN.md Template (Microservices)

# SYSTEM-PLAN.md

## 1. System Overview
- What the overall system does
- Why it's split into services (not just "because microservices")

## 2. Service Inventory
| Service Name | Owner/Developer | Purpose | Repo/Folder |
|---|---|---|---|

## 3. Service Boundaries & Data Ownership
- What each service owns (its own database/data — no shared DB access across services)
- What each service must NOT do

## 4. Communication Patterns
- Synchronous (REST/gRPC) vs. asynchronous (events/queue) — which services use which, and why
- Message broker / event bus (if used) and its topics/queues

## 5. Inter-Service API Contracts
| Provider Service | Consumer Service(s) | Contract (endpoint/event) | Schema/Payload | Versioning Policy |
|---|---|---|---|---|

## 6. Authentication & Authorization Between Services
- How services authenticate to each other (mTLS, service tokens, API keys, etc.)
- How a request's original user identity/permissions propagate across service calls

## 7. Shared Standards
- Common error response format across all services
- Common logging/tracing format
- Common versioning scheme for APIs and events

## 8. Deployment Topology
- Where each service runs (containers, orchestration, regions)
- Service discovery mechanism
- Independent deployability confirmed

## 9. Failure & Degradation Across Services
- What happens to Service A if Service B is down
- Timeout and retry policy for inter-service calls
- Circuit breaker strategy

## 10. Contract Change Process
- How a breaking change to a shared contract must be proposed, reviewed, and rolled out
- Which services must approve a change to a contract they consume

## 11. Open Questions
- Question 1
- Question 2
```

---

### BLUEPRINT 14 — `skills/quality-checklist/SKILL.md`

```markdown
---
name: quality-checklist
description: Use as a self-audit: before presenting plan.md/task.md at the Step 3 gate, and before declaring any phase or the project done (Appendix C).
---

# APPENDIX C — Quick Checklist

- [ ] `prd.md` provided
- [ ] `plan.md` generated per Appendix A with **comprehensive User Stories for all lifecycle scenarios**, every FR mapped to a test case
- [ ] `plan.md` Section 5 includes a concrete Project Directory Structure (not just prose)
- [ ] `plan.md` Section 8 has no JSON/JSONB fields unless `prd.md` explicitly required them
- [ ] `task.md` generated per Appendix E, derived from `plan.md` Section 23, covering every FR/User Story/Test Case/DoD item
- [ ] **Human explicitly approved both `plan.md` and `task.md` before any code was written (Step 3)**
- [ ] **GitHub repository initialized with Description, Topics, and remote tracking configured (Step 3.1)**
- [ ] **Domain & operational parameters clarified with human before implementation starts (Step 3.2)**
- [ ] Each phase implemented via Loop Engineering cycle, tests passing before moving on, and its tasks checked off in `task.md` as each one completes
- [ ] **Industry-grade root `README.md` created with architecture diagrams and run commands (Step 6)**
- [ ] **`docs/APPLICATION_DOCUMENTATION.md` created with full technical, API, and domain specs (Step 6)**
- [ ] Phase doc created after each phase in `docs/PHASE_*.md` (and `docs/MERGE_*.md` for merges)
- [ ] Multi-developer branches merged only after full-suite re-validation, semantic conflicts escalated to a human
- [ ] `main` protected — PR + green CI required; autonomous merge only if explicitly enabled, and never for auth/payments/secrets/data-deletion changes
- [ ] GitHub credentials given only after plan.md approval, as a repo-scoped token via environment variable — never pasted in chat, never printed/logged/committed
- [ ] **Automated Playwright browser E2E and complete User Story verification executed if project has a UI (Step 8.1)**
- [ ] **All code and documentation committed and pushed to remote GitHub repository (Step 7)**
- [ ] Deployment verified and URL handed to the human
- [ ] New features go through: update plan.md → re-approval of the diff → implement → full regression → phase doc → PR/merge → re-verify
- [ ] If this is a microservices project: `SYSTEM-PLAN.md` (Appendix D) approved before any service's `plan.md` was started, and each service's API Contract section matches it
```
