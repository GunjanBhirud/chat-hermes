---
name: frontend-development
description: Use for any frontend engineering work — building a new UI, planning a frontend architecture, reviewing/refactoring existing frontend code, or auditing a web app for production readiness. Technology-agnostic (React, Vue, Angular, Svelte, or plain HTML/CSS/JS). Trigger whenever the user asks to build, plan, review, or improve a website, web app, component library, design system, or any frontend/UI codebase — even if they only say "build me a dashboard" or "make this page" without naming this skill.
---

# Frontend Development

A production-grade, technology-agnostic frontend engineering workflow. Modeled on the Hermes SDLC skill pattern (propose → validate → diagnose → refine → converge, human review gates, checkable task lists) and specialized for frontend work end to end: requirements → architecture → design system → implementation → testing → performance → accessibility → security → production readiness.

**Core rule:** choose technology and architecture from the actual requirements in front of you. Don't default to whatever stack you used last time, and don't reach for a library when a native platform feature does the job.

## When to go deep vs. go light

- A quick component, a one-off page, a bug fix → skim Step 1 and Step 6 (design system tokens) and just build it well.
- A new app, feature area, or anything with forms/auth/data-tables/real-time → run the full workflow below.
- A review/audit request ("is this production ready?", "review my frontend") → jump straight to Appendix C (Production Readiness Checklist) in `references/best-practices.md` and grade the codebase against it.

## Workflow

### Step 1 — Analyze Before Building
Read the PRD, design docs, API contracts, user stories, wireframes — whatever exists. Identify users/roles/journeys, pages, forms/tables/dashboards, auth needs, real-time needs, and required loading/error/empty/responsive/a11y states. **Do not start implementing until this is understood.** If requirements are missing or ambiguous, ask — don't assume a "standard" set of pages (Login, Dashboard, Settings...) exists without confirming it.

### Step 2 — Requirements → Feature Map
For every feature, trace: `Feature → User Flow → Page → Components → API Dependencies → State → Validation → Loading/Error/Empty States → Permissions`. This map is what later steps (component architecture, state, testing) get derived from — don't skip it even for small features.

### Step 3 — Frontend Development Plan (Human Review Gate)
For anything beyond a trivial change, write a short plan covering: architecture, project structure, component architecture, design system, state management, API layer, auth/authz, error handling, responsive & accessibility approach, performance approach, security approach, testing strategy, and implementation phases. Present it before writing significant code — for a solo quick task this can be a few sentences; for a real feature or app, treat it as a blocking checkpoint: get explicit sign-off before building.

### Step 4 — Technology Selection
Evaluate framework, styling approach, component library, state management, data-fetching layer, forms/validation, routing, testing/E2E, and a11y tooling against the actual requirements — not habit or popularity. For each non-trivial choice, note *why* and what trade-off it accepts. Use the minimum technology necessary. Check `references/modern-stack-2026.md` for current framework/tooling defaults (Next.js, Tailwind v4, TanStack Query, Zustand, Vitest/Playwright, etc.) and `references/component-libraries.md` for a full comparison of installable component libraries (HeroUI, MUI, Ant Design, Mantine, Chakra UI, Base UI, React Aria) versus the shadcn copy-in approach, before defaulting to whatever was used last time.

### Step 5 — Project Structure & Component Architecture
Pick a structure sized to complexity (feature-oriented for larger apps — see `references/best-practices.md` §5 for the canonical layout). Components follow `Page → Feature → Container → Presentation Component → Primitive UI`, each with one clear responsibility. Avoid giant components, prop-drilling chains, duplicated UI, and business logic leaking into presentation components.

### Step 6 — Design System (Tokens + Components)
Before building screens, fix: typography scale, a semantic color token set (`primary`, `secondary`, `success`, `warning`, `error`, `info`, `background`, `surface`, `text`, `border`, `disabled`), and a spacing scale. Reuse a base component set (Button, Input, Select, Modal, Table, Toast, Card, Skeleton, Empty/Error states, etc.) rather than letting each screen invent its own visual language. **Don't design tokens from scratch if you don't have to** — see `references/design-references.md` for Google's Material Design 3 and a curated list of production, open-source design systems to borrow token structure, component APIs, and interaction patterns from. If the stack is React/Next.js + Tailwind, see `references/shadcn-references.md` for the full shadcn/ui copy-in component ecosystem (core primitives + free open-source registries like Magic UI, Aceternity, Origin UI, ReUI) instead of hand-building components from scratch.

