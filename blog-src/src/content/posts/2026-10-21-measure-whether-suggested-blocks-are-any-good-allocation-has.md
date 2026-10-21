---
title: "Measure whether suggested_blocks are any good — allocation has never been checked"
date: 2026-10-21
description: "Measure whether suggested_blocks are any good — allocation has never been checked"
tags: [briefing, report]
public: false
---

*Report — a research report (2026-10-21), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

**Stop emitting them in their current form.** Across 69 days (133 morning/afternoon briefings, 430 blocks, 2026-08-10 → 2026-10-21), blocks on code projects land on real session time about as often as a random window would, except for `localshout`, where there is a genuine lift (62% vs 34% control). The other 63% of blocks (admin, money, travel, fringe) cannot be checked against `code_sessions`, and the vault shows they mostly do not turn into finished tasks: 332 task-linked blocks produced 12 done tasks out of 87 distinct, and only 16 blocks (5%) were followed by their task completing within 72 hours.

## From prior context

- Vault note `Measure whether suggested_blocks are any good` (note_6dda70e9, seq 4035): the groomed spec says to join each block to `code_sessions` minutes and calendar events, report a followed/ignored rate with sample size, and recommend keep, tune or stop. Read-only; no briefing or API change. The evening ledger (4029) is archived, so actuals were joined directly.
- The note says `day_plan` and `suggested_blocks` overlap and only one is populated. Confirmed below.

## Method

- Blocks: `GET /api/briefing/history?limit=200`, latest briefing per (day, session), blocks with a concrete `start`. Window = `start` to `start + size_blocks × 25 min` ("pomodoro-sized", `skills/briefing/daily-v2/SKILL.md:350`).
- Actuals: `GET /api/code-sessions` (768 sessions since 2026-08-09) as intervals (`started_at`→`ended_at`; running sessions capped at 1h), and `GET /api/google-calendar/events` (381 events).
- "Followed" = at least 10 minutes of overlap between the window and a session on the block's own project. Only projects that exist in `code_sessions` are measurable: `jimbo`, `localshout`, `ns-guild`, `collectr`, `watchdog`.
- Control: the same clock-time window on each of the 14 preceding days, same project. This answers "would a session have been there anyway?".
- Vault proxy for non-code blocks: for blocks with a `vault_seq`, the task's status and `completed_at`.

## New findings

### 1. Only 37% of blocks can be checked against code time
161 of 430 blocks are on code-session projects. The rest are on `admin` (69), `fourfold` (61), `fringe-2026` (39), `money` (28), `vacation-2026` (21), `reinvent-me`, `life` or no project. `code_sessions` says nothing about them.

### 2. Where measurable, "followed" is high but mostly not caused by the block

| Project | Blocks | Window hit (≥10 min) | Control (same clock time, other days) | Lift |
|---|---|---|---|---|
| jimbo | 77 | 71 (92%) | 79% | +13 pts, near the ceiling |
| localshout | 77 | 48 (62%) | 34% | +28 pts, real |
| All code-measurable | 161 | 120 (75%) | 54% | +21 pts |

Jimbo is active on 86% of days (localshout on 23%), and a jimbo session is nearly always open, so a jimbo block is almost impossible to miss. Treat the 92% as an unfalsifiable block, not a followed one. Caveat: session intervals are open-window time, not active time (median 0.5h, mean 14h, because some sessions stay open for days), so every hit rate here is an upper bound. Afternoon blocks (54/68, 79%) were followed slightly more than morning blocks (66/93, 71%).

### 3. Task-linked blocks rarely finish the task
355 blocks carry a `vault_seq`; 332 resolve to 87 distinct tasks. Status today: 12 done, 25 active, 12 inbox, 38 archived. Only 9 blocks were followed by their task completing within 24h of the block start, 16 within 72h (5% of 332).

The same tasks are proposed repeatedly. 18 tasks were proposed 5+ times, and those absorb 193 block-slots without being done. Top offenders: seq 4799 (39 times, now archived), 4066 (20, done), 6261 Halifax→Lloyds (19, still inbox), 6818 (19, active), 6039 (18, inbox), 4675 (17, archived).

### 4. 23% of blocks collide with a calendar event
101 of 430 blocks overlap a timed calendar event by more than 5 minutes, against the skill's own rule "never colliding with calendar" (SKILL.md:350). Examples: 2026-08-19 three admin blocks over "Amazon"; 2026-08-26 "Inbox triage with Jimbo" over the 09:30 daily triage event; 2026-08-16 and 2026-08-23 admin blocks over "FOOTBALL Sunday". Some of these may be soft calendar entries, but it shows the planner is not honouring the one constraint it states.

