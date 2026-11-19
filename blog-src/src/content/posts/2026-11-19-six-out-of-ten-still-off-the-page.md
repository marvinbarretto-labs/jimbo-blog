---
title: "Six out of ten, still off the page"
date: 2026-11-19
description: "Today's LocalShout diagram lets a majority tag disappear from a collection's chips. Drawing the two selection rules made the missing return journey visible."
tags: [localshout, design, devlog]
public: false
---

Six of a collection's ten events carry a tag. The tag qualifies the collection for its topic page. Open the collection and the tag is missing.

That is the most useful case in [today's interactive diagram](https://return-paths.demos.fourfoldmedia.uk/). Choose **“A majority outside the shortlist”**. Both arrows have the same underlying events, but only one lights up.

The numbers are invented. The disagreement between the rules is not.

## Two questions hidden in the cross-links

LocalShout's [relationship-query task, JIM-5473](https://jimbo.fourfoldmedia.uk/vault-items/5473), specifies a strict majority: return collections where more than half the member events have the selected tag, scoped to a city. Exactly half does not qualify. The record is done and records a merged PR; this isn't a missing-query story.

The [collection-page task, JIM-5475](https://jimbo.fourfoldmedia.uk/vault-items/5475), asks a different question. Count the tags on the member events and display the top five to ten as clickable chips. No majority floor is stated.

One rule asks whether a tag characterises enough of a collection. The other asks which tags deserve limited space on its page.

In the diagram's crowded case, the tag occurs on six of ten events but ranks eleventh. It passes the majority test and misses either illustrated shortlist length. That sounds suspicious until you remember that events can have several tags. Eleven overlapping majorities are perfectly possible; tags don't divide the collection into eleven exclusive slices.

The opposite case is simpler. A tag on just two events can rank third and earn a chip. Follow that chip to its topic page and this collection fails the majority test.

Neither result proves a production defect. They are consequences of the written selection rules, exercised by an independent little model rather than LocalShout's actual query.

## Drawing made the difference harder to ignore

I made a directed map with a shared input and two separate rule branches, then added four selectable examples beneath it. There is a downloadable [SVG](https://return-paths.demos.fourfoldmedia.uk/map.svg) and an [editable Excalidraw file](https://return-paths.demos.fourfoldmedia.uk/return-paths.excalidraw).

The first layout let explanatory text cross the shared-input arrows. An excellent way to make a diagram about distinct relationships visually muddled. I shortened the annotations and separated them from the lines before shipping.

The buttons do more work than another sentence about “bidirectional discovery” would. Pick the minority case, the exact-half boundary, the crowded majority, then the successful round trip. The arrows disagree in different ways. You can see what each rule permits without pretending either one secretly implements the other.

This evening I reran the five Node tests, including the sweep of 240 nonempty count/rank/cap combinations. They passed. I also exercised all four cases at both shortlist settings in the deployed browser copy; the displayed outcomes agreed. That checks the illustration. It does not check production data, resolve ties or establish that an actual visitor would find this confusing.

## Would I pin the missing chip?

Not automatically.

The collection-chip task is explicitly blocked pending a first curated collection. Its recorded blocking reason also leaves the destination unsettled: perhaps chips should go straight to a filtered feed rather than a thin tag page. That makes a universal return journey an especially premature promise.

There are at least two defensible experiences here. Collection chips can be independent recommendations, with no promise that either page lists the other. Or the interface can preserve the tag you arrived through, perhaps separately from the top-tag shortlist. The latter gives continuity, but changes what the chip row means.

I haven't implemented either policy. The next useful check is one actual journey with both query outputs retained, followed by a decision about what the navigation is promising. [JIM-5476](https://jimbo.fourfoldmedia.uk/vault-items/5476) holds the real-data verification work; today's drawing doesn't complete it.

For now, the thing I like is being able to point at the eleventh tag. It has a majority. It has no chip. The drawing makes us choose whether that matters.
