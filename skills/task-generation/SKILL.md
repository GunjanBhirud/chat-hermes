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
