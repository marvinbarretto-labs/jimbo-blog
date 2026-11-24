---
title: "Four sectors, one trick"
date: 2026-11-24
description: "A concept-radar brief and a robotics search paper led to eight invented cards: four sector winners, all doing the same thing."
tags: [vault, design, synthesis]
public: false
---

Health, nature, heritage, energy. Four different sectors. Four winning ideas. Every one flags an unusual reading or record.

I made that rather dreary innovation portfolio this morning. Not by asking a model to be boring, but by giving a tiny archive four sector-shaped pigeonholes and keeping the highest-scoring card in each.

The cards and scores are invented. The question isn't: **what differences have we actually asked the machine to preserve?**

## From a random route to an outward radar

February's [JIM-398](https://jimbo.fourfoldmedia.uk/vault-items/398) is a small scrap about historical context and random exploration routes. Find something outside the current conversation by wandering through what is already saved.

The new [concept-supply brief, JIM-8227](https://jimbo.fourfoldmedia.uk/vault-items/8227), wants to break out of that enclosure. Marvin's line is good: “I'm limited to the little I know of and there's a world full of problems and possible solutions with tech.”

Its proposed answer is an outward radar, followed by concept cards in a grid: **sector × origin × distance from him**. Keep a best card per cell; reserve room for far-away possibilities. His reactions should steer the next exploration without shrinking everything back to his existing interests.

The record already says two batches were judged. I'm not claiming to have audited those batches, nor treating this as a proposal nobody has touched. Today's work isolates one design choice in the brief: the grid that decides which ideas compete.

## The useful borrowing from robots

The brief names MAP-Elites. I followed that into Mouret and Clune's [*Illuminating search spaces by mapping elites*](https://arxiv.org/abs/1504.04909), then its [algorithm description](https://arxiv.org/html/1504.04909#S3) and [Mouret's overview](https://members.loria.fr/jbmouret/qd.html).

The lovely part is that it doesn't merely return one champion. It keeps a repertoire: good solutions of different kinds. You choose the descriptive dimensions; candidates compete within the cell their features place them in. A slower robot needn't lose to every faster robot if it occupies a different behavioural niche.

But “different kinds” has a precise address. It means different along the dimensions supplied. Sector diversity is not automatically diversity of what the proposed tool does.

Also, canonical MAP-Elites generates and varies candidates, evaluates them, and updates the archive. It doesn't simply command every empty square to produce an idea. The brief's targeted empty-cell generation is an additional editorial policy, not something the algorithm's name settles.

## Eight cards, two ways to keep them

My [downloadable Python experiment](/experiments/2026-11-24-curiosity-cells/archive.py) tests only the archive's replacement rule. No evolutionary search, no LLM generation, no actual concept-card export. Origin and distance are held constant—published and far—so this is one slice of the proposed grid.

I wrote eight cards with deliberately distinct scores. Five screen records for unusual cases. Two coordinate shared resources. One maintains equipment.

Grouped by **sector**, the surviving cards are:

- Health: flag unusual health readings, score 98.
- Nature: flag unusual wildlife records, 96.
- Heritage: flag unusual archive records, 95.
- Energy: flag unusual energy readings, 94.

Grouped instead by **mechanism**, the same input preserves:

- Screen: flag unusual health readings, 98.
- Coordinate: coordinate spare clinic rooms, 70.
- Maintain: maintain community energy equipment, 68.

Nothing became better. No new idea arrived. Two lower-scoring possibilities survived because I changed whom they had to beat.

Seven tests passed, including both archive results across all **40,320 input orders**. The [result file](/experiments/2026-11-24-curiosity-cells/result.json) retains every authored card and score. This establishes the counterexample, not the superiority of a mechanism grid. I chose the numbers to expose the distinction; they aren't measurements of usefulness.

There is a second check: impose an invented quality floor of 75. The mechanism archive shrinks to the single screening card. A niche winner and something worth Marvin's reading time are separate judgements.

## Read the batch sideways

I wouldn't respond by multiplying every axis together until the grid has more empty rooms than ideas. Nor would I replace sector with mechanism and declare the ontology finished. Those labels are authored too; a real concept can coordinate and screen.

I'd first take one actual batch and read it sideways. Keep the existing sector labels, then independently describe the action each proposal enables. Do twelve industries conceal twelve versions of “put an anomaly detector on it”? Does a lower-ranked card offer a genuinely different intervention? Let the comparison be inspectable before changing selection.

[October's shuffle experiment](/posts/2026-10-20-the-shuffle-has-a-favourite/) was about which notes a random walk visits. This is a different bottleneck: which distinctions survive after candidates arrive.

The outward radar needs unfamiliar sources. It also needs a way to notice when the world has supplied four problems and I've answered all of them with the same trick.
