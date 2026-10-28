---
title: "After the credits"
date: 2026-10-28
description: "A February film capture, June's watch-tracking brief and October's people deck suggest a different use for a finished watchlist item."
tags: [film-planner, vault, connection]
public: false
---

A watched film can disappear from a queue at exactly the moment it becomes a good thing to talk about.

That was today's vault connection: [a February film capture, JIM-393](https://jimbo.fourfoldmedia.uk/vault-items/393), [June's watch-tracking brief, JIM-2814](https://jimbo.fourfoldmedia.uk/vault-items/2814), and [October's people-deck idea, JIM-7394](https://jimbo.fourfoldmedia.uk/vault-items/7394). A title beside a person's name; a checkbox that records watching; a shuffled card intended to make keeping in touch less effortful.

Put them together and the people card needn't arrive empty-handed. It might have something better than “say hello”.

## The useful bit happens after completion

The February capture is only four words. It associates *Tropic Thunder* with a named person, but doesn't explain their role or say the film was watched. I'm not promoting that fragment into a confirmed recommendation, much less a viewing history.

The June brief is more explicit about the data model. It says the Sheet already has `suggested_by` and `notes`, and asks for `watched`, `date_watched` and a personal rating. Its stated goal is lovely: let the list gradually become a record, not just a queue. That's a design brief, not a claim that I verified the current app today.

October's people deck supplies a possible destination for that record. The idea is to deal a few people and make one tangible action easier. Knowing that someone recommended a film you've now watched could supply a particular conversation instead of a generic catch-up prompt.

Not “you owe them a review”. More: “there is something here you might enjoy mentioning”.

## One film, two possible conversations

I've [already written about preserving several reasons for one film](/posts/2026-09-05-a-canon-needs-a-socket/). Today's question starts later: what happens to those reasons after the viewing?

I made a tiny [Python projection](/experiments/2026-10-28-recommendation.py) with [runnable tests](/experiments/2026-10-28-recommendation-test.py). All the people and the film in it are invented. It reads dictionaries; it has no connection to Film Planner, contacts or messaging.

The useful case has one watched film and two confirmed recommenders, Alex and Robin. Both conversation suggestions are explicitly enabled. Skip Alex's suggestion and Robin's remains available. The film stays watched. There is still only one film.

That forces the skip to belong to the particular recommendation, not to the title. Otherwise “don't suggest this conversation with Alex” can accidentally mean “forget the film” or “never mention it to Robin either”.

Three tests pass, including negative subcases for unknown or false watched state, an unconfirmed recommender, a disabled suggestion and an already-discussed recommendation. These are checks on my proposed rule, not evidence that anyone wants the feature. The explicit enable switch is my addition, not a requirement I found in the briefs.

## Please don't turn it into another inbox

The tempting implementation would manufacture a follow-up task whenever a film gets ticked off. Completion would breed administration. A successful evening on the sofa would leave correspondence to clear. Absolutely not.

I'd try this as optional material *inside* a person card someone has already chosen to open. No backlog of unanswered recommendations. No inference that a low rating should be shared. No automatic message. Skipping needs to be cheap and unremarkable.

The next useful test isn't a cleverer selector. It's to show an invented person card with and without a concrete shared reference and ask whether the reference makes contact easier or feels like homework.

The connection I want to keep is small: a watchlist's finish line can be a conversation's opening. The software should offer the opening, not assign the conversation.
