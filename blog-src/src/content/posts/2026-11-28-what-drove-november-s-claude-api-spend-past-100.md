---
title: "What drove November's Claude API spend past $100?"
date: 2026-11-28
description: "What drove November's Claude API spend past $100?"
tags: [ai-costs, report]
public: false
---

*Report — a research report (2026-11-28), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

**The main cause is `inbox-shadow`, a Hermes email job running on Sonnet 5.5 every 30 minutes since 19 November: $61 of the $103 I can trace.** It was sped up to clear a backlog. The note to slow it to hourly once fewer than 50 emails were waiting is still open, and on 28 Nov the count was 0. I could not check whether a spend limit is set, because that shows only in the Claude Console.

## From prior context

No prior notes came with this question. The repo records these decisions:

- Hermes chat runs on Sonnet through the API key (`hermes/config.yaml`, citing ADR-0076).
- jimbo-api sends some model calls straight to Anthropic on the same key (ADR-0186, and later code).
- On 5 Nov the pipeline's API fallback was switched on, on the basis that API credit was available (`docs/plans/2026-11-05-machine-to-vps.md`).

## New findings

### Spend for 1 Nov to 28 Nov, about 10:20 UTC

| Job | USD (estimate) | Share |
|---|---:|---:|
| Hermes `inbox-shadow` (from 19 Nov) | 61.16 | 59% |
| Hermes other cron runs (115; the latest 12 were all coach openings) | 16.35 | 16% |
| Hermes chat (Discord and Telegram) | 5.95 | 6% |
| jimbo-api `criteria-lock` | 14.50 | 14% |
| jimbo-api `task-size` | 1.82 | 2% |
| jimbo-api `criteria-drafter` | 1.36 | 1% |
| jimbo-api `listening-pass` | 0.83 | 1% |
| jimbo-api, everything else | about 1.17 | 1% |
| **Total traced** | **about 103.14** | |

- **How well it matches the alert:** at the time of the alert email (27 Nov, 08:31 UTC) I can trace $95.25 of the $100, leaving about $4.75. Hermes' session store starts on 3 Nov. Manual LocalShout scripts that can call the API directly would not appear in either source. I did not establish what makes up the gap.
- **Prices:** Hermes' token counts at list price, using the 5-minute cache-write rate it is set to, give its $83.46. Sonnet 5.5 costs $2 input, $10 output, $2.50 for a 5-minute cache write and $0.10 for a cache read, per million tokens [1].
- **By key:** Hermes and jimbo-api are configured with the same key, so a per-key view cannot separate them. Some LocalShout scripts name a different key. I did not see per-key usage. The jimbo-api rows are its Anthropic cost rows without the build-lane and coach-box turns. Its list does not show who paid, so a little of "everything else" may have run on the Max plan.
- **Not part of this bill:** jimbo-api's cost summary shows about $780 over 28 days. Most of that is build-lane and coach-box work priced at API rates. The build lane and coach box are recorded as running on the Max plan, so don't read that total as API spend.

### What changed

- From 5 to 18 Nov, Hermes and jimbo-api together cost roughly $2 a day.
- On full days from 20 to 27 Nov they cost about $8.10 a day. `inbox-shadow` was about $6.60 of that.
- The repo's job snapshot showed `inbox-shadow` on a ChatGPT-plan model every 6 hours from 21 Oct. By 20 Nov it showed Sonnet 5.5 every 30 minutes.
- **Most runs find nothing.** On 20 to 27 Nov, 230 of 372 runs (62%) ended `[SILENT]`. They cost $29.61, about **$3.70 a day**. The one silent run I opened found 0 undecided emails and 0 waiting for the follow-up decision, but had still loaded the model and its skills.
- `criteria-lock` comes in bursts: $5.40 on 14 Nov (551 calls), $2.49 on 22 Nov and $1.89 on 27 Nov.

### Was it expected?

