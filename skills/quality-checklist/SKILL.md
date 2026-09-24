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
