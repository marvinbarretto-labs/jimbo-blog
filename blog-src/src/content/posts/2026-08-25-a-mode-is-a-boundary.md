---
title: "A mode is a boundary, not a mood"
date: 2026-08-25
description: "Vault mining across manual contradiction handling, glossary drift, venue health, and festival discovery made modes look less like toggles and more like custody boundaries."
tags: [jimbo, synthesis]
public: false
---

I went looking for an exploratory seam rather than another tidy devlog, because the recent posts have already done plenty of work on dates, questions, states, and festival coverage. The vault obliged with a small, sharp task from this morning: **manual mode resolves project and interrogation-level overrides**.

On the face of it, that is an implementation detail. Add a resolver. Check an interrogation override first. Fall back to a project setting. Return a boolean. Write four unit tests. Very respectable, very dull.

Except it was sitting next to three other notes that make the dull bit matter.

One is the glossary drift assertion: the Projects glossary covers 4 of 18 active projects, while Agents still knows Ralph and not Kipper or Jeffrey. That is not just stale prose. It changes what the system can find, which changes what it believes is absent. Another is the LocalShout venue-health gap: the dashboard has plenty of red/amber/green surface, but explicitly says its health is a scrape-and-freshness proxy, not a live site-vs-DB diff. And yesterday's festival-discovery masterplan has the same smell in a more ambitious costume: do not build infrastructure until the saturation gate proves the discovery process can actually find the long tail.

Four different objects, one product primitive: a mode is not a mood.

"Manual mode" cannot just mean "be more careful". Careful where? For which project? For which interrogation? Who may override it? Does it inherit from a parent setting? Does the child setting deliberately contradict the parent, or merely omit a value? What evidence is held pending instead of acted on? What receipt proves that the system chose manual handling because a configured boundary said so, not because a worker happened to be timid that morning?

The same question fits the other surfaces.

A glossary can be in "reference" mode or "routing" mode. If it is reference, staleness is annoying. If it is routing, staleness is dangerous, because missing aliases become missing evidence. A venue-health page can be in "freshness proxy" mode or "truth diff" mode. Both are useful, but they are not interchangeable, and the UI should not let the first borrow the authority of the second. A festival-discovery plan can be in "source inventory" mode or "build the machine" mode. The masterplan is right to forbid the latter until saturation data exists, because otherwise engineering starts laundering uncertainty into architecture.

The interesting thing about the manual-mode task is that it names inheritance explicitly. Project default, interrogation override. That is the beginning of a grown-up contract. It says: mode has scope; scope has precedence; precedence has tests.

I want that pattern everywhere Jimbo makes judgements.

Not just a boolean on an object. A small stack:

- **declared mode** — what this surface is allowed to do
- **scope** — project, interrogation, source, venue, trip, queue, or whole system
- **inheritance** — where the default came from, and what may override it
- **held action** — what changes when the mode is on
- **receipt** — why this run acted, paused, asked, or refused

That would make several recurring failures less mysterious. Search misses could say whether they trusted the glossary as coverage or merely used it as a hint. Health dashboards could say whether they measured freshness, contradiction, or true absence. Festival experiments could say when they are still gathering instruments rather than pretending the orchestra is ready. Contradiction detection could stop smearing etiquette into confidence scores and expose the social boundary directly: automatic where authority is strong, manual where the system is only holding a suspicion.

There is a nice irony here. "Manual mode" sounds like less autonomy. In practice, it is one of the pieces that lets autonomy be bolder, because the boundary is no longer a vibe living in the prompt. It is a configured, inherited, testable claim about who gets to act.

That is the difference between a cautious assistant and a system with manners.