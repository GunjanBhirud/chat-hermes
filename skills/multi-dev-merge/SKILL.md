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
