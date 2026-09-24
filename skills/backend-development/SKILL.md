---
name: backend-development
description: Use whenever writing, reviewing, or refactoring backend/server-side code during implementation (Step 4) — enforces technology-agnostic production-grade best practices across architecture, API design, database engineering, transactions/concurrency, caching, security, auth, error handling, observability, resilience, performance, and deployment.
---

# Backend Development Best Practices
### A Technology-Agnostic Guide to Production-Grade Backend Engineering

> Applies regardless of language, framework, database, or cloud provider. Choose technology based on requirements — not popularity.

---

## 1. Analyze Before Coding

Before writing or changing code, inspect the existing system and document:

- Current architecture, stack, and integrations
- Database design, API design, auth model
- Deployment, CI/CD, infrastructure, monitoring, config
- Existing tests and security controls

Then produce a short risk assessment covering:

| Category | What to Look For |
|---|---|
| Performance | Slow paths, unbounded queries, blocking calls |
| Security | AuthN/AuthZ gaps, injection surfaces, secret handling |
| Scalability | Stateful assumptions, single points of failure |
| Reliability | Missing timeouts/retries, no failure handling |
| Database | Poor indexing, N+1 patterns, missing constraints |
| Operations | Logging, observability, deployment gaps |
| Technical Debt | Duplicated logic, tight coupling, dead code |

**Do not start coding until this analysis is complete.**

---

## 2. Choose the Right Architecture

Pick the **simplest** architecture that satisfies real requirements — don't default to microservices.

Options: monolith, modular monolith, microservices, event-driven, serverless, hybrid.

Evaluate against: expected traffic, team size, data boundaries, failure isolation needs, operational complexity, cost, and development speed. Document the trade-offs explicitly.

---

## 3. Clean Architecture & Code Organization

Maintain clear layering:

```
API / Transport Layer
        ↓
Application / Service Layer
        ↓
Domain / Business Logic
        ↓
Data Access Layer
        ↓
Infrastructure
```

**Avoid:** business logic in controllers, god objects, circular dependencies, global mutable state, tight coupling, hardcoded config, unnecessary abstraction layers.

**Apply intelligently:** SOLID, separation of concerns, dependency inversion, DRY, KISS, YAGNI.

---

## 4. API Design

- Consistent resource naming and correct HTTP/RPC semantics
- Request/response validation
- Pagination (offset, cursor, or keyset — chosen by workload), filtering, sorting, search
- Versioning, idempotency, request/correlation IDs
- Timeouts and rate limiting
- Consistent error response shape
- Never expose internal implementation details
- **Never return unlimited records from a collection endpoint**

---

## 5. Database Engineering

Analyze schema design, query patterns, read/write ratio, data volume/growth, consistency and transaction requirements.

**Avoid:**
- N+1 queries, `SELECT *`, queries inside loops
- Full-table scans and unbounded queries
- Loading large datasets into memory
- Unnecessary joins

**Use where appropriate:**
- Indexes and composite indexes (only after weighing read gains vs. write/storage cost)
- Query projections, pagination, batch/bulk operations
- Partitioning, read replicas, connection pooling
- `EXPLAIN` / `EXPLAIN ANALYZE` or equivalent before optimizing

---

## 6. Transactions & Concurrency

Handle race conditions, lost updates, duplicate requests, concurrent writes, deadlocks, and lock contention using:

- Transactions (kept short)
- Optimistic or pessimistic locking
- Atomic operations and unique constraints
- Idempotency keys
- Distributed locks — only when truly required

**Never rely solely on application-level validation for data integrity.**

---

## 7. Connection Management

Pool and manage lifecycle for every external resource (DB, HTTP, cache, broker).

Configure: pool size, max connections, timeouts, idle timeout, connection lifetime, retry behavior.

Prevent: connection leaks, pool exhaustion, unbounded connections.

---

## 8. Caching

Only cache if it provides clear value. Design explicitly for:

