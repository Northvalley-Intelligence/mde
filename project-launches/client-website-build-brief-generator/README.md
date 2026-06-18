# Client Website Build Brief Generator Launch Pack

This launch pack starts the planned `client-website-build-brief-generator` project.

The project generates current client website launch packs from assessment reports, client intake, and MDE knowledge.

Each launch pack should include:

- `codex-build.prompt.md`
- website build mission
- client intake summary and missing questions
- content-needed checklist
- technical implementation brief
- SEO/AEO and service-area strategy
- validation plan
- Cloudflare deployment checklist
- Northvalley GitHub repo and branch governance notes

The generated prompt must carry forward the rules from `context-packs/client-website-build.md` and `context-packs/website-assessment-to-build.md`, including service-area SEO/AEO, medinaclean-style technical stack, Cloudflare Workers/OpenNext deployment, and `main`/`prod` synchronization checks when a `prod` branch exists.

Use `bootstrap.prompt.md` in a new repo-specific Codex window.
