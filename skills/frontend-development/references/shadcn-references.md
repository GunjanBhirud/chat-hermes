> Reference file for the `frontend-development` skill. Used at Step 4 (Technology Selection) and Step 6 (Design System) whenever the stack is React/Next.js + Tailwind and a copy-in, no-lock-in component approach fits. shadcn's registry ecosystem moves fast and registries copy each other — check "last shipped" before trusting a star count, and preview a component before installing it.

# shadcn/ui — Open-Source Component & Registry References

## 1. What shadcn/ui actually is

Not a component library you `npm install` — it's a CLI that copies actual component **source code** into your own repo (built on Radix UI / Base UI primitives, styled with Tailwind CSS). No version lock-in, no black-box abstraction, and you own and can edit every line. In 2026 it expanded from "a set of components" into a full **registry** distribution system: any registry (official or third-party) can ship components, hooks, utilities, design tokens, fonts, whole design systems, project conventions, and even AI-agent instructions, all installable with one CLI command.

| Resource | URL |
|---|---|
| Official site + docs | https://ui.shadcn.com |
| GitHub (core) | https://github.com/shadcn-ui/ui |
| Component/blocks browser | https://ui.shadcn.com/docs/components |
| Registry docs (how to build/consume one) | https://ui.shadcn.com/docs/registry |
| Themes | https://ui.shadcn.com/themes |

**Install a component:**
```bash
npx shadcn@latest add button
```
**Install from any third-party or GitHub registry** (2026 feature — any public GitHub repo with a `registry.json` at its root becomes an installable registry, no server needed):
```bash
npx shadcn@latest add @acme/header
npx shadcn@latest add owner/repo/item
```

## 2. Free, open-source component & block registries (the actual "opensource shadcn" ecosystem)

These are community/independent registries that extend or restyle shadcn — copy-paste or CLI-installable, source open on GitHub. Quality and maintenance vary a lot; check the repo's last commit before relying on one.

| Registry | Focus | URL |
|---|---|---|
| **Magic UI** | Largest free animated registry (~150–250 components: beams, globes, marquees, buttons) | https://magicui.design |
| **Aceternity UI** | Large animated/hero/background effects registry, dark-mode-first | https://ui.aceternity.com |
| **Origin UI** | Extends shadcn primitives, barely changes the base look — good for product UI, not just marketing | https://originui.com |
| **Kokonut UI** | Smaller, well-maintained, strong on AI-input surfaces and one standout background component | https://kokonutui.com |
| **Cult UI** | Playful, interaction-led components | https://www.cult-ui.com |
| **Eldora UI** | ~50+ animated components (Framer Motion + Tailwind) | https://eldoraui.site |
| **ReUI** | One of the largest general/product-focused registries (forms, tables, dialogs — not just marketing) | https://reui.io |
| **Tailark** | Large marketing/landing-page block registry | https://tailark.com |
| **21st.dev** | Registry *directory* + its own registry/marketplace — best single place to browse and compare registries, with live previews before installing | https://21st.dev |
| **shadcn/vue** | Unofficial Vue port of shadcn/ui, same copy-in philosophy | https://www.shadcn-vue.com |
| **ReactBits** | Utility-first shadcn components & hooks | https://reactbits.dev |
| **Kibo UI** | Clean, modular components, Tailwind + shadcn DNA | https://www.kibo-ui.com |
| **Align UI** | Design-to-code aligned, polished/minimal/accessible | https://alignui.com |
| **8bitcn UI** | Retro 8-bit styled component registry | https://www.8bitcn.com |
| **awesome-shadcn/ui (list)** | Community-curated master list of shadcn tools, registries, and extensions — good starting point to discover more | https://github.com/birobirobiro/awesome-shadcn-ui |

**Theming tool:** https://tweakcn.com — visual editor for shadcn's CSS-variable theme tokens (generates the `globals.css` token block directly).

## 3. Larger / hybrid platforms (mostly free tiers, some paid blocks — verify before assuming "open source")

| Platform | Notes | URL |
|---|---|---|
| Shadcn Studio | Broad ecosystem: components, blocks, themes, Figma kit, MCP integration — mixed free/paid | https://shadcnstudio.com |
| Shadcnblocks | Large block/template library (1000+), mostly paid, some free blocks | https://www.shadcnblocks.com |
| v0 by Vercel | AI UI generator that outputs shadcn-compatible code; its outputs are installable as a registry (`@v0` namespace) | https://v0.dev |

## 4. How to use this at Step 4/6

1. Start from core shadcn/ui (`ui.shadcn.com`) for primitives — buttons, inputs, dialogs, tables. These are the most audited and stable.
2. If the product needs marketing/landing-page polish, pull specific components (not whole templates) from Magic UI, Aceternity, or Tailark — keep the count small so the app doesn't end up with five different animation styles.
3. If it's a data-dense product UI, check ReUI or Origin UI before Magic UI/Aceternity — the animated registries are "thin on the components a product actually runs on" (data tables, date pickers, settings screens).
4. Verify accessibility and maintenance yourself — being "shadcn-compatible" doesn't guarantee WCAG correctness; spot-check keyboard nav and screen-reader labels on anything pulled in.
5. Use `tweakcn.com` to generate a consistent token set across whatever mix of registries you use, rather than hand-tuning each import to match.
6. Record which registries/components were used in the project's own design-system doc (see `best-practices.md` §34) so future contributors know the provenance.
