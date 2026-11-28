---
title: "Dragos canary study: does it hold up, and are Jimbo or Claude Code links exposed?"
date: 2026-11-28
description: "Dragos canary study: does it hold up, and are Jimbo or Claude Code links exposed?"
tags: [security, report]
public: false
---

*Report — a research report (2026-11-28), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
The core claim holds up: several companies have since reported their own incidents, and MiniMax admits its systems opened links from forwarded prompts. Nothing found shows that Claude Code or any coding agent was tested or caught, but Dragos does not clear any direct route. **Jimbo's side is not clear: OpenRouter emailed on 22 Nov to say your account sent 7 requests to GMI Cloud on 20 Oct, which a third party may have read.**

## Act on this first
OpenRouter's notice, "Your OpenRouter requests through GMI Cloud may have been read" (support@openrouter.ai, 22 Nov; unread when checked on 28 Nov) [E1]:
- An attacker got in on 21–22 Oct and again from 27 Oct. The system kept about three days of request content, and the attacker searched it for credentials.
- It says to rotate any keys, passwords, tokens or signed URLs in those requests, and to check https://openrouter.ai/activity.
- GMI's own post gives the window as 18 Oct to 18 Nov and names no models [12].

**What those 7 requests probably were (an inference, not confirmed).** The weekly `model-bakeoff` Hermes job ran on 20 Oct at 14:44 UTC through OpenRouter, pinned to `deepseek/deepseek-v4-flash` with no host restriction [J1]. It asks which weekday in the next seven has the most calendar events. I did not confirm that it made these 7 requests, or how many it made. Another app on the same OpenRouter account could have.
- None of the values of the 8 long key, token, secret and URL settings in Hermes's `.env` that I checked appears in the saved run or the main prompt files, apart from the API address setting. This was not a scan for every kind of secret.
- The same calendar command run today for 20–26 Oct returns 26 events, 12 with a location. I found no links or password or PIN wording in titles or locations. Events may have changed since, and titles and locations are still personal data.
- The full requests are not in the saved output, so the activity page is the way to confirm the model and app behind them.

## Which tools were affected
Dragos sent about two million bait prompts from July to November, each with unique secrets, so any later use traced back to one prompt and route [1]. **It names no breached provider, reseller or lab in the post, and reports no test of Claude Code or another coding agent** [1].

| Finding | Who | Basis |
|---|---|---|
| Attackers stealing prompt data at 3 hosting providers; a couple hundred AWS keys in the largest | Unnamed | Dragos [1] |
| Marketplace sellers logging prompts, then trying the credentials by hand | Individual sellers, unnamed | Dragos [1] |
| Links fetched from more than half of prompts to one lab's models, including about two-thirds of those flagged zero-retention (ZDR) or no-data-collection | MiniMax, named later | [1][2][3] |
| One link posted in a Feishu chat 24 days later and opened from Beijing and Shanghai | Tied to MiniMax in coverage of Reuters | [1][3] |
| A link still crawled over two months after one search-endpoint call; another scraper returning days after each request, whatever the router | **Two unnamed large US providers** | Dragos [1] |

Vendors' own notices. These are not mapped to Dragos's three breaches:

| Vendor | What it reports |
|---|---|
| MiniMax [4] | Its security monitoring pulled URLs from forwarded requests and opened some, including ZDR ones. Routes: OpenRouter directly, and Novita, StreamLake, Atlas Cloud. It says it has disabled this and found no evidence that prompts or responses went to third parties. No date range given. |
| Atlas Cloud [5] | M3 and M2.7 prompts sent to MiniMax's API in Q3 and early Q4 had links opened. Says to treat secrets sent to M3, M2.7 or M3.1 Flash as exposed. |
| GMI Cloud [12] | Intruder reached a logging system holding request content. |
| Phala [13] | DeepSeek V4 Flash 0731 requests via OpenRouter, 21 Oct 02:25 to 1 Nov 02:03 UTC, at risk (152,092 requests, not proven read). |
| Together AI [14] | Stored June–July prompt samples downloaded after a leaked credential (MiniMax M3, GLM-5.2, Kimi K2.6). |
| Prime Intellect [15] | A DeepSeek V4.1 Flash deployment was swapped for a modified model, 8–10 Nov. It found no evidence that data left. |

OpenRouter says it off-boarded three providers, removed 125 endpoints from ZDR eligibility and found no breach of its own systems [6]. Its post does not name the three. Press lists that name them are inference, and Together says it was not removed [16].

## Does the claim hold up?
**Yes for "it happens", no for "how often, everywhere".**

For:
- Each bait secret went into one prompt on one route [1].
- MiniMax admits opening links, though not everything attributed to it [4]. GMI, Phala and Together report incidents of their own [12][13][14].
- Phala's report says the only canaries later misused were ones sent in its window (preliminary report: 21–22 Oct) [13].

Limits:
- The post has no limitations section, no per-provider totals and no example prompts. Several findings are hedged ("appeared not to honor") [1].
- It is the vendor's own research and ends with a product pitch [1].
- MiniMax did not address the Feishu chat or the later attempts to clone private repos [3].
- Moore reportedly saw Moscow-region activity, without evidence that the links were opened from Russia [3].
- I found no independent replication or critique in the pages read. The search was not exhaustive. I could not open Reuters, so its reporting here is secondhand [2][3].

