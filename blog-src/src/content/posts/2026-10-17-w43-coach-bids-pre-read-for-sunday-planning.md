---
title: "W43 coach bids: pre-read for Sunday planning"
date: 2026-10-17
description: "W43 coach bids: pre-read for Sunday planning"
tags: [council, report]
public: false
---

*Report — a research report (2026-10-17), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
The two W43 bids (gym, life) barely clash. Gym wants Mon/Wed/Fri at 14:30 and life wants Thursday 22 for Wellcome, so no day is contested. The real pressure is the Home slot (14:30–16:30), which gym's sessions would fill and life's cleaning slot also needs. Acceptance criteria 2 and 3 (Marvin's choice, who gave way) can only be met in the planning session. This document does not meet them; it is the draft for that session to start from.

## From prior context
Sources: vault note "Have each coach send a written bid into Sunday's weekly planning" (note_ff74d386); notebooks `bids-2026-w43-gym`, `bids-2026-w43-life`, `rulings`; week plan 2026-W42.
- Criterion 1 is met. Bids for gym and life were stored 16 Oct 02:27. Income and projects have no charter, so no bid.
- Bids are blind to each other, so any clash has to be found by the planning session.
- Only one ruling exists. RUL-1 governs how coaches message Marvin. It does not settle any scheduling clash, so no ruling applies to W43.

## New findings
**What each bid asks for**
- Gym: three full-body sessions of 45–60 min on Mon 19, Wed 21 and Fri 23 at about 14:30. A 30 g protein first meal daily, and whey after each session. Every set logged with RPE and food days ticked. Recommendation: hold Mon 19 Oct 14:30 for Gym B.
- Life: Thu 22 Wellcome Collection before Traitors night. Plan A leaves at 9am and adds the Regent's Canal walk; Plan B leaves at 12pm and does Wellcome only. One daytime Home slot of about 35 min for a cleaning script. 30 minutes at Sunday planning, life part first. Recommendation: add Wellcome to Thursday's Traitors trip.

**Where they collide (for the planning session to confirm)**
1. **Home slot, 14:30–16:30.** In the W42 plan this slot is where chores, cooking and Thursday's gym sat. Gym takes it on Mon, Wed and Fri. Life's cleaning script needs one daytime Home slot. Free options are Tue, Thu or the weekend. Thursday is probably out, because Wellcome plus Traitors fills the day. Tue or Sat is the natural place.
2. **Quota.** W42 set gym at 2. Gym now asks for 3. This is a change to the trial baseline, not a clash with life, but Marvin should say yes or no to it.
3. **Thursday's Out slot.** Plan A (leave at 9am) takes the Out slot (09:30–11:30) and Work 1 on Thursday. Gym is not on Thursday, so it is a cost to projects, not to gym. The planner should show which project loses the day.
4. **Gym's Friday.** Gym's own give-way is Friday as a 30-min Plan B at home. That makes Friday the cheapest thing to trade if the week is tight.

**Gaps the planner must fill.** Gym says "the W43 calendar isn't in my data". The planner has to check Mon–Sun 19–25 Oct against the calendar before it offers 14:30 on any day. I did not check it: the calendar tool I had only returned today.

## Comparison (draft options for Marvin)
| Question | Option A | Option B | Labelled recommendation |
|---|---|---|---|
| Gym count | 3 sessions (Mon/Wed/Fri) | 2 sessions (Mon/Wed, Fri as home Plan B) | A. Both of gym's give-way steps sit inside A, and Monday is anchored. |
| Cleaning slot | Tue Home slot, 35 min | Sat Home slot | A. It keeps the weekend free and it does not touch gym days. |
| Thursday | Plan A (9am, canal walk) | Plan B (12pm, Wellcome only) | B as the default and A if he is up. Life's own rule is Plan B if not out by 12. |
| Sunday 25 | Life 30 min first | Life 20 min | A. Life gives way here only if the day overruns. |

Planner's call, labelled as its own: agree the gym at 3 with Monday held first, Wellcome on Thursday, cleaning on Tuesday. Gym wins on frequency, life wins on Thursday, and the cleaning slot is what each gives up (life's cut order starts with cleaning).

## Recommendation
1. Run the planning session as specified. Optionally re-run `python3 ~/development/jimbo/skills/think/council/bids/run.py --live` first for fresher data.
2. Check the W43 calendar before offering any slot.
3. Present the four decisions above and record Marvin's answer to each in the W43 plan. Record who gave way and why: the loser of each trade is the coach whose give-way step was used.
4. Say plainly that the clash count is low. A trial that only produces one real conflict says little about whether bids work. Keep the format for another week before judging it (per his "try it out… we tweak it").
5. The "coach losing 3 weeks running" check needs a place to live. Put a `gave_way` line in the plan record each week so the third week can be counted.

## Sources
1. Vault note note_ff74d386 (task text and groomed section)
2. GET /api/council/notebooks/bids-2026-w43-gym
3. GET /api/council/notebooks/bids-2026-w43-life
4. GET /api/council/notebooks/rulings (RUL-1)
5. GET /api/week-plans, week 2026-W42 (slot times, quotas, Home slot usage)

