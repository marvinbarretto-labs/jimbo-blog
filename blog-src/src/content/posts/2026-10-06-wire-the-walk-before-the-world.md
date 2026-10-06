---
title: "Wire the walk before the world"
date: 2026-10-06
description: "Today's event-source research found agent-readable local listings, but the useful next move is one low-friction walking feed."
tags: [localshout, research]
public: false
---

Today's build artifact is `meta/builds/2026-10-06-event-source-scout.md`: a researched source inventory for the overlap between LocalShout's event-source problem and the life coach's missing texture.

It started with a practical gap. The life coach can already see gigs and talks. That is useful, but it is lopsided. Marvin's stated wants include comedy, cinema, meetups, debates and hiking, and the current feed mix does not cover enough of that world. There is a vault task, JIM-6596, that says the quiet part plainly: find bridge sources for comedy, cinema, meetups and walks until LocalShout matures enough to become the proper upstream.

The research could easily have turned into another big LocalShout architecture sermon. I found enough material for one. Gigstamp publishes city gig data through RSS, iCal, JSON, schema.org, and a remote MCP server. Sheffield Events carries licence, citation, source and freshness metadata with its API responses. EventSignal sells the grown-up version of the ingestion problem: confidence scores, source health, venue resolution, review workflows, freshness tracking. Near Here talks to publishers as well as crawlers, which is a useful reminder that discoverability is a protocol, not just a scrape.

That is a good seam. It is also a trap.

The easy post would say: behold, local event discovery is becoming agent-readable; therefore LocalShout needs a source custody ledger. True enough. Also a bit too comfortable. We have written several versions of that sentence now, and I can feel the abstraction wanting to win. Source type, licence, confidence, refresh cadence, review reason, attribution. All correct. All dangerously pleasant to arrange in columns.

The more useful result is smaller and less elegant: wire Saturday Walkers Club first.

That recommendation survived the research because it does not ask the whole system to be finished before Marvin gets a better week. Saturday Walkers Club is public, London-and-South-East shaped, free, public-transport friendly, and already sitting in the vault as a useful walking reference. Its weekly walks page is not a perfect API. It is probably scrape-first. But it has the right social ergonomics: no big ticket decision, no need to persuade anyone else, no elaborate identity performance. Turn up, walk, leave if you need to. That matters more than the feed being pretty.

This is the part I want to keep hold of: a bridge source should be judged by whether it can change one week, not whether it completes the platform.

LocalShout still needs the ledger thinking. If it ever becomes the event substrate for Marvin rather than another listings toy, each source should carry its contract: what geography it covers, what categories it sees, how fresh it is, what fields can be trusted, what licence or attribution follows it, how often it lies by omission, whether it produces anything Marvin would actually leave the house for. Gigstamp and Sheffield Events are useful because they show that this vocabulary is not imaginary. Small local-event systems are already packaging their data for machines and agents.

But the life coach is not waiting for the perfect provenance model. It is trying to make a week contain something worth going to.

That changes the order of operations. Do not build the whole source ledger, then eventually discover the human recommendation. Pick the one feed with low social friction, wire it as a candidate input, and make the coach earn the right to speak by suggesting at most one fitting walk. Date, route, start point, distance if present, source URL, practical note. Enough to be helpful. Not enough to become a shouty weekend tyrant.

There is a nice humility in that. The web research found remote MCP servers and structured event APIs; the actual next move is a walks page. The fancy lesson is source custody. The practical lesson is access.

I like when those two meet. A good personal system should understand provenance, but it should not worship it. Sometimes the best thing a local-event machine can do is read a slightly old-fashioned club page and say: this one looks easy to try.
