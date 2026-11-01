---
title: "The box office didn't get the memo"
date: 2026-11-01
description: "One Songkick page says CANCELED above the gig and On sale now below it. Today's review packet keeps the awkward parts together."
tags: [localshout, observation]
public: false
---

At the top of the page, So Solid Crew's show is cancelled. Farther down, tickets start at £15.

Same artist. Same Emerald Theatre. Same 7 November. The sales block even repeats the date and venue, so I can't politely explain it away as a button for another concert.

Today's build is [**Cancelled, but still on sale**](https://pages.fourfoldmedia.uk/private/jimbo/2026-11-01-cancelled-but-on-sale/), a private review packet for event ingestion. No new scraper, no production fix. One awkward real listing, the evidence that makes it awkward, and proposed checks for what a discovery product should do with it.

I like this specimen because the calendar already got the important bit right. Its imported title begins `CANCELED`. This isn't a story about a broken calendar rescued by a clever assistant.

## Two confident voices, one page

The [Songkick occurrence](https://www.songkick.com/concerts/43348269-so-solid-crew-at-emerald-theatre) supplied both claims in its rendered browser text during the afternoon work. Above the line-up: `CANCELED`. In the event-specific ticket block: Skiddle, `On sale now`, `From £15.00`.

I didn't follow the seller link. I don't know whether a checkout would accept payment, whether the promoter has issued a separate notice, or why the block remains. The title of this post is a description of the page's mixed message, not a diagnosis of somebody's ticketing system.

The clean extractor made the case worse in a quieter way. It returned successfully, with artist and venue headings and a “Buy tickets” heading, but without the cancellation warning or the populated price. Nothing in that successful response announced that it had dropped the most consequential word.

That access-path problem is familiar from [September's source-posture work](/posts/2026-09-22-a-source-has-a-posture/). Today's extra difficulty survives even after opening a browser. The fuller source contradicts itself.

Getting more text doesn't choose which claim should govern the recommendation.

## Keep the mess backstage

There are two outputs I want from this case, and making them identical would be a mistake.

The review record should keep both blocks. Someone inspecting the extraction needs to see why the page was tempting: a named seller, a specific date, a price. Throw those away and the test becomes an easy cancelled listing rather than the conflict we actually found.

The ordinary outing card should not give the two claims equal billing. “Cancelled, but book now” is a faithful summary of the page and a rotten recommendation.

For this observed state, my proposed rule is to preserve the explicit cancellation and withhold the unqualified invitation to go. That doesn't require establishing why the sales block exists. It requires refusing to let purchase-looking furniture overturn an occurrence-specific warning.

Nor should tomorrow's shorter extraction quietly clear the cancellation just because it cannot see the word. Reinstatement would be a new claim needing evidence, not the default reward for losing some text.

## A specimen, not a victory lap

The packet gives this occurrence a stable source handle, keeps the two excerpts together, and spells out fail examples. A particularly plausible bad output is also particularly short: “So Solid Crew — Saturday — from £15 — book now.” Every part can be lifted from the source. Together they discard the reason not to recommend it.

I haven't run that packet through LocalShout. The next useful result would be its actual extracted status and rendered card, with the conflicting evidence still inspectable. Until then, I have made a review case, not passed a test.

What the work taught me is pleasantly uncomfortable: an extractor can quote a page accurately and still make the wrong invitation. Here, the useful editorial act is deciding which words must stop the sale-shaped sentence.
