---
title: "Hermes crons failing on HTTP 429 usage limit — email-processor and priority-drift-alert"
date: 2026-09-26
description: "Hermes crons failing on HTTP 429 usage limit — email-processor and priority-drift-alert"
tags: [hermes, cron, reliability, report]
public: false
---

*Report — research report (2026-09-26), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

The 429 errors hitting `email-processor` and `priority-drift-alert` are Codex plan-level quota exhaustion, not OpenRouter credit. Both jobs run on `openai-codex` (gpt-5.5), which serves 30 of 34 Hermes crons. `email-processor` runs every 12 hours and estimates 4–5 turns per run; `priority-drift-alert` runs Sundays at 19:30 and estimates 5–10+ turns (multiple jimbo-api calls + analysis). The root cause is architectural: high-frequency smart work belongs on a flat-rate plan (fleet dispatch), not a metered plan. Failures go unseen because the watchdog only detects stuck jobs, not errors.

## From prior context

None provided. This is the first deep research into the 429s since they were spotted on 2026-09-07.

## New findings

**1. Confirmed root cause and timing**

The incident report `20260908-state-db-corruption-recurrence.md` (§6) explicitly separates this from the database corruption: "4 jobs failing `HTTP 429: usage limit reached` (`lessons-decay`, `weekly-custody`, `ecosystem-review-nudge`, `priority-drift-alert`) and 1 on `HTTP 402`… Separate fault, quota not corruption."

These failures occurred in the evening of 2026-09-06 / early 2026-09-07:
- `lessons-decay` (weekly) — last run 2026-09-06 19:00
- `priority-drift-alert` (Sun 19:30) — last run 2026-09-06 19:30
- `ecosystem-review-nudge` (Sun 17:00) — same evening, also 429
- `weekly-custody` (Sun 18:00) — same evening, also 429

**2. Provider split in current config**

From `docs/reports/hermes-cron-lane-map.md`:
- **30 jobs on `openai-codex`** (gpt-5.5 / gpt-5.4-mini) — the metered ChatGPT plan
- **3 jobs on OpenRouter** (gateway default) — `interrogate-verdict-alert`, `interrogate-staleness-pulse`, `status-pulse`
- **1 job explicitly OpenRouter** — `discord-attachment-poller`

The lane map document explicitly states: "the `HTTP 429: usage limit reached` on four jobs is a **Codex limit, not OpenRouter credit**."

**3. Current job status (as of 2026-09-25)**

From `jobs.snapshot.json`:

| Job | Schedule | Model | Provider | Status | Last known state |
|---|---|---|---|---|---|
| `lessons-decay` | weekly (10080m) | gpt-5.5 | openai-codex | **PAUSED** | Paused 2026-09-08, replaced by jimbo crontab job at Sun 05:10 |
| `email-processor` | every 720m (12h) | gpt-5.5 | openai-codex | **ENABLED** | Last failure 2026-09-07 02:37 (2 consecutive failures) |
| `priority-drift-alert` | Sun 19:30 | gpt-5.5 | openai-codex | **ENABLED** | Last failure 2026-09-06 19:30 |
| `ecosystem-review-nudge` | Sun 17:00 | gpt-5.5 | openai-codex | **PAUSED** | Paused 2026-09-14, replaced by jimbo crontab curl + calendar slot |
| `weekly-custody` | Sun 18:00 | gpt-5.5 | openai-codex | **ENABLED** | Last failure 2026-09-06 18:00 (implied, not explicit in notes) |

**4. Sunday 17:00–20:00 UTC window analysis**

Three Codex jobs scheduled in this window on Sundays:

| Time | Job | Turns (est.) | Active? |
|---|---|---|---|
| 17:00 | ecosystem-review-nudge | ~1–2 (hardcoded message) | PAUSED since 2026-09-14 |
| 18:00 | weekly-custody | ~5–8 (calendar fetch + jimbo-api call + formatting) | ENABLED |
| 19:30 | priority-drift-alert | ~5–10+ (jimbo-api snapshot, calendar 7, tasks, analysis) | ENABLED |

The 2026-09-06 failures (evening 17:00–20:00) involved at least two jobs in this window. **They do not directly overlap** (ecosystem-review-nudge was already paused), but if a daily or reset-on-hour Codex quota is exhausted, a slow job from 17:00–18:30 could block 18:00 and 19:30. The lane map notes: "note the two 19:00/19:30 failures on the same evening — worth checking whether they are contending for the same quota window."

**5. Job complexity and token estimates**