### Step 7 — UI/UX, Responsive & Accessibility
Apply the usability heuristics, visual hierarchy, feedback/interaction, and content-writing rules in `references/best-practices.md` §8 as you build, not as a polish pass. Design mobile-first or responsive per requirements with explicit breakpoint behavior. Target **WCAG 2.2 AA**: semantic HTML first, ARIA only where semantic HTML falls short, visible focus states, full keyboard operability, and `prefers-reduced-motion` support.

### Step 8 — State, Data Layer & API Contract
Classify state (local UI / server / global app / URL / form / session) and put each in the simplest home that fits — don't dump everything into global state. Centralize API access behind a data layer that owns auth headers, parsing, error handling, retries, cancellation, caching, and pagination. Treat the backend API as a typed contract; generate types from a spec where possible instead of hand-duplicating them.

### Step 9 — Implementation, Loop-Engineered
Implement phase by phase (from Step 3's plan). For each phase: **propose** the code → **validate** with real tests/lint/typecheck (not your own judgment) → if anything fails, **diagnose** the exact failure and **refine** → repeat, capped at 5 iterations before stopping to report the blocker rather than guessing further → **converge** only when checks actually pass. Cover error boundaries/resilience, routing (protected/lazy/deep-linked), forms/validation, and real-time features only where required.

### Step 10 — Performance, Security, i18n, SEO (as required)
Performance: code-split, lazy-load, avoid unnecessary re-renders and duplicate API calls, virtualize large lists — **measure before and after**, don't optimize blindly. Security: guard against XSS/CSRF/token leakage/unsafe HTML rendering; never ship secrets to the browser; treat everything shipped to the client as public. i18n/SEO/date-time-currency handling: implement only to the depth the product actually requires — see `references/best-practices.md` §18–27.

### Step 11 — Testing
Cover unit (utils/hooks/validation), component (interaction, forms, states, a11y), integration (workflows, auth, state transitions), and E2E (login, core CRUD, authorization, critical journeys) — prioritize critical business logic and user journeys over chasing 100% coverage.

### Step 12 — Production Readiness Review (Gate)
Before calling anything "done," grade it against the full checklist in `references/best-practices.md` Appendix C (Architecture, UI/UX, Performance, Security, Accessibility, Testing, Production/CI-CD). Don't declare production readiness without it.

## Reference files

- `references/best-practices.md` — the complete 38-point best-practices reference (design system spec, UI/UX heuristics, state/data-layer rules, performance/security/a11y checklists, testing matrix, project structure template, production readiness checklist). Read the relevant section as each workflow step needs it; don't load the whole thing for a small task.
- `references/design-references.md` — Google Material Design / Google's design resources plus a curated list of production-grade open-source design systems and UI-inspiration sources to reference for visual quality, component APIs, and interaction patterns.
- `references/shadcn-references.md` — the full open-source shadcn/ui ecosystem: core CLI/registry usage plus free component/block registries (Magic UI, Aceternity UI, Origin UI, Kokonut UI, ReUI, 21st.dev, and more) for React/Tailwind stacks.
- `references/component-libraries.md` — full, installable React component libraries (HeroUI, MUI, Ant Design, Mantine, Chakra UI, Base UI, React Aria, daisyUI, Tremor, Untitled UI) versus shadcn's copy-in approach, plus Vue/Angular/Svelte equivalents.
- `references/modern-stack-2026.md` — current (2026) defaults across meta-frameworks, styling, state/data/forms, auth/ORM, and testing — a checklist to verify Step 4 choices against, not a permanent answer.

## Guiding principles (quick recall)

1. Read requirements before designing the frontend — never assume the stack or the page set.
2. Don't copy a previous project's architecture blindly.
3. Server state and UI state are different things — keep them separate.
4. APIs are contracts. Loading/empty/error states are designed from the start, not patched in.
5. Accessibility and performance are engineering concerns, measured — not a final pass or a guess.
6. Frontend authorization never replaces backend authorization; never ship secrets to the client.
7. Use the simplest architecture that reliably satisfies requirements — don't overengineer (no micro-frontends, no SSR, no offline mode, no extra state libraries) unless requirements justify it.
8. Don't declare production readiness without running the full checklist.
