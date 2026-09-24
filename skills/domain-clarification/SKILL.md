---
name: domain-clarification
description: Use immediately before implementation starts, to surface domain-specific thresholds, retention rules, caps, or policy defaults not stated in prd.md and get them clarified by the human (Step 3.2).
---

## Step 3.2 — Domain & Operational Parameters Clarification Gate (MANDATORY)

Immediately prior to starting Step 4 implementation, Hermes must inspect the planned system entities and operational features to identify any domain-specific business thresholds, retention rules, resource caps, or policy defaults that were not explicitly stated in `prd.md`.

- **Proactive Clarification:** Present these specific domain choices to the human in a single, structured question list (e.g. data retention horizons, operational thresholds, capacity/resource limits, default system timeouts, or policy constants relevant to the application domain).
- **Incorporate Answers:** Apply the human's specified operational parameters across configuration files, environment variables, validation schemas, and database default constraints before writing core feature code.