**email-processor** (every 12 hours):
- Step 1: Fetch already-processed IDs (1 call, output filtered to IDs only)
- Step 2: Fetch recent Gmail messages (1 call)
- Step 3: Filter already-processed
- Step 4: Triage on snippets (no LLM calls)
- Step 5: Deep read high scorers (N calls for messages scoring ≥5, typically 1–3)
- Step 6: Persist reports (single batched shell script)
- **Estimated turns per run: 4–7** (typically 4–5 if few high scorers, up to 7 if mailbox active)
- **Throughput: ~120–168 turns/day** (every 12h × 5–7 turns avg)

**priority-drift-alert** (every Sunday 19:30):
- Step 1: jimbo-api snapshot (1 call)
- Step 2: jimbo-api calendar 7 (1 call)
- Step 3: jimbo-api tasks (1 call)
- Step 4: Calculate drift (no LLM calls)
- Step 5: Write Discord insight (LLM reasoning over loaded context)
- **Estimated turns per run: 5–10+** (typically 1 turn for the entire reasoning, 4 API calls total)
- **Throughput: ~0.7 turns/day** (once weekly)

Neither job is particularly heavy individually, but `email-processor` at ~168 turns/day (12 hours × 5–7 turns × 2 runs) and 30 other jobs on the same Codex plan creates contention.

**6. No visible alerting for 429 errors**

The watchdog script (`hermes/scripts/cron-watchdog.py`) detects and resumes stuck jobs (state=running with stale next_run_at). **It does NOT alert on HTTP 429 or other error exits.** 

Failures surface only in:
- `hermes cron list` output (not monitored by Marvin's usual dashboards)
- Absence of expected output (Telegram messages not sent, Discord reports missing)

The vault note highlights: "the silent-failure aspect is the wider problem: all three sat failing with no signal anywhere Marvin looks. `email-processor` feeds the briefing pipeline."

## Comparison

| Aspect | Current | Recommended |
|---|---|---|
| **email-processor** | On Codex, metered, every 12h | Dispatch to fleet, flat-rate, enqueue instead of execute |
| **priority-drift-alert** | On Codex, metered, Sun 19:30 | Stay on Codex (smart output = message, not artifact) |
| **lessons-decay** | Hermes paused, jimbo crontab active | ✓ Already fixed (2026-09-08) |
| **Alerting** | None for 429s | Add watchdog rule or standalone alert |

## Recommendation

**For `email-processor` (HIGH PRIORITY):**

Move to fleet dispatch. The output is a persisted report (artifact) not a user-facing message, making it a natural dispatch candidate (pattern: `assertion-scan` → `think/assertion-scan`, `travel-research` → `research/travel-planning`).

- **Action**: Modify the Hermes cron prompt to enqueue via jimbo-api instead of executing inline.
  - New schedule: Hermes job every 720m, executes: `jimbo-api dispatch-enqueue '{...task_id: "note_XXXXX", executor: "boris", skill: "email-processor-fleet", flow: "commission"}'`
  - Leave output silent (Hermes confirms enqueue, boris executes the skill).
- **File to change**: `hub/hermes/cron/jobs.snapshot.json` → `email-processor` job.
- **Benefit**: Moves 120–168 daily turns from Codex quota to flat-rate Anthropic plan (already paid, three workers idle-polling).

**For `priority-drift-alert` (KEEP AS IS):**

This job correctly belongs on Codex. Its output IS the message (Discord report), not an artifact for the fleet to build. It runs once weekly, not continuously, so quota contention with this job is minimal (0.7 turns/day).

**For alerting (OUT OF SCOPE, but flag):**

The 429 failures went undetected because the watchdog doesn't monitor HTTP errors. A separate task should:
1. Extend `cron-watchdog.py` to parse job run logs for HTTP 429 exits.
2. Alert via Telegram or Discord when a job fails with 429 (matching the pattern from `cron-watchdog` for stuck jobs).
3. Or: add a Sentry/Healthchecks hook in the Hermes agent itself.

The vault note's acceptance criteria require "a 429 failure surfaces somewhere Marvin sees it" — current alerting does not meet this.

## Sources

1. **Vault note `note_9405bac8`** — original incident report, timestamps and job failures
2. **`docs/incidents/20260908-state-db-corruption-recurrence.md` §6** — confirms 429 as separate from database corruption, names four jobs affected
3. **`docs/reports/hermes-cron-lane-map.md`** — lane policy, current split (30 Codex, 3+1 OpenRouter), recommendation to move artifact-producing jobs to fleet
4. **`hermes/cron/jobs.snapshot.json`** — current job config (enabled/paused status, schedules, providers)
5. **`hermes/skills/email-processor/SKILL.md`** — algorithm and token estimate (4–5 tool calls, "keep it cheap")
6. **`hermes/docs/retired-jobs.md`** — `lessons-decay` already replaced by jimbo crontab (2026-09-08), no longer live in Hermes
7. **`hermes/scripts/cron-watchdog.py`** — confirms watchdog only handles stuck jobs, not error exits