### 5. `day_plan` is dead; `suggested_blocks` is the live one
`day_plan` is non-empty in only 2 of the 200 history rows (both 2026-09-08 evening, `deepseek/deepseek-v4-flash`). In every Claude-era briefing it is `[]`, while `suggested_blocks` carries 2-4 blocks per morning/afternoon briefing. The overlap Marvin flagged resolves itself: one concept is used and the other is vestigial.

### 6. Not measured
No ▲/▼ exists for the section, walk/gym blocks were too few to score (`gym-app` appears twice, `body` six times), and "useful" was not measurable from these sources. Evening briefings have no blocks.

## Briefing days analysed

Each row is one day; blocks are the union of that day's morning and afternoon briefings. Hit = ≥10 min on the block's own project, code-measurable blocks only.

| Day | Blocks | Projects | Code-measurable (hit/total) | Calendar clashes |
|---|---|---|---|---|
| 2026-08-10 | 7 | admin, jimbo, localshout | 0/2 | 0 |
| 2026-08-11 | 7 | -, fringe-2026, jimbo, localshout | 3/4 | 0 |
| 2026-08-12 | 7 | admin, fringe-2026, jimbo, localshout | 4/5 | 0 |
| 2026-08-13 | 8 | admin, jimbo, localshout | 3/3 | 0 |
| 2026-08-14 | 8 | admin, jimbo, localshout | 5/5 | 0 |
| 2026-08-15 | 7 | admin, jimbo | 2/2 | 0 |
| 2026-08-16 | 6 | admin, fringe-2026, jimbo, localshout | 3/3 | 2 |
| 2026-08-17 | 7 | fringe-2026, jimbo, localshout | 4/4 | 0 |
| 2026-08-18 | 6 | fringe-2026, jimbo, localshout | 3/3 | 0 |
| 2026-08-19 | 8 | fringe-2026, jimbo | 2/2 | 3 |
| 2026-08-20 | 8 | fringe-2026, jimbo | 2/2 | 0 |
| 2026-08-21 | 6 | fringe-2026, pmq-bingo | 0/0 | 0 |
| 2026-08-22 | 7 | admin, fringe-2026, localshout | 1/1 | 3 |
| 2026-08-23 | 8 | fringe-2026, jimbo, localshout | 4/4 | 2 |
| 2026-08-24 | 4 | fringe-2026, jimbo | 2/2 | 0 |
| 2026-08-26 | 4 | -, jimbo, localshout | 3/3 | 2 |
| 2026-08-27 | 7 | -, fringe-2026, jimbo, localshout | 4/4 | 0 |
| 2026-08-28 | 6 | -, jimbo, localshout | 2/2 | 1 |
| 2026-08-29 | 3 | fringe-2026, jimbo | 2/2 | 0 |
| 2026-08-30 | 6 | -, jimbo, vacation-2026 | 1/1 | 3 |
| 2026-08-31 | 5 | -, jimbo | 3/3 | 1 |
| 2026-09-02 | 4 | body, jimbo, localshout | 1/2 | 0 |
| 2026-09-03 | 2 | localshout, travel | 0/1 | 1 |
| 2026-09-04 | 7 | fourfold, jimbo, localshout, travel | 2/3 | 1 |
| 2026-09-05 | 7 | admin, jimbo, localshout | 1/5 | 2 |
| 2026-09-06 | 7 | jimbo, localshout, vacation-2026 | 4/5 | 1 |
| 2026-09-07 | 7 | fourfold, jimbo, vacation-2026 | 2/3 | 0 |
| 2026-09-08 | 7 | fourfold, jimbo, localshout | 2/5 | 0 |
| 2026-09-09 | 7 | -, fourfold, jimbo, localshout | 5/5 | 0 |
| 2026-09-10 | 8 | admin, fourfold, localshout, vacation-2026 | 2/2 | 1 |
| 2026-09-11 | 7 | fourfold, localshout, vacation-2026 | 2/2 | 0 |
| 2026-09-12 | 8 | fourfold, jimbo, localshout, vacation-2026 | 2/2 | 4 |
| 2026-09-13 | 7 | fourfold, localshout, vacation-2026 | 1/1 | 2 |
| 2026-09-14 | 7 | fourfold, localshout, money, vacation-2026 | 0/1 | 1 |
| 2026-09-15 | 7 | fourfold, money, vacation-2026 | 0/0 | 0 |
| 2026-09-16 | 5 | fourfold, money, vacation-2026 | 0/0 | 3 |
| 2026-09-17 | 5 | fourfold, jimbo, money | 1/1 | 0 |
| 2026-09-18 | 5 | admin, fourfold, money | 0/0 | 0 |
| 2026-09-19 | 5 | admin, fourfold, jimbo | 1/1 | 2 |
| 2026-09-20 | 6 | admin, fourfold, jimbo | 2/2 | 2 |
| 2026-09-21 | 7 | admin, fourfold, jimbo | 2/2 | 0 |
| 2026-09-23 | 8 | admin, fourfold, reinvent-me | 0/0 | 2 |
| 2026-09-24 | 6 | admin, fourfold | 0/0 | 2 |
| 2026-09-25 | 7 | fourfold, jimbo, localshout, money | 1/2 | 4 |
| 2026-09-26 | 6 | jimbo, localshout | 4/6 | 0 |
| 2026-09-27 | 7 | fourfold, jimbo, localshout, reinvent-me | 3/5 | 1 |
| 2026-09-28 | 6 | fourfold, jimbo | 4/4 | 3 |
| 2026-09-29 | 6 | fourfold, jimbo, money | 2/2 | 0 |
| 2026-10-01 | 5 | admin, fourfold, localshout | 0/1 | 1 |
| 2026-10-02 | 7 | admin, fourfold, localshout | 1/2 | 0 |
| 2026-10-03 | 5 | -, admin, fourfold, localshout | 2/2 | 0 |
| 2026-10-04 | 6 | admin, jimbo, localshout | 3/3 | 0 |
| 2026-10-05 | 7 | localshout, money, reinvent-me | 3/3 | 0 |
| 2026-10-06 | 6 | localshout, money, reinvent-me | 3/3 | 3 |
| 2026-10-07 | 5 | localshout, money, reinvent-me | 1/2 | 4 |
| 2026-10-08 | 6 | -, localshout | 0/3 | 1 |
| 2026-10-09 | 6 | -, life-admin, localshout | 1/2 | 0 |
| 2026-10-10 | 7 | admin, localshout, money | 2/2 | 0 |
| 2026-10-11 | 7 | admin, localshout, money | 1/2 | 0 |
| 2026-10-12 | 6 | -, jimbo, localshout | 1/3 | 3 |
| 2026-10-13 | 6 | -, admin, ns-guild | 0/3 | 6 |
| 2026-10-14 | 6 | -, admin, jimbo, ns-guild, reinvent-me | 2/3 | 6 |
| 2026-10-15 | 7 | admin, life, ns-guild | 0/2 | 7 |
| 2026-10-16 | 7 | -, admin, life, localshout | 1/2 | 7 |
| 2026-10-17 | 4 | -, admin | 0/0 | 4 |
| 2026-10-18 | 6 | admin, localshout, reinvent-me | 2/2 | 5 |
| 2026-10-19 | 5 | admin, money | 0/0 | 0 |
| 2026-10-20 | 6 | admin, gym-app, localshout, money | 0/1 | 4 |
| 2026-10-21 | 4 | gym-app, localshout, money | 0/1 | 1 |

