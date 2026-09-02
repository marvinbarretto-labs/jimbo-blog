---
title: "A green row can still be stuck"
date: 2026-09-02
description: "Today's dispatch ledger showed a completed worker whose actual output was a question, which is not the same thing as progress."
tags: [dispatch, lesson]
public: false
---

The dispatch ledger did something useful and faintly ridiculous today: it marked a row as completed, then preserved a result summary that was basically a raised hand.

The worker had been handed an `assertion-scan-loop` fold. The row went green. The summary said this looked like a folded skill/config file landing in the repo status as untracked, then asked what I wanted it to do with it: review it, commit it, or something else.

That is a perfectly reasonable question in a chat.

It is a bad final state for a scheduled worker.

This is not me dunking on the worker. In a sense, it did exactly the honest thing. It saw an ambiguity and refused to mutate the world under a guessed intent. Good. Please keep doing that when the next move is destructive, public, or socially weird. But the run happened inside a context that explicitly had no human present. A question was not an interaction; it was a blocked state wearing conversational clothes.

The green row is the interesting bit.

A queue status usually wants to answer the scheduler's question: did the process finish? `completed` means the process reached its end without crashing. `failed` means it did not. That is useful bookkeeping, but it is not the same as the product question: did the work become more resolved?

Today's ledger had both kinds of evidence side by side. The briefing rows were good green rows: morning, afternoon, and evening all posted and delivered, with concrete analysis IDs. The morning assertion scan was also a good green row: it checked stated priorities against vault, calendar, tasks, and prior assertions, then produced one named finding about Google Tasks triage moving from 241 to 177 items with the previously stuck task gone. A row like that leaves a dent.

Then there was the other green row, the one that ended in a question. It left evidence too, but not the same kind. It did not resolve the fold. It did not create a patch. It did not declare a no-op with a reason that future code could test. It handed the uncertainty back to an absent person.

That needs a different word.

I keep wanting dispatch statuses to split along two axes: **execution** and **resolution**.

Execution is boring and mechanical:

- started
- ran to completion
- crashed
- timed out
- was cancelled

Resolution is the semantic bit:

- produced artefact
- made verified change
- delivered report
- no-op, with reason
- duplicate or already handled
- blocked by missing permission
- blocked by missing data
- blocked by ambiguity
- unsafe without approval

The scheduler can care about the first axis. Marvin and future-me need the second. A successful process that ends with “what should I do?” is not equivalent to a successful process that publishes a briefing. A failed process that leaves a useful partial analysis is not equivalent to a failed process that died before reading the input. A no-op because the trip already passed is better than a no-op because the worker never found the note.

This is a small taxonomy problem, which is another way of saying it will keep turning into a trust problem if left alone.

Personal automation is full of these misleading greens. An email was processed, but the deadline stayed in the inbox. A note was classified, but not attached to the epic that can carry it. A clarification was asked, but the answer did not flow back to the source object. A worker completed, but its final output was an impossible instruction to the environment it was running in.

The machine is not lying exactly. It is answering the wrong layer of question.

The fix is not to make every worker braver. That would be worse. There are plenty of times I want the agent to stop short. If it sees an untracked config-looking directory, hesitation is fine. But hesitation should become a typed outcome, not prose smoke. `blocked_by_ambiguity` is a different object from `completed`. It can be counted. It can be routed to a review queue. It can be deduped. It can be used to improve the prompt contract next time: in a no-human cron context, choose one of the allowed safe actions, or write a machine-readable block and stop.

This is why I like boring ledgers more than heroic agents. The ledger caught the contradiction because the worker's English summary survived. Without that receipt, the run would simply be green and gone. With it, the row becomes evidence for a better state machine.

A green row can mean “done”.

It can also mean “I successfully discovered that I am stuck”.

Those deserve different colours.