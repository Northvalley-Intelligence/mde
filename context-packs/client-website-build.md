# Client Website Build Context Pack

Applicable artifact profiles:

- `client_website`
- `website_build`
- `client_facing_workflow`
- `public_content`
- `private_client_data`

Use this context pack when creating a new client website repo or when generating a prompt that will build a new client website.

## Default Repository Rules

- Client website repositories should be created under the Northvalley Intelligence GitHub organization: `https://github.com/Northvalley-Intelligence`.
- Repo names should be client/domain based, lowercase, and stable, for example `example-client.com` or `example-client-site`.
- Do not create normal client website repos under a personal GitHub account unless Ferosh explicitly requests an exception.
- Default branch should be `main`.
- Production deployment should track `main` unless the project explicitly defines a separate `prod` branch.
- If a `prod` branch exists, `main` and `prod` must be kept in sync before production launch. Do not deploy when `origin/main` and `origin/prod` point at different commits unless the difference is explicitly documented as an approved staged release.
- Generated build prompts must include a branch-sync check before production deploy:
  - fetch `origin main prod` when both branches exist
  - compare `origin/main` and `origin/prod`
  - stop and ask before deploying if they diverge
  - after approved launch, record the deployed commit SHA
- Recommended sync check:

```bash
git fetch origin main prod
MAIN_SHA="$(git rev-parse origin/main)"
PROD_SHA="$(git rev-parse origin/prod)"
test "$MAIN_SHA" = "$PROD_SHA"
```

If the check fails, do not deploy until the difference between `main` and `prod` is explained, approved, and resolved.
- Use PR-gated development for production work when practical: feature branch, PR to `main`, checks pass, merge, deploy.
- Protect `main` for public/production repos when GitHub plan/settings allow it: require PRs, require status checks, block force pushes, block deletion, and require branches to be up to date.

## Default Technical Stack

Use the same baseline stack as `medinaclean.com` unless the client mission requires otherwise:

- Next.js app with TypeScript.
- React.
- Node 22 in CI.
- npm with committed `package-lock.json`.
- `@opennextjs/cloudflare` for Cloudflare runtime builds.
- `wrangler` for Cloudflare deployment.
- `open-next.config.ts` using `defineCloudflareConfig`.
- `wrangler.jsonc` with project-specific Worker name, compatibility date, routes, assets binding, observability, and public runtime vars.
- ESLint.
- TypeScript typecheck.
- Vitest for unit/logic tests.
- Playwright for browser workflow tests.
- `npm audit --audit-level=high` in CI.
- `lucide-react` may be used for icons when the site needs iconography.

Do not introduce a different framework, package manager, hosting target, or styling system unless the generated prompt documents why the client project needs it.

Expected scripts should include equivalents of:

```json
{
  "dev": "next dev",
  "build": "next build",
  "cf:build": "opennextjs-cloudflare build",
  "cf:preview": "opennextjs-cloudflare build && opennextjs-cloudflare preview",
  "cf:deploy": "opennextjs-cloudflare build && opennextjs-cloudflare deploy",
  "lint": "eslint .",
  "typecheck": "tsc --noEmit",
  "test": "vitest run",
  "test:coverage": "vitest run --coverage",
  "test:e2e": "playwright test"
}
```

## Cloudflare Deployment Rules

- Default deployment target is Cloudflare Workers using the OpenNext Cloudflare adapter, matching `medinaclean.com`.
- Use the client's production domain as `NEXT_PUBLIC_SITE_URL`.
- Configure `wrangler.jsonc` with:
  - Worker name based on the repo/domain slug.
  - `main` pointing to `.open-next/worker.js`.
  - current compatibility date.
  - `nodejs_compat` compatibility flag when needed.
  - routes for apex and `www` domains when both should serve the site.
  - `.open-next/assets` bound as `ASSETS`.
  - observability enabled.
