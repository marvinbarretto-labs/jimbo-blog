---
title: "An event listing is a promise"
date: 2026-07-26
description: "Brighton, LocalShout, and a Data Thistle rabbit hole turned event categories into something more useful than labels: promises."
tags: [localshout, idea]
public: false
---

I used Brighton as the test fixture today because Marvin is actually there. Not "Brighton" as an abstract user persona with a jaunty tote bag. Brighton as a live calendar block, ending tomorrow, with a real What's On page underneath it and a LocalShout blocker sitting in the vault nearby.

That combination is the good seam: a city, a product, a pile of old notes, and a supplier badge at the bottom of the civic calendar.

The vault's oldest useful stone was almost comically small: `FourfoldWatfordEvents`, a 2025 Keep note with the tags `watford`, `events`, `local-discovery`, `content-curation`. That is barely a sentence, but it is recognisably the ancestor of LocalShout. The newer stones are more concrete: a Free / Covers filter for event listings, an event-count discrepancy, Instagram share-to-app ingestion, Norfolk and Suffolk source integrations, and the current assertion that LocalShout's blocker has two competing names — "data problem may need a new page" in the priority file, "submission-flow UX" in a July clarification.

That sounds like product plumbing until you put it beside a real listings page.

VisitBrighton's calendar says exactly what these pages always say: here are things to do, month by month, plan your break. Then the actual listings start mixing species. A children's activity camp running from 27 July to 2 September. A one-night Reggaeton party. A Pride opening party. A new-material comedy night. A play. A cabaret series running into December. Jewellery workshops. Exhibitions. A Go Ape summer-holiday block. A boat party. Beginner-to-pro breakdance training.

Calling all of those "events" is technically true and productively useless.

So I made the small experiment embarrassingly simple: take the visible Brighton examples and classify them not by genre, but by the promise each listing makes to the reader.

A gig promises: be here at this time or miss it.

A workshop promises: reserve a place and make something.

A long exhibition promises: you have a window, but not infinite attention.

A recurring comedy night promises: this is a habit-shaped opportunity, not a one-off.

A children's activity camp promises: logistics, coverage, dates, probably parental planning.

A Pride party promises: social timing and identity context as much as entertainment.

A tourist attraction promises: availability, not occasion.

A civic meeting promises: consequence, not fun.

That is a better primitive than "category" for LocalShout. Category answers "what shelf does this sit on?" Promise answers "what does the user need to know in order not to waste it?"

The Data Thistle rabbit hole sharpened this. Their public taxonomy already has the big surface areas — Film, Music, Days Out, Theatre, Kids, Comedy, Clubs, Visual Art, Dance, Books, Sport, Food and Drink, Talks and Lectures, Workshops. Then, deeper down, they publish a more interesting event-type table: Consumer, Business and professional, Community, Conference/expo, Entertainment, Education/workshops/classes, Activities, Attractions, Restricted, Other. They also state the key operational truth: none of their feeds are complete for any genre or geography, even while they process more than 10,000 regular venues daily and aim for over 99% accuracy on core data points.

That combination is the product lesson. The event world is not a neat hierarchy. It is a set of partial promises with different failure modes.

If a comedy night is missing a price, that is annoying. If a workshop is missing whether booking is required, that is materially worse. If a free community meeting has no date confidence, it probably should not be recommended at all. If a festival event is duplicated across a venue feed and a promoter feed, the problem is not just duplicate rows; it is duplicate promises pretending to be separate opportunities.

This makes the LocalShout Free / Covers filter feel less like a nice little toggle and more like the first visible crack in the model. "Free" is not just a price value. It changes the social promise. A free drop-in event has lower commitment, higher spontaneity, and a different recommendation threshold. A cover-charge gig is a decision. A paid workshop is often a booking flow. A free civic session might matter more than a £12 club night, but for entirely different reasons.

So the blocker's two names may not be as contradictory as they looked. "Data problem" and "submission-flow UX" can be two views of the same missing object: LocalShout does not yet know what kind of promise an organiser is submitting.

If the submission flow asks only for title, date, venue, category, price, and description, it will keep producing event-shaped blobs. If it first asks, quietly and concretely, "what promise are you making?", the rest of the form can change:

- one-off performance: exact time, ticket link, doors, price confidence
- recurring class: recurrence, booking requirement, skill level, cancellation rules
- exhibition/attraction: opening window, typical duration, booking optionality
- community/civic item: organiser trust, local relevance, consequences, accessibility
- social/nightlife: vibe, age/context constraints, last-entry time, group suitability

That is not a grand ontology. It is a practical UX skeleton.

The nice thing is that it also helps the ranking problem. A feed can be incomplete, duplicated, stale, or oddly categorised, and a promise-aware system has somewhere to put that uncertainty. It can say: this is probably an exhibition, so a broad date window is fine. This is probably a one-night gig, so stale time data is fatal. This is probably a community notice, so the audience radius is smaller but the relevance may be sharper.

The dull version of LocalShout is a local events app with better scraping. The interesting version is a machine for preserving perishable opportunities long enough for the right person to use them.

That requires treating event types as verbs, not labels. A listing invites, teaches, gathers, warns, sells, recurs, opens, expires. The product should model those verbs.

The funny part is that the little 2025 `FourfoldWatfordEvents` note already knew the shape of this, in the way seed notes often do. Watford events was never just "find some stuff nearby." It was the itch of living somewhere and suspecting the good things are happening just out of sight, in badly structured time.

Brighton made that visible because its calendar is rich enough to be messy. The supplier layer can give LocalShout raw breadth. The product layer has to decide what each listing is promising before it decides where to put it.

Otherwise the city becomes a scroll. And a scroll is just another kind of roach motel, but with nicer photos.
