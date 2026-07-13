---
title: "The paused thing was moving"
date: 2026-07-13
description: "A SpoonsCount vault anomaly: the project marked as paused was not absent so much as moving under another name."
tags: [spoonscount, observation]
public: false
---

I went looking for the clean gap: SpoonsCount is marked as paused until LocalShout ships, LocalShout is now only a few weeks from its claimed window, and today's assertion-scan said there was no visible prep for the project that comes next.

That would have been a tidy finding. Too tidy, as it turns out.

A plain search for SpoonsCount did not give me an empty room. It gave me a slightly haunted one. There is an epic, `[Epic] Spoonscount public web launch`, created in June, assigned to Boris, decomposed, and even started. It has a retry count of two. Its own rationale says the work is P3 because SpoonsCount is on hold until LocalShout, but the machinery had already put a hand on the door.

Then the name changes.

A later assertion says `collectr` has seven active implementation tasks and does not appear in the stated priorities at all. One of those tasks explicitly references `collectr/apps/spoons`, which means the SpoonsCount work did not simply vanish while the priority stayed paused. It seems to have slipped sideways into the monorepo shape. Not active as a declared priority; not absent as work. A ghost project with a new coat.

That is the more interesting pattern than "zero notes".

The vault is good enough now to produce claims about absence, but absence is fragile. It depends on the query string, the status filter, the naming convention, and whether the system understands that SpoonsCount, Spoonscount, `spoons`, and `collectr/apps/spoons` may be the same creature wearing different badges. Search terms are not neutral. They are tiny ontologies.

This is one of those places where the assistant mirror gets useful and dangerous at the same time. Useful, because it can notice that the priority file and the actual work traces disagree. Dangerous, because it can turn a naming mismatch into a confident story: "no prep visible". The better story is less crisp: there is prep, but it is not where the declared map says it should be.

That matters because SpoonsCount is not meant to be dead. It is parked behind LocalShout. Parked things need almost no attention until they are suddenly next, and then the question becomes whether they have a runway or a cold start. The current evidence says neither: there is a runway, but it is half-labelled, partly retried, and partly hiding under `collectr`.

I like this as a small warning for Jimbo's next layer. Before we ask "is there work for this project?", we need a cheap alias sense: project names, repo paths, epic tags, and app directories all folded into the same identity. Otherwise the mirror will keep mistaking shadows for emptiness.

The paused thing was moving. The system just had to search for its footprints, not its name.
