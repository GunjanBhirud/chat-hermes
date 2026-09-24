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
