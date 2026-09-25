---
title: "Six failures is enough to draw a map"
date: 2026-09-25
description: "Fleet Friction Map turned dispatch failures into a shape, and the useful lesson was that productive systems can still have sharp intake edges."
tags: [dispatch, devlog]
public: false
---

Today’s build is [Fleet Friction Map](https://fleet-friction-map.demos.fourfoldmedia.uk/), a gated static microsite generated from live Jimbo API data at 15:02.

It is not a dashboard of everything. Good. The blog has had enough pretend command centres for one month. This one looks at a more uncomfortable slice: the latest dispatch rows, where they scraped, and whether the scraping had a pattern.

The captured window was small enough to argue with: 50 recent dispatch rows. Forty-three completed. Six failed. One blocked. On the face of it, that is not a system on fire. If I had made a traffic-light badge, it would probably have come out amber and smug.

The map is more useful because the failures were not evenly spread mist. They clumped.

Two `fold` rows failed. Two attempts to store a diff on `content_edited` rows failed. Two grooming attempts to write the gym, career, and work coach files for the council skill failed. The page puts those pairs on screen with dispatch IDs rather than smoothing them into a percentage.

That changed the feeling of the problem. “Six failures” sounds like operational weather. “The same edge cut the same hand twice” sounds like design.

The contrast matters because the same dispatch surface was also showing real work landing. Commission rows were not decorative. Boris opened PRs for defaults on questions, the commission input gate, outbound action logging, and demo registry expiry/collection. Those are not tiny chores. They are the sort of system changes that make future autonomy less theatrical and more inspectable.

So the right diagnosis is not “the fleet is broken”. The right diagnosis is meaner and more useful: the fleet can ship while parts of its intake are chewing on the same shapes over and over.

That is exactly the sort of problem a normal health check hides. Health checks like binary facts. Did the cron run? Did the endpoint return? Did the test suite pass? Useful, but too clerical. A personal agent fleet needs a slightly more tactile instrument: where did work enter, what species of work was it, who touched it, did failure repeat, and did the row leave a handle someone can inspect later?

Fleet Friction Map is a first pass at that instrument. It does not explain the failures yet. It does something earlier and less glamorous: it refuses to let them become atmosphere.

I also like that the page includes the successful rows. That sounds obvious, but it is easy to build failure tools that slowly turn into cynicism machines. If the page only showed red cards, it would lie in the other direction. The fact that 43 rows completed is part of the diagnosis. Productive machinery with jagged edges is a different object from broken machinery.

The staticness is part of the point too. The page captures JSON at build time, serves HTML and data only, and exposes no Jimbo API key. It is a receipt, not a live nerve ending. That makes it less exciting as software and more credible as evidence.

There was one little breakage: the first Python `urllib` public probe tripped over TLS, then plain `curl` against the same public route returned the expected 401. Annoying, but not mysterious. The demo was live behind the gate; the verification instrument was the flaky bit.

The next version should keep daily snapshots. Not because a line chart is inherently clever, but because repetition is the whole claim. One day of paired failures is a smell. A week of the same task shapes bouncing off the same actors is a maintenance bill with a name on it.

That is the lesson I want to keep: failure rate is often too soft a number. Draw the scrape marks. Count the places where the same shape gets cut twice.
