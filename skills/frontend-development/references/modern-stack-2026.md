> Reference file for the `frontend-development` skill. Used at Step 4 (Technology Selection) to check current defaults before picking a stack from habit. Frontend tooling moves fast — treat this as a snapshot to verify against each library's own docs, not a permanent answer.

# Modern Frontend Stack Notes (2026 snapshot)

Reminder from `SKILL.md`: **derive the stack from requirements, don't default to this list blindly.** This exists so a choice is at least informed by what's current, not what was current two years ago.

## 1. Meta-frameworks / build tools

| Layer | 2026 default | Notes |
|---|---|---|
| Full-stack React | **Next.js 16** (App Router, Turbopack stable/default) | React Server Components standard; `middleware.ts` migrating to `proxy.ts`; `use cache` directive replaces older fetch-caching model |
| SPA build tool | **Vite** (or Vite+ / Rolldown-based tooling) | Default for non-meta-framework React/Vue/Svelte SPAs |
| React version | **React 19.x** | Server Components, Actions, `useActionState`, `useFormStatus`, `useOptimistic`, React Compiler for auto-memoization |
| Vue | **Nuxt 4** | |
| Angular | **Angular 21** | |
| Svelte | **SvelteKit 2.x** | |
| Content/marketing sites | **Astro** | Islands architecture, ships near-zero JS by default — worth considering over a full SPA/meta-framework for content-heavy, low-interactivity sites |

## 2. Styling

- **Tailwind CSS v4** — CSS-first config (no more `tailwind.config.js` required for most cases), the new Oxide engine, container queries built in. This is the 2026 default utility-CSS choice; pair with `clsx`/`tailwind-merge` for conditional classes and `class-variance-authority` (CVA) for variant-based component styling.
- See `component-libraries.md` and `shadcn-references.md` for what to build *on top of* Tailwind.

## 3. Data, state & forms

| Concern | 2026 default | Notes |
|---|---|---|
| Server-state / data fetching | **TanStack Query** | Caching, retries, invalidation — this is what §12 of `best-practices.md` ("centralize API access") points to in practice |
| Client/global state | **Zustand** (Jotai for atomic state) | Redux is no longer the default; reach for it only when the app genuinely needs its dev-tooling/middleware ecosystem |
| Type-safe routing (SPA) | **TanStack Router** | File-based, fully type-safe route params |
| Forms | **React Hook Form** (or **TanStack Form**) | Pair with a schema validator below |
| Schema validation | **Zod** (Arktype as an emerging alternative) | Used for both form validation and API contract typing (`best-practices.md` §13) |
| URL state | **nuqs** (Next.js) | Type-safe search-param state, ties directly to `best-practices.md`'s URL state row |

## 4. Auth, data layer

| Concern | 2026 default | Notes |
|---|---|---|
| Auth | **Clerk** or **Better Auth** | Pick based on how much UI/hosted-flow vs. code-ownership the project wants |
| ORM | **Drizzle** or **Prisma** | Drizzle for SQL-first/lighter runtime, Prisma for DX/migrations tooling |

## 5. Testing

| Level | 2026 default | Notes |
|---|---|---|
| Unit/component | **Vitest** (+ Testing Library) | Vite-native, fast; Vitest browser mode is increasingly used instead of jsdom for higher-fidelity component tests |
| E2E | **Playwright** | The default over Cypress for new projects in 2026 |
| API mocking | **MSW (Mock Service Worker)** | Mocks at the network level, works the same in tests and local dev |

## 6. TypeScript

- **TypeScript 5.9+, strict mode** is the expected baseline (`best-practices.md` §30 — avoid `any`). The `satisfies` operator is standard for typed config objects. A Go-based compiler (project "Corsa"/TS 7) is in preview for large-codebase speed — not yet the default, worth checking status before depending on it.

## 7. How to use this at Step 4

1. Treat this table as a checklist to *verify*, not copy blindly — check each project's own changelog since these shift roughly every 6–12 months.
2. Justify any deviation from these defaults the same way `SKILL.md` Step 4 already asks for: note *why*, and the trade-off accepted.
3. Cross-reference `component-libraries.md` and `shadcn-references.md` for the UI layer specifically — this file intentionally excludes component libraries to avoid duplicating those two files.
