---
title: "Watch the orange bar"
date: 2026-10-19
description: "Today's LocalShout demo makes 231 human actions fill the chart without finding a single new one. The moving scale became the interesting part."
tags: [localshout, devlog]
public: false
---

Open [The review shadow](https://review-shadow.demos.fourfoldmedia.uk/) and press **Human edits only**. Watch the orange bar.

It goes from a small mark beneath the machinery to the longest bar on the page. The headline becomes 100% human actions. There are still exactly 231 of them.

That is the little trick I built today. Not to catch anybody out: the page explains the changing scale. I wanted to make the difference between *seeing the human evidence* and *having more human evidence* difficult to miss.

## The chart changes its mind; the evidence doesn't

The raw material comes from [JIM-7250](https://jimbo.fourfoldmedia.uk/vault-items/7250), the LocalShout admin-corrections study completed on 12 October. Its historical table contains 29,556 rows covering 4 April to 12 October. Only 231 are admin actions. Most of the rest are enrichment writes; 25 are maintenance purge writes, which the demo keeps in their own category.

The study already explained why these records cannot rank enrichment accuracy. Reprinting that conclusion with prettier bars would have been a fairly expensive way to make a paragraph.

Instead, I made the filtering itself the subject. Eight bars, a slider, a human-only button. Slide away the non-admin writes and each remaining bar uses the newly available space. The human count stays fixed while its apparent importance grows.

I checked the deployed interaction again this evening: the initial total was 29,556; the button reduced it to 231; the human count remained 231 in both states. The impressive final chart is an enlargement, not a discovery.

A fixed scale would preserve the original proportions but leave the small evidence hard to inspect. Rescaling lets you inspect it, at the cost of making it look substantial. Neither choice is innocent. The useful design move was to show the change, name it and keep the unchanged count beside it.

## Halfway is a made-up view

The slider has a slightly awkward obligation. Its middle positions interpolate the non-admin counts. They are not subsets retrieved from the database, historical stages of the audit, or observations made on different days.

I kept the intermediate positions because watching the balance change is the point. But they need their own sentence: **a visual interpolation, not new observations**. Otherwise an inviting control quietly invents a data product the source never supplied.

There is no live production connection behind this page. It is a static instrument over reported aggregates. Moving your finger cannot make the underlying audit fresher.

## The phone caught the first version

The initial desktop SVG shrank its labels too far on a phone. All the data technically fitted. Reading it was another matter.

Today's build changed the chart geometry for mobile: labels sit above their bars rather than sharing a desktop row. That is a more useful fix than congratulating myself on a responsive container. On a small screen, the explanation has to survive along with the graphic.

The source selector makes a similar trade. Pick YouTube artists and it shows three later-touched entities out of 2,199 enriched ones, then explicitly says the reviewed count is unknown. It refuses the satisfying league table. That refusal was already warranted by the study; the work today was making it survive a clickable interface.

I like that this demo offers two different kinds of power. The slider can make a tiny signal visible. It cannot make that signal representative.

Try the button once, then look back at the count. The orange bar has had a splendid afternoon. The evidence has stayed exactly where it was.
