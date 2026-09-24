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
