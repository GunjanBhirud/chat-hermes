> Reference file for the `frontend-development` skill. Sections are numbered §1–§38 and referenced by number from `SKILL.md`. Section 37 is "Appendix C" (Production Readiness Checklist) referenced from the skill's Step 12 gate.

# Frontend Development Best Practices
### A Technology-Agnostic Guide to Production-Grade Frontend Engineering

> Applies regardless of framework (React, Vue, Angular, Svelte, etc.). Choose technology based on requirements — not popularity. Don't blindly reuse a previous project's architecture; derive decisions from the current product's requirements.

---

## 1. Analyze Before Building

Before writing code, study the PRD, design docs, API contracts, user stories, and wireframes. Understand:

- Users, roles, and journeys
- Features, pages, navigation, workflows
- Forms, tables, dashboards, notifications
- Auth requirements, real-time needs
- Loading/error/empty states, responsive & accessibility needs

**Do not start implementation until requirements are understood.**

---

## 2. Requirements → Feature Map

Trace every feature through this chain:

```
Feature → User Flow → Page → Components → API Dependencies
    → State → Validation → Loading/Error/Empty States → Permissions
```

Derive pages and components from the PRD — don't assume a standard set (Login, Dashboard, Settings, etc.) exists without confirming it.

---

## 3. Frontend Development Plan

Before major implementation, produce a plan document covering: product understanding, architecture, project structure, component architecture, design system, state management, API layer, auth/authz, forms, error handling, responsive design, accessibility, performance, security, testing, CI/CD, deployment, implementation phases, risks/trade-offs, and a production readiness checklist.

---

## 4. Technology Selection

Evaluate: framework, language, build tool, styling, component library, state management, data-fetching layer, form/validation libraries, routing, testing/E2E frameworks, charting, a11y tooling, linting.

For each major choice, document **why**, alternatives considered, and trade-offs (performance, maintainability). Use the minimum technology necessary — avoid unnecessary dependencies.

---

## 5. Project Structure

Choose structure based on complexity — feature-oriented for larger apps:

```
src/
├── app/
├── features/
│   └── feature-a/
│       ├── components/
│       ├── pages/
│       ├── hooks/
│       ├── api/
│       ├── state/
│       ├── schemas/
│       └── types/
├── components/
├── layouts/
├── routes/
├── services/
├── lib/
├── hooks/
├── utils/
├── config/
├── styles/
└── types/
```

Avoid giant component/utility folders, circular dependencies, feature coupling, and business logic in presentation components.

---

## 6. Component Architecture

```
Page → Feature → Container → Presentation Component → Primitive UI
```

Avoid oversized components, unrelated business logic mixed in, excessive prop drilling, duplicated UI, and over-abstraction. Each component should have one clear responsibility.

---

## 7. Design System

Define consistently:

- **Typography** — family, sizes, weights, line heights, heading hierarchy
- **Colors** — semantic tokens (`primary`, `secondary`, `success`, `warning`, `error`, `info`, `background`, `surface`, `text`, `border`, `disabled`)
- **Spacing** — a consistent scale
- **Components** — Button, Input, Select, Checkbox, Modal, Drawer, Dropdown, Tabs, Table, Pagination, Badge, Alert, Toast, Card, Skeleton, Spinner, Empty/Error states

Don't let every page invent its own visual language.

---

## 8. UI/UX Best Practices

Good UI/UX is a first-class engineering concern, not a polish pass at the end.

**Usability heuristics**
- Visibility of system status — always show what's happening (progress, saved state, connection status)
- Consistency — same action always looks and behaves the same way across the app
- Recognition over recall — don't make users remember information across screens
- Minimize user effort — sensible defaults, autofocus, autofill, smart pre-selection
- Error prevention — confirm destructive actions, disable invalid submissions before they happen

**Visual hierarchy & layout**
- Guide the eye with size, weight, spacing, and color — the most important action or information should be the most visually prominent
- Group related elements; separate unrelated ones with whitespace, not just borders
- Align to a consistent grid; avoid arbitrary spacing values
- Limit the number of competing calls-to-action per screen

**Interaction & feedback**
- Every user action gets immediate, visible feedback (hover, active, pressed, focus states)
- Distinguish disabled vs. loading vs. error states clearly — never leave a control ambiguously unresponsive
- Use optimistic UI updates only when failure can be gracefully rolled back
- Micro-interactions (transitions, subtle animation) should clarify state changes, not decorate — respect `prefers-reduced-motion`

**Navigation & information architecture**
- Users should always know where they are, how they got there, and how to go back
- Keep primary navigation shallow; avoid deeply nested menus for frequent tasks
- Breadcrumbs, active-state indicators, and clear page titles for orientation

**Content & microcopy**
- Write clear, action-oriented labels ("Delete project" not "Submit")
- Error messages explain what went wrong and how to fix it — never just "Something went wrong"
- Avoid jargon; match the user's vocabulary, not the internal data model