## Recommendation

**Stop emitting `suggested_blocks` as a standalone section, and keep one narrow replacement.**

1. The section fails on evidence. Where it can be checked it is either trivially satisfied (jimbo, 92% hit against a 79% background) or only modestly better than chance. For the 63% of blocks that are admin, money or travel, the proxy is worse: 5% of task-linked blocks were followed by the task finishing in 72 hours, and 18 tasks were re-proposed 5+ times.
2. It breaks its own rule, with 23% calendar collisions.
3. It duplicates a dead field. Remove `day_plan` from the schema at the same time; it has been empty in every Claude-era briefing.
4. Keep only what earns its place: `localshout` blocks show real lift (62% vs 34%). If Marvin wants a nudge, emit at most one block per briefing, only for a project with a recent gap, and only when the start time is clear of the calendar.
5. Do not tune the rest. The briefing is shorter and more honest without a section whose repeated items (seq 4799 ×39) tell Marvin nothing new.
6. Before deciding, one cheap fix would make this measurable next time: record active minutes (heartbeats) rather than open-window time. Stopping the section costs nothing; keeping it needs that to be checked again in a month.

Not done here (out of scope per the note): no change to the briefing skill or API.

## Sources

1. Vault note note_6dda70e9 (seq 4035), `Measure whether suggested_blocks are any good`: scope and acceptance criteria.
2. `jimbo/skills/briefing/daily-v2/SKILL.md:312,350`: `suggested_blocks` schema and "2-4, pomodoro-sized, never colliding with calendar".
3. jimbo-api `GET /api/briefing/history?limit=200`: 200 briefing rows, 2026-08-09 → 2026-10-21.
4. jimbo-api `GET /api/code-sessions` (768 sessions since 2026-08-09, 1,160 total).
5. jimbo-api `GET /api/google-calendar/events` (381 events, 2026-08-09 → 2026-10-22).
6. jimbo-api `GET /api/vault/notes/{seq}` for the 87 resolved `vault_seq` values.

