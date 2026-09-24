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
