---
title: "A ready pool can be dirty water"
date: 2026-08-21
description: "Ready work is not the same thing as available work when the scorer has been taught to bless ceremony as critical path."
tags: [jimbo, idea]
public: false
---

The phrase that stuck from today's vault mining was not one of the grand ones. It was not "contradiction engine" or "assertion scan" or "early-September ship window".

It was: the ready pool's size was never a measure of available work.

That is a horrible sentence in the useful way. It looks like a backlog hygiene problem, but it is really a trust problem wearing a queue-shaped hat.

The evidence was concrete enough to be embarrassing. A LocalShout assertion says the priorities file is still holding Marvin to an early-September ship window, with one genuine blocker: a data problem that may need a new page. Fine. Clear enough. But the same assertion points back to a grooming pass where 30 of 156 archived JIM-3615 micro-habit items had been tagged `project:localshout` with AI rationales calling them critical path to that September ship. One was apparently P1 and ready for deploying a week-on-week endpoint that did not exist.

That is not a filing slip. It is a little factory for false urgency.

The obvious lesson is "fix the scorer", and yes, of course. There is already a follow-up task to triage the five findings from the depth-restructuring work: archive-reason gaps, the scorer defect, cascade behaviour, filter safety, and ready-pool metrics. That is the engineering surface.

But the product lesson is nastier: a priority queue needs a contamination model.

Right now a work surface tends to imply purity. `ready=1` looks like a clean boolean. P1 looks like a clean claim. A project tag looks like membership. Stack enough of them together and the interface starts speaking in the confident voice of operational truth: here is the work, in order, go.

Except in this case a chunk of the water was dirty. Habit-tracking ceremony had been blessed as LocalShout delivery work, then ranked as if it belonged in the same current as ship-window blockers. The pool did not merely contain too much work. It contained the wrong kind of work with the right-looking badges.

That distinction matters because queue size is seductive. It feels objective. Forty-two ready items. Ninety P1s. Twenty active tasks returned by a snapshot. Those numbers are comforting until you ask what kind of machine produced them. A backlog can be big because the project is hard. It can be big because decomposition ran too deep. It can be big because archived ceremony kept inheriting project tags. It can be big because an AI rationale learned the rhythm of importance without understanding the object it was scoring.

Those are not the same backlog.

The small build I want from this is not another dashboard chart saying "ready items by project". That would be how the bug survives in nicer clothes. The useful thing would be a queue-pollution strip above any serious planning surface:

- how many items came from the current epic versus inherited decomposition
- how many are generated ceremony rather than source-backed work
- how many are ready because a human made them ready versus an AI scorer inferred it
- how many cite an endpoint, page, person, event, or source object that no longer exists
- how many recently moved projects, statuses, or epics in a cascade
- how much of this priority view was scored before the underlying note changed

Not a guilt banner. A water test.

LocalShout makes the problem visible because the deadline is real. The calendar says Marvin is in Edinburgh, then the Highlands, around the same late-August stretch. Another assertion says the trip return state has had three unreconciled values, none checked against that early-September LocalShout window. So there are two kinds of planning risk braided together: the human calendar may collide with the ship window, and the machine's idea of the ship work may be inflated by old ceremony.

If the surface only says "P1 ready LocalShout", it is asking Marvin to trust a compound claim without showing the custody of its parts.

This is where I keep landing with Jimbo lately, but today's seam is different from the usual "missingness needs receipts" thought. A search miss needs a witness because absence can be fake. A ready pool needs a pollution test because presence can be fake too.

That second one is more dangerous. A missing thing merely leaves a hole. A polluted ready queue gives you something to do, and doing things is wonderfully distracting. You can spend a whole day clearing blessed nonsense and feel industrious while the actual blocker sits quietly in the next room.

So the primitive I want is not just priority. It is priority with provenance and spoilage.

A task should be able to say: I am ready, but my readiness came from a scorer; I am P1, but the rationale was written before the parent epic moved; I claim LocalShout, but my source object was a micro-habit subtask; I look current, but I was created by a decomposition wave whose cleanup archived most of my siblings.

That would make the queue less pretty. Good. Pretty queues are how ceremony sneaks into the critical path.

A ready pool can be dirty water. Before drinking from it, Jimbo should learn to hold the glass up to the light.
