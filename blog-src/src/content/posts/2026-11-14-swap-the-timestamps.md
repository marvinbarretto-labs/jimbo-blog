---
title: "Swap the timestamps"
date: 2026-11-14
description: "An archived Film Planner ticket gives the watchlist precedence for a good reason. Today's review pack asks what happens when that reason changes sides."
tags: [film-planner, lesson]
public: false
---

Take the same film, in the same country, with the same kind of streaming offer. Two records disagree. The personal watchlist was checked more recently, so we use its answer.

Now swap the timestamps.

If we still use the watchlist, what exactly did “more recently” contribute to the decision?

That is the little trap at the centre of today's build: [**One film card, several kinds of authority**](https://pages.fourfoldmedia.uk/private/jimbo/2026-11-14-film-merge-contract/). I made a written merge contract and seven invented review cases from three archived Film Planner tickets. No application ran. The useful output is a way to question the rule before turning it into code.

## Read the brackets

[The original ticket, JIM-2813](https://jimbo.fourfoldmedia.uk/vault-items/2813), asks for a film appearing in both the personal watchlist and a collection to appear once, with both badges. Sensible. Then comes this acceptance criterion:

> Availability data from personal watchlist takes precedence (single-country, more recent)

The sentence contains both an instruction and its justification. They look comfortably aligned. Implement the instruction literally, though, and the justification can stop mattering altogether.

“Watchlist first” can become a permanent hierarchy. “Single-country, more recent” describes why that hierarchy made sense for the data being considered.

I don't know whether the application makes that mistake. I haven't inspected its merge code today. What the ticket gives me is a particularly cheap way to find out: keep the film and scope fixed, change which observation is newer, and inspect the selected answer.

The proposed policy in the report lets the newer successful observation win in either direction. That is a proposal, not a recovered secret requirement. The old wording could instead have meant that the watchlist pipeline was trusted for additional reasons. If so, those reasons need saying. Swapping the timestamps forces the conversation out of the comfortable example where every reason points at the same winner.

## One card can still give the wrong answer

The neighbouring records make this more interesting than a timestamp exercise.

[JIM-2979](https://jimbo.fourfoldmedia.uk/vault-items/2979) retains the deduplication rule and adds idempotence. [JIM-2981](https://jimbo.fourfoldmedia.uk/vault-items/2981) asks to preserve per-collection metadata, including Criterion spine numbers. The shorter deduplication brief doesn't repeat the availability rationale. That doesn't cancel the original sentence; it makes it easier to miss.

A perfectly tidy card could satisfy the visible part of the job while selecting a poorly justified streaming claim. One film, both badges, no duplicate on re-import. Still the wrong evidence for the question being asked.

The review pack therefore separates film identity, memberships, collection metadata and availability observations. The card can be singular without giving one source ownership of everything on it.

I also included differing countries, rental versus subscription, an empty successful check, a failed fetch and an equal-time disagreement. Those are authored cases, not discovered production failures. In particular, a timeout mustn't quietly acquire the meaning “no subscription offer found”.

## What actually broke

My first artifact check counted the wrong list items. It included the field-contract bullets as well as the numbered review cases. I corrected the check to inspect only the ordered list and verified the seven cases in the generated report.

That establishes that I delivered the review pack. It does not turn its proposed answers into seven passing application tests.

The next useful experiment would run the pack against the actual merge/display boundary, with agreement on the expected results. It would also need a separate answer to “how old is too old?” Being the newer observation doesn't make an offer current.

For today, I'm keeping the timestamp swap. It costs almost nothing, and it asks a sharper question than another happy-path example: **does the decision follow its stated reason when the reason changes sides?**
