---
title: "Briefing arrives when you wake, not when cron fires"
date: 2026-10-10
description: "Briefing arrives when you wake, not when cron fires"
tags: [health-connect, report]
public: false
---

*Report — a research report (2026-10-10), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**Verdict: dead.** Zero `health_connect` / `sleep_session` events in the last 14 days (2026-09-26 → 2026-10-10), and zero ever returned by the type filter. The break is at the **phone permission layer**: the app lacks `android.permission.health.READ_SLEEP` (and `READ_HEART_RATE`). Screen-unlock events also do not reach the API. The wake-triggered briefing cannot be built on either signal today.

## From prior context
- Vault note "Briefing arrives when you wake, not when cron fires" (note_e64b0ac7): sleep flow was unverified; live-status returned `sleep_hours` null on 2026-09-30; JIM-3477 records no sleep measurement exists; JIM-4647 (POST_NOTIFICATIONS, NotificationTriggerPlugin) is unbuilt. This research confirms and explains the null.

## Findings (queried `GET /api/telemetry/events` on 2026-10-10)
| Check | Result |
|---|---|
| `collector=health_connect&type=sleep_session`, since 2026-09-26 | **0 events** (total 0) |
| Other HC types in the window | Flowing: `calories_total(_daily)`, `steps(_daily)`, `distance(_daily)`, `calories_active`, `exercise_session`, `hc_diagnostic` (latest samples 2026-10-08) |
| `hc_diagnostic` payload | Identical in all 500 rows inspected (2026-09-14 → 2026-10-08): `missing_permissions: [READ_HEART_RATE, READ_SLEEP]` |
| Screen events (`screen_unlock`, `screen_on`) | **0**. The `device` collector emits only `battery_level` (339 events in the window, 2026-09-26 → 2026-10-08) |
| End times populated? | Not assessable, with no sleep rows. Moot until the permission is granted |

So the HC collector works and the ingest path works (steps, calories, exercise arrive). The collector itself reports exactly why sleep is absent: it was never granted READ_SLEEP. Layer: **phone permission**, not collector code or ingest.

Screen-unlock: no such event type exists in the data at all. I found no Android source in this checkout to confirm whether the collector was ever meant to emit it, so treat it as not built.

## Recommendation
1. **File a follow-up (not here):** grant/request `READ_SLEEP` in the Android app's HC permission flow (and fix whatever stops it appearing in the requested set). Then re-run the 14-day query after a night's sleep to confirm `sleep_session` rows with `ts_end` populated. Also note it needs Pixel's sleep source (Fitbit / Google Clock bedtime / a wearable) actually writing sessions to Health Connect — permission alone won't produce data if nothing writes sleep.
2. **Add a screen-unlock event** to the device collector (`ACTION_USER_PRESENT`) as a separate task; it is a prerequisite for "first unlock after wake".
3. **Fallback wake signal until then:** phone-activity dark-period end (per JIM-3477), i.e. the first non-battery device activity after a long gap, inside the 05:30–10:00 window. Caveat: the `device` collector currently emits only battery_level, so even this is weak; first phone interaction would need to come from screen events (item 2).
4. **JIM-4647 must ship first:** POST_NOTIFICATIONS + NotificationTriggerPlugin, since nothing can notify without it.
5. Don't start the WorkManager wake job until 1 or 2 is verified flowing. Briefing generation (hermes cron) stays untouched.

## Sources
1. Vault note note_e64b0ac7 — task, groomed scope and ACs.
2. jimbo-api `GET /api/telemetry/events` (live, queried 2026-10-10) — counts and `hc_diagnostic` payloads above.

