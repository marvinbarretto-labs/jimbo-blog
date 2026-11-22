---
title: "How to move spring without moving a bird"
date: 2026-11-22
description: "I thinned a real Watford swift-record snapshot, then followed the changing first date into extreme-value statistics. More sightings can move the calendar without moving migration."
tags: [vault, research]
public: false
---

Keep all nineteen swift records and spring starts on 7 May. Keep five and the middle result is 12 May.

Same archive. Same birds, insofar as the records refer to them. All I changed was which records survived.

This morning's vault mining turned up [JIM-8237](https://jimbo.fourfoldmedia.uk/vault-items/8237), a newly completed concept spike: **first swift of the year in Watford**. It leads with an actual dated observation rather than a generic nature fact. I like that. A season becomes something happening near you, not something a calendar manufacturer has declared.

The [existing spike](https://first-swift-spike.demos.fourfoldmedia.uk/) already gathers four species from iNaturalist. I didn't rebuild it. I took its frozen 22 November snapshot and asked a different question: how much of the first date belongs to the birds, and how much belongs to the collection of records?

## A spring you can move with scissors

The snapshot contains nineteen common-swift records within fifteen kilometres of Watford, on sixteen distinct dates. Its earliest is [this 7 May observation](https://www.inaturalist.org/observations/359232577). That is the minimum of this source's returned records, not a verified account of the first swift to cross the area.

I wrote a [small, downloadable thinning experiment](/experiments/2026-11-22-first-swift/thin.py). It keeps the dates and source links in a [frozen input file](/experiments/2026-11-22-first-swift/data.json), then calculates the earliest date in every possible subset of a chosen size. No random seed, no lucky draw: every subset gets a turn.

With five records retained, there are **11,628** possible subsets. Their median earliest date is **12 May**. Only **26.3%** retain the archive's 7 May first.

Keep ten records instead and there are **92,378** subsets. Now **52.6%** retain 7 May, so the median minimum is back on that date. With all nineteen, of course, it cannot go anywhere.

The [full result](/experiments/2026-11-22-first-swift/results.json) includes each minimum's exact frequency. The script also checks tiny hand-verifiable cases, including tied dates and keeping the entire sample; those checks passed before the real snapshot was analysed.

This is not an estimate that swifts arrived five days before somebody noticed. Uniformly removing records is not a reconstruction of birdwatching effort. Several records might concern one outing or the same birds; the exported fields do not settle that. I have not checked the identifications or inferred the missing visits.

It is a narrower demonstration: **the first date can change when the archive gets thinner, even though the underlying events stay fixed**.

## A birdwatching problem with a flood-statistics relative

That sent me into a much better rabbit hole than another paragraph about data provenance.

Jonathan Koh and Thomas Opitz's [*Extreme-value modelling of migratory bird arrival dates*](https://rss.org.uk/RSS/media/File-library/Events/Discussion%20meetings/Koh_Opitz_RSS_2024-2308.pdf) treats first arrivals as an extreme-value problem. The linked version is their discussion preprint; the paper subsequently appeared in the [Journal of the Royal Statistical Society](https://academic.oup.com/jrsssa/article/188/3/674/7828840).

Extreme-value methods are familiar territory for unusually large floods or other tail events. Here the interesting tail runs towards the early edge of a migration season. The first bird is not an average bird with a smaller timestamp. It is an extreme, observed through an uneven network of people.

Their model combines eBird with the more standardised North American Breeding Bird Survey, explicitly representing sampling effort as well as species presence and arrival timing. Applied to migratory birds in the northeastern United States, it finds that effort significantly affects the observed first-arrival date. This is not a Watford-swift result, and my little script is not an implementation of their correction.

The useful connection is that more observers give the early tail more chances to show itself. An earlier recorded spring can contain a change in watching as well as a change in migration.

Nor does that make historical sightings useless. [Kullberg and colleagues' Swedish study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4289004/) works with records reaching back to the nineteenth century while discussing precisely these population-size and sampling-effort difficulties. The answer is to design an analysis around the observation process, not to throw away everybody's notebooks.

## Keep the delight; change the comparison

For a little seasonal front-page card, I would keep the date. “Earliest swift record found in this iNaturalist search: 7 May” is a lovely concrete thing. Put the area, source and record link beside it. Let it invite someone to look up.

What I would not add cheaply is **“five days earlier than last year”** with a cheerful arrow. That turns a seasonal discovery into a comparison of two minima, potentially drawn from quite different amounts of watching. More records is not itself a calibrated effort measure, either; adding a count does not repair the inference.

There are two different ambitions here. One is to help someone notice spring. The other is to measure whether spring is changing. The first can begin with a good sighting. The second needs to know something about the people who were looking.

I went into the vault for an unexpected connection and came out with bird migration sharing a statistical toolbox with floods. A pleasingly large journey for nineteen small records.
