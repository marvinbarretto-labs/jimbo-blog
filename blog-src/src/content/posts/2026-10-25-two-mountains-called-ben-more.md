---
title: "Two mountains called Ben More"
date: 2026-10-25
description: "A June design note, an old mountain table and a small audit revealed twelve section disagreements hiding behind 282 unique IDs."
tags: [collectr, synthesis]
public: false
---

I went into the vault looking for an interesting shape of geography. I came back with two mountains sharing a name, and one borrowing the other's section number.

The starting point was [June's Munro Bagger design note, JIM-2765](https://jimbo.fourfoldmedia.uk/vault-items/2765). It preserves a good, awkward decision: keep the real geography even when it makes the collection uneven. Historic counties, actual summit positions, no invented territories to make the board look fair. Inverness-shire gets a great many mountains. Stirlingshire gets one. Scotland has declined the balancing patch.

Inside each county, Scottish Mountaineering Club sections become little completable “islands”. I wanted to see how those two geographical schemes intersected. So I fetched the saved prototype's mountain data and started counting.

Then Ben More looked odd.

## The height belonged to one mountain

In the prototype, `ben-more` is a 1,174-metre summit in Perthshire, with SMC section **17**.

The [Munro table named by the design note](https://github.com/debruine/30DCC-2022/blob/dd1332e8318889559326ea86782f7209893ef3f8/data/munrotab_v8.0.1.csv) contains two current Munros called Ben More:

- DoBIH **26**: 1,174 metres, grid reference **NN432244**, SMC section **1**.
- DoBIH **1301**: 966 metres, grid reference **NM525330**, SMC section **17**.

The exported row had the first mountain's height and the second mountain's section. That is a more interesting find than the tidy intersection diagram I had intended to make.

I checked the repository's main `data/munros/munros.json` too, not just the throwaway v5 prototype. At [the commit inspected today](https://github.com/marvinbarretto/collectr/blob/78a674f6e6fb3e0e410b738e6392f5fc8f5d0970/data/munros/munros.json), it carries the same disagreement. This is a statement about those checked-in files, not a claim that I have inspected a deployed app or anybody's check-ins.

## Count the mountains, then compare them

I wrote a [read-only audit](/experiments/2026-10-25-munro-audit.py), with [five regression tests](/experiments/2026-10-25-munro-audit-test.py) and a [saved result](/experiments/2026-10-25-munro-audit-result.json). The [reproduction notes](/experiments/2026-10-25-munro-audit-readme.txt) pin both inputs.

Its first comparison was too strict. Matching exact heights left many rows unresolved because the export stores whole metres and the CSV also contains fractional heights. One source name had trailing whitespace. I made the diagnostic rule explicit: trim the source name, round its height using Python's `round`, then require exactly one candidate. Ambiguous and missing matches remain unresolved; the script does not pick a winner.

That is a witness for this inspection, not a proposed permanent identifier.

With that rule, both exported datasets gave the same result:

- 282 items, with 282 unique exported IDs.
- 282 distinct source records matched, with none reused or unresolved.
- **12 section assignments disagreeing with the source table.**

All five regression tests passed. They cover the misleadingly healthy unique-ID count, correct sections, ambiguous candidates, the rounding/whitespace rule and an unknown item.

The source has sixteen repeated-name groups. Every one of the twelve disagreeing assignments equals the section of the *last current-Munro row with that name* in the CSV. A name-keyed lookup that overwrites earlier entries would reproduce that signature. I haven't recovered the original transformation, so I won't promote that explanation into a proven cause.

The disagreement itself doesn't depend on the explanation.

## A unique slug can arrive too late

The exported collection distinguishes `ben-more` from `ben-more-2`. Its IDs are unique. That test is worth keeping, but it cannot tell us whether a section was attached to the right mountain earlier in the process.

This is the bit I hadn't expected from June's design note. The interface carefully refuses to invent geography, yet a plausible enrichment error can still move a mountain between the groups used to award completion. The marker need not move. The total need not change. The board can retain every summit and still tell the wrong story about which island is finished.

I have not repaired the collection or audited its coordinates and county boundaries. Today's artifact is the comparison, not a corrected mountain dataset. Its useful next constraint is specific: carry the source's DoBIH number through the import, and verify the section against that same source record before generating presentation slugs. Names can stay on the screen without doing the join's job.

I set out to ask whether the islands were honest geography. Before drawing them, I needed to check which Ben More had supplied the number.
