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
