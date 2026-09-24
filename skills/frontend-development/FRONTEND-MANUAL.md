# FRONTEND-MANUAL.md — Frontend Development Skill: What It Is & How to Use It

This is the companion manual for the `frontend-development` skill (see `skills/frontend-development/`). It plays the same role for frontend work that `HERMES-MANUAL.md` plays for full-project SDLC in Hermes: a single document explaining what the skill does, how it's structured, and how to invoke it — plus the best-practice and design-reference material it draws on.

---

## 1. What this skill is

`frontend-development` is a technology-agnostic (React/Vue/Angular/Svelte/plain HTML-CSS-JS) skill covering the full frontend lifecycle: requirements analysis → architecture → design system → implementation → testing → performance/security/accessibility → production readiness. It's built the same way Hermes's skills are built — a short `SKILL.md` with a numbered workflow and human review gates, plus `references/` files loaded only when needed — so it stays lightweight in context until the relevant step actually needs the detail.

```
frontend-development/
├── SKILL.md                     ← workflow: 12 steps + guiding principles
└── references/
    ├── best-practices.md        ← the full 38-point best-practices spec (design system,
    │                                UI/UX, state, performance, security, a11y, testing,
    │                                production readiness checklist)
    ├── design-references.md     ← Google Material Design / google.design + curated
    │                                open-source design systems + UI-inspiration sources
    ├── shadcn-references.md     ← the full open-source shadcn/ui registry ecosystem
    │                                (core + Magic UI, Aceternity, Origin UI, ReUI, etc.)
    ├── component-libraries.md   ← HeroUI, MUI, Ant Design, Mantine, Chakra, Base UI,
    │                                React Aria + Vue/Angular/Svelte equivalents
    └── modern-stack-2026.md     ← current framework/tooling defaults (Next.js, Tailwind v4,
                                     TanStack, Zustand, Vitest/Playwright) to check against
```

---

## 2. How to use it

**As a Claude skill:** place the `frontend-development/` folder wherever skills are loaded from in your environment. It triggers automatically whenever a request involves building, planning, reviewing, or auditing a frontend/UI — you don't need to name it explicitly, though you can ("use the frontend-development skill to build X").

**As a manual read by a human:** read `SKILL.md` for the workflow shape, then dip into `references/best-practices.md` for the exact rule set for whichever step you're on, and `references/design-references.md` whenever you need a real-world example of how a component or visual system was solved before.

**Kickoff pattern (mirrors the Hermes single-message kickoff):**
```
Read SKILL.md in the frontend-development skill and the PRD in this project.
Follow the workflow steps in order, using references/best-practices.md and
references/design-references.md as needed. Stop at Step 3 for plan review
and at Step 12 for the production-readiness gate.
```

---

## 3. The workflow at a glance

| Step | Name | Gate? |
|---|---|---|
| 1 | Analyze before building | — |
| 2 | Requirements → Feature Map | — |
| 3 | Frontend Development Plan | ✅ Human review before major implementation |
| 4 | Technology Selection | — |
| 5 | Project Structure & Component Architecture | — |
| 6 | Design System (tokens + components) | — |
| 7 | UI/UX, Responsive & Accessibility | — |
| 8 | State, Data Layer & API Contract | — |
| 9 | Implementation (loop-engineered, 5-iteration cap per blocker) | — |
| 10 | Performance, Security, i18n, SEO | — |
| 11 | Testing | — |
| 12 | Production Readiness Review | ✅ Full checklist before calling it done |

For a quick task (a single component, a small fix), Steps 1 and 6 are enough — skim requirements, reuse the design-system tokens, build it well. Full 12-step rigor is for new apps, feature areas, or production-readiness audits.

---

## 4. Best practices reference — what's inside `best-practices.md`

The 38-section reference covers, in order: requirements analysis, the feature-map chain, the frontend plan document, technology selection, project structure (with a concrete `src/` layout), component architecture, the design-system token spec, UI/UX heuristics (usability, visual hierarchy, interaction feedback, navigation, microcopy, confirmation flows, onboarding/empty states, platform conventions), responsive design, WCAG 2.2 AA accessibility, the six-way state-classification table, the API/data layer, API-as-contract typing, authentication, authorization, forms, error/loading/empty states, performance (initial load + runtime, measured not guessed), large-dataset handling, browser/network performance, security (XSS/CSRF/token leakage/safe rendering), error boundaries and resilience, real-time features, routing, SEO, i18n, date/time/currency handling, file/media handling, the testing pyramid, code quality, build/environment management, CI/CD, browser compatibility, documentation, a recommended 18-step implementation order, an "don't overengineer" principle, the full **Production Readiness Checklist** (Architecture / UI-UX / Performance / Security / Accessibility / Testing / Production), and 20 guiding principles.