**Confirmation & destructive actions**
- Require explicit confirmation for irreversible actions (delete, remove access, cancel subscription)
- Offer undo where feasible instead of a confirmation dialog, when the cost of a mistake is recoverable

**Onboarding & empty states**
- First-run experiences should orient new users without blocking them
- Empty states explain what belongs there and offer a clear next action — not just "No data"

**Consistency with platform conventions**
- Follow established patterns for the platform (web, iOS, Android) so the app behaves the way users already expect
- Don't reinvent standard interactions (scrolling, form controls, keyboard shortcuts) without strong justification

**Validate with users, not assumptions**
- Usability-test critical flows where possible
- Use analytics/heatmaps/session replay to find friction points, then iterate
- Treat UX debt (confusing flows, inconsistent patterns) as seriously as technical debt

---

## 9. Responsive Design

Design mobile-first or responsive per requirements — don't just shrink desktop layouts. Define breakpoints and explicit behavior for navigation, tables, forms, modals, and sidebars. Test key workflows across viewport sizes.

---

## 10. Accessibility

Mandatory — target **WCAG 2.2 AA** where practical:

- Semantic HTML, keyboard navigation, visible focus states
- Screen-reader labels, accessible forms/dialogs/tables
- Color contrast, reduced-motion support
- ARIA only where semantic HTML isn't enough — never as a substitute for it

---

## 11. State Management

Classify and separate state types:

| State Type | Example | Typical Home |
|---|---|---|
| Local UI | Modal open/close | Component state |
| Server | API data | Data-fetching layer |
| Global App | Theme | Persistent/global store |
| URL | Search/filters | URL state |
| Form | Field values | Form state |
| Session | Auth | Session/auth state |

Use the simplest solution for each — avoid dumping everything into global state.

---

## 12. API / Data Layer

Centralize API access — don't scatter fetch calls through components. The data layer should handle requests, auth headers, response parsing, error handling, retries, cancellation, caching, invalidation, and pagination.

---

## 13. API Contract

Treat the backend API as a contract: define request/response/error types, pagination shapes, enums, DTOs. Generate types from an API spec where possible instead of duplicating them manually.

---

## 14. Authentication

Design per actual requirements: login/logout, session expiration, token refresh, SSO/OAuth/OIDC, MFA, password reset, session persistence. Never store sensitive auth data insecurely, and avoid exposing tokens to JavaScript when a safer browser mechanism exists.

---

## 15. Authorization

Frontend authorization is **UX control, not security**:

```
User → Role → Permission → Feature Access → UI Visibility
```

Support route protection, feature/action visibility, disabled states, permission-aware navigation — but always assume the backend performs the real check.

---

## 16. Form Engineering

Support client-side and server-side validation, field- and form-level errors, async validation, loading/submission states, and unsaved-changes handling. Prevent double submission, invalid payloads, lost form data, and poor error feedback.

---

## 17. Loading / Error / Empty States

Every data-driven screen must explicitly handle: loading, success, empty, error, partial data, retry, permission denied, and offline/network failure. Use skeletons, loading indicators, empty-state messaging, retry actions, and error boundaries — never leave a blank screen.

---

## 18. Performance

**Initial load:** code splitting, lazy loading, tree shaking, asset optimization, compression, caching, critical rendering path.

**Runtime:** avoid unnecessary re-renders, expensive per-render calculations, large component trees, duplicate API calls, memory leaks. Use memoization, virtualization, debouncing, throttling, and request cancellation appropriately.

**Measure before and after — don't optimize blindly.**

---

## 19. Large Datasets

Avoid rendering thousands of DOM nodes. Use server-side pagination/cursor pagination, virtual scrolling, lazy/incremental rendering, and server-side filtering/sorting. Debounce search inputs; throttle expensive operations.

---

## 20. Browser & Network Performance

Optimize JS/CSS bundle size, images, fonts, API payload size, and caching/compression. Avoid duplicate API calls, oversized payloads, loading all data at startup, and loading unused components.

---

## 21. Security

Guard against XSS, CSRF, token leakage, open redirects, clickjacking, vulnerable dependencies, unsafe HTML rendering, sensitive data exposure, and malicious file uploads. Never render unsafe HTML without proper sanitization, and never ship secrets in frontend source.

> Anything shipped to the browser must be treated as publicly accessible.

---

## 22. Error Boundaries & Resilience

One feature failing shouldn't crash the whole app. Use error boundaries, feature-level fallback UI, retry mechanisms, network recovery, request cancellation, and offline handling where appropriate.

---

## 23. Real-Time Features

If required, choose among WebSockets, Server-Sent Events, polling, or event streams based on actual need. Handle connection loss, reconnect/backoff, duplicate events, ordering, auth, and cleanup.

---

## 24. Routing

Support nested/protected/lazy-loaded routes, route-level permissions, 404/error routes, deep linking, and URL state. Don't keep state only in memory if it needs to survive refresh or navigation.

---

## 25. SEO

