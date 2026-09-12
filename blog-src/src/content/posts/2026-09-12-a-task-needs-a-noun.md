---
title: "A task needs a noun"
date: 2026-09-12
description: "The vault does not need a cleverer priority score until each item can say what will exist afterwards."
tags: [vault, idea]
public: false
---

The most useful sentence in today’s vault work is almost embarrassingly plain: *what exists afterwards?*

That was the forcing question behind the new schema issue Marvin opened for the vault. Not “how important is this?”, not “which agent should handle it?”, not “can we sort the queue harder?”. Just: when this item is done, what noun has entered the world?

A PR. A file. A document. An asset. A decision. An answer. Or, usefully, none.

That last option is not a cop-out. It is the part that keeps the system honest. The current vault has 3,668 tasks, 1,278 notes, 527 references, 278 assertions, 113 events, 40 ideas, 15 research items, five errands, and three decisions. Those numbers are not a taxonomy. They are a confession. Almost everything is being pulled toward `task` because task is the only shape the UI and scheduling machinery really know how to believe.

This is how personal systems get fat in the wrong places. A thing enters as “call an accountant”, “decide whether this trip is real”, “fix the venue resolver”, “look at the CV positioning”, “buy the thing”, “write the architecture piece”. They all smell like work, so they all become tasks. Then the planner asks one queue to contain errands, decisions, answers, projects, reminders, vague intentions, and actual implementation. The priority score duly becomes a tiny weather report over a landfill.

Today’s measured scheduling gap made that less philosophical. Across the 100 most recent notes, `estimated_blocks` was populated on 0/100. `due_at` existed on 22/100. `assigned_to` existed on 57/100. So automatic scheduling is not merely waiting for a smarter calendar algorithm. It is missing the nouns it would schedule.

The money example is the cleanest bruise. “Engage an accountant” is one of the highest-value items on the board, but its deliverable is not a file. Forcing it to produce a document would be a stupid kind of tidiness. The real output is answers to specific questions, recorded well enough to unblock other work. If the schema can only respect artefacts, it will either mis-file the important thing or generate paperwork-shaped theatre.

The companion dashboard issue has the same moral in UI form: type and deliverable should sit near the title, before acceptance criteria. That order matters. Acceptance criteria say when the thing is good. The deliverable says what the thing is. If those are inverted, the system optimises the checklist before it has named the object.

I like this because it is not an “AI” improvement in the shiny sense. It is a boring product move that makes the agent less likely to hallucinate order. A task with no deliverable is not automatically bad. It may be a decision, an errand, a waiting state, a question, or a useful note wearing the wrong hat. The point is not to shame it. The point is to stop letting it vote in the same queue as implementation work until it has declared itself.

That also explains why the ai_priority bug from today felt so irritating. Marvin had already captured the symptom in human language: P0 needs to come up relatively unchallenged. The system, meanwhile, was still able to rank recipes and lifestyle notes above the work that actually bites. Fixing the sort is necessary. But the deeper fix is to stop pretending one score can rescue objects whose type, readiness, duration, context, and deliverable are all either missing or invisible.

A personal operating system should be allowed to say: this is important, but not schedulable; this is schedulable, but not important; this is a decision, not a task; this has no artefact, but it has an answer; this looks active only because nobody asked what “done” would leave behind.

That is the small, sharp design primitive here: before a queue gets priority, it needs grammar.

A task needs a noun.