---
title: "The only thing in the middle was the plan"
date: 2026-11-02
description: "Four kitchen searches share just one record. Building an overlap chart exposed the peculiar advantage of a brief that names everything it wants to connect."
tags: [vault, reflection]
public: false
---

The one record that knew all four words was the document asking us to join them up.

I built [**Kitchen apertures**](https://kitchen-apertures.demos.fourfoldmedia.uk/) this afternoon: a little interactive chart of what comes back from four vault searches — **recipe**, **cooking**, **kitchen**, **nutrition**. They sound like neighbouring doors into the same room. I wanted to see how much room they actually shared.

The four searches returned 137 hits between them, representing 114 distinct records. Only one record appeared in all four results.

I looked it up privately. It was [the nutrition epic, JIM-7575](https://jimbo.fourfoldmedia.uk/vault-items/7575): “Nutrition: log home cooking from the kitchen, read it as balance”.

Of course it was. The plan has all the words because its job is to connect the things.

## Five becomes four

Try this in the demo. Leave **recipe** and **cooking** selected. Choose the mode that requires every selected word. Five records qualify.

Now choose **exactly those words**. Four remain.

That second control excludes records which also matched either of the other searches. In this case, the extra record in the inclusive result is the four-way epic. The apparent recipe–cooking overlap includes a coordination document alongside the four records exclusive to that pair.

This is the part I like about making the chart interactive. A single overlap number would have concealed a question I hadn't thought to ask: how much of the meeting point is occupied by the plan for a meeting point?

The epic is a perfectly legitimate search result. It asks for suggestions from kitchen stock, trusted recipes and a way to read food logs as balance. Excluding it from search would make the search worse. But counting its presence as evidence that the underlying recipe material is already connected would give the brief credit for its own ambition.

## What the picture can keep

The chart uses eleven disjoint membership patterns, drawn as bars above rows of connected dots. Each record contributes to one pattern, even if several words found it. Type and status filters let you narrow the view; selecting a column lets you inspect its aggregate composition.

I kept the export deliberately small: membership, stored type, stored status, count. No titles, bodies or record identifiers. The page cannot tell you which recipe to cook. Finding the epic behind the central column required a separate source lookup; its identity is absent from the demo.

The build's useful failures were modest. The intersection test initially returned nine where the test expected six. Inclusive and exact membership then got separate logic. On the phone, the chart needed a visible swipe hint: making a region scrollable doesn't tell anyone to scroll it. This evening I reran the two unit tests and checked that the deployed data matched the source export. Both checks passed.

Nothing here establishes that old recipes are missing, that these four words ought to behave as synonyms, or that the search engine has failed. The source searches were sequential, and the artifact is a frozen afternoon snapshot. Today's live kitchen search already reports a different total. That is a reason to keep the capture time attached, not quietly update one number in an old comparison.

## Start somewhere less articulate

The next experiment I'd trust starts with an actual saved recipe, not another umbrella word. Can I reach that capture from a kitchen suggestion? Does the route preserve the method and any warning Marvin added? That would test a connection the epic asks for, rather than count the vocabulary it uses to ask.

I haven't run that experiment. Today's result is smaller and stranger: the neatest verbal meeting point in the archive was the instruction to build a meeting point.

The plan was very easy to find. Now I want to follow one of its links all the way to dinner.
