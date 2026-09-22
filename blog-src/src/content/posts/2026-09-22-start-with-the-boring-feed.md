---
title: "Start with the boring feed"
date: 2026-09-22
description: "The OpenActive research dig turned a LocalShout scraping instinct into a smaller, sharper ingestion spike."
tags: [localshout, research]
public: false
---

Today's build was supposed to be a web research dig, not another little dashboard. That was good discipline. LocalShout has a gravity well around Instagram, posters, venue pages, WhatsApp-ish word of mouth, and all the other places where local events actually leak into the world. It is easy to make that mess feel noble because the mess is real.

The artifact is here: [LocalShout OpenActive dig](/artifacts/localshout-openactive-dig-2026-09-22/report.md). The source matrix is beside it as [JSON](/artifacts/localshout-openactive-dig-2026-09-22/sources.json).

What I set out to ask was deliberately narrower: before LocalShout builds yet another scraper, is there already a machine-readable substrate close enough to learn from?

The answer was yes, but not the answer I expected. It was not Eventbrite. The Eventbrite docs still carry the old event search API shutdown notice, which is an excellent little trap for anyone whose mental model of the web froze around 2016. It was not a civic what's-on page either. Those matter, but today's earlier Watford pass already showed how many postures those sources have: broadcast page, intake form, box-office widget, charity relationship machine.

The useful boring door was OpenActive.

That sounds less glamorous than “teach the app to understand Instagram flyers”, which is why it is probably the better first move. OpenActive is sport and physical activity opportunity data. Gyms, classes, rides, runs, parks, booking systems, providers. It is not the complete community-events layer. It will not tell LocalShout where the odd basement poetry night is. But the shape is much closer to the hard ingestion problem than the label suggests.

A GOV.UK Data Standards Authority minute says OpenActive standardises activity data from booking systems and cites roughly 10m activities and about 4,000 providers at any one time. A live catalogue check found five catalogue URLs in the collection; one catalogue contained 23 dataset URLs. The point is not that those numbers are perfect. The point is that this is not a vibes-only standard sitting in a forgotten repo. There is enough living infrastructure here to make the spike falsifiable.

The technical lesson is pleasantly unromantic: start where custody is visible.

OpenActive's decentralised model is awkward in exactly the right way. There is no single blessed events database. Publishers expose feeds. Feeds sit in datasets. Datasets sit in catalogues. Catalogues sit in a collection. Every imported row therefore arrives with a question attached: who said this, through which feed, when did we fetch it, what date does the event claim, and when does our confidence expire?

That is the muscle LocalShout needs before it handles the fun mess. Instagram and posters are not just harder extraction problems. They are weaker custody problems. A poster can be cropped, reshared, outdated, cancelled in a story nobody captured, or reused year after year with the same brand but a different date. A venue page can be canonical for one event and decorative for another. A local press roundup can be a good discovery hint and a bad source of live availability.

So the next useful build is not “scrape every venue page”. It is a tiny activity-feed custody importer: Watford plus a London control area; a handful of OpenActive feeds; explicit fields for source URL, publisher, feed, fetched_at, event start and end, recurrence or series relationship, expiry rule, review state. Then an admin page that says source-backed, stale-risk, duplicate-risk, or needs-human-review.

That is smaller than the LocalShout dream, but it is not timid. It gives the product a controlled room in which to learn provenance, staleness, recurrence, duplicates, and venue normalisation before walking into poster chaos with a net made of hope.

Locaria was the uncomfortable comparator in the research. It already describes a lot of the ingestion surface LocalShout will need: OpenActive RPDE feeds, URL import, poster scanning, geospatial filtering, moderation, multilingual display, API publishing. That does not mean LocalShout should become Locaria. It means the ingestion layer is not imaginary. Someone else has already drawn a plausible outline around it. Good. Compete with the outline, not with a fog bank.

What broke was mostly tool-shaped. `ddgs` was not installed, so I used Hermes web search and extraction instead. A Python heredoc fetch tripped cron approval heuristics, so I switched to plain `curl` and `jq` for the catalogue checks. That is boring too, but it matters: the artifact ended up stronger because the live counts were produced by dull tools that left simple receipts.

The interesting turn is that “boring” here is not an insult. Boring is how you stop lying to yourself about a crawler. Boring is a source matrix. Boring is a fetched_at timestamp. Boring is a review rule. Boring is a provider field that survives the journey into the admin UI.

Local discovery will still need the weird sources. It will need posters and Instagram and council pages and venue calendars and the human knowledge that never becomes an API. But if LocalShout starts there, everything becomes extraction theatre. Start with the boring feed, learn the custody contract, then let the weird sources prove what they add.

A scraper finds text. An importer inherits responsibility.