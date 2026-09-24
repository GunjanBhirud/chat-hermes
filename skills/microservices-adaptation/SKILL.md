---
name: microservices-adaptation
description: Use instead of the single-plan.md flow when the application is split into multiple independently-owned services. Contains the SYSTEM-PLAN.md template and per-service binding/contract-testing/deployment rules (Step 10).
---

## Step 10 — Microservices Adaptation

Use this instead of the single-`plan.md` flow when the application is split into multiple services, each owned by a different developer (and possibly a different Hermes session).

**Folder structure:**
```
project-root/
  SYSTEM-PLAN.md
  service-<name-a>/
    prd.md
    plan.md
    docs/
  service-<name-b>/
    prd.md
    plan.md
    docs/
```

### 10.1 Create `SYSTEM-PLAN.md` First (before any service-level work)

Before any developer starts on an individual service, generate `SYSTEM-PLAN.md` using the template in **Appendix D** — which is located further down in **this same file** (`skills/microservices-adaptation/SKILL.md`), under the heading `# APPENDIX D — SYSTEM-PLAN.md Template (Microservices)`. Read the entire file to reach it. The template has 11 numbered sections: System Overview, Service Inventory, Service Boundaries & Data Ownership, Communication Patterns, Inter-Service API Contracts, Authentication & Authorization Between Services, Shared Standards, Deployment Topology, Failure & Degradation Across Services, Contract Change Process, and Open Questions.

This is the cross-service equivalent of `plan.md` Sections 5–8 — it defines what each service owns, how they communicate, and what contracts they must not silently break.

`SYSTEM-PLAN.md` goes through the **same Human Review Gate as Step 3** — do not let any service's `plan.md` be written until `SYSTEM-PLAN.md` is approved.

### 10.2 Each Service's `plan.md` Is Bound to `SYSTEM-PLAN.md`

- Each service still gets its own full `plan.md` (Appendix A), generated and approved via Steps 1–3, scoped to that service's `prd.md`.
- Section 7 (API Contract) of a service's `plan.md` **must match** what `SYSTEM-PLAN.md` says that service is allowed to expose and consume.
- If implementing a service reveals a need to change a shared interface: **stop**, update `SYSTEM-PLAN.md` first, get it re-approved by the human, then update the affected services' `plan.md` files. Never change a cross-service contract quietly from inside one service's own plan.

### 10.3 Contract Testing (mandatory addition to Section 14)

For every service, add a **Consumer-Driven Contract Tests** category to `plan.md` Section 14:
- The service tests its own implementation against the contract `SYSTEM-PLAN.md` says it must expose (as a provider).
- The service tests against a mock of each dependency's published contract (as a consumer).
- Add corresponding test cases to Section 15 with `Type = Contract` and note which other service the contract is with.

### 10.4 Git/CI/CD, Per Service

- Each service keeps its own repo or its own top-level folder in a monorepo, with its own branch protection and CI pipeline (Step 7's policy applies per-service).
- Add one extra CI job per service: run its contract tests against the **currently deployed** version of the services it depends on, before promoting that service to production.

### 10.5 Multi-Developer Merge Within a Service

Step 5's merge-readiness loop still applies **within a single service** if more than one person works on it. Across services, coordination happens through `SYSTEM-PLAN.md`, not through git merges.

### 10.6 Deployment & Verification, Per Service

- Each service deploys independently (Step 8), but its post-deployment verification must also include a **contract check against live dependent services**.
- Give the human the URL/endpoint for each service deployed, plus a one-line summary of which contracts were verified against which dependencies.

### Prompt to Use — Starting a Microservices Project

```
This project is a microservices application with the following services:
<list service names and one-line purpose for each>

Before any service-level work:
1. Create SYSTEM-PLAN.md using Appendix D of HERMES-MANUAL.md.
2. Present it to me for approval — do not start any service's plan.md yet.

Once SYSTEM-PLAN.md is approved, for each service:
3. Create <service-folder>/plan.md per Appendix A.
4. Add Consumer-Driven Contract Tests to that service's Section 14/15.
5. Present each service's plan.md to me for approval before implementing it.

If at any point building one service requires changing an interface another
service depends on, stop and tell me — update SYSTEM-PLAN.md and get my
approval before changing any service's plan.md.
```

# APPENDIX D — SYSTEM-PLAN.md Template (Microservices)

# SYSTEM-PLAN.md

## 1. System Overview
- What the overall system does
- Why it's split into services (not just "because microservices")

## 2. Service Inventory
| Service Name | Owner/Developer | Purpose | Repo/Folder |
|---|---|---|---|

## 3. Service Boundaries & Data Ownership
- What each service owns (its own database/data — no shared DB access across services)
- What each service must NOT do

## 4. Communication Patterns
- Synchronous (REST/gRPC) vs. asynchronous (events/queue) — which services use which, and why
- Message broker / event bus (if used) and its topics/queues

## 5. Inter-Service API Contracts
| Provider Service | Consumer Service(s) | Contract (endpoint/event) | Schema/Payload | Versioning Policy |
|---|---|---|---|---|

## 6. Authentication & Authorization Between Services
- How services authenticate to each other (mTLS, service tokens, API keys, etc.)
- How a request's original user identity/permissions propagate across service calls

## 7. Shared Standards
- Common error response format across all services
- Common logging/tracing format
- Common versioning scheme for APIs and events

## 8. Deployment Topology
- Where each service runs (containers, orchestration, regions)
- Service discovery mechanism
- Independent deployability confirmed

## 9. Failure & Degradation Across Services
- What happens to Service A if Service B is down
- Timeout and retry policy for inter-service calls
- Circuit breaker strategy

## 10. Contract Change Process
- How a breaking change to a shared contract must be proposed, reviewed, and rolled out
- Which services must approve a change to a contract they consume

## 11. Open Questions
- Question 1
- Question 2
