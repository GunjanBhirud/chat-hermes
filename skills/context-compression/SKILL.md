---
name: context-compression
description: Use to compress the conversation context at any checkpoint — after a phase, when context grows large, or when the human says "compress context". Writes SESSION-STATE.md so a fresh Hermes session can resume with zero conversation history but full fidelity.
---

## Context Compression

Hermes runs this skill whenever:
1. A phase completes and its docs/tests/push are done (auto-compress before starting next phase).
2. The human says **"compress context"** or **"/compress"**.
3. Context is clearly large (many tool calls, long error logs, repeated attempts visible in history).

---

## What Compression Does

It writes `SESSION-STATE.md` in the project root — a single structured file that replaces the entire conversation history for a resume session. The file is compact by design: it captures decisions, not transcripts.

**What gets preserved (written to SESSION-STATE.md):**
- Project identity and goal
- GitHub repo, branch policy, autonomous-merge setting
- Tool availability (RTK, Ponytail, Agent-Reach: installed or not)
- Domain parameter answers given at Step 3.2
- Completed phases — 2–3 sentence summary each (not logs)
- Current `task.md` content pasted verbatim (already compact)
- Key implementation decisions made during build that differ from or add to plan.md
- Current pipeline position (exact step + phase)
- Next action (exactly what Hermes does immediately on resume)
- Open blockers or pending human decisions

**What gets discarded (safe to drop):**
- Full conversation transcript
- Verbose test runner output (already in `docs/PHASE_*.md`)
- Intermediate error messages from loop engineering (already in phase docs)
- Tool call results whose content is now in project files
- Repeated attempts and their outputs

---

## SESSION-STATE.md Template

Write this file to the project root. Fill every field — do not leave any section blank or write "N/A" without a reason.

```markdown
# SESSION-STATE.md
Generated: <ISO timestamp>
Purpose: Context resume file. A fresh Hermes session reads this + plan.md + task.md
         to resume with no conversation history.

---

## 1. Project Identity
- **Name:** <project name>
- **Goal (1–2 sentences):** <what this project does and why>
- **GitHub Repo:** <owner/repo>
- **Local path:** <absolute path to project root>

## 2. Pipeline Position
- **Current step:** Step <N> — <step name>
- **Current phase:** Phase <N> of <total> (<phase name from plan.md Section 23>)
- **Phase status:** <In progress / Just completed / Not started>

## 3. Tool State
- Ponytail: <installed and active>
- RTK: <installed and active>
- Agent-Reach: <installed and active>
- RTK initialized for this project: <yes / no>

## 4. GitHub & Branch Policy
- Remote origin: <URL>
- Default branch: <main / master>
- Autonomous merge enabled: <yes / no>
- Current feature branch (if any): <branch name>

## 5. Domain Parameter Answers (Step 3.2)
<Paste the exact answers the human gave at Step 3.2 — operational thresholds, retention rules,
resource caps, policy defaults. These must be applied in all remaining implementation work.>
- <param 1>: <value>
- <param 2>: <value>

## 6. Completed Phases Summary
<One entry per completed phase. 2–3 sentences max each. What was built, what tests passed,
what was deployed. Do not paste logs — just the outcome.>

### Phase 1 — <name>
<summary>
Docs: docs/PHASE_1_<name>.md

### Phase 2 — <name> (if completed)
<summary>
Docs: docs/PHASE_2_<name>.md

## 7. Current task.md State
<Paste the full current content of task.md verbatim — it is already compact.>

```
<paste task.md here>
```

## 8. Key Implementation Decisions
<Decisions made during implementation that are NOT in plan.md but affect remaining work.
Examples: a library was swapped, a schema field was added, an endpoint was renamed,
a test was deferred, a third-party API behaved differently than documented.>

- <decision 1>
- <decision 2>

## 9. Open Blockers & Pending Human Decisions
<Anything that was stopped or deferred that needs resolution before or during next phase.
If none, write "None".>

- <blocker or pending item 1>

## 10. Next Action for Hermes (Resume From Here)
<Exact instruction — what Hermes does immediately after reading this file.
Be specific: which step, which phase, which task, what command to run first.>

Example:
"Resume Step 4, Phase 2 (Authentication). Open skills/phase-implementation/SKILL.md
and begin with task: 'implement POST /auth/login endpoint'. Run unit tests after each
function. Reference plan.md Section 15 for TC-006 through TC-010."

---
*Resume prompt for a new Hermes session:*
```
Read HERMES-MANUAL.md, SESSION-STATE.md, plan.md, and task.md in this folder.
Resume from the "Next Action" in Section 10 of SESSION-STATE.md.
Do not ask me to repeat anything already documented — treat SESSION-STATE.md as the
authoritative record of what has happened and what comes next.
```
```

---

## When to Compress — Decision Rules

| Condition | Action |
|---|---|
| Phase just completed, all tasks checked off in task.md | Auto-compress before starting next phase |
| Human says "compress context" or "/compress" | Compress immediately, stay in same session |
| Loop Engineering blocker hit (5 iterations) | Compress before stopping to report to human — so resume is clean |
| Very long debug session (many tool calls visible) | Compress when the current task passes validation |

---

## After Writing SESSION-STATE.md

1. Confirm to the human: *"Context compressed. SESSION-STATE.md written to project root. You can start a new Hermes session with the resume prompt in Section 10, or continue in this session — your choice."*
2. Do NOT end the session yourself. Let the human decide whether to continue or start fresh.
3. If continuing in the same session: proceed with the next action as documented in Section 10.

---

## Resume Prompt (Copy-Paste Ready)

Give this to a fresh Hermes session to resume:

```
Read HERMES-MANUAL.md, SESSION-STATE.md, plan.md, and task.md in this folder.
Resume from the "Next Action" in Section 10 of SESSION-STATE.md.
Do not ask me to repeat anything already documented — treat SESSION-STATE.md as the
authoritative record of what has happened and what comes next.
Follow HERMES-MANUAL.md exactly for all remaining steps.
```
