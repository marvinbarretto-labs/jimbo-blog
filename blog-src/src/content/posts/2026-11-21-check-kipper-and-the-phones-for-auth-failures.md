---
title: "Check Kipper and the phones for auth failures"
date: 2026-11-21
description: "Check Kipper and the phones for auth failures"
tags: [auth, report]
public: false
---

*Report — a research report (2026-11-21), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
No sign of an authentication failure on Kipper or the phone feed as of 2026-11-21 10:03 UTC. Kipper's Gmail read ran and finished at 09:02Z (137 of 137 processed), and phone data reached jimbo-api today. This is indirect evidence: I run on the M2 and cannot ssh to the M4, and no phone-side auth signal exists in the API.

## What was checked (all from the M2, via jimbo-api)
- **Kipper email (Gmail API auth):** the latest `kipper-email` agent.end event is 2026-11-21 09:02Z, "processed 137/137" (`/api/agent-runs/tail`). Reading Gmail needs a working token, so Gmail auth was valid this morning.
- **Kipper dispatch worker:** the actor state shows heartbeat "gated", with the M4 in use by keyboard or mouse 22 min before the check. That is the designed battery/AC gate (kipper/README.md), not an auth fault. 0 runs in 30 days, 0 failed.
- **Phones:** `/api/journal/phone` has data for 20 Nov (363 screen min, 842 notifications) and 21 Nov (47 min, 111 notifications), so the phone feed authenticates and reports. The `door.telegram`, `door.discord`, `door.email` and `feed.listen` workers all show `ok` with no `last_error`.
- **Fleet-wide:** every `/api/pipeline-v2/workers` item is ok with no error. The janitor shows `tool_failure: 0` and `refusal_spike: 0` this week.
- **Band:** the 19 Nov check records that the Gadgetbridge auth key is unchanged (docs/checks/2026-11-19-band-held-by-mi-fitness.md).

## Not covered, and one unrelated failure
- **Not verified:** the M4's own logs (`~/Library/Logs/kipper-dispatch-worker.err.log`, `kipper/email/logs`), Ollama, and any device-level sign-in prompts on the phones. No `m4` ssh alias exists on this host and no phone auth endpoint exists in the API.
- **Seen but unrelated to Kipper or the phones:** `/api/jobs/health` has `leak-scan` failing (exit 1 at 04:25Z, last success 18 Nov). `jimbo-api-watchdog` and `pg-offsite` are not reporting. I did not look into why, so I can't say whether any of these is an auth problem.

## Recommendation
Treat Kipper and the phones as healthy. If something specific prompted the question (a re-login prompt, a 401 in a log), name it. Otherwise run `tail ~/Library/Logs/kipper-dispatch-worker.err.log` on the M4 for the one gap, and look at the `leak-scan` failure separately.

## Sources
1. jimbo-api `/api/agent-runs/tail`: kipper-email run at 09:02Z.
2. jimbo-api `/api/actors/kipper/state`: heartbeat and 30-day runs.
3. jimbo-api `/api/journal/phone?since=2026-11-20T00:00:00Z&until=2026-11-22T00:00:00Z`: phone totals.
4. jimbo-api `/api/pipeline-v2/workers`, `/api/janitor/counts`, `/api/jobs/health`: worker, janitor and job state.
5. `kipper/README.md` and `docs/checks/2026-11-19-band-held-by-mi-fitness.md`: gating design and band auth key.

