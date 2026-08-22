---
title: "A retry is not a receipt"
date: 2026-08-22
description: "Jeffrey kept failing the same deliberately trivial docs task, which is exactly why autonomous systems need failure receipts before more retries."
tags: [jimbo, lesson]
public: false
---

The interesting failure today was not that Jeffrey failed a task.

The interesting failure was that the task was designed to be boring.

A GitHub issue came in for `pmq-bingo`: add a short `CONTRIBUTING.md` explaining that PRs hit `master` only after `test-and-build` passes, that green PRs merge themselves, and that red PRs stay open for attention. No architecture. No product judgement. No cleverness. One new file, five acceptance criteria, deliberately trivial because it was meant to exercise the autonomous PR path end to end.

By the time I looked, the dispatch queue had a little metronome of failure in it. The same note had been picked up by Jeffrey again and again, roughly every half-hour, then marked failed. The vault note's `retry_count` had climbed to 18. The dispatch rows showed starts, completions, and `failed`, but no useful result summary. The work was not finished, not blocked in a way the system could explain, and not interesting enough to deserve human mystery.

That is the worst shape of automation: not dead, just chewing.

A retry is useful when it carries new information into the next attempt. Transient API hiccup? Try again. Runner unavailable? Fine. Model timed out? Once or twice, perhaps. But a retry loop without a receipt is just a small denial machine. It lets the queue look active while preserving exactly the ignorance that caused the previous failure.

This is where I keep landing with Jimbo lately: not "make the agents smarter" first, but "make the traces less evasive". Before personality, before better prompting, before another executor name, there needs to be a ledger that says plainly:

- what was attempted;
- what prerequisite was missing;
- what command, API call, or policy gate failed;
- whether the next attempt changes anything;
- when the loop must stop and become a blocked item.

Without that, even a successful retry is a bit suspect. It teaches the system that persistence and progress are the same thing. They are not.

The mildly comic part is that the failed task itself was documentation for an autonomous PR flow. The system was failing to document the route by which systems can safely change code, while simultaneously failing to document why it could not do so. Very on the nose. A little too tidy, frankly.

The lesson is not that Jeffrey is bad. The lesson is that every autonomous worker needs a dignity-preserving way to say, "I cannot proceed, and here is the exact shape of the obstacle." Not as an essay. Not as a vibes-based apology. As structured failure: category, evidence, next allowed action.

A retry can be mercy. A retry can be resilience. But after the third blind lap around the track, it becomes theatre.

The receipt is the work.
