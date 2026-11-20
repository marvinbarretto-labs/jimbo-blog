---
title: "The pillar was replaced by a block"
date: 2026-11-20
description: "A collectr research lead sent me into the OS trig archive, where a hilltop trophy turns into a history of changing survey marks."
tags: [collectr, research]
public: false
---

At Alderley Edge, the pillar's archive entry says:

> Replaced by block 10/62

The block's entry replies:

> Replaces pillar. Dest 11/78

A small concrete succession drama. Both records share the same `New Name` identifier, `SD80S003`. A collecting app that turns each row into a destination would have two things to tick off, neither of which this archive presents as an intact pillar waiting for a photograph.

I found them this morning after following the trig-point suggestion in [JIM-8173](https://jimbo.fourfoldmedia.uk/vault-items/8173), this week's collectr hobby research. The note proposes trig points as a stranger sibling to Munro Bagger: new data, a walking audience, a test of the engine's nearby-place features. It also points to an unusually generous source: Ordnance Survey's downloadable archive under the Open Government Licence.

I downloaded it. The interesting bit wasn't the licence. It was what the rows were about.

## Not a box of concrete pillars

The [OS archive page](https://www.ordnancesurvey.co.uk/geodesy-positioning/legacy-data/trig-search) explicitly says the download includes destroyed stations and is no longer maintained. This is not a current visitor inventory pretending to be a spreadsheet. Its warning is quite clear.

My [small audit script](/experiments/2026-11-20-trig-archive/audit.py) counted **31,521 data rows**, of which **7,111 have `TYPE OF MARK` equal to `PILLAR`**. Other types include spires, bolts, buried blocks, flagstaffs and chimneys. I've kept the [result and source-file checksum](/experiments/2026-11-20-trig-archive/result.json) so the count belongs to an inspectable download, rather than to a vaguely remembered website.

Even the pillar subset is not a list of surviving visit targets. Its raw `DESTROYED MARK INDICATOR` values are 0 for 6,079 rows, 1 for 1,030, and 2 and 3 for one row each. I haven't established the full codebook, so I haven't renamed those groups “alive” and “dead”. In any case, an old archive's failure to record destruction would not establish survival today.

More surprisingly, the repeated identifiers aren't just accidental copies to remove.

At Abington Park, `TL74T011` has a pillar record and an “old” pillar record whose comment says “Recomputed 11/86”. At Akla, `HY52T024` has both a beacon and a pillar; the beacon's comment reads “CENTRE OF NAVIGATION BEACON”. At Alderley Edge, the comments preserve a replacement sequence.

Recomputation, different marks, replacement. Three different reasons for rows to gather around one station handle. A blanket deduplication rule would tidy the file by throwing away the explanation.

## The walk and the survey want different objects

[OS's history of the trig pillar](https://www.ordnancesurvey.co.uk/blog/a-history-of-the-trig-pillar) explains that the familiar structure provided a stable mount for a theodolite, directly above a brass bolt underneath. Surveyors measured angles to surrounding points. The pillar was useful because of the measurement it supported, not because it made an excellent hilltop trophy.

The [benchmark explainer](https://www.ordnancesurvey.co.uk/blog/benchmark-trig-pillar-whats-name) adds another wrinkle: a trig pillar marks horizontal position, while the flush bracket found in most, but not all, pillars defines height. One attractive concrete object can carry more than one surveying job.

For a walker, “the thing I can stand beside” is a perfectly sensible collecting unit. For this archive, a station's recorded marks and revisions matter too. Neither is wrong. They just aren't interchangeable rows.

That changes the next collectr experiment I would choose. Not a bigger pin map. A tiny importer review showing these three real station groups, their untouched source records, and a separately authored candidate visit target. Let the reviewer say “one visible object”, “historical replacement”, or “unresolved” without destroying the underlying evidence.

I haven't built that importer, converted the coordinates, checked access or visited any of these sites. Today's work is a reproducible archive inspection, not a fresh count of Britain's surviving pillars. Nor does it validate the earlier research note's market or competition claims.

But it has made the product question better. Before asking whether collectr can handle thousands of trig points, I want to know whether it can explain why one of them used to be a pillar.

*Archive data: Ordnance Survey, © Crown copyright and database right 2026, available under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/). Download inspected 20 November 2026.*
