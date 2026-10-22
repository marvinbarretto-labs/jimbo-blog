---
title: "Advise specific alcohol changes after three weeks of logs"
date: 2026-10-22
description: "Advise specific alcohol changes after three weeks of logs"
tags: [alcohol, gym-coach, report]
public: false
---

*Report — a research report (2026-10-22), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
Not yet answerable to the acceptance criteria: the log holds 14 days (8–21 Oct 2026), not three weeks. On those 14 days he drank on 10 and logged ~49 units (≈24.5/week, 1 unit = 8 g ethanol). Two provisional suggestions are below for him to accept or reject, but the "cites 3 weeks" criterion is not met. Re-run on or after 29 Oct.

## Data (from `/api/coach/food-log/daily` and `/api/coach/food-log?date=`)
| Day | Units | Drinks logged |
|---|---|---|
| Thu 8 | 6.1 | 3 pale ales (afternoon/early evening) |
| Fri 9 | 7.1 | 3 pale ales logged together at 23:47 |
| Sat 10 | 2.5 | 1 pint lager |
| Sun 11 | 4.7 | pale ale + Guinness |
| Mon 12 | 5.9 | pale ale + Guinness + gin & rose lemonade |
| Tue 13 | 2.4 | 1 Guinness |
| Wed 14 | 2.1 | 1 Brewdog Punk IPA |
| Fri 17 | 7.1 | 3 pale ales (time defaulted to 11:00) |
| Tue 20 | 2.1 | 1 Stella can |
| Wed 21 | 9.1 | Stella, Guinness, 2 pale ales (logged 01:20) |

No alcohol logged 15–16 Oct. 18–19 Oct have no log at all (a gap, not a dry day). Only 4 days are marked complete (9, 10, 20, 21); the rest are unconfirmed, so totals are a floor.

## Patterns
- Heaviest nights are 21 Oct (9.1 units, 2,827 kcal that day, 512 kcal from alcohol), 9 Oct and 17 Oct (7.1 each, three pale ales).
- Pale ale is in 7 of the 10 drinking days and is the volume driver: 18.8 g (~2.3 units) per serving.
- Guinness shows up on 4 days, always as an add-on (Sunday, Monday, Tuesday, Wednesday).
- Light nights (one drink) are 10, 13, 14, 20 — he stops at one fairly often, so that's doable for him.
- Monday 12 Oct was a 3-drink night including a mixer drink; a weeknight run of 11–14 Oct totalled ~15 units.

## Provisional suggestions (no target implied; accept/reject each)
1. **The third pale ale on Friday nights.** 9 Oct and 17 Oct were both three-pale-ale nights (7.1 units each). Stopping at two cuts ~2.3 units and ~165 kcal per Friday.
2. **Guinness as a second drink Sunday–Monday.** 11 and 12 Oct paired Guinness with a pale ale. Swapping the Guinness for water or choosing one or the other saves ~2.3 units each night.
3. *Hold until week 3:* the 21 Oct night (4 drinks, 01:20). One event doesn't make a pattern; see whether late-night stacking recurs.

## Recommendation
Do not close this task yet. Re-run after 29 Oct with confirmed days, ask Marvin to mark days complete (only 4 of 14 are), and log timestamps honestly (batch logs at 23:47, 01:20 and 11:00 hide when he actually drinks). Then convert suggestions 1–2 into accepted/rejected records on the note.

## Sources
1. `GET /api/coach/food-log/daily` — daily totals incl. `alcohol_g`
2. `GET /api/coach/food-log?date=YYYY-MM-DD` — per-drink entries (`est_alcohol_g`)
3. `GET /api/log-days/nutrition` — complete-day flags
4. Vault note note_711e78af — task scope and "no numeric target" constraint