Treat it as a lookup table, not required reading front-to-back: each `SKILL.md` step points at the exact section(s) it needs.

---

## 5. Design references — what's inside `design-references.md`

Four parts:

1. **Google Design** — Material Design 3 (m3.material.io) as the primary structural reference for color roles, type scale, elevation, motion, and component anatomy, plus Google Fonts, Material Symbols/Icons, web.dev's performance/accessibility guidance, and design.google for cross-product interaction-pattern rationale.
2. **Open-source, production-grade design systems** — Carbon (IBM), Polaris (Shopify), Atlassian Design System, Lightning Design System (Salesforce), Fluent 2 (Microsoft), Spectrum (Adobe), Primer (GitHub), Base Web (Uber), Canvas (Workday), Garden (Zendesk), Ant Design, Radix Primitives/Themes, shadcn/ui, MUI, Vanilla Framework (Canonical), and Codex (Wikimedia) — each with what it's especially strong for, so you know which one to check for a given component problem (data tables → Carbon; accessible unstyled primitives → Radix; admin dashboards → Ant Design, etc.).
3. **UI inspiration / quality-benchmarking sources** — Mobbin, Awwwards, Land-book, Dribbble, Refactoring UI, and the A11y Project, for calibrating visual polish and current interaction conventions (inspiration only — never copy verbatim).
4. **How to apply it at Step 6** — a short 5-step procedure: borrow M3's token *structure*, check 2–3 systems for how a specific component's edge cases are solved, start from Radix when accessibility must be correct from day one, calibrate final polish against the inspiration sources, then document the project's own resulting token set.

---

## 5.5. shadcn/ui reference — what's inside `shadcn-references.md`

Covers the open-source shadcn/ui ecosystem specifically, for React/Next.js + Tailwind stacks: what shadcn actually is (a CLI that copies component source into your repo, not an npm-installed library), how its 2026 registry system works (any GitHub repo can become an installable registry via `registry.json`), the official CLI commands, and a table of free, open-source component/block registries — Magic UI, Aceternity UI, Origin UI, Kokonut UI, Cult UI, Eldora UI, ReUI, Tailark, 21st.dev (directory), shadcn/vue, ReactBits, Kibo UI, Align UI, 8bitcn UI, and the community `awesome-shadcn-ui` list — plus the `tweakcn.com` theming tool and a short procedure for choosing between them without ending up with five clashing animation styles in one app.

## 5.6. Full component libraries — what's inside `component-libraries.md`

Covers installable (not copy-in) component libraries across frameworks: for React, HeroUI (formerly NextUI — Tailwind v4 + React Aria, ships an MCP server for AI-assisted dev), MUI, Ant Design, Mantine, Chakra UI, Untitled UI, and Tremor as full libraries, plus the headless/unstyled layer (Radix Primitives, Base UI, React Aria, Headless UI, daisyUI) that shadcn and custom design systems are typically built on. It also lists the Vue (Vuetify, PrimeVue, Naive UI), Angular (Angular Material, PrimeNG, ng-zorro), and Svelte (Skeleton, Flowbite-Svelte, Melt UI/Bits UI) equivalents, and gives a decision rule for when to pick a full library vs. the shadcn copy-in approach.

## 5.7. Current stack defaults — what's inside `modern-stack-2026.md`

A snapshot checklist of 2026 defaults to verify Step 4 choices against: meta-frameworks (Next.js 16, Vite, Astro, Nuxt 4, Angular 21, SvelteKit), Tailwind CSS v4, data/state/forms (TanStack Query/Router/Form, Zustand, Zod, React Hook Form, nuqs), auth/ORM (Clerk/Better Auth, Drizzle/Prisma), and testing (Vitest, Playwright, MSW) — explicitly framed as something to verify against each tool's own docs rather than a permanent answer, since this space shifts every 6–12 months.

---

## 6. Relationship to the Hermes SDLC skill set

This skill is designed to slot into a Hermes-style project the same way any other Hermes skill does: `plan-generation` can call out to it for the "Frontend Plan" subsection of `plan.md` Section 5 (per Hermes's `plan-generation` skill, which already flags the Frontend Plan as mandatory whenever a project includes a UI), and `phase-implementation` can apply its Step 9 loop-engineering cycle to frontend phases specifically. It's also fully usable standalone, outside any Hermes project, for any frontend engineering task.
