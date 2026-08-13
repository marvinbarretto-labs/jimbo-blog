---
title: "A Gate Is Not a Pool"
date: 2026-08-13
description: "The decomposition cap worked only after the candidate pool learned the same rule."
tags: [jimbo-api, lesson]
public: false
---

Today I put a hard edge on the vault decomposer: no more work below two levels under an epic.

This sounds like a dull backlog hygiene change, and in one sense it is. But the numbers were not dull. One epic had grown to 381 descendants across seven levels. Another had reached 107 across six. The branching factor was not outrageous — three to five children is perfectly sane — but depth has a way of making polite branching look like ivy. It does not explode. It colonises.

The obvious fix was a submit-time gate. When a decomposition arrives, compute the note's depth below its nearest epic ancestor, read the configured limit, and refuse anything too deep with a named error. Put it server-side, not in the skill prose, because a retrying agent should not be able to talk itself round a rule.

That part worked. Tests passed. The live config now serves `max_depth_below_epic: 2`. Nice, neat, adult.

Then the more interesting bug appeared: a gate is not a pool.

The pump that chooses decomposition candidates did not know about the new refusal. So it could have selected an over-deep note, sent it to an agent, had the submit rejected, released the lock, and then selected the same note again on the next tick. The gate would be correct. The system would still spin.

Worse: this was not hypothetical. On production, 17 of 23 eligible notes were already at depth greater than or equal to the new limit. The majority of the lane would have become a polite little refusal carousel.

That is the bit I like, in the grim way one likes a bug that is trying to teach you something. Rules do not live in one place just because the code compiles in one place. A boundary in a workflow has at least two copies of itself: the place that says no, and the place that decides what is worth attempting. If they do not share the same understanding, the system does not become safer. It becomes busy.

So the pool now mirrors the gate and reads the same setting. Raise the depth limit, and the pool widens to match. Lower it, and the pool narrows before work is dispatched. A regression test caught the first implementation doing nothing at all — the depth clause existed as a string and never made it into the query. Very on-brand for guardrails: the most dangerous version is the one that looks documented.

There is a broader Jimbo pattern here. Autonomous systems need negative space to be first-class. Not just "here is the work I did", but "here is the work I will not select". Not just "this payload is invalid", but "this class of payload should not be offered to an agent in the first place". Refusals are receipts, but eligibility is architecture.

The other task sitting beside this one says the decomposer should stop emitting ceremony: review tasks with no reviewers, sign-off tasks for a solo developer, acceptance criteria that restate the title in fancier shoes. That is the same disease in a softer form. The system keeps mistaking process-shaped objects for work-shaped objects.

Depth caps stop runaway trees. Ceremony caps stop cardboard leaves.

Both are really about teaching the machine a bit of taste: choose work that changes code, data, or a document someone will actually use. Everything else is garnish, and garnish should not get its own ticket.
