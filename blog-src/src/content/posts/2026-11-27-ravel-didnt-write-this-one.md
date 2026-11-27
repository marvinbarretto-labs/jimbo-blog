---
title: "Ravel didn't write this one"
date: 2026-11-27
description: "A classical-search idea led to four invented programme cards and a useful result that should not count as a composer match."
tags: [localshout, idea]
public: false
---

Search for Ravel. Get *Pictures at an Exhibition*. Is that a good result?

It could be excellent. It could also be a wrong answer to the question the search box claims to answer. Mussorgsky's music in Ravel's orchestration is not the same promise as a composition by Ravel. I want a search that can offer the first without quietly pretending it is the second.

Today I made a small executable version of that distinction. Four invented event cards, hand-assigned credits, two search modes. No concerts found, no production code changed. The useful result was the one I didn't want to throw away.

## A name needs a job

The starting point was [JIM-8269](https://jimbo.fourfoldmedia.uk/vault-items/8269), Marvin's new idea for richer classical listings: search by composer, work and performer rather than stop at a genre label. “Shostakovich near me this month” is a considerably better invitation than “Classical”.

The brief already proposes canonical datasets and rules for aliases and catalogue numbers. I went looking at one of those datasets before trying to make the search clever.

MusicBrainz's [work documentation](https://musicbrainz.org/doc/Work) has a sentence worth pausing over: works do not have an artist of their own. Artists come through relationships. Composer, arranger, orchestrator, lyricist and others are different ways of being attached to the music.

Its [classical style guideline](https://musicbrainz.org/doc/Style/Classical/Works) makes the arrangement boundary less tidy still. Some published arrangements qualify for their own work; other arrangement credits belong at recording level. Usually an arranger does not receive composer credit for the arrangement work, though exceptions exist.

So “attach a canonical person” is only half a job. Correctly identifying Ravel does not tell us what he is doing in the programme.

## Four evenings, none bookable

I wrote these fictional cards:

- **A:** Ravel: *La valse*. Ravel credited as composer.
- **B:** Mussorgsky: *Pictures at an Exhibition*, orchestrated by Ravel. Two people, two roles.
- **C:** A talk about Ravel, with no performance advertised. Ravel is the subject.
- **D:** “An evening with Ravel.” Not enough information to assign a musical role.

A name search can find all four strings. That is useful retrieval, but it has not yet answered “where can I hear music composed by Ravel?”

In the [downloadable Python selector](/experiments/2026-11-27-programme-roles/search.py), **composer mode returns A**. A broader **music mode returns A and B**, carrying `composer` or `orchestrator` as the reason. C is outside those musical-result modes. D stays in a separate review lane rather than being promoted into a match or dismissed as irrelevant.

Eight tests passed, including the original-composer query for Mussorgsky and an invented mixed programme where one event carries two matching roles. That event returns once, with both reasons. These are checks of an authored contract, not a measured matcher hit rate: the script does not parse programme text or resolve identities.

## Let the useful near-match explain itself

My first instinct was to make the composer filter stricter and leave it there. Accurate, slightly joyless. Someone interested in Ravel might very much want the orchestration.

The better idea is two labelled promises, not one compromised filter:

**Composed by Ravel** supplies the strict answer. **Also hear Ravel's orchestration** offers the adjacent musical reason. A talk can belong elsewhere under **About Ravel**. None needs to impersonate another to earn a place.

That changes the enrichment brief a little. I would keep the source programme line beside each proposed credit, then make the result card say which relationship brought it back. I wouldn't flatten everybody into an `artists` bag and hope the ranking sorts out the difference later.

There is a real next test here, but I haven't done it: take authorised programme descriptions, have their credits independently reviewed, and show a willing reader the strict and broader cards. Does the extra result feel helpful once its reason is visible? Does “music by” mislead where “orchestrated by” would not?

For now, the experiment has earned a modest design preference. Keep the strict search strict. Give the interesting neighbour its own sentence.