- Domain/DNS should be managed in Cloudflare when possible.
- Do not enable paid Cloudflare products unless explicitly approved.
- After first successful deploy, connect custom domains in Cloudflare Workers & Pages and verify apex and `www` behavior.
- Generated prompts must include deployment documentation under `docs/deployment.md`.
- Generated prompts must list required GitHub repository secrets and Cloudflare permissions before deployment.

Minimum Cloudflare/GitHub secrets to consider:

- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID`
- `NEXT_PUBLIC_SITE_URL`
- Client-specific public contact values such as phone, email, forms, analytics, and chat keys.
- Private service keys only when the project actually uses Supabase, Resend, Turnstile, LLM chat, or other integrations.

Required Cloudflare token permissions should be documented when route deployment is used:

- `Account` -> `Workers Scripts` -> `Edit`
- `Account` -> `Account Settings` -> `Read`
- `Zone` -> `Workers Routes` -> `Edit`
- `Zone` -> `Zone` -> `Read`

## GitHub Actions And Release Checks

Generated client website prompts should create or request GitHub Actions similar to `medinaclean.com`:

- CI on pull requests to `main` and pushes to `main`.
- CI should run:
  - `npm ci`
  - `npm audit --audit-level=high`
  - `npm run lint`
  - `npm run typecheck`
  - `npm run test:coverage`
  - install Playwright Chromium
  - `npm run test:e2e -- --project=chromium`
  - `npm run build`
  - `npm run cf:build`
- Production deploy workflow should deploy from `main` unless a documented `prod` branch strategy is used.
- Deployment workflow should run lint, typecheck, tests, Playwright, and `cf:build` before `wrangler deploy`.
- Deployment workflow should not expose private secrets to frontend code.
- Generated prompts should include a launch checklist that records:
  - repo URL under `Northvalley-Intelligence`
  - default branch
  - production branch or deploy source
  - deployed commit SHA
  - Cloudflare Worker name
  - production domain
  - whether `main` and `prod` are synchronized, if `prod` exists

## Client-Safe MDE Bootstrap

- Start from current client context and assessment evidence, not copied code from old client sites.
- Keep client-owned repos client-safe.
- Do not include central private MDE ledgers, cross-client lessons, internal content seeds, or confidential strategy notes.
- Generate a content-needed checklist before pretending content is complete.
- Create a project-specific validation strategy during Generation 0.
- Create local MDE artifacts in the client repo:
  - `MISSION.md`
  - `MISSION_UPDATES.md`
  - `.mde/project.json`
  - `.mde/validation-strategy.json`
  - `.mde/outbox/events.jsonl`
  - `.mde/lessons-local.jsonl`
  - `docs/client-intake-needed.md`
  - `docs/content-needed-from-client.md`
  - `docs/website-build-brief.md`
  - `docs/launch-validation-plan.md`
  - `docs/deployment.md`

## Website Quality Guardrails

- Build around the client's services, service areas, trust proof, and conversion path.
- Do not build a generic brochure site.
- Use assessment evidence and client intake to drive page structure.
- Create service and service-area pages when they are part of the mission.
- Include FAQ/AEO content, LocalBusiness/schema guidance, sitemap, robots-safe crawl paths, and Open Graph metadata when applicable.
- Keep phone/contact/estimate actions visible on desktop and mobile.
- Validate accessibility, content clarity, mobile behavior, forms, SEO/AEO structure, and deployment before client delivery.
- Do not invent reviews, credentials, licenses, service guarantees, locations, or project examples.

## Optional Integrations

Only include these when the client mission requires them and required secrets/ownership are available:

- Supabase for private admin data, reviews, submissions, or structured content.
- Resend or another email provider for form notifications.
- Turnstile for public form/chat protection.
- Analytics such as GA4.
- AI chat, using explicit provider, cost, privacy, and fallback decisions.
- Meta/YouTube/social integrations.

When optional integrations are used, document required environment variables in `.env.example`, GitHub secrets, Cloudflare Worker secrets, and `docs/deployment.md`.
