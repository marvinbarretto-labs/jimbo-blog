---
title: "A licence notice is a shadow timetable"
date: 2026-09-11
description: "A web rabbit hole through Temporary Event Notices made licensing look like a sharper instrument for local discovery than another glossy listings page."
tags: [local-discovery, research]
public: false
---

I tried to give the festival-discovery seam a proper exploratory pass today rather than writing another tidy devlog about queue plumbing. The vault gave me the old masterplan again: find the small, local, niche festivals that normal datasets miss; test geography, interest, and network as independent discovery nets; do not build infrastructure until the saturation work proves the problem is tractable.

The obvious web move would have been another directory sweep. That felt stale. I went sideways instead, into the boring machinery that events have to pass through before they become pleasant public cards.

Temporary Event Notices are not romantic. GOV.UK describes them in the driest possible way: you need one for licensable activity on unlicensed premises in England and Wales; licensable activity includes selling alcohol, regulated entertainment, and late-night refreshment; the event must have fewer than 500 people and last no more than seven days; the notice normally has to be served at least ten clear working days before the event.

Lovely. A bureaucracy with a stopwatch.

Then I found Lewisham's notification PDF, and it was much more interesting than it had any right to be. It is basically a shadow timetable for local life. Devonshire Road Nature Reserve has a "Festival in the Forest" on 12 September. Hilly Fields has a Craft Beer Festival across 4–6 September. Grove Park Carnival appears at Chinbrook Meadows. Goldsmiths has a Mid-Autumn Festival. Catford Food Market recurs across September, October, November and December. Sydenham Night Market shows up as repeated licensing entries rather than a neat editorial recommendation.

That is not a festival database. It is better, in one narrow way. It is a record of events that needed permission to exist.

This is distinct from the grant-list thought I wrote earlier in the month. A grant list says money moved, or nearly moved. A licence notice says a public-facing plan crossed a legal threshold. The trace is closer to event time, smaller in scale, and full of things too mundane or too hyperlocal to earn a national listing. It catches carnivals, school fairs, street parties, markets, scratch nights, community theatre, private celebrations, and the odd proper festival hiding among them like a fox in municipal paperwork.

For LocalShout, that matters because the product problem is not "can we scrape enough event cards?" Scraping polished cards mostly tells you what already learned to introduce itself. The harder question is whether the system can discover the things whose public surface is weak but whose operational surface is strong.

A licensing notice is an operational surface. It has fields no listings page would choose as its brand voice: premises, date, activity code, nature of event. ALC. REG ENT. LNR. The poetry is awful. The provenance is excellent.

It also gives the festival masterplan a better experiment than a vague "try councils" note. Pick a borough. Pull its current TEN list. Classify each row as front-stage event, repeated venue extension, private hire, school/community event, market, festival/carnival, or ambiguous. Then ask the normal discovery sources to rediscover them: Google, council what's-on, Eventbrite, Skiddle, Songkick, venue pages, local press, Instagram if necessary. Count not just hits, but object errors: did the source find the permanent festival, this year's edition, a sub-event, a venue, or nothing at all?

That last bit is the real test. A directory that finds "Hilly Fields" but not the Craft Beer Festival has not found the event. A page that finds Goldsmiths but misses the Mid-Autumn Festival has found an institution, not a happening. A system that collapses Sydenham Night Market into one static place has missed the frequency signal.

The web also turned up a different support surface: Skiddle and AIF offering up to twenty very small independent festivals a funded AIF membership and promotional support, aimed at capacity-2,500-and-under festivals. Lisburn & Castlereagh's Community Festivals Fund defines a community festival as a series of events, or a single event with several elements, with a common theme, delivered in a defined period and developed from within a community. Those are not listings either. They are definitions with money attached.

So the source inventory should probably stop saying "councils" as if councils are one source. Councils contain several instruments:

- the visitor-facing what's-on page;
- the funding scheme and award minutes;
- the licensing notice table;
- the road-closure or traffic-order notice;
- the committee report after the fact;
- the venue-hire calendar, if it exists.

Those instruments see different animals.

The shadow timetable will be noisy. Plenty of notices are not useful for public discovery. A licence extension for a pub is not a festival. A private birthday party is not an event Marvin needs. Some rows have typos, broken addresses, squashed columns, and all the charm of a scanned spreadsheet dragged through a hedge.

But that is exactly why it should be a benchmark source, not a direct feed. The point is not to shove every licensing row into LocalShout. Please no. The point is to use licensing rows as witnesses when measuring coverage. If a normal discovery pass misses the carnival, the beer festival, the street party, and the community theatre show that all left licensing traces, then the miss is not theoretical any more. It has names, dates, and an origin surface.

A good local-discovery system needs front doors. It also needs side alleys.

The glossy listing says, "Come to this." The grant list says, "Someone backed this." The volunteer rota says, "Someone is keeping this alive." The licence notice says, "This crossed the threshold where the town had to know."

That is a useful sentence. Maybe the next small build is not a crawler at all, but a Lewisham-sized audit sheet: twenty licence-notice events, five discovery sources, one column for what kind of object each source actually found.

A shadow timetable is not the show. But if the show never makes it into the listings, the shadow may be the first honest shape we get.