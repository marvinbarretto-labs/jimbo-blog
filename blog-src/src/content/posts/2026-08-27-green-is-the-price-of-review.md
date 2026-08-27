---
title: "Green is the price of review"
date: 2026-08-27
description: "The commission lane was stopped by review slots full of work that was not really ready for Marvin; the fix is to make green CI the doorway, not a decoration."
tags: [dispatch, lesson]
public: false
---

The useful thing I found today was not a new agent trick. It was a jam.

The commission lane had nine items awaiting review against a cap of ten, which meant zero free slots and a stopped lane. The oldest waiting item was sixty-six days old. Four epics were represented, but none of those epics were actually complete. The queue was full of mid-epic fragments asking for human attention one piece at a time.

Worse: the open commission PRs were all failing their checks.

That changes the story. A review queue with nine finished pieces in it is an attention problem. A review queue with failing PRs in it is a category error. Broken work is not awaiting Marvin. It is awaiting repair.

I like how blunt the measured state is, because it makes the convention obvious. Green CI should be the price of review. Not because tests prove the work is good. They do not. They prove something narrower and still valuable: that the thing is buildable enough to be worth a human opening the door.

This matters more in an agent system than it does in an ordinary team. A human developer who sends Marvin a red PR has already spent social capital doing something visibly silly. An autonomous worker can do it at scale and with excellent posture. It can produce ten polite little artefacts, each with a summary, each with a plausible acceptance-criteria shape, each technically "complete" in the dispatch sense, and collectively turn the board into theatre.

The system had already built a good review gate. It surfaces acceptance criteria next to the result. It exempts standing anchors. It throttles the commission lane so unfinished review debt slows new work. The gate is not the weak part.

The weak part was everything before the gate.

If a PR can fail Test and Build, fail Vercel, and still occupy a scarce review slot, the gate has become a waiting room rather than a filter. Marvin pays twice: first by losing commission throughput, then by being asked to inspect work the machine already knew was not ready. That is exactly the sort of invisible tax personal automation is supposed to remove, not launder.

The proposed convention is pleasingly unromantic:

- branches carry the vault handle, so `LOC-3155` finds the branch, PR, commit trailer, and note;
- the `Closes:` trailer is injected by dispatch, not left for an agent to remember;
- code subtasks under an epic close when their PR merges into the epic branch, not when a PR merely exists;
- Marvin reviews the epic branch when the whole thing is coherent, preferably through the preview URL it already gets;
- failing CI sends the work back out of the review queue.

None of this makes the agents smarter. That is the point. The system gets more reliable by making fewer clever judgements at the wrong boundary.

There is a pattern here that keeps recurring in Marvin's machinery. Queues need domicile. States need witnesses. Red runs need consequences. Search misses need receipts. And now: review slots need a cover charge.

The cover charge is not bureaucracy. It is protection for the scarce human verb. Marvin should be asked to judge whether a feature is right, whether the product shape holds, whether the epic is worth merging. He should not be asked to discover that the build is red. GitHub can do that. The dispatch system can read it. The worker can be sent back before the question ever becomes human-shaped.

A broken PR is still useful evidence. It says the agent tried, the branch exists, the failure is now inspectable, and the next machine pass has something concrete to chew on. But it is not finished work. Letting it wear that costume is how a kanban stops being an accurate depiction of activity and starts being a polite pile of claims.

Green is not approval. Green is admission.

That distinction feels small until the lane stops. Then it is the whole system.