- Strategy (cache-aside, write-through, write-behind, read-through)
- Cache key structure and TTL
- Invalidation and consistency
- Eviction policy
- Failure behavior and stampede protection

**Never cache without an invalidation strategy.**

---

## 9. Background Processing

Move out of the request path: large data processing, emails/notifications, report generation, file processing, long integrations, ML jobs, scheduled/cleanup tasks.

Implement: retry policy with exponential backoff, job timeouts, idempotency, dead-letter handling, status tracking, failure recovery. Avoid infinite retries and retry storms.

---

## 10. Asynchronous & Concurrent Processing

Use async/concurrency where it adds real value (I/O-bound work, parallelizable CPU work, streaming). Don't add complexity without justification. Never let blocking operations stall the main request path.

---

## 12. Rate Limiting & Abuse Protection

Apply targeted limits to: login, password reset, public APIs, expensive operations, file uploads, search, and AI/compute-heavy endpoints. Support **distributed** rate limiting across multiple instances.

---

## 13. Security (Defense in Depth)

Core controls: authentication, authorization (RBAC/ABAC), input/output validation, secure password storage, token/session security, encryption, secrets management, secure headers, CORS, CSRF/SSRF protection, file upload security, request size limits, dependency scanning.

**Guard against:** SQL/NoSQL injection, XSS, CSRF, SSRF, IDOR, privilege escalation, auth bypass, path traversal, command injection, insecure deserialization.

Never store secrets in source code or expose them in logs.

---

## 14. Authentication & Authorization

Every protected operation validates the full chain:

```
Identity → Authentication → Tenant/Org → Role/Permission → Resource Access
```

Prevent privilege escalation, cross-user/cross-tenant access, and IDOR. **Frontend checks are never sufficient security** — enforce everything server-side.

---

## 16. Error Handling

Centralize error handling with a consistent shape:

```json
{
  "success": false,
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Resource not found",
    "request_id": "abc123"
  }
}
```

Never leak stack traces, internal paths, raw DB errors, SQL, secrets, or infra details to clients — log the details internally instead.

---

## 17. Logging

Structured logs per request: timestamp, request ID, trace ID, method, endpoint, status, latency, service, environment, user/tenant ID where relevant.

**Never log:** passwords, access/refresh tokens, API keys, secrets, sensitive PII.

---

## 19. External Service Resilience

For every external dependency: connection/read/overall timeouts, retry with exponential backoff, circuit breakers, rate-limit handling, connection pooling. Never let a dependency hang the app indefinitely, and never blindly retry non-idempotent operations.

---

## 20. Reliability & Failure Handling

Design explicitly for: DB/cache/broker/API unavailability, network timeouts, crashes/restarts, duplicate requests, partial failures, dependency overload, disk failure.

Use: timeouts, retries, circuit breakers, fallbacks, idempotency, dead-letter queues, graceful degradation, backpressure.

---

## 21. Performance Engineering

Measure before optimizing: CPU, memory, DB/query latency, network latency, serialization cost, cache performance, queue latency, external API latency. Track req/sec and p50/p95/p99 for critical endpoints.

---

## 22. Memory & Resource Management

Prevent memory leaks, unbounded collections/caches, large in-memory datasets, file descriptor and connection leaks. Use streaming, pagination, chunked processing, resource limits, TTLs, and proper cleanup.

---

## 23. File Handling

Enforce max file size, allowed types, content validation, secure filenames, path-traversal protection, malware scanning where required, streaming, object storage, access control, and signed URLs. **Never trust client-provided filenames or MIME types.**

---

## 24. Configuration

Externalize config per environment (dev/test/staging/prod). Validate required config at startup. Never hardcode passwords, API keys, tokens, credentials, or environment URLs.

---

## 25. Containerization & Deployment

If containerized: minimal images, multi-stage builds, non-root execution, health checks, graceful shutdown, resource limits, reproducible builds, vulnerability scanning.

If orchestrated (e.g., Kubernetes): scaling, health probes, resource requests/limits, rolling deployments, isolation, autoscaling, disruption handling, security context. **Don't assume Kubernetes is required.**

