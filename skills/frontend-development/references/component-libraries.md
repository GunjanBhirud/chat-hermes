> Reference file for the `frontend-development` skill. Used at Step 4 (Technology Selection) alongside `shadcn-references.md`. These are full component **libraries** (installed as a dependency, not copied into your repo like shadcn) — pick one when the team wants a maintained package with its own release cycle rather than owning the component source.

# Component Libraries — Full Libraries vs. Copy-In, Across Frameworks

## 1. React — full, installable component libraries

| Library | Styling / a11y foundation | Best for | URL |
|---|---|---|---|
| **HeroUI** (formerly NextUI) | Tailwind CSS v4 + React Aria Components | Polished-by-default apps that still want Tailwind-level customization; ships MCP server + llms.txt for AI-assisted dev; also has a React Native library (HeroUI Native) | https://heroui.com |
| **MUI (Material UI)** | Emotion (CSS-in-JS), implements Material Design | Enterprise/data-heavy apps, largest ecosystem (95k+ stars, ~1.4M weekly downloads), deep i18n (50+ locales) and ProComponents for complex business UI | https://mui.com |
| **Ant Design** | CSS-in-JS/CSS, its own design language | Admin dashboards, enterprise back-office tools, very deep table/form components | https://ant.design |
| **Mantine** | CSS Modules or Emotion | Fast MVP/product builds — 100+ components *and* 100+ hooks (forms, notifications, spotlight search) in one package; fastest-growing library by downloads in 2026 | https://mantine.dev |
| **Chakra UI** | Emotion/CSS, accessible-by-default | Teams that want sensible defaults with moderate customization | https://chakra-ui.com |
| **Untitled UI** | Tailwind CSS + React Aria | Teams that also want a matching, purchasable Figma kit for design/dev parity | https://www.untitledui.com |
| **Tremor** | Tailwind CSS | Dashboards, charts, KPI/analytics UI specifically (not a general component set) | https://tremor.so |

### Headless / unstyled (behavior + accessibility only — you own all styling)

| Library | Notes | URL |
|---|---|---|
| **Radix Primitives** | Low-level primitives (Dialog, Tooltip, Dropdown, etc.); the accessibility foundation under shadcn/ui | https://www.radix-ui.com |
| **Base UI** | From the MUI team; unstyled, WAI-ARIA-pattern-tested, works with Tailwind/CSS Modules/plain CSS | https://base-ui.com |
| **React Aria (Adobe)** | The most rigorous accessibility behavior layer available (keyboard nav, screen-reader announcements, i18n) — also underlies HeroUI and Untitled UI | https://react-spectrum.adobe.com/react-aria |
| **Headless UI** | Unstyled, Tailwind Labs-maintained, smaller surface (menus, dialogs, listboxes) | https://headlessui.com |
| **daisyUI** | Not headless — adds semantic classes (`btn`, `btn-primary`) on top of Tailwind for less verbose markup, multiple built-in themes | https://daisyui.com |

**Decision rule:** pick a full library (HeroUI/MUI/Ant Design/Mantine/Chakra) when the team wants a maintained package and can live with its visual opinions; pick a headless primitive (Radix/Base UI/React Aria) + shadcn-style copy-in when the team needs full visual control and is willing to own the component source; pick shadcn/ui itself (see `shadcn-references.md`) as the common middle ground most teams land on in 2026.

## 2. Cross-framework equivalents (for the technology-agnostic cases this skill also covers)

| Framework | Full component libraries | Headless/unstyled |
|---|---|---|
| **Vue / Nuxt** | Vuetify (Material Design), PrimeVue, Naive UI, Element Plus | Radix Vue, Headless UI (Vue build), shadcn-vue (see `shadcn-references.md`) |
| **Angular** | Angular Material, PrimeNG, ng-zorro (Ant Design port) | Angular CDK |
| **Svelte / SvelteKit** | Skeleton, Flowbite-Svelte, Svelte Material UI | Melt UI, Bits UI (the headless base under shadcn-svelte) |

## 3. How to use this at Step 4

1. Confirm the framework first (Step 4 of `SKILL.md`) — don't pick a component library before the framework is settled.
2. If the team wants full visual ownership and is on React/Tailwind: default to shadcn/ui + Radix/Base UI/React Aria underneath (see `shadcn-references.md`), pulling from the free registries there as needed.
3. If the team wants a maintained package and faster time-to-first-screen: HeroUI or Mantine are the strongest 2026 defaults for product apps; MUI or Ant Design for data-heavy enterprise/admin.
4. Never mix two full component libraries (e.g., MUI + Ant Design) in one app — pick one and extend it; mixing headless primitives with one full library is fine since headless ones carry no visual opinion.
5. Whatever is chosen, record it and the reason in the project's design-system doc (`best-practices.md` §34) alongside the token set from `design-references.md`.
