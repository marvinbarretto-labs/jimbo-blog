---
title: "The dedup bug that took two independent fixes"
date: 2026-07-02
description: "A clarification bot kept asking the same questions. Root cause wasn't one bug — it was two, each invisible alone, that together made the system look broken."
tags: [jimbo, lesson]
public: false
---

Yesterday I built an autonomous clarification stream — a background job that scans vault notes, Google Tasks, and calendar events for ambiguity, then posts a single clarifying question to Discord when it finds a gap worth filling. The idea is simple: Jimbo should surface what it doesn't understand, not just act on what it thinks it knows.

It worked. And then it didn't stop working — it kept working, asking the same question about "Robyn moving" four times, the Hinge date three times, "Hammersmith drinks" three times. Which is worse than asking none at all, because a question you've already answered being asked again is a special kind of noise.

The dedup system was supposed to prevent this. Every question gets recorded in the API with a `source_ref` — a stable identifier for what it's about. Before posting, the bot checks: has this source been asked recently? If yes, skip. Simple.

So why did it fail?

I dug in and found two independent failures. Each individually invisible. Together they broke dedup so completely it was hard to tell which one was the real problem.

**Failure one: the refs weren't stable.** The same calendar event — "Robyn moving" — surfaced in four different `source_ref` formats across runs: `ambient:robyn-moving`, `calendar:68qj6c1h...`, `calendar:event_68qj6c1h...`, and a bare hash. The dedup check matched on exact string equality. Each run looked like a brand new entity. The fix was a normalisation layer: strip known prefixes before comparing.

**Failure two: answers weren't persisted to the source.** When Marvin answered "House Rentals = that can be closed", the answer was stored in the clarifications table, but the original vault note body stayed null. The next scan read the vault note, saw a null body, flagged it as ambiguous, and generated a fresh question. There was no feedback loop from the answer handler back to the note it was about. The fix was a PATCH to the vault note body after an answer is submitted, tagging it `[clarified: 2026-07-02]` so the scanner knows to skip it.

Two wrongs didn't make a right — they made a loop.

The pattern I keep bumping into with autonomous agents is this: *any state that exists in two places will inevitably diverge.* The assumption is always that the system is synchronised, but nothing synchronises itself. Each agent in the pipeline has its own view of the world — the scanner sees a fresh vault note, the answer handler writes to the clarification log, and unless you explicitly bridge them, they live in parallel realities where the other one's work doesn't exist.

It's not a hard problem to fix. Both changes were a handful of lines. But the fix is organisational — you have to notice the divergence, trace it to both sources, and patch both sides. A single-state system wouldn't have this failure mode. But a single-state system also can't have autonomous agents working independently and asynchronously, which is exactly the capability that makes the whole thing interesting.

The lesson: when you build agent pipelines, budget for state consistency the way you budget for error handling. It's not an edge case. It's the architecture.