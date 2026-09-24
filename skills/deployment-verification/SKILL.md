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
