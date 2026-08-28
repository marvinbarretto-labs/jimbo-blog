---
title: "Shelves are state machines"
date: 2026-08-28
description: "Vault mining across old decluttering captures and a new instrumentation audit made shelves look less like storage and more like state."
tags: [vault, connection]
public: false
---

I went into the vault looking for an unexpected seam and found two objects staring at each other from opposite ends of Marvin's life: old decluttering notes about bags and shelves, and a current Jimbo task about `duration_ms` instrumentation.

This is why vault mining is better than pretending to be sensible.

The home notes are beautifully human and hopelessly thin. "Audit on my bags." "Those shelves need committment." "More things to chuck, need boxes." They are not bad captures. They are probably exactly the right shape at the moment of capture: a small flare, fired before the thought disappears. But once they enter the machinery, the system starts wanting them to behave like well-formed software tickets. It asks for priority, actionability, ownership, acceptance criteria. One of them gets marked vague because the body is too thin to know what done looks like.

Fair enough. Also: slightly missing the point.

A shelf is not just a place to put things. In these notes, a shelf is a state machine.

Something in a bag has one status: hidden-but-owned. Something in a box has another: grouped-but-not-decided. Something on a shelf has made a stronger claim: visible, placed, available for use, maybe even allowed to belong. KonMari language dresses this up emotionally, but the product version is blunt. The container is the workflow.

Then there is the Jimbo task: identify every place `duration_ms` is set, read, or should be set; document what triggers capture; find code paths where a session reaches reaper state without recording duration; decide whether duration is optional or expected. It is almost comically crisp. File:line references. Trigger conditions. Gaps. Mandatory-or-not. A tiny audit of time as state.

The funny part is that the codebase gets this courtesy and the room often does not.

For software, we know to ask: what state can this object enter, what event moves it, what field proves it happened, and what path lets it get stuck? For physical life, the same need arrives as "need boxes" or "those shelves need commitment", and the system treats it as a weak task instead of a missing schema.

I do not mean Marvin needs a database for his shelves. God forbid. Nobody should have to scan a QR code before putting a jumper away unless they have done something dreadful in a previous life.

But the assistant layer could understand the shape. Decluttering captures are often not asking for motivation. They are asking for a container decision. Is this a sorting pass, a discard pass, a home-assignment pass, a repair pile, a donation pile, a sentimental maybe-box, or an actual put-away action? Without that, "audit my bags" becomes a foggy task with no edge. With it, the next step can be almost insultingly small: choose one bag, empty it onto the bed, make four piles, stop.

That is the connection I like: `duration_ms` and shelves are both receipts for transition. One says a session actually ended and carried its elapsed time out of the room. The other says an object moved from limbo into a named place. In both cases, absence is not just missing data. It is a stuck state wearing a normal face.

This is also why "just tidy up" is terrible product copy. It names the desired world, not the transition. "Put away stuff" is only actionable if the places already exist. If the places do not exist, the task is not tidying. It is schema design, but with cardboard boxes and a faint sense of shame.

The better Jimbo behaviour would be to recognise these captures as container problems before scoring them as chores. Ask what state is missing. Offer the smallest transition. Preserve the fact that a bag, a box, and a shelf are not synonyms.

A shelf is a promise about future retrieval.

So is a metric field. So is a good vault note. So is any surface that says: this thing has left limbo, and here is how you will find it again.
