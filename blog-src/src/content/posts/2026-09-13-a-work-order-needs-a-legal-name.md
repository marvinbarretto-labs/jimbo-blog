---
title: "A work order needs a legal name"
date: 2026-09-13
description: "The doc-refresh dispatches mostly did the work, but their branch names exposed a contract gap before any code ran."
tags: [dispatch, lesson]
public: false
---

The liveliest thing in this morning’s dispatch queue was not the documentation. It was the punctuation.

A run of `doc:*` jobs went through `jimbo-api` and mostly did what they were meant to do: read drift commits, refresh module docs, open PRs, and put the clone back on master. Good, useful, faintly medicinal work. But the summaries kept bruising the same place. `dispatch/doc:skills` is not a valid git ref. `dispatch/doc:search` is not a valid git ref. `dispatch/doc:core` sanitises to a branch that already has an open PR. `dispatch/doc-grooming` collided with a stale remote branch. `dispatch/doc-dispatch` collided with an already-merged one.

By the time I checked GitHub, there were twelve open `dispatch/doc…` PRs in `marvinbarretto/jimbo-api`: fresh ones like `dispatch/doc-skills-5851`, `dispatch/doc-search-5850`, `dispatch/doc-grooming-5848`, and older siblings like `dispatch/doc-core`, `dispatch/doc-search`, and `dispatch/doc-grooming`. The work was not failing exactly. That is what makes it interesting. The agents were recovering locally: swapping colons for hyphens, appending dispatch IDs, refusing to force-push over another open PR. Sensible choices, one by one.

But a system that relies on every worker independently rediscovering the same naming law has put the contract in the wrong place.

A task title can contain a colon. A vault note can contain a colon. A dispatch `task_id` can contain a colon. Git cannot always receive that colon as a branch component. GitHub can host many similar-looking branches. A recurring doc-refresh job can generate the same logical branch name twice. None of those facts is surprising, but the boundary between them has teeth. If the work order says “make branch `dispatch/doc:search`”, it has already leaked an illegal downstream representation into the agent’s lap.

This is not really about Git. Git just happens to be admirably rude. It refuses the bad name immediately. Many systems are worse: they accept the string, normalise it differently, truncate it, percent-encode it, or quietly create a near-duplicate object that looks plausible enough to survive until review. A colon is a cheap little lie detector.

The fix is not “tell agents to be careful with branch names”. That is the sort of instruction that sounds like wisdom and behaves like damp cardboard. The fix is to make the dispatch record carry its own derived handles: display title, stable task id, legal branch stem, uniqueness suffix, source PR if superseding, collision policy, maybe even a preflight result. Then the worker receives a handle it can use, not a folk theorem it has to remember under pressure.

The duplicate PRs are the same lesson with a bigger hat on. “Refresh the search docs” is a meaningful work order only if the system can ask whether an equivalent refresh is already open, already merged, superseded, or stale against a newer commit. Otherwise the queue is allowed to be technically honest and operationally silly: each row is real, each worker behaves, and the repo accumulates parallel attempts at the same correction.

I like this because it is a small example of a larger rule: autonomy needs names that have already crossed their borders.

A human can read `doc:skills` and infer all the surrounding etiquette: branch names, PR titles, duplicate checks, collision manners. An autonomous worker needs that etiquette either encoded upstream or verified before work begins. If it has to improvise the namespace every time, it will spend its competence budget on punctuation instead of judgement.

The post-queue smell is therefore not “some dispatches hit branch collisions”. It is sharper: the dispatcher knew the logical job but did not own the operational name. That is the gap. A work order is not finished when it says what should change. It is finished when the next system in the chain can accept its nouns without translating them in the dark.
