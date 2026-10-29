---
name: agent-native-mcp
description: Make a website/service agent-native — build a Model Context Protocol (MCP) server that lets AI assistants (Claude, ChatGPT, Gemini) use it, then get it listed in the assistant directories. Use when adding an MCP booking/lead/tools front door onto an existing web app (especially Next.js on Cloudflare Workers/OpenNext), reusing the app's existing intake/notification/logic, and when preparing or walking a client through the ChatGPT (OpenAI) or Claude connector-directory submission. Also covers Google OAuth branding verification when the app uses Google scopes.
metadata:
  source: medinaclean.com GEN-001 (agent-native MCP lane) + GEN-002 directory submission, 2026-08;
    northvalleyintel.com second implementation (Cloudflare Pages Functions variant), 2026-08-06;
    horizonpetwastesolutions.com Codex/ChatGPT Agent Plugins package (PR 20, handoff 23), 2026-09-30;
    horizonpetwastesolutions.com APPROVED 2026-10-15 + published 2026-10-16 (board stream
    complimentary-report-horizonpetwastesolutions-com L1/L2 2026-10-15, L3 2026-10-17 00:05);
    smartcashsheet openai-01 docs re-read 2026-10-28 (OAuth, review block in plugin.json)
  status: battle-tested on two independent stacks (live MCP booking in Claude + ChatGPT;
    OpenAI directory submitted for medinaclean.com; northvalleyintel.com/mcp live);
    first two OpenAI submissions REJECTED 2026-08-22 — causes diagnosed, fixes shipped,
    lessons folded into Part 2 and Part 9; northvalleyintel.com v1.0.2 REJECTED again 2026-09-19
    (test-case fidelity across web+mobile, explicit annotation justifications, input minimization,
    sensitive-data solicitation) — folded into Part 9 as a pre-submission checklist; Part 7a added
    2026-09-30 for the current Agent Plugins ZIP/portal format; horizonpetwastesolutions.com's
    plugin.json package went through the live portal 2026-09-30, passed the portal checks after 5
    rounds and was SUBMITTED for review at 21:45 (OpenAI "Submission Received" mail); OpenAI APPROVED
    it 2026-10-15 ("ChatGPT Plugin Submission Approved", "Horizon Pet Waste Solutions (v1.0.0)") and
    Ferosh PUBLISHED it 2026-10-16; the live listing was verified 2026-10-17 (portal shows version 1.0.3
    Published, 4 tools, no scan findings) — the first Northvalley directory APPROVAL, and proof the
    Agent Plugins ZIP is the format that passes today (Part 7's chatgpt-app-submission.json stays a
    fallback reference only); r1→r5 history, the approved package's contents, and what to check
    BEFORE submitting are in Part 7a and Part 9; Part 7b (OAuth-protected servers) added 2026-10-28
    from first-hand reads of the current docs — not yet proven through the portal
---

# Agent-Native MCP

Turn an existing web app into something an AI assistant can use, by exposing a small MCP server that
**reuses the app's existing logic**, then (optionally) list it in the assistant directories. Written from
the medinaclean.com build — a bilingual local cleaning service that now takes bookings from inside Claude
and ChatGPT.

## Core principle: reuse, don't rebuild

