# Bootstrap Prompt

Start the `client-website-build-brief-generator` project using MDE Generation 0.

Read this launch pack, then create local MDE artifacts from the seed files.

Do not implement the generator yet. First define mission, project identity, dependencies, risk register, initial task graph, and project-specific validation strategy.

Required context:

- Load `context-packs/client-website-build.md` and apply its Northvalley repo, medinaclean-style stack, Cloudflare deployment, GitHub Actions, client-safe MDE, and branch synchronization rules.
- Load `context-packs/website-assessment-to-build.md` and apply its assessment evidence, SEO/AEO, service-area, lead conversion, trust, and common assessment failure-mode rules.
- Use `validation-strategy.seed.json` as the starting Validation Strategy and preserve its Critical validations unless the user explicitly changes the mission.

Required focus:

- consume demand data and website assessment reports
- detect stale assessment data
- identify missing client details
- protect privacy and confidentiality
- generate a client website launch pack, not only a prose prompt
- generate client questions, website mission, technical brief, content-needed checklist, SEO/AEO service-area strategy, validation strategy suggestion, deployment checklist, and Codex build prompt
- require the generated Codex prompt to target repos under `https://github.com/Northvalley-Intelligence`
- require the generated Codex prompt to use the medinaclean-style Next.js, TypeScript, OpenNext Cloudflare, Wrangler, Vitest, Playwright, ESLint, and npm baseline unless explicitly overridden
- require the generated Codex prompt to include Cloudflare deployment documentation and required secret/permission checklist
- require the generated Codex prompt to include a `main`/`prod` sync check when a `prod` branch exists
- require assessment-derived recommendations to trace to evidence, client intake, or documented assumptions
- require missing content to be listed instead of invented
- record outbox event for central `mde`
