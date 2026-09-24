> Reference file for the `frontend-development` skill, used at Step 6 (Design System) and whenever visual/interaction quality needs a benchmark. These are real, actively maintained systems — read the linked docs directly rather than guessing at their token names or component APIs from memory, since they evolve.

# Design References — Google Design & Open-Source Design Systems

Don't invent a design language from scratch when a battle-tested one already solves the problem. Use these to borrow token structure (type scale, color roles, spacing scale), component anatomy, interaction/motion patterns, and accessibility baselines — then adapt to the product's own brand.

---

## 1. Google Design (primary reference for visual & interaction quality)

| Resource | URL | Use it for |
|---|---|---|
| Material Design 3 (M3) | https://m3.material.io | The most complete public design system spec: color system (dynamic color, tonal palettes), type scale, elevation, shape, motion, and full component specs (buttons, cards, nav, dialogs, etc.) |
| Material Design components (web) | https://m3.material.io/components | Per-component anatomy, states (enabled/hover/focus/pressed/disabled), and usage guidance — good baseline even outside Material-styled apps |
| Material Web (open-source implementation) | https://github.com/material-components/material-web | Actual buildable components implementing M3, useful as an implementation reference |
| Material Symbols & Icons | https://fonts.google.com/icons | Free, open-source icon set (outlined/rounded/sharp), variable font |
| Google Fonts | https://fonts.google.com | Open-source, production-safe web fonts — pair a display and a body typeface here rather than shipping unlicensed fonts |
| Google's design principles / case studies | https://design.google | Cross-product design rationale (search, workspace, Android) — good for interaction-pattern inspiration beyond raw specs |
| web.dev (Google) | https://web.dev | Google's own frontend engineering guidance — performance (Core Web Vitals), accessibility, responsive design, PWA — pairs directly with §18–20 and §10 of `best-practices.md` |
| Android Material guidelines (for hybrid/responsive-to-native thinking) | https://developer.android.com/design | Useful when a web app has a native counterpart and needs pattern parity |

**When to actually apply Material vs. just reference it:** use M3's *structure* (semantic color roles, type scale, spacing, component states) as a checklist even when the product has its own brand identity — you don't have to ship Google's literal visual style to benefit from how rigorously they've solved states, contrast, and elevation.

---

## 2. Open-source, production-grade design systems (component & token references)

These are real companies' public design systems — each ships actual code, not just a style guide. Good for seeing how a specific component (data table, complex form, date picker, permission-aware nav) is solved at production scale.

| System | Company | URL | Especially strong for |
|---|---|---|---|
| Carbon Design System | IBM | https://carbondesignsystem.com | Enterprise data tables, complex forms, dense dashboards |
| Polaris | Shopify | https://polaris.shopify.com | E-commerce admin UI, content/microcopy guidance, merchant-facing UX |
| Atlassian Design System | Atlassian | https://atlassian.design | Navigation, collaboration UI, empty/loading states |
| Lightning Design System | Salesforce | https://lightningdesignsystem.com | CRM-scale forms, tables, and accessibility depth |
| Fluent 2 | Microsoft | https://fluent2.microsoft.design | Cross-platform (web/desktop) consistency, motion |
| Spectrum | Adobe | https://spectrum.adobe.com | Creative-tool UI, precise interaction states |
| Primer | GitHub | https://primer.style | Developer-tool UI, dark mode, accessible color system |
| Base Web | Uber | https://baseweb.design | Themeable component architecture (React) |
| Canvas Design System | Workday | https://canvas.workday.com | HR/enterprise dense-data UI, accessibility |
| Garden | Zendesk | https://garden.zendesk.com | Support/ticketing UI patterns |
| Ant Design | Alibaba (open community) | https://ant.design | Admin dashboards, rich form components, i18n support |
| Radix Primitives / Radix Themes | WorkOS (open-source) | https://www.radix-ui.com | Unstyled, fully accessible component primitives — best starting point when building a *custom* design system that must be WCAG-correct |
| shadcn/ui | Open-source (built on Radix + Tailwind) | https://ui.shadcn.com | Copy-in (not npm-locked) component source, good default aesthetic, easy to restyle — see `shadcn-references.md` in this same folder for the full open-source registry ecosystem (Magic UI, Aceternity, Origin UI, ReUI, and more) |
| MUI (Material UI) | Open-source | https://mui.com | Ready-made Material-based React components when you want M3 semantics without building from spec |
| Vanilla Framework | Canonical/Ubuntu | https://vanillaframework.io | Lightweight, CSS-only system for marketing + product sites |
| Codex | Wikimedia | https://doc.wikimedia.org/codex | High-traffic, accessibility-first public site patterns |

**How to use this table:** don't adopt one wholesale unless the product is genuinely enterprise-admin-shaped. Instead, when Step 6 needs to decide "how should our data table handle sorting + row selection + bulk actions," go look at how 2–3 of these solved it, then design your own token set informed by the pattern.

---

## 3. UI inspiration & quality-benchmarking sources

Use these to calibrate visual polish and current interaction conventions — not to copy verbatim (respect copyright; treat any screenshot as reference/inspiration only, never reproduce it).

| Source | URL | Use it for |
|---|---|---|
| Mobbin | https://mobbin.com | Real production app flows (mobile + web), organized by pattern (onboarding, checkout, empty states) |
| Awwwards | https://www.awwwards.com | High-end visual/interaction design, marketing sites |
| Land-book | https://land-book.com | Landing page patterns by industry |
| Dribbble | https://dribbble.com | Concept-level visual direction (treat as inspiration, not implementation-ready) |
| Refactoring UI / UI patterns | https://www.refactoringui.com | Practical, engineer-friendly visual-hierarchy heuristics — pairs directly with §8 of `best-practices.md` |
| A11y project | https://www.a11yproject.com | Community-maintained accessibility checklist and patterns, complements WCAG 2.2 directly |

---

## 4. Applying this at Step 6

1. Pull the semantic color roles, type scale, and spacing scale structure from M3 (§1) as your starting checklist.
2. For each non-trivial component (table, form, modal, nav, permission-aware UI), check 1–2 systems from §2 for how they handle states and edge cases (empty, loading, error, disabled, overflow).
3. If building a custom design system that must be accessible from day one, start component *behavior* from Radix Primitives (unstyled, WCAG-correct) and layer your own visual tokens on top rather than re-deriving keyboard/focus/ARIA behavior yourself.
4. Calibrate final visual polish against §3 sources, not against habit.
5. Document the resulting token set and component inventory in the project's own design-system doc (see `best-practices.md` §7 and §34) — these references inform it, they don't replace it.
