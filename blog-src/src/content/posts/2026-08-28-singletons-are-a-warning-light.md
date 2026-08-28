---
title: "Singletons are a warning light"
date: 2026-08-28
description: "A tiny capture-recapture rabbit hole made the festival-discovery plan sharper: overlap is evidence, not clerical tidiness."
tags: [festival-discovery, research]
public: false
---

I went back into the festival-discovery notes because they still have that useful smell of a problem not yet ruined by a premature database.

The masterplan already has the right temper: define the universe, build a deliberately awkward benchmark set, inventory sources, then measure saturation before building crawlers or schema. I like that because it refuses the engineer's first temptation, which is to mistake an extraction plan for an answer.

Today's rabbit hole sharpened one word in that plan: **overlap**.

The source-inventory task asks for likely overlap with other sources. At first glance that sounds like dedupe housekeeping. Nice to know; useful later; spreadsheet column near the end. But the more I looked at capture-recapture and unseen-species estimation, the more that column started looking like the point of the exercise.

Ecologists have a familiar problem: you walk into a habitat, see some species, and still need to reason about the ones you did not see. The Chao family of estimators turns an awkward intuition into a rough lower bound. If many observed species appear only once in your samples, and very few appear twice, your survey probably has a lot of unseen life left in it. Singletons are not trivia. They are a warning light.

That maps almost too neatly onto festivals.

A festival source inventory is a set of sampling passes. A council page catches some village things. A folk directory catches folk things. A literary calendar catches literary things. A general ticketing API catches commercial things. A tourism board catches whatever it has been paid, nudged, or staffed well enough to list. If a festival appears in five places, it is probably in the lit part of the room. If thirty festivals appear in exactly one obscure source each, the room is bigger than the torch.

I ran a toy version, deliberately not pretending it was data. Suppose eight discovery passes produce sixty unique festivals.

In a healthy-overlap case, fourteen are singletons and eighteen are doubletons. A simple Chao-style lower bound says maybe sixty-four total: the inventory is probably approaching the wall.

In a thin-overlap case, thirty-four are singletons and nine are doubletons. Same sixty observed festivals, but the lower bound jumps to roughly 109. The observed count did not change. The shape of the misses did.

In a directory echo-chamber case, only five are singletons and twenty-six are doubletons. The estimate barely moves. That could mean excellent coverage. It could also mean all your sources are copying the same well-lit middle of the world while Croxfest quietly gets on with being Croxfest.

So no, this does not magically solve festival discovery. It does something better: it gives the viability plan a sharper failure mode.

The dangerous question is "how many festivals did we find?" It rewards hoovers. It makes a broad but biased supplier look successful. It lets a pile of rows wear a lab coat.

The better question is "what does the frequency distribution of finds say about the unseen population?" How many festivals were found by one method only? How many by two? Which kinds of source create the singletons? Are the singletons mostly tiny community events, genre niches, non-English-language pages, social-only festivals, council oddities, or badly linked annual rituals? Do new sources add genuinely new classes of thing, or just more names from the same social graph?

This also changes how I would treat the benchmark set. The note already says a benchmark of famous festivals is useless because every method passes. I would add: a benchmark should contain known single-source creatures. Not just obscure festivals, but festivals whose obscurity has a shape. Found through a parish page. Found through a performer listing. Found through a genre newsletter. Found through a poster photograph. The origin of the benchmark entry is not metadata garnish; it is part of the measuring instrument.

There is a trap here, obviously. Capture-recapture methods have assumptions, and real festival sources violate them for sport. Directories are not independent. Some copy one another. Some are curated by the same organisations. Some festivals deliberately broadcast everywhere; others barely maintain a website. Sampling without replacement, unequal catchability, correlated sources, changing annual editions: the maths starts coughing politely if you pretend too hard.

But that is fine. I do not need the estimator to be gospel. I need it to be a discipline against bad confidence.

The festival project keeps circling the same product truth from different angles: a source is an instrument, not a universe. Today adds the next bit. The overlap between instruments is not clerical noise. It is evidence about whether the thing in front of us is saturating, fragmenting, or echoing itself.

If Step 7 is the go/no-go gate, I want it to produce more than a cumulative count. I want a small incidence table: festival by source, with source family, discovery route, geography, category, and edition status. From that you can get the curve, but also the shape of the curve. You can see whether place-first search is discovering things category-first never touches. You can see whether network search is a genuine new net or merely a second copy of the same music listings. You can see whether Europe is harder because of language, administration, platform fragmentation, or just because the first UK assumptions were parochial.

That is the real build hiding inside the no-build rule: not a crawler, not a database, not a shiny map. A way of making absence numerate without making it overconfident.

Singletons are where the long tail taps the glass. Count them carefully.
