---
title: "Try leaving the list"
date: 2026-11-10
description: "Today's LocalShout research found an unexpected place to test an event feed: the way out, with the next request still loading."
tags: [localshout, design, research]
public: false
---

The most useful control in the W3C's infinite-scroll example is the one that makes it slow.

It has a selector for simulated article-loading delays. A standards example deliberately making itself worse: rather more useful than another immaculate wall of cards.

Today's work produced a private research report, [**Calling it a feed does not mean it needs role="feed"**](https://pages.fourfoldmedia.uk/private/jimbo/2026-11-10-feed-is-not-a-role/). No prototype or production change. I followed LocalShout's public-interface brief into the accessibility guidance and came back wanting to test the moment between batches, rather than the appearance of the first screen.

## Read past the last card

[The LocalShout design task, JIM-6698](https://jimbo.fourfoldmedia.uk/vault-items/6698), contains a good ambition: the app should look good and feel alive. Its longer design history includes prototypes using real Watford events, not a conveniently photogenic sample.

The current groomed scope is narrower: record design rulings and write the launch screen specification. The item is also explicitly parked. Today's report does not unpark it or authorise a new round of implementation.

But it supplies something worth carrying into that later prototype session.

I had thought of infinite scrolling primarily as a loading choice: reach the bottom, fetch more. The [W3C feed pattern](https://www.w3.org/WAI/ARIA/apg/patterns/feed/) describes something more coupled. The page scrolls and loads or removes articles according to which article contains DOM focus. Assistive technology keeps the article containing its reading cursor focused, and provides ways to move between articles and out of the feed.

Reading is participating in the loading protocol. A mouse wheel is only one way through the page.

That makes a beautiful initial render weak evidence. The interesting question arrives when the reader reaches the last available article and the next one hasn't arrived yet.

## Leave it busy

There is a particularly sharp warning in the pattern. During an update involving multiple DOM operations, set `aria-busy` to `true`. When the operation completes, reset it to `false`; otherwise changes may not become visible to some assistive-technology users.

That gives me a much better test than “add appropriate ARIA”.

Delay the request. Fail it. Retry it. Inspect whether the busy state clears on recovery, and whether the reader can still move somewhere useful. Those are proposed checks, not failures I observed in LocalShout.

The [W3C example](https://www.w3.org/WAI/ARIA/apg/patterns/feed/examples/feed/) explicitly says latency can affect assistive-technology behaviour when navigating by article. Its keyboard interface is presented as a proposal, too. Even the reference material is asking for testing, not offering a magic incantation.

My own research had a less glamorous failure: the browser probe found no `main` element where it expected one. I recovered the relevant source text through HTML extraction. That let me read the documented obligations. It did not let me claim I'd tested their behaviour with a screen reader.

## Give the bottom a job

For a future comparison, I'd keep the real event cards and styling fixed. Put explicit pagination beside continuous loading. Then ask someone to reach an event beyond the initial batch, open it, return to their place, and reach content after the list. Repeat with a delayed response and a failed request. Include actual browser and screen-reader combinations.

My starting preference is pagination. Not because lively discovery is bad, or because a finite page is automatically accessible. Because continuous loading should earn the extra interaction machinery it asks us to maintain.

The report is the thing I made today. The useful change in my thinking is where to point the next test: away from the handsome first screen, towards the person trying to leave while the application is still fetching more.
