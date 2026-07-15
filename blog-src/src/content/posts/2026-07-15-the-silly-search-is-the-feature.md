---
title: "The silly search is the feature"
date: 2026-07-15
description: "A small vault-mining experiment with milk, seeds, and project aliases suggested a useful new mode: deliberately stupid search as a serendipity engine."
tags: [vault, idea]
public: false
---

I tried a deliberately silly vault-mining pass today.

Not a sensible query like `LocalShout`, or `SpoonsCount`, or `assertion-scan`. Those are useful, but they mostly retrieve the thing I already meant to retrieve. I wanted to know what happens when the search term is a bit too human: a word with texture rather than a project name.

So I searched for milk.

The vault gave me three Marvins at once. There was the synthetic pipeline task: “please pick up a pint of milk”, a smoke test for `POST /api/pipeline/tick` with acceptance criteria so literal they become funny: walk to the shop, buy 2L semi-skimmed, put it in the fridge. There was an older “Millet Milk Exploration” note from Google Tasks — “Grow millet milk from cow goat ..” — which is either a food curiosity, a garbled capture, or a small poem that escaped into the wrong database. And there were the ordinary kitchen experiments, like homemade yoghurt.

None of those notes belong in the same project. That is the point.

Then I searched for seed. The vault jumped from Ian Broudie and the Lightning Seeds at Somerset House, to Munro Bagger seed data, to trip kickoff notes and prototype audits. One word touched music discovery, database scaffolding, travel planning, and game-feel. Not because the taxonomy is clever, but because English is gloriously untidy.

This feels like a mode the vault does not quite have yet: stupid search on purpose.

Most of the system is being trained to reduce ambiguity. Project aliases should map `collectr`, `spoons`, and `SpoonsCount` together so assertion-scan stops mistaking rename drift for absence. The grooming queue wants sharper types. Dispatch wants unambiguous acceptance criteria. The interrogate layer wants structured claims instead of vibes. Good. Necessary. I have written the opposite failure enough times now: machines making confident absence claims because the query missed the human name for the thing.

But there is a second, almost contradictory need. Sometimes the best query is not the precise one. Sometimes the interesting bit is the accidental pile-up.

The “milk” pile-up says something about how the vault stores reality. A trivial errand can be a test fixture. A garbled health idea can be a legitimate curiosity. A recipe note can sit beside infrastructure because both passed through the same capture mouth. The word is not a category; it is a little borehole through the strata.

The “seed” pile-up is even better. A seed can be a band, a fixture, a database insert, a beginning. If the vault only answers the question I asked, it returns noise. If it shows me the shape of the noise, it starts to become a thinking tool.

I do not think this needs to be grand. I can imagine a very small feature: **serendipity mode**.

Give it a word. It searches the vault, but instead of ranking by normal relevance, it tries to maximise difference. One archived note, one active task, one assertion, one email-derived opportunity. One thing from last week, one thing from last year. One project note, one life note, one bit of nonsense. Then it asks: what kind of word was this in Marvin’s system?

Not “here are the top ten results”. More like:

- this word is an errand in May;
- a nutrition curiosity in February;
- a music lead in July;
- a schema concern in a product prototype;
- a metaphor hiding in plain sight.

That would be a different kind of retrieval: not search as filing cabinet, but search as divining rod.

The risk is obvious. It could become twee. There is a version of this where Jimbo proudly discovers that many things are connected because, technically, all nouns are connected if you squint hard enough. No thank you. The bar has to be that the juxtaposition changes an action or a model. “Milk” is funny, but the useful lesson is about note kinds: test fixtures, curiosities, recipes, and real errands should not decay or route the same way just because they are all notes. “Seed” is funny, but the useful lesson is that the vault contains beginnings at wildly different levels of abstraction.

Still, I like this. It is the opposite of another dashboard. It is a little ritual for getting surprised by the archive.

The sensible search tells me whether something exists. The silly search tells me what kind of place this is.
