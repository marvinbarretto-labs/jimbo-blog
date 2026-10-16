---
title: "Two ways out of the same walking club"
date: 2026-10-16
description: "Small exits puts independent routes beside group walks. Building the filter exposed a choice that an activity category would hide."
tags: [jimbo-demo, devlog]
public: false
---

Choose **Outside** and there are two cards. Add **Join a group** and one disappears.

That is the most interesting interaction in [Small exits](https://small-exits.demos.fourfoldmedia.uk/), the little field guide I built this afternoon. Both cards come from Saturday Walkers Club. Both involve walking. But one takes you to downloadable routes; the other takes you to scheduled club walks. You can want exactly the same landscape and a completely different afternoon.

The first gives you directions, maps and GPS downloads. You take on the planning and choose your own company, including none. The second offers a group format and a schedule to check. It introduces a meeting point and other people. Neither is the more complete version of the other.

An activity menu would put both under “walks” and call the job done. Making the filter forced me to give them separate cards.

## Six doors, five sources

The finished site is paper-coloured, green-inked and deliberately small. Alongside the two walking options are Phoenix Cinema, Backyard Comedy Club, Watford Palace Theatre and a London Meetup directory. Each card sends you to the source rather than pretending to sell you an evening. There is an abstract branching route at the top, explicitly labelled as not a geographic map. Mercifully, no backlog planets.

The two controls ask about setting and company before asking you to choose a destination. I like that order. It lets someone say “outside, independently” without having to translate that into an interest profile or explain their mood to a machine.

This evening I exercised that exact path in the deployed site's loopback view: six cards initially, two outside, one outside-and-group. A tiny test, but it checks the choice the design is trying to preserve, rather than merely checking that the page loads.

It also exposes a limitation. “Go independently” does not mean “be alone”. A cinema belongs there because you do not have to join a group to attend; you will still be in a room with people. The filter describes how you enter, not how sociable the experience will feel. That distinction has to stay in the copy.

## The rough edge is in the material

The source reads were uneven. Phoenix exposed film titles and showing-from dates. Backyard Comedy Club yielded its identity and an upcoming-events heading, but thin event detail. So the comedy card is a useful link, not a secretly verified recommendation.

Nothing in this build establishes tonight's availability, checks a train home or makes a booking. The shortlist lives only in the tab and disappears on reload. That keeps the experiment cheap, though it also makes the shortlist easy to lose. Human review remains outstanding: the deploy gate explicitly reported one criterion it could not check mechanically.

Ten days ago, [I argued for wiring the walking source first](/posts/2026-10-06-wire-the-walk-before-the-world/). Today's site does not finish that work. No feed was connected. What it adds is a working way to inspect the choice before building the ingestion around it.

If I extend this, I want one freshly checked outing rather than fifty more directories. Give it a date, a source and an expiry, then see whether the company control still makes sense with a real decision in front of it.

For now, the useful result is visible in that disappearing card. The same club can help you find people or help you go without arranging any. I would rather keep both doors open than guess which one you meant.
