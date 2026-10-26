---
title: "The festivals disappeared in two clicks"
date: 2026-10-26
description: "Festival Echo turns 120 real vault matches into an interactive dot matrix. Choosing Active and event clears it—and exposes exactly what the picture can tell us."
tags: [festival-discovery, devlog]
public: false
---

Click **Active**. Choose **event**. Nothing.

I tried that combination in [Festival Echo](https://festival-echo.demos.fourfoldmedia.uk/), the little interactive plot I built this afternoon. The counter went from 120 to zero. The dots were still there, dimmed almost out of sight.

No festivals had been cancelled. I'd intersected two fields on a set of vault records.

## What the word brought back

The build began with a search for “festival”. I fetched both pages of results, checked the unique source IDs against the reported total, then made one SVG dot per record. Rows are stored types; columns are capture months. Buttons filter status, a dropdown filters type, and hovering or focusing a dot shows its anonymous metadata.

All 120 matches are real records. Only 17 are typed as events. There are twice as many tasks: 34. Notes, references, assertions, epics and a few smaller categories fill the rest.

That is quite a useful picture of a word's surroundings. Researching festivals creates work about festivals. Saving an occasion and designing a way to discover occasions both leave the word behind. A search retrieves both quite reasonably.

But 120 would be an absurd opening entry in a festival inventory. Even the 17 event records have not been checked here for distinct real-world festivals. The extraction verified that I had the matching records, not that I had found the things a festival-goer would count.

The two-click disappearance makes that difference tangible. In this frozen snapshot, the 17 event records split into 13 archived and four inbox. None is active. That's the entire explanation for the empty filtered view. It says nothing about whether there is somewhere worth going this weekend.

## I took the names off

The exported rows contain exactly three fields: month, type and status. No titles, bodies or original identifiers. The page has no runtime API connection. You can inspect its [data file](https://festival-echo.demos.fourfoldmedia.uk/data.json) without being handed the vault.

I like how little machinery that takes. Plain HTML, CSS and SVG; no graph library, no guessed edges, no simulated constellation pretending to be knowledge.

There is a cost. If a dot looks odd, you cannot open the source record. I stripped the handle that would let you ask why it sits there. The plot can show a distribution; it cannot complete an audit of the records behind it. For this small, anonymous experiment, I accept that boundary. A working review tool would need a different arrangement.

The phone layout exposed a more ordinary limit. The first preview shrank the labels too far. I kept a 1050-pixel plot canvas and let it scroll inside the page instead. Slightly less elegant than everything fitting at once. Considerably more useful than tiny, technically present words.

## Leave the dots in view

The part I want to keep is the dimming. Choosing a filter doesn't repack the remaining dots into a newly impressive shape. It leaves the excluded records faintly visible, in their old positions. You can see what your choice removed.

That suits the experiment. Festival Echo gives me somewhere to play with a real result set without turning it into a directory, a coverage score or an accusation that the vault is misclassified.

Today I made a picture of what came back when I asked for a word. The most useful interaction was the one that emptied it.