Put the MCP server **inside the existing app as API routes**, not as a separate service. Each tool wraps
logic the app already has (pricing engine, service-area check, the form's intake + notification path).
**Extract a shared helper** so the website form and the MCP tool call the *same* intake — one path, one
DB table, one notification. Never build a parallel intake (it drifts and doubles the abuse surface).

## Trust invariant (for anything that writes on a human's behalf)

If a tool takes a real-world action, decide the human-in-the-loop model up front and enforce it in code:
for bookings, **the assistant REQUESTS; it never CONFIRMS.** Return a `pending_review` status, write the DB
row with the default `pending` status (no migration needed — don't invent a new enum value), tag `source`
so you can tell assistant-origin records apart, and repeat "request, not confirmed" in every tool
description, the server `instructions`, the inline UI, and every localized string.

---

## Part 1 — Build the server (Next.js on Cloudflare Workers/OpenNext)

- SDK: `@modelcontextprotocol/sdk` (built on zod). Import via subpaths: `.../server/mcp.js` (`McpServer`),
  `.../server/webStandardStreamableHttp.js`, `.../client/index.js` + `.../inMemory.js` (for tests).
- **Transport (the key gotcha):** use **`WebStandardStreamableHTTPServerTransport`**, NOT the default
  `StreamableHTTPServerTransport`. The default is built on Node `http` req/res and does **not** fit a
  Next.js App Router route handler (which gets a Web `Request`/`Response`). The web-standard one is made for
  "Node 18+, Cloudflare Workers, Deno, Bun." Construct it **stateless** with `enableJsonResponse: true`.
- Route (`src/app/mcp/route.ts`): build a **fresh `McpServer` + transport per request**, `await
  server.connect(transport)`, `return transport.handleRequest(request)`. Add permissive CORS + an `OPTIONS`
  handler; `GET` → 405. `nodejs_compat` in `wrangler.jsonc` helps it bundle.
- **Static-export projects: use a Pages Function, and prefer it.** If the app is
  `output: "export"` there are no route handlers at all — put the server at `functions/mcp.ts` instead.
  This is a *better* fit, not a workaround: a Pages Function already receives a Web `Request` and returns
  a Web `Response`, which is exactly what `WebStandardStreamableHTTPServerTransport` targets, so the
  Node-transport mismatch never arises. Add `compatibility_flags = ["nodejs_compat"]` to `wrangler.toml`
  (a config edit — rerun the full suite after). Verified on northvalleyintel.com: the SDK bundles and the
  stateless handshake works unchanged.
- **Pin the SDK.** If the repo pins dependencies to `latest`, do not follow that convention here. A public
  MCP endpoint is a contract; an upstream bump can change it silently. Pin `@modelcontextprotocol/sdk`
  and `zod` to exact versions.
- Verify Workers compatibility with `opennextjs-cloudflare build` (the repo's `cf:build`) — `/mcp` should
  bundle as a dynamic Worker function.
- **Tool annotations — set ALL THREE on EVERY tool, explicitly true/false:** `readOnlyHint`,
  `openWorldHint`, `destructiveHint`. Read tools → `{readOnlyHint:true, openWorldHint:false,
  destructiveHint:false}`. A write tool that hits external systems → `{readOnlyHint:false,
  destructiveHint:false, openWorldHint:true}`. **Directory scans compare the live server to your manifest;
  a "Missing" hint ≠ a `false` hint and will skip your justifications.** Also give every tool a `title` and
  an action-oriented `description` with chaining hints (e.g. "call check_service_area first").
- Inline UI: ship self-contained HTML as MCP UI resources referenced by `_meta["openai/outputTemplate"]`
  plus `structuredContent` on the tool result. Do **not** pull in `@openai/apps-sdk-ui` unless you're
  committing to a full ChatGPT App (separate iframe bundle, ChatGPT-only, dev-mode to verify).
- Localize every output (return disclaimer/reason **codes**, localize at the render/message layer).

## Part 2 — Abuse protection for a public write path ($0)

Assistants can't solve CAPTCHAs. Gate the write path with: phone validation, a honeypot, an optional shared
secret (disabled when unset, like a Turnstile helper) — **but the shared secret must NEVER appear in the
tool's public inputSchema.** A field literally named `secret` on a directory-submitted tool got
medinaclean.com REJECTED by OpenAI review as "soliciting sensitive data" (2026-08-22). If you keep a
shared-secret gate, carry it out-of-band (e.g. an HTTP header checked by the route), never as a tool
argument an assistant would be asked to fill — and a **$0 throttle that counts recent rows in your
existing DB** (e.g. `appointment_requests` per phone within a window) — **no KV/Durable Objects** (keeps it
free). Separate the pure policy (given count → allow/deny) from the DB IO so it's unit-testable.
- Gotcha: repeated test calls with the **same phone** trip the throttle and look like "request failed."
  Use a fresh phone per test take. Warn that directory reviewers testing repeatedly may hit it too.
- **Check the throttle substrate before copying this pattern.** "Count rows in the existing DB" only ports
  to projects that *have* one. Before concluding a project has no persistence, grep `wrangler.toml` for
  `d1_databases`/`kv_namespaces` and look for an existing rate-limiter to reuse — northvalleyintel.com was
  believed to have no storage, but already bound a D1 database *and* already implemented a per-minute and
  per-hour row-count throttle in its chat function. Reusing that avoided new infrastructure entirely.
  If there genuinely is no store, say so explicitly and pick one; never let "reuse, don't rebuild" quietly
  become "ship an unthrottled public write path."
- **Fail closed when the store is missing.** If the DB binding is absent at runtime, reject the write with
  a polite message rather than proceeding unthrottled.
- Hash contact identifiers in the throttle table. It needs to count, not to read; the human-readable copy
  belongs in the notification email.

## Part 3 — Testing

- Unit-test each `lib` tool. Test the server with an **in-memory client** (`Client` +
  `InMemoryTransport.createLinkedPair()`) for `listTools`/`callTool`.
- **Critical:** the in-memory client uses ONE persistent connection, so it will NOT catch the
  stateless-per-request question (does `initialize` then a *separate* `tools/call` work against a fresh
  server?). **Verify that against the LIVE deployed endpoint with sequential `curl`s** (initialize →
  tools/list → tools/call). It does work in the SDK's stateless mode — but prove it live.
- e2e in both desktop + mobile viewports. **Run the FULL unit suite after any `next.config.ts`/config edit**
  (config has its own `*.test.ts`) and the **FULL e2e after shared-page edits** (a second form on a page
  causes `getByLabel` strict-mode failures — scope assertions to the specific form).
- **Write a contract validator with two modes.** Static checks (tool set, all three hints present, write
  tools return pending, no paid content reachable, transport is the web-standard one) run in CI; a live
  mode driven by an env var (`MCP_CONTRACT_URL`) drives the deployed endpoint with sequential requests.
  When the live URL is unset, *print that static checks do not prove the endpoint works* — otherwise a
  green CI run reads as proof it does.
- **Run the live mode against the PR preview deployment before merging.** Cloudflare Pages gives a preview
  URL per PR; that proves the bundle and the stateless handshake on real infrastructure while the change is
  still revertable. Get the URL from the Pages job log (the branch alias is truncated and easy to guess wrong).
- If the repo has no test runner, do not introduce one for this. Match the existing convention (e.g. bespoke
  `scripts/validate-*.mjs`) — a new framework is a bigger change than the feature.
- **Beware assertions that match their own target.** A check for the *default* transport written as
  `!src.includes("StreamableHTTPServerTransport")` fails on correct code, because
  `WebStandardStreamableHTTPServerTransport` contains that substring. Use a word boundary. A validator that
  fails on correct code trains people to weaken assertions.

## Part 4 — Connect it in each assistant (works today, no listing needed)

A standard remote MCP server (Streamable HTTP, HTTPS, use the `/mcp` path — NOT `/sse`) can be added by URL:
- **Claude:** Settings → Connectors → Add custom connector → URL. No-auth is allowed.
- **ChatGPT:** Settings → Connectors → Advanced → **Developer Mode** → add the URL (paid tiers). The generic
  "unreviewed server" warning is fine for your own domain.
- **Gemini:** Connected Apps (personal) / Manage team → Connected apps (Enterprise) → add the URL.

## Part 5 — Discovery / GEO

Advertise the endpoint + tools + the request-never-confirm behavior in `/llms.txt`; allow AI answer agents
(OAI-SearchBot, Google-Extended, ClaudeBot, PerplexityBot, …) in `robots.ts`. Use the working URL
(`medinaclean.com/mcp`), not an unconfigured subdomain.

---

## Part 6 — Google OAuth branding verification (only if the app uses Google scopes)

Separate from MCP. If the admin app uses Google Calendar / YouTube (owner refresh token), branding
verification is needed (refresh tokens expire in ~7 days in Testing mode). To clear "home page does not
explain the purpose of your app":
- The consent-screen **App name must match the site exactly** (e.g. "Medina Clean" not "MedinaClean").
- The **home page URL must be a static 200 with NO redirect.** A same-domain `/`→`/en` redirect can trip
  it. **Root redirects hide in THREE places: `next.config.ts` `redirects()`, `middleware`/seo-redirects, and
  `page.tsx`** — remove all three and render the homepage at root (canonical → localized). `next.config`
  redirects need a **dev-server restart** to take effect locally.
- State the **app purpose + per-scope data use ABOVE THE FOLD** (a reviewer shouldn't have to scroll), plus
  a fuller "About" section. Privacy URL must match the consent screen.
- Rejections often reflect the **pre-deploy snapshot** (review/email lag) — redeploy, then resubmit and wait.

---

## Part 7 — Submit to the ChatGPT / OpenAI plugin directory

**Gate 1 — verified developer/business identity** (in the OpenAI Platform Dashboard, "Verifications"):
- Choose **Business** for a registered company; business type **Entity** for an LLC (NOT "Sole Proprietor").
  You'll attest control-person / beneficial-owner (≥25%) and pass an ID check. Takes a few days.
- Verify from the **same org** you'll submit from; submitter needs **Apps Management = Write**.

**Gate 2 — eligibility:** OpenAI restricts in-app **commerce to physical goods** (services excluded). A
booking/lead tool that **doesn't transact** (no payment/checkout; billing happens offline) is a **lead/
request tool, not commerce** — do NOT check "links/directs users out to make purchases"; affirm no sales /
no digital goods. Frame it this way if review pushes back.

**Prep (mostly code/content, do before the portal):**
- A `/terms` page and a `/privacy` page. Privacy MUST cover: categories of data, purposes, **recipients**,
  **retention timelines**, contact. Incomplete privacy = instant reject in both directories.
  - **Name the recipients as actual companies** (Cloudflare, Resend, any sibling service), not "our
    providers". Give retention as **real durations** ("90 days", "24 months"), not "as long as necessary".
    Those two omissions are the usual reject.
  - Add a short section on what an assistant does and does not send you: the tool's declared fields only,
    never the wider conversation, and that the assistant provider's own policy governs the chat itself.
  - Terms should state plainly that a submitted request creates no contract, books nothing, charges
    nothing, and that credentials are refused.
  - Link both from the site footer and include them in the sitemap; the portal asks for the URLs early and
    they must already resolve.
- **Icons:** if the brand logo is already a square emblem, both sizes are one `sips -Z <n>` each — no design
  work. Only reach for a manual crop when the source is a wide lockup.
- The `chatgpt-app-submission.json` manifest (prefills tools + test cases + app_info in one upload):
  - `$schema` **must be** `https://developers.openai.com/apps-sdk/schemas/chatgpt-app-submission.v1.json`
    (the portal rejects the `/plugins/schemas/` value even though the schema's own `const` claims it).
  - `schema_version: 1`; `app_info` {display_name, subtitle ≤30 chars, description ≤4000, category enum e.g.
    LIFESTYLE}; `tools` keyed by name, each with `annotations` (all three hints) + `justifications` (a string
    per hint); `test_cases` and `negative_test_cases`, each {description, user_prompt,
    tools_triggered, expected_output}. The manifest does **not** carry URLs — those are portal fields.
  - **`tools_triggered` is a single non-empty STRING, not an array.** It names exactly one tool. An array,
    an empty string, or an omitted value on a positive case is rejected with
    `test_cases[N].tools_triggered must be a non-empty string`. Consequences worth designing around: a case
    that deliberately triggers **no** tool (e.g. "assistant should gather missing required fields before
    calling") cannot be expressed as a positive test case — put that behavior in the tool description and
    server instructions instead. A case exercising a **chain** of two tools must be attributed to the one
    that matters. On negative cases the field may be omitted entirely, which is the right way to express a
    request refused before any tool runs.
  - **Exactly 5 test cases and exactly 3 negative test cases.** The published schema says `minItems: 5`
    and `minItems: 3` with no maximum, but the portal enforces an exact count and rejects a sixth with
    `test_cases must include exactly 5 entries`. **Portal validation is stricter than the published
    schema** — when the two disagree, the portal wins, so budget a couple of upload-and-fix rounds and
    treat each rejection message as the real spec.
  - **`annotations` and `justifications` use DIFFERENT casing in the same object.** Annotations are
    camelCase (`readOnlyHint`, `destructiveHint`, `openWorldHint`); justifications are snake_case with a
    `_justification` suffix (`read_only_justification`, `destructive_justification`,
    `open_world_justification`). Mirroring the annotation keys into `justifications` is rejected at upload
    with `Tool "<name>" must include non-empty string justifications.read_only_justification`. All three
    justifications are required and must be non-empty.
  - The manifest's annotations must **exactly match the live server's** or justifications get skipped.
- Two square PNG icons: directory icon (≥256×256) + composer icon (≥48×48). A wide logo padded to a square
  is valid but reads poorly small; an emblem-only mark is much better. macOS `sips` only center-crops
  (`-p H W --padColor` to pad to square); no offset crop — use Preview/Figma for an emblem crop.

**Portal URLs** (verified against OpenAI docs 2026-08-06):
- Submission portal: **`https://platform.openai.com/plugins`** → **Create plugin**
- Role check (need **Apps Management = Write**): `https://platform.openai.com/settings/organization/people/roles`
- Identity verification: `https://platform.openai.com/settings/organization/general`
- Expect terminology drift in the UI — "plugin", "app" and "connector" all appear for the same thing. If
  **Create plugin** is greyed out, check the role page before suspecting the org verification lapsed.

**Portal flow:** Create plugin → **With MCP** → **Standard** (same URL for all users) → upload the manifest
→ **Info** (name, developer identity = your verified org, logo, category, website=app site, support,
privacy=`/privacy`, terms=`/terms` — defaults are `example.com`, replace them) → **MCP** (server URL `/mcp`,
auth None, **domain verification**, Scan Tools) → **Skills** (skip — MCP-only) → **Prompts** (natural
starter prompts, no "Using X" prefix) → **Testing** (5+3 cases + **required Demo Recording URL**) →
**Global** (choose countries) → **Submit** (release notes REQUIRED — write a real one, not the default;
+ 7 policy attestations + mature-content = No).

**Start from this manifest skeleton.** Three separate upload rejections on the northvalleyintel.com
submission came from shapes that are not inferable from the docs. Copy this and fill it in; do not
hand-derive the field shapes from the schema, which is looser than the portal.

```jsonc
{
  "$schema": "https://developers.openai.com/apps-sdk/schemas/chatgpt-app-submission.v1.json",
  "schema_version": 1,
  "app_info": {
    "display_name": "...",
    "subtitle": "...",              // <= 30 chars
    "description": "...",           // <= 4000; state "no payment is collected"
    "category": "PRODUCTIVITY"
  },
  "tools": {
    "<tool_name>": {
      "annotations": {              // camelCase
        "readOnlyHint": true,
        "destructiveHint": false,
        "openWorldHint": false
      },
      "justifications": {           // snake_case + _justification suffix
        "read_only_justification": "...",
        "destructive_justification": "...",
        "open_world_justification": "..."
      }
    }
  },
  "test_cases": [                   // EXACTLY 5
    {
      "description": "...",
      "user_prompt": "...",
      "tools_triggered": "<tool_name>",   // single non-empty STRING, not an array
      "expected_output": "..."
    }
  ],
  "negative_test_cases": [          // EXACTLY 3
    {
      "description": "...",
      "user_prompt": "...",
      "expected_output": "..."      // omit tools_triggered when nothing runs
    }
  ]
}
```

Write a validator that checks these shapes locally so the portal is not your linter. Give every test case
a realistic name and email — reviewers run them, and the write tools send real mail.

**Portal paste sheet.** Every URL field defaults to `example.com` and every one must be replaced. Have
these ready before starting:

| Field | Value |
|---|---|
| Website URL | `https://<domain>` |
| Customer support URL | a real page; a homepage `#contact` anchor is accepted if there is no `/support` |
| Privacy policy URL | `https://<domain>/privacy` |
| Terms of Service URL | `https://<domain>/terms` |
| MCP Server URL | `https://<domain>/mcp` |
| Authentication | **None** for anonymous request-submission tools |
| Demo Recording URL | unlisted YouTube/Loom link (a **URL**, not a file) |
| Commerce checkbox | **leave unchecked** for a lead/request tool |
| Skills tab | **skip** for an MCP-only app |
| Release notes | required; the default is rejected — write real ones |

The demo field asks for coverage across web, iOS and Android. A web-only recording is normally fine for an
MCP connector, because the same server answers every client and there is no client-side component.

**Order of operations that avoids burning attempts:**
1. Deploy `/privacy` and `/terms` first — the portal asks for the URLs early and they must resolve.
2. Fill Info and MCP, run **Scan Tools**, and confirm it matches the manifest. If it differs, fix the
   server or the manifest deliberately — never edit the manifest just to match a surprise.
3. At domain verification, get the token, set the env var, **redeploy**, then `curl` and byte-compare
   before clicking Verify. Pages env vars only apply to a new deployment, and the verifier fetches once.

**Domain verification:** enter Challenge Base URL = `https://<domain>`, it gives a token; host it at
`/.well-known/openai-apps-challenge` returning the **exact token as `text/plain`**. On Cloudflare/OpenNext,
serve it from **middleware** (not just a `public/.well-known/` static file — dotfolder static assets are
unreliable), then click Verify. `curl` it and byte-compare before verifying.

**Demo Recording URL is REQUIRED (can't skip).** A **silent** screen recording is fine — it just has to
*show the tools working*. The connector is already live/public, so **add it in ChatGPT Developer Mode and
record BEFORE finishing the portal's MCP tab** (no chicken-and-egg). Force real tool calls (enable only your
connector; the booking's returned request-id is undeniable proof). Host on YouTube-unlisted/Loom, paste the
URL. If tool-call chips don't render in the UI, the specific outputs (exact estimate, request id) are the
proof — reviewers know surfacing varies.

## Part 7a — Plugin package (current portal, 2026-09)

Docs read first-hand 2026-09-30: `https://developers.openai.com/codex/plugins/build`,
`https://developers.openai.com/plugins/build/plugins`, `https://developers.openai.com/plugins/build/mcp-server`,
`https://developers.openai.com/plugins/build/skills`, `https://developers.openai.com/plugins/deploy/submission`,
`https://developers.openai.com/plugins/plugin-guidelines`. Built and merged once
(horizonpetwastesolutions.com, PR #20, handoff 23): `plugin/plugin.json`, `plugin/mcp.json`, `plugin/assets/`,
`plugin/skills/horizon-quote/SKILL.md`, validated by `tests/codex-plugin.test.ts`.

This is a **second, newer manifest format** ("Agent Plugins" — a portable schema hosted at `agent-plugins.org`,
shared between Codex CLI/IDE and ChatGPT) alongside the `chatgpt-app-submission.json` manifest in Part 7.
**The current submission docs do not mention `chatgpt-app-submission.json` anywhere** — that's silence, not an
explicit "deprecated." **Confirmed 2026-09-30:** this is the live answer — the `plugin.json`/`mcp.json`/
`skills/` ZIP is what `platform.openai.com/plugins` actually asks for and accepts today; the
horizonpetwastesolutions.com package went through 5 rounds on this exact format, was **SUBMITTED for review**
2026-09-30 21:45, **APPROVED 2026-10-15** and **published 2026-10-16** (see "What the approved Horizon package
contained" below). Keep Part 7's `chatgpt-app-submission.json` as a **fallback reference only** (it is what
medinaclean.com and the first northvalleyintel.com submission used, under the OLD portal) — do not start a
new submission from it.

**Valid `extensions["com.openai"].interface.category` values** (from
`developers.openai.com/plugins/deploy/submission-errors`, confirmed live): **Productivity, Creativity,
Developer Tools, Business & Operations, Data & Analytics, Communication, Education & Research, Security,
Finance, Healthcare, Travel, Entertainment, Other** — Title Case exactly as listed; omitting the field also
defaults to Other. `"Lifestyle"` and `"LIFESTYLE"` are both rejected with `"Select a valid category."` — that
is the SCREAMING_SNAKE_CASE enum from Part 7's `chatgpt-app-submission.json` schema, which does **not**
carry over to this dashboard's own category picker. A local service with no exact-fit category (e.g. a
pet-waste cleanup quote tool) should use **Other** rather than force a near-fit. **The banner "We couldn't
confirm the selected category…" is a WARNING, not one of the documented error codes** — the same
submission-errors page states errors block submission and warnings do not; do not keep rewriting the
listing text chasing this banner once `category` is a value from the list above and the package shows "No
issues" — submit anyway (Horizon burned two rounds, 4 and 5, on this before confirming it was non-blocking).

**Package layout — root-level, no wrapping folder.** Zip the plugin root's *contents* directly, not a parent
folder containing them: every path inside the manifests is `./`-relative to that root (e.g. `./assets/icon.png`,
`./skills/get-started/SKILL.md`), which only resolves if those files sit at the zip root.
- `plugin.json` — required.
- `mcp.json` — present when the package bundles MCP servers.
- `skills/<name>/SKILL.md` — present when the package includes skills.
- `assets/` — icons/screenshots referenced by `./`-relative paths.

**`plugin.json` fields:**
- `$schema`: `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`.
- `name` — stable, kebab-case; the plugin identifier/component namespace, and must match the `mcpServers` key
  in `mcp.json`.
- `version` (semver), `description`, `author` {name, email, url}, `homepage`, `repository`, `license`,
  `keywords`.
- `extensions["com.openai"].interface` — **the key is the literal string `"com.openai"`** (a namespaced
  identifier, like `"publisher.extension"`), **NOT** a nested `{com: {openai: {...}}}` object — the single
  easiest field to mis-code, and it fails silently (valid JSON, wrong shape) rather than throwing a validator
  error. Under `.interface`: `displayName`, `shortDescription`, `longDescription`, `developerName`, `category`,
  `capabilities` (e.g. `["Read","Write"]`), `websiteURL`, `privacyPolicyURL`, `termsOfServiceURL`,
  `defaultPrompt` (array of starter prompts), `brandColor`, `composerIcon`, `logo` (both `./`-relative into
  `assets/`), `screenshots` (array, may be empty).
- Keep `plugin.json`, `mcp.json`, and `skills/` at the plugin root; every path under `extensions.com.openai` is
  relative to that root and starts with `./`.

**`mcp.json` fields:**
- `$schema`: `https://agent-plugins.org/schemas/1.0.0/mcp.schema.json`.
- `mcpServers.<name>`: `{type: "streamable-http", url}` — one entry, `<name>` matching `plugin.json`'s `name`,
  `url` the live `/mcp` endpoint.

**`skills/<name>/SKILL.md` frontmatter:** YAML frontmatter with `name` (matches the folder) and a non-empty
`description` naming when an assistant should reach for the skill; the body should name every live tool at
least once and restate the trust invariant (request, never confirm) for any write tool.

**Portal flow** (`https://developers.openai.com/plugins/deploy/submission`, read 2026-09-30) — same
`platform.openai.com/plugins` portal as Part 7, different upload:
1. Confirm org/project ownership + developer identity verification (Gate 1, unchanged from Part 7).
2. Plugins dashboard → **Upload new or existing plugin** → choose verified identity → **Upload plugin** →
   choose the **ZIP file**.
3. Automated validation of the package; fix and re-upload on error.
4. Review the **Metadata & Skills** findings.
5. **Connect/scan the MCP server** — the portal's Connect MCP server dialog issues a **domain-verification
   challenge token**. Host it as **plain text, only the token, no JSON wrapper**, at
   `https://<host>/.well-known/openai-apps-challenge`, with `Cache-Control: no-store`. A missing route reads
   as `"Challenge endpoint returned HTTP 404"`. On Next.js App Router, add
   `src/app/.well-known/openai-apps-challenge/route.ts` returning `new Response(TOKEN, {status: 200,
   headers: {"content-type": "text/plain; charset=utf-8", "cache-control": "no-store"}})`, token in one
   exported constant — same idea as Part 7's middleware route, just the App Router shape. `curl` and
   byte-compare before clicking Verify (Part 7's gotcha applies unchanged). Then click **Scan
   Tools**/**Rescan** to read the live server's annotations against the manifest (same idea as Part 7's
   Scan Tools).
   - **Scan results are CACHED on the portal, not re-read automatically.** After ANY server deploy —
     including a tool rename — press **Rescan** before trusting what the MCPs tab shows. Horizon's round 5
     re-showed a renamed tool's OLD name as a live issue for four hours after the rename had deployed; the
     portal was still serving round 3's cached scan. Pressing Rescan re-read the live server and the issue
     vanished with no code change. Treat "the issue came back" as "did I rescan?" before treating it as a
     regression.
6. Complete **Review information** (Metadata & Skills → Review information → Review details). Horizon's r5
   package had no review block, so the form was blank and the 5 + 3 cases were typed in by hand
   (fields Scenario / User prompt / Tool triggered / Expected output) — that is what was approved.
   **Update 2026-10-28 (docs, `developers.openai.com/plugins/deploy/submission` "Automatically provide
   submission and review information"; UNVERIFIED through the portal by us):** `plugin.json` can now carry
   them under `extensions["com.openai"].review` — `test_cases.positive[]` / `test_cases.negative[]` with
   `description`, `prompt`, `tools_triggered` (string; may list several, comma-separated), `expected_behavior`
   (note: not `expected_output`), plus `demo_recording_url`, `commerce`, `commerce_description` — and
   `extensions["com.openai"].publication` {`countries` (e.g. `["US"]`), `release_notes`}. Imported cases are
   **read-only** in the dashboard (change the ZIP to change them). Exactly 5 positive + 3 negative are
   required at submission. **Never** put credentials in the ZIP: `test_credentials` and
   `reviewer_instructions` are rejected; reviewer sign-in goes in the Review details form only.
   Either way, verify every expected behaviour against the LIVE server first and keep the cases in the
   client stream so a re-submission doesn't re-derive them.
7. Select the draft → **Submit for review** → confirm policy attestations. The confirmation mail is
   "ChatGPT Plugin Submission Received" — that means SUBMITTED, not approved (Horizon 2026-09-30: the board
   wrote "accepted" from it and had to correct the record the next day).
8. The decision arrives by email ("ChatGPT Plugin Submission Approved [<plugin id>]" for Horizon, 15 days
   after submission). **Publish** is a separate, owner-only press on the approved version; then verify the
   live listing against `tools/list` (Horizon L3 2026-10-17 00:05).
9. **After publication** (docs, 2026-10-28): OpenAI rescans the live MCP server **daily**; changed tool
   metadata is evaluated per tool and *held* if flagged (the previously approved definition stays live),
   new tools stay unavailable until approved, removals take effect after a scan. Metadata/skills changes
   still need a new ZIP + review. Changing the MCP URL needs OpenAI support. So: freeze tool names/schemas
   during review, and treat every post-launch tool change as a mini-submission (Rescan, read Issues).

**Versioning:** bump `plugin.json`'s `version` on every re-upload, even a one-field fix — the portal lists
and diffs by version, and re-uploading the same version number can read as a re-run of the already-rejected
upload rather than a new one. Horizon's ZIPs were r1 `1.0.0`, r2 `1.0.0` (not bumped — avoid), r3 `1.0.1`,
r4 `1.0.2`, r5 `1.0.3`. Observed but unexplained: both OpenAI mails ("Received" 09-30, "Approved" 10-15) name
**v1.0.0** while the portal lists **1.0.3 · Published** (Horizon L3 2026-10-17 00:05) — the mail's version
label is not a reliable record of which ZIP was reviewed; check the portal.

**Keep a round log.** When a submission needs more than one round, keep a dated message → field → fix table
(portal message verbatim, the exact field it pointed at, what changed, which PR) in the client stream's
SOP — not just in memory. Horizon needed 5 rounds; re-reading
`developers.openai.com/plugins/deploy/submission-errors` BEFORE round 1 (rather than after round 2) would
have avoided the category-casing guesses in rounds 1–2, so read that page first on every future submission.

**What the approved Horizon package contained** (r5 ZIP, `complimentary-report-horizonpetwastesolutions-com/
attachments/horizon-codex-plugin-2026-09-30-r5.zip`, unzipped and diffed against r1–r4 on 2026-10-28):
- Files at the ZIP root: `plugin.json`, `mcp.json`, `assets/logo.png` (512×512), `assets/composer-icon.png`
  (96×96), `skills/horizon-quote/SKILL.md`.
- `plugin.json`: `name` `horizon-pet-waste-solutions`, `version` `1.0.3`, one-sentence purpose `description`,
  `author` = Northvalley Intelligence (the submitting developer, not the client), `homepage`, `repository`,
  `license` `UNLICENSED`, `keywords`, root `"skills": "./skills/"` (the current docs call that field Codex-only
  and say portable packages discover `skills/` automatically — it was present and harmless), and
  `extensions["com.openai"].interface` with `displayName`, `shortDescription` (≤30), `longDescription`
  (purpose sentence first), `developerName` Northvalley Intelligence, `category` **Other**, `capabilities`
  `["Read","Write"]`, the four URLs (`websiteURL`, `supportURL` = the client's `/contact`, `privacyPolicyURL`,
  `termsOfServiceURL`), exactly 3 `defaultPrompt`s, `brandColor`, `composerIcon`, `logo`, `screenshots: []`.
  No `review`/`publication` block (test cases typed by hand).
- `mcp.json`: one `streamable-http` server keyed by the plugin `name`, URL `https://www.<domain>/mcp`, **no
  auth block** (auth None chosen on the MCPs tab).
- Portal-side, not in the ZIP: domain verification via `/.well-known/openai-apps-challenge` (Next.js route),
  Rescan, the 5 + 3 cases, the YouTube-unlisted demo URL (`B2HepUf6bac`), countries, release notes,
  attestations (commerce No).
- Server: 4 tools, all three hints explicit; the write-ish tool only DRAFTS an email (`draft_quote_request_email`).

| Round | ZIP | Portal message(s) | Fix |
|---|---|---|---|
| r1 → r2 | `1.0.0` → `1.0.0` | developer shown as the client (Isaac); "Support URL is required."; "Select a valid category." (`Lifestyle`); "Add no more than three prompts."; skills check pending; MCP configuration incomplete | `author`/`developerName` → Northvalley Intelligence; `supportURL` added; category → `LIFESTYLE` (wrong guess); 4 → 3 prompts; root `skills` added; MCP tab steps are portal-side (domain, auth, scan) |
| r2 → r3 | `1.0.0` → `1.0.1` | "Select a valid category." again | category → `Other` |
| r3 → r4 | `1.0.1` → `1.0.2` | "Challenge endpoint returned HTTP 404"; tool `request_a_quote` "name appears unclear" | challenge route added; tool renamed `draft_quote_request_email` everywhere |
| r4 → r5 | `1.0.2` → `1.0.3` | "We couldn't confirm the selected category…" (warning) | description/longDescription open with one purpose sentence; pricing wording removed |
| r5 | `1.0.3` | stale tool issue → **Rescan** cleared it; category banner stayed (non-blocking) | submitted as is, 2026-09-30 21:45 → approved 2026-10-15 |

Sources: Horizon SOP `attachments/sop-openai-directory-submission-2026-09-30.md` round tables; Horizon L3
2026-09-30 03:20–17:25; L2 2026-09-30 17:50 and 2026-10-15 13:05.

**Validator test pattern** (`tests/codex-plugin.test.ts`, horizonpetwastesolutions.com): a static contract check
mirroring Part 3's philosophy — assert the manifest shapes without a network call, then gate a live check
behind an opt-in env var:
- `plugin.json`: `$schema` literal match; `name` kebab-case and equal to the live server's name; `version`
  matches semver; `description` non-empty; `extensions["com.openai"].interface` carries every required field
  non-empty; `websiteURL`/`privacyPolicyURL`/`termsOfServiceURL` equal the live site's own URLs (`/privacy`,
  `/terms`) — not hand-typed copies that can drift; `composerIcon`/`logo`/each `screenshots` entry resolve to a
  real file under `assets/`.
- `mcp.json`: `$schema` literal match; exactly one `streamable-http` server; its `url` equals the live `/mcp`
  endpoint; its key equals `plugin.json`'s `name`.
- `skills/<name>/SKILL.md`: file exists; frontmatter has `name` + non-empty `description`; body mentions every
  live tool by name.
- Package shape: `plugin.json`, `mcp.json`, `assets/`, `skills/` all exist at the plugin root.
- Opt-in live check (env-var gated, not run by default in CI): fetch both `$schema` URLs at `agent-plugins.org`
  and confirm 200 — presence/reachability only, not a full JSON Schema validation; print a skip notice when the
  env var is unset so a green run is never mistaken for a live-schema proof.

## Part 7b — OAuth-protected server (per-user data) — submission specifics

Written 2026-10-28 for smartcashsheet (the first Northvalley submission with auth ≠ none), from first-hand
reads of `developers.openai.com/plugins/deploy/submission.md`, `/plugins/build/plugins.md` ("Configure MCP
authentication"), `/plugins/deploy/submission-errors.md`, `/plugins/plugin-guidelines.md`, plus the live
smartcashsheet production server. **Not yet proven through the portal** — treat portal behaviour below as
UNVERIFIED until a submission has gone through; record each round's real messages here.

**Auth is declared in `mcp.json`, not typed into the portal.** The MCPs tab "reads advanced authentication
settings from your package's `mcp.json`" and "doesn't provide an advanced OAuth settings editor". Put it on the
server entry, under the server's own `extensions["com.openai"].auth` (not in `plugin.json`):
```json
{ "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
  "mcpServers": { "<name>": { "type": "streamable-http", "url": "https://<host>/<mcp-path>",
    "extensions": { "com.openai": { "auth": { "type": "oauth", "client": { "mode": "dcr" } } } } } } }
```
- `type`: `none` | `oauth` | `mixed` (public + OAuth) | `api_key` — **the portal has no API-key/bearer flow**
  ("Uploading an API-key declaration alone won't complete MCP setup"); never embed a token in `headers`
  (public submission rejects non-empty headers); never declare a protected server as `none`.
- Client registration `client.mode`: `dcr` (Dynamic Client Registration — registration endpoint from
  discovery, or `registrationUrl` override; no client id/secret in the package), `cimd` (Client ID Metadata
  Document, falls back to DCR), or `provided` (`clientId` + `tokenEndpointAuthMethod`; the secret is typed in
  the portal, `clientSecret` in the manifest is rejected). Supabase Auth's OAuth 2.1 server supports DCR once
  "Allow Dynamic OAuth Apps" is on — use `dcr` and let discovery supply the endpoints.
- Overrides only when discovery can't supply them: `authorizationUrl`, `tokenUrl`, `registrationUrl`,
  `authorizationServerBase`, `resource`, `baseScopes`, `defaultScopes`, `oidc*`. Field names are
  case-sensitive (`clientId`, not `client_id`).
- "Existing client registration can lock credential changes" — check the saved connection after a new upload
  instead of assuming it replaced the client. The portal's DCR client becomes a real OAuth app on the
  provider (e.g. Supabase → Authentication → OAuth Apps): **never delete it in a probe-client clean-up.**

**Discovery the server must serve (smartcashsheet, verified live 2026-10-28):** unauthenticated `POST /api/mcp`
→ `401` with `WWW-Authenticate: Bearer realm="…", resource_metadata="https://<host>/.well-known/oauth-protected-resource"`;
that RFC 9728 document (also at the path-aware `/.well-known/oauth-protected-resource/<mcp-path>`) lists
`resource`, `authorization_servers`, `bearer_methods_supported: ["header"]`, `scopes_supported`; the
authorization server's metadata (`<as>/.well-known/oauth-authorization-server…`) carries
`registration_endpoint`, `code_challenge_methods_supported` incl. `S256`, and
`token_endpoint_auth_methods_supported` incl. `none` (public PKCE clients). With OAuth, **`initialize` and
`tools/list` also return 401** — you cannot read the tool list anonymously; read tools from source, and let
the portal's scan (after you authorize) be the live check. Serve on the canonical host (apex → `www` 307
redirects are a risk for POST clients; give the portal the `www` URL).

**What the portal asks for when auth ≠ none** (docs, `plugins/deploy/submission` §2–3):
1. MCPs → **Connect**: check URL + Authentication read from `mcp.json`; complete **domain verification**
   (same `/.well-known/openai-apps-challenge` plain-text token as Part 7a; for a production app whose code is
   released on a schedule, ship the route reading the token from an env var *before* the portal session so
   the token is an env change + redeploy, not a code release); then **authorize an account** so the portal
   can scan — use the reviewer test account, never a real user's.
2. **Reviewer credentials** in Review information → Review details (never in the ZIP): "a dedicated test
   account, login URL, workspace or tenant details, and sign-in instructions. Use sample data, not a real
   user's account. The account needs the permissions and data required by your test cases and should work
   immediately **without MFA approval, email or SMS codes, magic links, or private-network access**." "Keep
   the test account and sample data available for subsequent reviews." Final submission requires
   "Reviewer-ready demo credentials when the server uses OAuth" (`submission-errors`).
   - Plan/entitlement gates: if tools are gated by a paid plan, the reviewer account must be on that plan
     for the whole review (comp it; don't rely on a checkout that can lapse — Horizon's review took 15 days).
   - Use a mailbox you control; a public inbox (yopmail etc.) lets anyone reset the reviewer password.
   - Creating that account on a client's production is a production write: it is the client's/owner's
     step, not an agent's, wherever production is read-only for agents.
3. **Consent page** (the authorization server's UI on your host): guidelines — "the flow must be transparent
   and explicit. Users must be informed of all requested permissions, and those requests must be limited to
   what is necessary". In practice: name the account being connected, render every scope in plain words
   (e.g. `offline_access` → "Keep this connection active until you disconnect it"), list what each tool can
   see, say it can't change anything, and say where to disconnect. The demo video must show this page.
4. **Scopes:** request the minimum (identity + the read scopes the tools need); disclose any refresh-token
   scope in the consent card and the privacy policy.
5. **Privacy policy / terms** must exist for MCP review and meet the guidelines' minimum: categories of data,
   purposes, **categories of recipients**, **retention timelines**, user controls — "as long as necessary"
   fails. For per-user data add: what the assistant receives (tool results only, never the chat), what you
   log for each call and for how long, how to disconnect. The listing URLs must "identify the same publisher
   as the submission" — submit under the verified identity of the company named on those pages.
6. **Annotations on read tools:** `readOnlyHint: true` only if the call modifies nothing — "Use `false` for …
   persisting artifacts". Audit-log rows are generally fine; a read path that also refreshes/syncs user
   records is not literally read-only — remove that write from the MCP path or be ready to appeal with the
   reason. `openWorldHint: false` is right for "a bounded private account". Annotation **justifications**:
   the guidelines (2026-10-28) say "no longer required", but `submission-errors` still lists "a justification
   for each value on every MCP tool" — prepare them anyway.
7. **Response minimization** (guidelines, Tool data handling): do not return internal row ids, sync
   timestamps or request ids unless the user's question needs them — per-user finance/CRM data paths reused
   from an in-app assistant usually carry them; strip them in the MCP layer.
8. **Plan/upgrade wording:** a tool may say a feature needs a different plan but "must not … promote
   upgrades" or start a checkout — "Upgrade to use this" is upsell wording; state the fact only.
9. **Regulated categories (finance, health):** keep tools to figures/information, never a verdict or advice;
   say "not financial advice" in the listing; no restricted inputs (PCI card data, PHI, government IDs,
   credentials/OTPs).

## Part 8 — Submit to the Claude / Anthropic connector directory

- Portal: **claude.ai admin settings → directory submissions** — requires a **Team or Enterprise** org
  (individual plans can't submit; the connector still works by URL). Submitter needs Directory-management /
  Libraries permission.
- Requirements: tool `title` + `readOnlyHint`/`destructiveHint` on every tool; **no-auth is an allowed**
  connection type; public privacy policy (incomplete = instant reject); a reviewer test account/instructions
  (for a public no-auth connector, none needed — but note a write tool will send real notifications during
  review); MCP Apps (interactive UI) also need 3–5 PNG screenshots.
- Portal steps: Info → Connection → Tools (auto-sync; fix missing annotations on the server first) → Listing
  (name ≤100, tagline ≤55, description ≤2000, categories, docs URL, privacy URL, support, icon, permanent
  slug) → Use cases → Company → Authentication (None) → Data handling → Test & launch → Compliance (7
  acknowledgments) → Review.

---

## Part 9 — Passing the directory REVIEW (real OpenAI rejections 2026-08-22 and 2026-09-19; horizonpetwastesolutions.com SUBMITTED 2026-09-30, APPROVED 2026-10-15)

Both first submissions were rejected AFTER clean portal uploads. Submission mechanics (Part 7) and passing
human review are different games. Design for the reviewer from day one:

**Rejection 1 — medinaclean.com: "app solicits sensitive personal data" + "returns personal identifiers
that isn't required for the user's request."** Root causes and the shipped fixes, all generalizable:
- **No credential-shaped input fields.** The abuse-gate `secret` argument read as soliciting sensitive
  data (see Part 2). Remove it from the schema entirely; reviewers judge the schema, not your intent.
- **Constrain every free-text field or it reads as a PII invitation.** An unconstrained `notes` field
  implies "put anything here." Fix: description states its narrow purpose and an explicit prohibition
  ("Brief access/scheduling notes only (e.g. pets, gate code, parking). Do NOT include health, payment,
  ID/SSN, or other sensitive information — such notes are rejected."), AND the server enforces it by
  rejecting submissions whose notes contain sensitive patterns. Say "rejected", and mean it in code.
- **Write minimization + purpose + privacy into the write-tool description itself:** what is collected,
  why each field is needed, "used solely to…, never sold, never used for anything else", plus the privacy
  URL. The description is your consent/disclosure surface — the reviewer won't hunt for your privacy page.
- **Never echo input PII in tool results.** Return a request id + status ("pending_review") only. Echoing
  the name/phone/address back is "returning personal identifiers not required for the request" — the
  assistant already has what the user typed; repeating it only creates a violation.

**Rejection 2 — northvalleyintel.com: "one or more of your test cases did not produce correct results."**
- **The submitted test cases are a CONTRACT the reviewer executes.** Every `expected_output` claim (e.g.
  "lists four review areas", a specific phrase like "agent-native service delivery") must be literally
  satisfiable from the live tool output on the day of review. The rejection reproduced instantly with one
  live `tools/call`: the tool output contained zero of the four promised review areas — output had drifted
  from the submission.
- **Wire the submission JSON into CI as the source of truth.** Keep `chatgpt-app-submission.json` in the
  repo and make the contract validator (Part 3) assert each test case's expected claims against real tool
  output — in static mode against the local server, in live mode against prod. Then output/submission
  drift fails a build instead of a review cycle (each cycle costs days).
- **Before resubmitting, re-run every submitted test case against the LIVE endpoint yourself** — not the
  source, not a preview: the exact URL the reviewer will hit. Green deploy + correct merged source still
  produced a stale live endpoint here (see gotcha below); resubmitting on source-level evidence would have
  burned the appeal on an infrastructure defect.

**Rejection 3 — northvalleyintel.com v1.0.2, 2026-09-19: four reasons, none new individually — run this
checklist before every (re)submission.** The email cited: test cases didn't produce correct results
consistently on both ChatGPT web AND mobile; annotations must be explicit `true`/`false` (never null) with a
justification tied to the tool's actual behavior; tools request input data that's overly broad, unnecessary,
or includes the full conversation history; the app solicits sensitive personal data (health, biometric, SSN,
payment-card). Treat all four as a pre-submission gate, not a one-time fix:
- [ ] Re-run every submitted test case against the **live** endpoint from **both** ChatGPT web and ChatGPT
  mobile. Rejection 2's rule below ("re-run against the live endpoint") was proven web-only; mobile is a
  separate client/session surface and can diverge from web on the same server.
- [ ] Every tool's three hints (`readOnlyHint`/`destructiveHint`/`openWorldHint`) are explicitly `true` or
  `false` — never omitted or null — diffed against the live `tools/list`, each with a plain-English
  justification describing that tool's *actual* behavior, not a template sentence copied across tools.
- [ ] Every tool's `inputSchema` asks for only the fields that specific call needs. No field is shaped to
  capture or forward the full conversation history, and no field is an unconstrained catch-all beyond what
  Part 2's free-text minimization already requires.
- [ ] No tool schema, description, or server instruction solicits health information, biometric data, SSNs,
  or payment-card data — grep every field's name and description for these categories before submitting;
  don't rely on memory of what was added months ago.

**Checklist — horizonpetwastesolutions.com, Agent Plugins format, SUBMITTED 2026-09-30 after 5 portal rounds, APPROVED 2026-10-15: what
actually worked.** Most of the 5 rounds were avoidable by reading
`developers.openai.com/plugins/deploy/submission-errors` first instead of after round 2 — run this
checklist BEFORE the first upload of a `plugin.json` package, not after a rejection:
- [ ] `extensions["com.openai"].interface.category` is one of the exact Title Case values from Part 7a's
  list (or omitted for Other) — never the old `chatgpt-app-submission.json` SCREAMING_SNAKE_CASE enum, and
  never a near-fit guess like `"Lifestyle"`.
- [ ] If the portal still shows "We couldn't confirm the selected category…" after that, check whether the
  package shows "No issues" overall and whether this message appears on
  `plugins/deploy/submission-errors` as a documented error — if not, it's a non-blocking warning; submit
  rather than keep rewriting the listing.
- [ ] Every tool is named for exactly what it does, not what it aspires to do — a tool that only drafts an
  email and does not send/book anything is named `draft_..._email`/`draft_..._request`, not
  `request_...`/`book_...`. Rename consistently everywhere the tool is referenced (server, `plugin.json`,
  `mcp.json` is unaffected, `skills/<name>/SKILL.md`, tests, the client SOP) — a partial rename reads as a
  new unclear name.
- [ ] `description` and `longDescription` both open with ONE plain sentence stating the plugin's single
  purpose before any detail on how it works; neither field advertises pricing (state that pricing
  information is available via a tool, never quote the price itself in the listing text).
- [ ] The domain-verification challenge token is live at `/.well-known/openai-apps-challenge` (plain text,
  only the token, `Cache-Control: no-store`) BEFORE running Scan Tools/domain verification on the MCP tab —
  `curl` and byte-compare first.
- [ ] After every deploy to the live MCP server (a rename, a new tool, an annotation fix), press
  **Rescan** on the portal's MCPs tab before reading its findings — scan results are cached and a fixed
  issue can appear to "come back" for hours on a stale scan.
- [ ] The Review-information test-case form is filled in by hand (it is not prefilled from `plugin.json`);
  every `expected_output` typed in was just verified against a live `tools/call`, not assumed from the
  manifest or memory.
- [ ] `version` in `plugin.json` is bumped from the last uploaded value, even for a one-field fix.
- [ ] A dated message → field → fix table for this submission exists in the client stream's SOP (not just
  in chat/memory) so a later round, or a different reviewer's rejection, doesn't re-derive the same fixes.

**Pre-submission checklist (merged 2026-10-28: rejections 1–3 + Horizon's approved run + Part 7b OAuth). Run
it top to bottom before the FIRST upload; every item is a past rejection, a past portal round, or a
documented final-submission rule.**
- [ ] Read `developers.openai.com/plugins/deploy/submission-errors` and `/plugins/deploy/submission` today
  (append `.md` for raw text) — the field reference moves; Horizon lost rounds 1–2 and 4–5 to not doing this.
- [ ] Publisher: the verified developer identity = the company named on the privacy/terms pages; the
  submitter has Apps Management = Write in that org.
- [ ] Owner/client written go to list the app (directory listing is promotion, not just a connector).
- [ ] `/privacy` + `/terms` live, with named recipients, real retention durations (incl. the MCP call log),
  what the assistant receives, how to disconnect, a visible date. (Rejection 1; guidelines.)
- [ ] `supportURL` is a real support/contact page (Horizon r1 "Support URL is required").
- [ ] Icons square PNG, logo ≥512 recommended (docs minimum 48), composer 96; from a real emblem, not a lockup.
- [ ] `plugin.json`: `$schema`, kebab `name` = `mcp.json` key, bumped semver, purpose-first `description` and
  `longDescription`, `displayName`/`shortDescription` ≤30, `developerName` = publisher, `category` from the
  documented Title-Case list (Horizon r1–r3), ≤3 `defaultPrompt`s ≤128 chars (Horizon r1), no pricing/upsell
  text (Horizon r4), four HTTPS URLs.
- [ ] `review` block: exactly 5 positive + 3 negative, each positive with `tools_triggered` + `expected_behavior`
  that the LIVE server satisfies on ChatGPT **web and mobile** (rejections 2–3); `demo_recording_url`;
  `commerce: false` unless physical goods; no credentials in the ZIP.
- [ ] Every tool: name says exactly what it does (Horizon r3), all three hints explicit booleans matching
  behaviour (a read path must not write), justifications prepared (rejection 3).
- [ ] Every input: minimal, purpose-stated, no credential-shaped field, no restricted data, no conversation
  history/location, free text constrained (rejections 1 and 3).
- [ ] Every output: no echoed input PII, no internal ids/timestamps the question didn't need (rejection 1;
  guidelines).
- [ ] OAuth only: `mcp.json` auth block; discovery verified live (401 + resource_metadata → AS metadata with
  `registration_endpoint`/S256); consent page names the account, plain-language scopes, data list, disconnect
  path; reviewer account on the right plan, sample data, no MFA/codes, mailbox you control, kept for later
  reviews (Part 7b).
- [ ] Challenge route live (env-driven for release-gated apps), byte-compared before Verify (Horizon r3).
- [ ] After every server deploy: **Rescan** before reading MCP findings (Horizon r5).
- [ ] Demo video: shows the connect (OAuth consent) flow and the main tools on the reviewer account, nothing
  real; unlisted URL plays signed-out.
- [ ] Release notes written; countries chosen; attestations answered honestly.
- [ ] Record: "Submission Received" = submitted; only "Submission Approved" = approved; Publish is the owner's
  press; verify the live listing after (Horizon 2026-09-30 correction, 2026-10-17 check).

**Resubmitting after a rejection:** open the app in the portal and click **Edit — not "View plugin"**. The
View page is read-only and Scan Tools renders empty/disabled there, which reads as a broken portal or a
need to re-upload files; it isn't. In Edit mode, re-run Scan Tools (so the portal re-reads the FIXED live
schema), keep test cases unless an expected_output referenced removed behavior, write real release notes
describing the remediation, and re-attest. No manifest re-upload is needed when the tool set and
annotations are unchanged — verify that with a diff against live tools/list, not by memory.

**Both rejections arrived as email with no field-level pointers** ("please see the details below" + a
category sentence). Reproduce the violation yourself against the live endpoint before fixing — the fix
must make the reviewer's category sentence impossible, not just plausible-looking.

## Deploy/verify gotchas (Cloudflare) — burned real time on these

- **Edge cache:** pages ship `s-maxage=300`, so right after a deploy the bare URL serves the OLD version for
  up to ~5 min. Cache-bust with `?cb=<nanos>` (query strings aren't always honored — also check
  `cf-cache-status`) to confirm content is live. `/mcp` itself is dynamic (not cached).
- **Worker propagation lag:** immediately after a deploy, some edges still serve the previous Worker — an MCP
  `tools/list` can show stale annotations for a minute. Re-check before concluding a change didn't ship.
  This bit three times in one session on northvalleyintel.com: a brand-new page 404ing, `www` serving older
  markup than the apex, and a fresh `robots.txt` missing its new rules — all correct within a minute. **Make
  re-probing the default response to a post-deploy failure**, before editing anything. Cache-busting does not
  help here; it is Worker propagation, not the CDN cache.
- **Domain-verification token:** serve it from middleware and return the bare token as `text/plain`. Set it
  from an env var so the route 404s until configured, and remember Pages env vars only take effect on a
  **new deployment** — set the variable, redeploy, `curl` and byte-compare, and only then click Verify. The
  verifier fetches once.
- **Always deploy from `main` via PR**, let CI (lint/typecheck/coverage/e2e/build/**cf:build**/audit) gate it,
  then verify the live endpoint/page directly (curl `/mcp`; screenshot the page).
- **"Deploy green" is not "live correct" — even beyond the propagation window.** On northvalleyintel.com
  (2026-08-22) a squash-merged PR showed a successful Pages deploy, the merged source verifiably contained
  the new output, yet live `/mcp` still served the OLD tool output hours later — a build-pipeline/edge
  defect, not propagation. Root cause when finally run to ground: the custom domain's CNAME pointed at a
  DIFFERENT, stale Pages project (`<name>-43m.pages.dev`) left over from an earlier setup — CI deployed to
  the right project for weeks while the domain never looked at it. When live and pages.dev disagree, diff
  the DNS target against the project CI deploys to before suspecting the build; and delete superseded
  Pages projects instead of leaving them attached to domains. Treat the live diff itself as the acceptance
  test for anything you'll resubmit to a reviewer.
- **Give every deploy workflow `workflow_dispatch`.** cloudflare-pages.yml without it means the only
  redeploy lever is a fresh push (or clicking around the dashboard) — exactly when you need a clean rebuild
  to rule the pipeline out. Add the trigger when you first touch the workflow, not when you're stuck.

## Second-implementation notes (northvalleyintel.com, 2026-08-06)

What actually cost time the second time round, none of it MCP-specific:

- **Three sequential manifest rejections**, all shape rather than substance: camelCase justification keys,
  six test cases where exactly five are allowed, and `tools_triggered` as an array where a string is
  required. The skeleton above prevents all three. The content of the claims was never questioned.
- **Believing a stale assumption about the stack.** The project was thought to have no persistence, so a
  new KV binding was nearly provisioned — while an existing D1 database and a working row-count throttle
  sat in the same repo. Grep the config before concluding what a project does not have.
- **A credential that verifies but cannot act.** `/user/tokens/verify` returned `active` for a token with
  zero zone visibility. Probe the specific resource you need during planning, not the generic verify
  endpoint, or you will plan automation you cannot perform.
- **Post-deploy propagation read as failure three separate times** — a new page 404ing, `www` serving older
  markup, a fresh `robots.txt` missing rules. All correct within a minute. Re-probe before editing.
- **Env vars stored as secrets cannot be read back**, so a misconfigured sender is invisible from the API;
  the only evidence is the `From:` header on a delivered message. Prefer changing them in the dashboard
  over an API patch that could clobber values you cannot restore.

Worth repeating because it generalised: an assistant-origin write path was verified end to end by calling
the live tool and reading the resulting email, not by trusting a green CI run. Every genuine defect this
session — an unreachable subdomain, a sender that could not deliver to customers, a missing table — passed
every local and CI check right up until something real was driven against production.

## One-line reusable checklist
Reuse existing intake · request-never-confirm · web-standard transport (Pages Function is fine, often
better) · pin the SDK · all-three tool annotations matching the manifest · reuse the existing DB for the
throttle, fail closed without it · verify stateless flow live, on the PR preview before merge · static
no-redirect home w/ purpose above the fold (OAuth) · `/terms` + `/privacy` with **named recipients and real
retention durations** · `$schema`=apps-sdk URL · justifications snake_case, annotations camelCase ·
**exactly** 5 + 3 test cases · `tools_triggered` is a **string** · replace every `example.com` default ·
domain token via middleware, set var → **redeploy** → byte-compare → then Verify · OAuth: auth in `mcp.json`
(`dcr`), reviewer account w/o MFA on the right plan, plain-language consent page, read path writes nothing,
no internal ids in results · Submission Received ≠ Approved · silent demo recorded via
live connector · business=Entity verification · booking=lead not commerce · re-probe before believing a
post-deploy failure · **no `secret`/credential-shaped tool args** · constrain free-text fields + reject
sensitive content server-side · minimization + purpose + privacy URL in write-tool descriptions · results
return request-id + status, **never echo input PII** · submitted test cases are a contract — validate them
in CI against real output and re-run them against the LIVE endpoint before (re)submitting · deploy
workflows get `workflow_dispatch`.