For public-facing apps: metadata, titles/descriptions, Open Graph, structured data, sitemap, robots, and SSR/SSG where beneficial. For authenticated enterprise apps, explicitly document that SEO is not required.

---

## 26. Internationalization

Design for i18n from the start if multi-language support is possible — avoid hardcoding user-facing text. Consider translations, date/number/currency formatting, pluralization, and RTL. Only fully implement i18n when the product requires it.

---

## 27. Date / Time / Currency

Never assume timezone, locale, currency, or date format — handle explicitly per requirements, and avoid browser/server timezone inconsistencies.

---

## 28. File & Media Handling

Handle upload progress, size/type validation, retry, cancellation, preview, error states, and secure downloads. Don't load large files entirely into browser memory unnecessarily.

---

## 29. Testing Strategy

| Level | Focus |
|---|---|
| Unit | Utilities, hooks/composables, business rules, validation |
| Component | User interaction, forms, loading/error states, permissions, a11y |
| Integration | Feature workflows, API integration, auth, state transitions |
| E2E | Login, core workflows, CRUD, authorization, logout, critical processes |

Prioritize critical business logic and user journeys over chasing 100% coverage.

---

## 30. Code Quality

Use linting, formatting, static analysis, type checking, dependency and complexity checks. Avoid unsafe types (`any`), giant components, duplicate/dead code, magic numbers, and hardcoded config.

---

## 31. Build & Environment Management

Separate development, testing, staging, and production configs. Never expose secrets, and never assume build-time configuration is secret.

---

## 32. CI/CD

At minimum: install, lint, format check, type check, unit tests, component tests, build, security/dependency scan, and E2E tests for critical workflows. Broken builds must not reach production.

---

## 33. Browser Compatibility

Define supported browsers based on real requirements; test responsive layouts, keyboard interaction, and key workflows on them. Don't support obsolete browsers without a business reason.

---

## 34. Documentation

Maintain (only where they add real value): `FRONTEND_DEVELOPMENT_PLAN.md`, `FRONTEND_ARCHITECTURE.md`, `FRONTEND_COMPONENT_GUIDELINES.md`, `FRONTEND_TESTING_GUIDELINES.md`.

---

## 35. Recommended Implementation Order

```
1. Project setup            10. Feature implementation
2. Architecture             11. Forms/validation
3. Design system            12. Error/loading/empty states
4. Application shell        13. Responsive behavior
5. Routing                  14. Accessibility
6. Authentication           15. Performance optimization
7. Authorization            16. Testing
8. API/data layer           17. Security review
9. Shared components        18. Production build validation
```

Adjust order to fit actual project needs.

---

## 36. Don't Overengineer

Don't automatically introduce micro-frontends, global state, multiple UI libraries, heavy design systems, SSR, WebSockets, service workers, offline mode, or advanced caching unless the requirements justify them.

> **Use the simplest architecture that reliably satisfies requirements and scales with the product.**

---

## 37. Production Readiness Checklist

**Architecture**
- [ ] Clear feature boundaries, maintainable structure, no unnecessary abstractions or circular dependencies

**UI/UX**
- [ ] Consistent design system, responsive, loading/empty/error states, confirmation flows, user feedback

**Performance**
- [ ] Bundle analyzed, renders minimized, API calls optimized, large lists optimized, assets optimized, lazy loading applied

**Security**
- [ ] No frontend secrets, safe HTML rendering, secure auth handling, permission-aware UI, dependencies checked

**Accessibility**
- [ ] Keyboard navigation, focus management, semantic HTML, screen-reader support, contrast, accessible forms

**Testing**
- [ ] Unit, component, integration, critical E2E, and accessibility checks

**Production**
- [ ] Production build succeeds, environment config verified, CI passes, error monitoring considered, performance validated, deployment strategy documented

---

## 38. Guiding Principles

1. Read the PRD before designing the frontend.
2. Don't assume the technology stack.
3. Don't copy an old project's architecture blindly.
4. Create the frontend plan before major implementation.
5. Document architectural decisions and trade-offs.
6. Derive pages and features from requirements, not assumptions.
7. Keep components maintainable and reusable.
8. Keep server state separate from UI state.
9. Treat APIs as contracts.
10. Design loading, empty, and error states from the beginning.
11. Accessibility is part of implementation, not a final patch.
12. Performance is measured, not guessed.
13. Frontend authorization never replaces backend authorization.
14. Never put secrets in frontend code.
15. Don't overengineer.
16. Prefer simple solutions when they satisfy requirements.
17. Test critical user journeys.
18. Review security before production.
19. Review performance before production.
20. Don't declare production readiness without completing the final checklist.

---

### Final Objective

```
PRD → Requirements Analysis → User Journeys → Feature Map → Technology Evaluation
    → Frontend Architecture → Development Plan → Implementation → Testing
    → Performance Optimization → Security Review → Accessibility Review
    → Production Readiness Review → Production-Ready Frontend
```

The result must be **maintainable, scalable, performant, secure, accessible, responsive, testable, observable, and production-ready** — without unnecessary complexity.