---

## 26. Graceful Shutdown

```
Stop accepting new work → Finish active work → Stop background processing
    → Close connections → Flush telemetry/logs → Exit cleanly
```

---

## 27. Database Migrations

Manage all schema changes through migrations, accounting for backward compatibility, large tables, lock duration, deployment order, and rollback strategy. Never apply unsafe schema changes blindly.

---

## 28. Testing Strategy

| Level | Focus |
|---|---|
| Unit | Business logic, services, validation, security logic |
| Integration | Database, cache, queues, external integrations, transactions |
| API | Auth, validation, pagination, filtering, error handling, rate limits |
| Security | Unauthorized access, privilege escalation, IDOR, tenant isolation, injection, tokens |
| Performance | Concurrent users, req/sec, p50/p95/p99, error rate, resource usage |

---

## 29. CI/CD

Automate: formatting, linting, static analysis, type checking, unit/integration tests, security & dependency scanning, build verification, migration verification, container scanning. Critical failures must block deployment.

---

## 30. Dependency Management

For every dependency ask: Is it necessary? Is there an existing solution? Is it maintained? Does it add security risk or complexity? Remove unused dependencies; upgrade on a controlled schedule.

---

## 31. Documentation

Keep accurate, current docs for: APIs, auth, configuration, database, deployment, environment variables, background jobs, architecture, and operational procedures.

---

## 32. Production Readiness Checklist

**Architecture**
- [ ] Right-sized architecture, clear boundaries, no unnecessary complexity/microservices

**Database**
- [ ] Optimized queries, reviewed indexes, no N+1, pooling, reviewed transactions, migration strategy

**API**
- [ ] Validation, pagination, error handling, rate limiting, idempotency, timeouts

**Security**
- [ ] AuthN/AuthZ, RBAC/ABAC, tenant isolation, secrets management, input validation, security testing

**Performance**
- [ ] Query optimization, justified caching, efficient serialization, async/background work, resource limits

**Reliability**
- [ ] Retries, timeouts, circuit breakers, graceful degradation, idempotency, failure recovery

**Scalability**
- [ ] Horizontal scaling, load balancing, statelessness, connection limits, backpressure, autoscaling

**Observability**
- [ ] Structured logging, metrics, health checks, trace IDs, distributed tracing, alerting

**Testing**
- [ ] Unit, integration, API, security, and performance tests

---

## 33. Development Workflow

1. **Analyze** — inspect the system; no code changes yet. Document architecture, stack, DB, API, deployment, security, performance, risks.
2. **Design** — propose the production architecture and justify every technology choice.
3. **Implement** — incrementally, running build/lint/static analysis/tests/security checks after each major change.
4. **Optimize** — hunt for N+1s, slow/unbounded queries, missing indexes, blocking calls, memory issues, connection leaks, race conditions, retry storms.
5. **Production Review** — final audit; report remaining critical, high, and medium-risk issues plus technical debt without hiding anything.

---

## 34. Guiding Principles

1. Requirements first, technology second.
2. Prefer simplicity over unnecessary complexity.
3. Measure before optimizing.
4. Security must be enforced server-side.
5. Design for failure.
6. Avoid single points of failure where redundancy is justified.
7. Keep applications stateless where practical.
8. Use database constraints for data integrity.
9. Never trust client input.
10. Never expose secrets.
11. Don't introduce infrastructure without a clear reason.
12. Don't blindly copy architectural patterns.
13. Every scalability decision needs a reason.
14. Every performance optimization must be measurable.
15. Every retry must consider idempotency.
16. Every cache must have an invalidation strategy.
17. Every external dependency needs a timeout.
18. Every critical operation should be observable.
19. Every production system needs a failure strategy.
20. The result must be maintainable by another team.

---

### Final Objective

Build a backend that reliably operates under normal and high traffic, concurrent load, database strain, external service failures, instance/network failures, partial outages, security attacks, data growth, rolling deployments, and horizontal scaling — driven by actual requirements, not a predetermined stack.
