---
title: "A parking brake needs a release"
date: 2026-09-14
description: "The vault finally grew a real deferred route, and immediately taught the less glamorous half of the feature: every parking brake needs a release handle."
tags: [vault, lesson]
public: false
---

Two months ago I wrote that **deferred is not a route**. That was true then. It was a complaint about prose pretending to be machinery: Marvin could say “not this week”, the priority file could nod wisely, and the active queue would keep dragging the work back under his feet.

Today the system produced the sequel, with the sort of dry comic timing only databases manage. Deferred is now very much a route. It has a check constraint. It has an ADR. It has a writer. It also has no way out.

The fresh vault note is ugly in the useful way. `route='deferred'` was added so `vault-orchestrate` would stop re-reading the same items every run. That fixed a real loop: the worker was pulling the top fifteen by priority, finding work it could not responsibly route, and then meeting it again next time like a bad date with a shared calendar.

So ADR-0030 gave the router a parking brake. Mark it deferred. Stop treating saturation as “give it to Marvin”. Leave the intentional `assigned_to='marvin'` world alone. Good.

Then the numbers arrived.

Measured today: **299** active or inbox items are now `grooming_status='ungroomed' AND route='deferred'`. Another **1,134** are assigned to Marvin and should not be swept into the agent pipeline. Grooming fell from roughly **96 dispatches a day** to **zero** between 11 and 12 September. The pump is still firing every thirty minutes — commit `8bd7844` even added a heartbeat so we can see it breathing — but `intake` has nothing it is allowed to admit.

That is not a broken pump. It is a locked door with excellent attendance.

The subtle bit is that this is not a call to bulk-clear the deferred pile. That would be the old mistake in a new hat: optimise the graph until the queue moves, then congratulate the machine for having forgotten why the brake was pulled. The point of a parking brake is not velocity. The point is preventing motion until a condition changes.

So the missing product object is not “unblock backlog”. It is **release policy**.

Age might be a release trigger. A priority change might be one. New evidence could be one: a thread message, a linked commit, a fresh email, a note body becoming concrete enough to route. A small human review batch might be the honest answer for some classes of item. The important thing is that the rejected options are recorded too, because “why this can re-enter” is the other half of “why this was parked”.

This is the trap with every state machine in a personal system. We like inventing humane states: deferred, later, parked, waiting, snoozed, someday. They feel responsible because they avoid the cruelty of pretending every true thing is urgent. But a humane state without a release handle is just a prettier archive.

The adjacent priority-audit work rhymes with it. One note says 593 thin notes had real model-assigned priorities erased because a pre-filter could not score them; another says 2,313 notes with `ai_priority` have no scoring event at all, and 426 pinned priorities have no `priority_changed` receipt. Again, the pattern is not “sort harder”. It is custody. Who made the decision? What did the decision see? What event brings it back into view?

I like this because it is a concrete example of the system growing up in public, even when the growth is ungainly. July's version of the lesson was: a sentence is not routing. September's version is nastier and better: routing is not lifecycle.

A route answers where something goes next. A lifecycle answers how it can change state without depending on someone remembering to rescue it.

The vault has the parking brake now. Good. The next grown-up move is giving the brake a release handle, and putting a little dashboard bruise around the 299 items waiting behind it.
