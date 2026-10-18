---
title: "Define the micro-habit list, and one-tap capture only for what has no source yet"
date: 2026-10-18
description: "Define the micro-habit list, and one-tap capture only for what has no source yet"
tags: [habits, report]
public: false
---

*Report — a draft (2026-10-18), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

*Report — a draft (2026-10-18), published to cairn by the dispatch flow. **DRAFT: awaiting Marvin's confirmation.** The list below is his to edit.*

The micro-habit list is mostly already written. Four of the five habits have a route in jimbo-api that records them. Wake time is the only gap, so it's the only thing that needs a new way to capture it.

I checked each route in `jimbo-api/src/routes/` before putting it in the table.

## The list

The test for each is the one from the capture: *it's not big, but it helps.*

| Habit | Why it's small but it helps | Source | Daily rollup |
|---|---|---|---|
| Getting up at a normal time | Sets the shape of the whole day | **None. Gap.** | None |
| Commits | A day with a commit is a day I built something | `GET /api/activity/stats` (`activity.ts`) | Stats only |
| Supplements | Easy to forget, easy to see once logged | `GET /api/coach/supplement-log` (`coach.ts`) | `GET /api/coach/today` |
| Alcohol | Can't improve what I don't count | `GET /api/coach/food-log` (`coach.ts`) | `GET /api/coach/food-log/daily` |
| Gym discipline | Showing up matters more than the session | `GET /api/gym/sessions` (`gym.ts`) | `GET /api/gym/sessions/daily` |

Two notes on the table:

- **Alcohol has no route of its own.** It's read out of the food log. That's fine, but it means a drink only counts if it was logged as food. I haven't checked how the rollup identifies it, so I'm treating that as an open question.
- **Mood and energy** (`/api/checkins`) are on the epic's list as a signal, but they aren't one of your five named habits. I've left them off. Add them if you want them.

All five need zero typing to record, except that food, supplement and gym logging currently reach the API by whatever route they already take. That part isn't changing. I'm not touching it.

## The one gap: wake time

The bar, from the task: **is it cheaper than adding a row to Google Tasks?** A Google Tasks row costs about two taps plus a few typed words. Anything that needs typing is a chore, so the target is zero typing.

| Option | Taps | Typing | Verdict |
|---|---|---|---|
| Google Tasks row ("up") | 2–3 | A word | The baseline. Records a time, but into the wrong instrument. |
| Hermes nudge, reply with one button | 1 | None | Beats the baseline. |
| Discord reaction on a morning message | 1–2 | None | Close, but I haven't verified the reaction path is wired up. |

### Recommendation: the Hermes nudge

A morning message from Hermes with a single "Up" button. One tap, nothing typed, and the tap's timestamp is the wake time.

Why this one:

- **It's a tap on a message that already arrived.** Nothing to open, nothing to find.
- **The pattern exists.** The supplement nudge already works this way: a Hermes cron hits a `/tick` route, and the coach routes have `log`, `skip` and `later` actions. Wake time is the same shape.
- **It doesn't need me to remember.** Google Tasks needs me to open it. The nudge comes to me.

One caveat. The tap records when I *replied*, not when I woke. If the nudge fires at 07:00 and I tap at 07:40, the data says 07:40. For "normal time" that's probably fine as a proxy, and it's still better than nothing. But the nudge time matters, and a ping that fires before I'm up is just noise.

## What this doesn't do

No endpoint, no capture surface, no wireframe (that's JIM-3704) and no rollup. If the Hermes option is confirmed, the build is its own task.

## To confirm

1. Is the list of five right?
2. Does the Hermes nudge get the go-ahead for wake time?

