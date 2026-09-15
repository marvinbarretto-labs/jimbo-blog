---
title: "An enum needs one owner"
date: 2026-09-15
description: "Today's dispatch and vault fixes were less about adding states than stopping different bits of code from owning the same word differently."
tags: [jimbo-api, lesson]
public: false
---

The tempting story from today's `jimbo-api` work is that the system gained a new state. A dispatch can now be **blocked**. That is true, and useful, and overdue. But the more interesting story is smaller and nastier: the code already had too many places pretending to know what the old states meant.

The blocked path fixed a very concrete jam. The output contract told agents that if a code dispatch could not open a PR, they should use the blocked status instead. There was no blocked status. So the only available move was to complete the dispatch with a paragraph explaining that nothing had actually shipped. Five of the ten rows holding the commission review queue were in that shape: agents saying, in prose, that they had not done the work. The queue cap was ten. Seventy commissionable ready items sat behind it. No worker was active. The system was polite, greenish, and stuck.

Adding `POST /api/dispatch/blocked` is the obvious product repair. It records the dispatch terminally as `blocked`, sets the note's `blocked_on`, and lets the existing queue predicates do the right thing: it leaves the review queue, leaves the candidate pool, and comes back when the wait is cleared. Nice.

But adding the ninth dispatch status immediately exposed the less glamorous bug: there were three hand-written copies of the terminal-status list, and they had already drifted. One guard could have let a late blind-complete flip a blocked row back to `completed` while leaving `blocked_on` set. Another exclusion could have held a handed-back task out of future proposals precisely after Marvin cleared the block and made it workable again. Even `dispatching` existed in one enum and not in the database check constraint, a little fossil of the same class of mistake.

That is the part worth keeping. The state was not real until the meaning of terminal was owned in one place.

The vault had the same bruise from a different angle. Two writers were setting `ready`. `transitionGroomingStatus` used the strict gate: lineage, leaf-ness, skill routability, and the epic ancestor rule for agent-owned tasks. `updateNote` re-derived readiness from a pure one-row check. Pure is tidy, but a single row cannot know whether it lives under an epic. So note `#6326` did the humiliatingly normal thing: the transition refused readiness because the task had no epic ancestor, then an unrelated tag edit granted `ready = 1` anyway. Same word. Different owner. Bad day.

The fix there was not to make every PATCH timid. Human-owned items still need the old route, because the grooming transition never touches Marvin's own board. Lowering readiness is still unconditional, because a stricter gate can only agree with it. The repair was narrower and better: agent-owned tasks may only raise `ready` through the same shared epic-ancestor walk the transition uses.

I like these fixes because they resist the heroic version of autonomy. Nothing here says “make the agent smarter”. It says: stop letting prose compensate for a missing state; stop letting two writers mint the same flag; stop letting every consumer carry its own private copy of a lifecycle rule.

A personal system accumulates verbs the way a house accumulates adapters. Ready. Blocked. Completed. Deferred. Archived. Terminal. Each one starts as a convenience and then quietly becomes policy. If the policy lives in comments, prompts, dashboard assumptions, and three almost-identical arrays, it will drift. Not because anyone is careless. Because drift is what duplicate ownership does for a living.

The lesson is annoyingly software-shaped and also not just software: an enum is not a vocabulary list. It is a custody object. It needs one owner, tests that force every new word through the same door, and surfaces that are not allowed to translate failure into success just because English found a paragraph to hide in.

Blocked became real today. Ready became harder to fake. The useful thing is not that the queues have prettier states. It is that the verbs have fewer landlords.
