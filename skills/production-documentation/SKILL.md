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
