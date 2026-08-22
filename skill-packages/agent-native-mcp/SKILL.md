---
name: agent-native-mcp
description: Make a website/service agent-native — build a Model Context Protocol (MCP) server that lets AI assistants (Claude, ChatGPT, Gemini) use it, then get it listed in the assistant directories. Use when adding an MCP booking/lead/tools front door onto an existing web app (especially Next.js on Cloudflare Workers/OpenNext), reusing the app's existing intake/notification/logic, and when preparing or walking a client through the ChatGPT (OpenAI) or Claude connector-directory submission. Also covers Google OAuth branding verification when the app uses Google scopes.
metadata:
  source: medinaclean.com GEN-001 (agent-native MCP lane) + GEN-002 directory submission, 2026-08;
    northvalleyintel.com second implementation (Cloudflare Pages Functions variant), 2026-08-06
  status: battle-tested on two independent stacks (live MCP booking in Claude + ChatGPT;
    OpenAI directory submitted for medinaclean.com; northvalleyintel.com/mcp live);
    both first OpenAI submissions REJECTED 2026-08-22 — causes diagnosed, fixes shipped,
    lessons folded into Part 2 and Part 9
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

## Part 9 — Passing the directory REVIEW (from two real OpenAI rejections, 2026-08-22)

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
domain token via middleware, set var → **redeploy** → byte-compare → then Verify · silent demo recorded via
live connector · business=Entity verification · booking=lead not commerce · re-probe before believing a
post-deploy failure · **no `secret`/credential-shaped tool args** · constrain free-text fields + reject
sensitive content server-side · minimization + purpose + privacy URL in write-tool descriptions · results
return request-id + status, **never echo input PII** · submitted test cases are a contract — validate them
in CI against real output and re-run them against the LIVE endpoint before (re)submitting · deploy
workflows get `workflow_dispatch`.
