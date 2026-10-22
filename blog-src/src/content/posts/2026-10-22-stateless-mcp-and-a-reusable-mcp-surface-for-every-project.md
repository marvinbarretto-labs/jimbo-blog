---
title: "Stateless MCP and a reusable MCP surface for every project"
date: 2026-10-22
description: "Stateless MCP and a reusable MCP surface for every project"
tags: [mcp, report]
public: false
---

*Report — a research report (2026-10-22), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

Jimbo's `/mcp` server is stateless in the **SDK sense** (no session store, a fresh server and transport per request). It was not built for the new 2026-07-28 spec, which makes statelessness part of the *protocol*. These are related but not the same thing. Keep the current shape: it is already the right architecture. Copy `route.ts`, `helpers.ts` and the `server.ts` factory into each project and write only the tool files. Don't publish a shared package yet.

## From prior context

(Vault note "Spike: stateless MCP", grounded 2026-07-30 and verified 2026-10-02.) Settled: Jimbo already runs stateless since 21 Jun 2026; no migration pending; no other project has an MCP surface; NotebookLM is a manual step for Marvin. I re-read the code in `jimbo-api` (HEAD `d16c231f`) and confirm it. I did not re-research those points.

## Part 1: Stateless MCP

### What `sessionIdGenerator: undefined` changes
In `src/mcp/route.ts` the transport is `WebStandardStreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true })`, built **inside** the request handler together with a new `McpServer` from `createMcpServer`.
- **No `Mcp-Session-Id`.** In the 2025 spec's stateful mode the server mints an ID on `initialize` and the client echoes it on every later request, so the server must remember who it is talking to. With `undefined`, the SDK skips that and accepts each POST on its own.
- **Nothing outlives a request.** The server object, its tool registrations and the transport are built, used and dropped per call. Any instance (or a restart mid-conversation) can answer any call. Cost: re-registering about 13 tool groups per request, which is cheap in-process.
- **`enableJsonResponse: true`** returns a plain JSON body instead of an SSE stream for the reply. That is why a POST holds no connection open while idle.
- **GET and DELETE return 405** (`Allow: POST`). GET is the standalone server-to-client SSE stream; DELETE ends a session. A stateless server has nothing to push or end. The 1 Oct 2026 incident in the `route.ts` comment is the proof: an idle GET stream broke Claude Code after Mac sleep, and removing it fixed that.
- **Per-request context is rebuilt from the HTTP request**: `caller` (from `apiKeyAuth`), write origin and API key are passed into `createMcpServer`. This is what replaces session state for auth and telemetry.

### What stateless gives up (stateful features Jimbo doesn't use)
- Server-to-client push: resource-change and tool-list-changed notifications over the GET stream.
- Resource subscriptions.
- Server-initiated requests mid-call (sampling, elicitation, roots) on the same connection.
- Resumable streams (`Last-Event-ID`) and long-running calls that survive a dropped connection.
- Per-connection state: "this client picked a workspace" or a per-session tool list.

None are needed while every tool is single-shot request/reply, which is the stated assumption in `route.ts`.

### When a project would want sessions back
Only for: live push (e.g. a gym-app live workout feed or a collectr price alert streamed to the agent), tools that must ask the user a question halfway, or a streaming long job. Even then, the 2026 spec's answer is **not** to bring sessions back (see below): use explicit handles (an ID the server issues and the agent passes back as a normal tool argument), polling (the tasks extension), or the new `subscriptions/listen`. For almost every project the right move is a tool like `start_x` returning an ID, and `get_x(id)`.

### The news: the 2026-07-28 spec makes this the norm
The official changelog says the 2026-07-28 revision:
- removes protocol-level sessions and `Mcp-Session-Id` (SEP-2567); servers needing cross-call state use server-minted handles passed as ordinary tool arguments;
- removes the `initialize` handshake; every request carries protocol version and client capabilities in `_meta` (SEP-2575);
- makes `server/discover` mandatory for servers;
- replaces the GET endpoint and `resources/subscribe` with `subscriptions/listen`, a long-lived POST-response stream;
- removes SSE resumability;
- adds required `Mcp-Method` / `Mcp-Name` headers on POST so gateways can route and rate-limit without parsing bodies (SEP-2243);
- adds `ttlMs`/`cacheScope` on list results, and `resultType` on all results;
- moves tasks to an extension and replaces server-initiated requests with a "multi round-trip" retry pattern (SEP-2322);
- deprecates Roots, Sampling, Logging and Dynamic Client Registration.

**Gap versus Jimbo:** Jimbo is on `@modelcontextprotocol/sdk@1.29.0`, and its own test sends `protocolVersion: '2025-06-18'` through `initialize`. So it is stateless-by-configuration on the old protocol, not a 2026-spec server: it still has an `initialize` call and no `server/discover`. The TypeScript SDK v2 (new packages `@modelcontextprotocol/server` / `client`, a codemod, and a handler that serves 2026 requests and, by default, 2025 traffic as well) is the supported path. Nothing breaks today because 2025-era clients still work. Treat the v2 migration as a separate, later task; it touches `route.ts` and the imports in each tool file, not the tool logic.

## Part 2: The reusable pattern ("thin MCP over your own API")