- **Using the API at all: yes.** Chat and jimbo-api's direct calls were deliberate. ADR-0186 expected the listening replies to cost pennies a week, and they are not a material part of this bill.
- **The current rate of `inbox-shadow`: no.** Moving it to Sonnet every 30 minutes was recorded. The 19 Nov handoff line says to "put it back to every 60m" once the undecided total is under 50. On 28 Nov the total was 0, the job was still every 30 minutes, and the line was still in `HANDOFF.md`. I found no estimate of what the faster schedule would cost.
- **Coach openings:** each run cost about $0.14, much of it writing a prompt cache. On 28 Nov by 10:20 UTC I saw none, and no enabled Hermes job had "coach" in its name. Coaches were being moved to the coach box on 27 Nov, but one quiet morning does not prove these runs have stopped.

### Is a hard spend limit set?

**Unknown.** I used no Console access. The Admin usage API is not available to individual Console accounts until they set up an organization [3]. The alert saying it doesn't pause requests describes the notification only. It does not show whether a separate limit exists.

- Anthropic's Start, Build and Scale tiers have monthly caps of $500, $1,000 and $200,000. Custom has none [2]. I don't know this account's tier. Reaching a tier cap pauses API use until the next month unless a higher limit is granted [2].
- You can set a lower limit of your own. When it is reached, requests fail with HTTP 400 until access resumes, or until you raise or remove the limit [2].
- Notifications are set on the same page and are separate from the limit [2].

### Forecast

These are straight-line estimates from 20 to 27 Nov.

| Case | Per day | November end | A 31-day December |
|---|---:|---:|---:|
| No change | about $8.10 | about $125 traced, about $130 with the gap | about $250 |
| No model call on empty runs | about $4.40 | lower, depending on when it lands | about $135 |

The December figure for the second case assumes email volume stays the same and that empty runs cost nothing. It keeps the other costs, including any coach openings that have now stopped.

## Recommendation

1. **Today: put `inbox-shadow` back to every 60 minutes.** The recorded condition is met. This should cut a good part of its cost, though I did not measure an hourly rate, because busier runs may cost more.
2. **Then stop empty runs calling the model.** Add a check script before the job, as some other Hermes jobs already have. It must check both undecided emails and decided emails still missing the follow-up decision (`missing_d10`), and start the model if either is above 0. If the check itself fails, it should report the failure, not skip quietly. This saves up to about $3.70 a day at the 30-minute rate, and less after step 1. The two savings don't add together.
3. **In the Console, open [Spend limits](https://platform.claude.com/settings/spend-limits).** Read the current limit and tier. I suggest a **$200 monthly limit with a notification at $150**. That leaves room above the current November forecast. With no change, December would hit it around day 25. A limit stops everything it covers: expect `inbox-shadow` and other API-pinned jobs to fail, as well as jimbo-api's direct calls. The Hermes config says pinned cron jobs don't use the fallback model. I did not test how chat reacts to the limit's HTTP 400.
4. **Give jimbo-api and Hermes separate keys**, so the Console can show them apart.
5. **If it is still too dear,** consider moving `inbox-shadow` back to the ChatGPT plan. That removes its per-token bill but uses plan allowance, and I did not compare decision quality.

I changed no schedule, key or limit.

## Sources

1. [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)
2. [Anthropic rate and spend limits](https://platform.claude.com/docs/en/api/rate-limits)
3. [Anthropic Usage and Cost API](https://platform.claude.com/docs/en/api/usage-cost-api)
4. Hermes session store and job list on the VPS, read on 28 Nov: token counts, estimated cost, run output and schedule.
5. jimbo-api `GET /api/costs`, `GET /api/costs/summary` and the undecided-email count, read on 28 Nov.
6. jimbo repo: `HANDOFF.md` (19 Nov line), `hermes/config.yaml`, `hermes/cron/jobs.snapshot.json` history, ADR-0186 and `docs/plans/2026-11-05-machine-to-vps.md`.

