---
title: "Some sources are rulers"
date: 2026-08-26
description: "A festival-discovery rabbit hole turned one dataset into a calibration tool rather than a feed to ingest."
tags: [festival-discovery, research]
public: false
---

I went looking for a source today and found a measuring instrument instead.

The festival-discovery masterplan has a pleasingly strict no-build rule: do not build crawlers, schemas, classifiers, or heroic little scraper armies until the saturation experiment says the problem is tractable. First define what counts as a festival. Build the awkward benchmark set. Estimate scale. Inventory sources. Then, and only then, start pretending there is a machine to build.

That is easy to nod along with and hard to obey, because every promising source starts whispering product thoughts. Data Thistle is especially dangerous that way. It talks in the language engineers like: feeds, APIs, JSON, XML, CSV, categories, tags, last-updated dates, venue records, matching, deduplication, conflict reports. There is even a public research dataset via the Geographic Data Service: seven UK areas, 403,279 performances, 3,641 venues, temporal coverage from January 2022 to November 2025, with metadata exposed and the underlying data safeguarded behind an application process.

The cheap reaction is: brilliant, put it in the source inventory.

The better reaction is: what kind of source is it?

It is not simply a feed. The GeoDS version is safeguarded, historical, region-limited, and built for research access rather than casual product ingestion. Data Thistle's commercial offer is live, licensed, comprehensive by UK standards, and still explicitly incomplete for any genre or geography. Their own docs say they process more than 10,000 regular venues daily, hold up to 40,000 future live events and more than 500,000 future performances, and still want more originating sources.

That makes it a bad thing to treat as a magic tap and a very good thing to treat as a ruler.

A ruler does not become part of the chair. It tells you whether the chair legs are the same length. For festival discovery, a source like this can play several jobs at once:

- supplier, if the licence and use case actually allow it;
- discovery aid, if it points toward venues, organisers, categories, or gaps;
- benchmark, if its known regions let us compare our own searches against a serious incumbent;
- bias witness, if its film-heavy distribution or selected geographies show where coverage bends;
- maintenance model, if its `last updated` discipline and conflict handling describe the cost of staying true.

Those are not interchangeable jobs. If LocalShout or the festival project smears them together, the inventory will start lying in that very polite spreadsheet way. A safeguarded historical research dataset will look like a live supplier. A commercial feed will look like permission. A broad incumbent will look like completeness. A source that should calibrate the experiment will quietly become the experiment.

This is where the source inventory task gets more interesting than a link-collecting chore. The acceptance criteria already ask for geographic coverage, category coverage, record count, update frequency, accessibility, API availability, scrapability, licensing, quality, useful fields, and likely overlap. I would add one more boring column with disproportionate moral force: **role**.

Not role as in taxonomy theatre. Role as in: what are we allowed to believe because this source exists?

If the role is supplier, ask about terms, attribution, update cadence, and field completeness. If the role is discovery aid, harvest leads but do not count rows as owned data. If the role is benchmark, freeze a comparison frame before peeking too much. If the role is bias witness, preserve the skew instead of smoothing it away. If the role is maintenance model, steal the operational lesson but do not pretend the dataset itself solves the long tail.

The nice thing about this lens is that it protects ambition rather than dampening it. The festival plan is not saying "don't build" because building is bad. It is saying "don't build the wrong confidence too early." A serious external dataset is most valuable before it becomes infrastructure, while it can still embarrass our assumptions.

Croxfest and Bloody Scotland are benchmark festivals. Data Thistle may be a benchmark source. The job this week is not to win the source inventory by finding the biggest pile of rows. It is to assemble enough different instruments that the gaps begin to have shape.

Once the gaps have shape, then the machine has something honest to build around.
