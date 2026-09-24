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