## Could links sent through Claude Code or Jimbo be exposed?

### Claude Code
- **No evidence of exposure from this study.** The post's one Anthropic reference seen is a route-tracing figure caption, not a leak [1].
- **Not a clean bill.** Dragos does not name the two large US providers that crawled links, so Anthropic and OpenAI can be neither ruled in nor out. It calls going direct to a "first-tier provider" the smallest exposure you can buy, and gives no test showing direct routes were clean [1].
- On the Mac checked, no `ANTHROPIC_BASE_URL` or OpenRouter variable was set in the shell, and the settings `env` block only set a subagent model [J2]. I did not check other machines or every settings file.
- Anthropic keeps consumer-plan data 5 years if model training is allowed, otherwise 30 days; commercial and API data 30 days by default [7].
- Before WebFetch opens a page it sends Anthropic the hostname only, for a safety check [7]. That says nothing about links inside prompts, which are sent as part of the prompt.

### Jimbo
| Route | Exposure |
|---|---|
| Hermes chat (Anthropic direct) and most cron jobs (OpenAI Codex) [J1] | Same position as Claude Code: not tested by name, not cleared |
| Hermes via OpenRouter on DeepSeek V4 Flash: compression, approval, MCP and skills-hub helpers, the fallback model, two cron jobs [J1] | **The weak spot.** I found no host or data-collection restriction in `config.yaml`. Compression can carry conversation history. Account-level OpenRouter settings were not checked. |
| jimbo-api via OpenRouter [J3] | Personal-data model stacks send `data_collection: deny`. That is not ZDR, and I did not check that every caller uses a stack or the flag. Dragos found privacy flags often ignored [1]. |

- **MiniMax:** I found no sign of use in the study window. The cost ledger (from 3 Jul) has no MiniMax, StreamLake, Novita or Atlas match, nor do the Hermes logs searched (from about 11 Nov or earlier rotations). A free MiniMax fallback was removed from jimbo-api in late June [J3]. This does not rule out other apps on the account, and the ledger does not generally record which host served an OpenRouter call.
- **Phala:** DeepSeek V4 Flash is what Hermes uses, and Phala's window is 21 Oct–1 Nov [13]. A 30-day mail search for "openrouter" showed no Phala notice, only the GMI one. OpenRouter says it notified affected users [6], but check the activity page for Phala too.

## Recommendation
1. **Today:** open https://openrouter.ai/activity, find the 7 GMI requests on 20 Oct, and check model, app and any content you can recover. Rotate anything secret that was in them. In the same view, look for Phala between 21 Oct and 1 Nov, and GMI up to 18 Nov.
2. **Restrict OpenRouter.** Choose "ZDR only" at https://openrouter.ai/settings/privacy [8], and limit Jimbo to named hosts you trust, not just a flag. `zdr: true` alone can still allow "Safety Retention" endpoints under some settings [8]. Check the Hermes jobs and jimbo-api stacks still resolve afterwards. I did not establish DeepSeek's own retention or training policy.
3. **Consider moving the Hermes helpers off open-weight resale routes** to a direct provider, compression first. This follows Dragos's advice [1] and costs more per call.
4. **Treat any link that grants access by itself as a password:** signed URLs, private calendar feeds, share links. Do not paste them into a prompt. If one went through OpenRouter from July onwards and still works, revoke it.
5. **Optional:** plant your own canary token in Hermes context and alert on any use [1].

## Sources
Web:
1. https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens (primary, 19 Nov)
2. https://chipdispatch.com/articles/dragos-names-minimax-as-the-ai-lab-that-opened-secret-links-in-user-prompts
3. https://www.unite.ai/dragos-identifies-minimax-in-ai-prompt-privacy-investigation/ (labelled AI-written, editor-reviewed)
4. https://www.minimax.io/blog/update-on-url-access-in-forwarded-api-requests-20261124
5. https://www.atlascloud.ai/blog/ai-updates/security-and-privacy-commitment
6. https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/
7. https://code.claude.com/docs/en/data-usage
8. https://openrouter.ai/docs/guides/features/zdr.md
12. https://www.gmicloud.ai/en/blog/security-incident-affecting-gmi-cloud-endpoints-on-openrouter
13. https://phala.com/posts/phala-november-detailed-incident-report (supersedes https://phala.com/posts/phala-november-preliminary-incident-report)
14. https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026
15. https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution
16. https://www.bleepingcomputer.com/news/security/openrouter-drops-ai-providers-over-leaked-prompts-and-secrets/

Your own records, read on 28 Nov:
- E1. OpenRouter's email of 22 Nov, quoted above.
- J1. Hermes `config.yaml` (current, and as committed before 21 Oct), the cron job snapshot, and the saved `model-bakeoff` run of 20 Oct.
- J2. This Mac's shell variables and `~/.claude/settings.json`.
- J3. jimbo-api source, git history and cost ledger.