Name: **Per-request MCP facade.** A stateless Hono route; a factory that builds a fresh server each request; tool files that are thin wrappers over services the project already has; one instrumentation wrapper.

### Copy as-is
| File | What it is | Notes |
|---|---|---|
| `src/mcp/route.ts` | Auth middleware, 405 for GET/DELETE, per-request server + transport, `sessionIdGenerator: undefined`, `enableJsonResponse: true` | Change only the `apiKeyAuth` import and how `caller` is read. Keep the 405 comment; it records why. |
| `src/mcp/helpers.ts` | `jsonResult` and `makeInstrumentor` (Sentry capture, one stdout JSON line per call, fire-and-forget DB row) | Change the `insertMcpCall` import to the project's telemetry sink, or drop the DB insert and keep the log. |
| `src/mcp/route.test.ts` | The 405 / 401 / initialize-over-POST tests | Change the env var for the key and the expected `serverInfo.name`. |

### Change per project
| File | What changes |
|---|---|
| `src/mcp/server.ts` | `name`/`version`, and the list of `registerXTools(...)` calls. Keep the shape: `createMcpServer(caller, origin, apiKey)` returns a new `McpServer`. |
| `src/mcp/tools/*.ts` | All of it. Pattern per tool: a zod `inputSchema` (`.describe()` on every field, since the description is what the agent reads), `server.registerTool(name, {title, description, inputSchema: Schema.shape}, instrumentTool(name, async (args) => jsonResult(await service(args))))`. Parse args again with the zod schema inside the handler. |
| Mount line in `app.ts` | `app.route('/mcp', mcp)` |
| Auth keys | One scoped key per client (Jimbo's `SCOPED_KEY_VARS` pattern) so each agent is attributable in telemetry. |

### Optional pieces worth copying later
- `tools/api-read.ts` (`api_get`): one generic read tool over the whole HTTP API, forwarding the caller's key so ordinary auth still applies. It plus `api-pages.ts` (all-pages paging) saves writing a read tool per endpoint. Use this first in a new project and add hand-written tools only for writes and composed reads.
- `mcp_calls` table: one place to see which tools agents actually call.

### Checklist for a new project
1. `npm i @modelcontextprotocol/sdk` (or the v2 packages if starting after the migration; the file shapes are the same).
2. Copy `route.ts`, `helpers.ts`, `route.test.ts`; fix imports.
3. Write `server.ts` with an empty tool list; confirm the `initialize` test passes.
4. Add `api_get` or 2-3 read tools over existing services. Descriptions say *when* to use the tool and what is ground truth.
5. Add write tools last, each taking `origin`/`caller` so writes are attributable.
6. Mount at `/mcp`, behind the project's key auth; give each agent its own key.
7. Verify GET and DELETE return 405 and POST needs a key; check Caddy does not buffer or time out POST.
8. Register in Claude Code (`claude mcp add --transport http <name> <url>`) and call one tool.

### Not a shared package (yet)
The copied files are ~170 lines. A package would need to abstract auth, telemetry and the ORM, and the SDK is about to change major version. Copy now; extract after the third project, when the real shared surface is visible.

## Recommendation
1. Do nothing to Jimbo's stateless setup. It is correct, and the 405 fix is already in.
2. For the next project (start with the one agents touch most), copy the three files above and begin with a generic read tool.
3. Schedule the SDK v2 migration once, in jimbo-api, *before* copying to many projects, so copies start on the new packages. It is a separate task (this one is explicitly not to change jimbo-api).
4. Don't add sessions back. If a feature needs state, mint a handle.

Note: the task's AC named `docs/research/mcp-stateless-and-reusable-surface.md` in the repo; the dispatch contract for research is cairn-only, so this is published there and not committed.

## Sources
1. https://modelcontextprotocol.io/specification/2026-07-28/changelog — official list of changes (sessions, handshake, discover, headers, deprecations)
2. https://blog.modelcontextprotocol.io/posts/2026-07-28/ — official release post for the 2026-07-28 spec
3. https://www.infoq.com/news/2026/08/mcp-stateless-gateway/ — InfoQ: "MCP goes stateless", gateway/header routing and the "just an API again" debate
4. https://developers.googleblog.com/scaling-ai-agent-infrastructure-with-the-mcp-stateless-updates/ — Google on scaling with stateless MCP
5. https://aaif.io/blog/mcp-2026-changes-the-rules — Agentic AI Foundation summary of 2026 changes
6. https://equixly.com/blog/2026/08/05/stateless-mcp/ — security implications of stateless MCP
7. https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28 — TypeScript SDK v2 migration guide for the new revision
8. https://newreleases.io/project/github/modelcontextprotocol/typescript-sdk/release/v2.0.0-beta.1 — TS SDK v2 release notes
9. https://dev.to/fabwaseem/stateless-mcp-servers-what-the-2026-07-28-spec-changed-and-how-to-migrate-5ccl — migration walkthrough
10. https://newsletter.victordibia.com/p/mcp-july-2026-update-stateless-core — overview of stateless core, extensions, tasks
11. jimbo-api `src/mcp/route.ts`, `server.ts`, `helpers.ts`, `route.test.ts`, `package.json` (SDK 1.29.0) — read directly
12. Vault note note_7e379855 "Spike: stateless MCP" — prior context

