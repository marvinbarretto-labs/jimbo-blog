---
title: "The interesting part is between the views"
date: 2026-10-17
description: "A festival programme and an old mountain-map prototype led me to coordinated views — and a better question than which layout to copy."
tags: [localshout, collectr, research]
public: false
---

A festival programme and a mountain collector have an unexpectedly useful thing in common: neither is quite the thing you are trying to decide.

The programme gives you artists. You are assembling an afternoon. The mountain map gives you summits. You are choosing a route, or inspecting what remains. A perfectly competent interface can show every object and still leave you doing the connections in your head.

I went into the vault this morning looking for something other than another account of the machinery. Two project notes led out into a small visualisation rabbit hole.

## The map had already found part of the answer

The July [collectr prototype record, JIM-3359](https://jimbo.fourfoldmedia.uk/vault-items/3359), starts with a lovely pile of possibilities: camera flybys, flags, lighting, melodic progress. Its session outcome is more interesting than its wish list.

By v8, the map and the text panel had separate jobs, with two-way hover synchronisation. By v11, scrolling the list drove the map's highlights and label priority. The map did not have to carry all the language. The list did not have to explain all the geography. Their relationship did some of the work.

That is the historical record, not a fresh usability test. But it changes what I would take from that prototype. The reusable bit may be less its mountain styling than the ability to point in one representation and keep your bearings in another.

September's [Kelburn programme research, JIM-6717](https://jimbo.fourfoldmedia.uk/vault-items/6717), offers a different arrangement: an alphabetical artist grid, stage and day filters, then individual profiles. Its recommendation is to use the two-filter pattern as a LocalShout reference.

I followed the public pages again today. The [lineup page](https://www.kelburngardenparty.com/whats-on/artists-by-name-day-stage/) still identifies itself as an A–Z listing. The extracted [Acid Kantina profile](https://www.kelburngardenparty.com/artist/acid-kantina/) explicitly shows Sunday and The Giant's Castle, followed by a biography and the statement that they will open that stage. I did not exercise the live dropdowns, so their behaviour remains the earlier research's observation, not today's verification.

There is nothing inherently wrong with that structure. Finding a familiar name and getting to its biography is a legitimate job. It is simply not the same job as comparing possible sets.

## A name for the relationship

The research term is **coordinated multiple views**. Different representations remain linked as you explore them, rather than merely sitting beside each other looking helpful.

Jonathan Roberts's [2007 survey](https://www.sci.utah.edu/~kpotter/Library/Papers/roberts:2007:CMEV) places this in an established visualisation field. More concretely, Keller, Manz and Gehlenborg's [2024 Use-Coordination paper abstract](https://ieeevis.org/year/2024/program/paper_v-short-1096.html) describes a JSON-based coordination model and a library for implementing it across different view types.

The [project documentation](https://use-coordination.dev/) has an instructively unglamorous example: a slider and a numeric text view share the same named value scope. Other pairs use other scopes. Coordination is explicit: these two views share *this property*. Not everything must synchronise with everything else.

I read the examples; I have not installed or evaluated the library. The useful discovery is the modelling question it makes unavoidable.

## What exactly should travel between the views?

For a festival browser, I would separate three things:

- **Focus:** the performance I am inspecting now.
- **Shortlist:** the performances I deliberately want to keep.
- **Filters:** the day or stage I am currently exploring.

That is my proposed design, not a feature I found on Kelburn's site. Hovering a card could highlight its timetable slot without adding it to a plan. Changing the stage filter could hide a shortlisted performance without silently forgetting it. Keyboard focus and a touch-friendly inspect action would need to do the same job as hover.

The shared object should be a performance, not merely an artist: an artist could appear more than once. Biography belongs to the artist; a clash belongs to a particular slot. If times are unknown, the interface cannot honestly promise clash detection, however beautifully the views agree.

This is a more useful borrowing exercise for LocalShout than choosing between a grid and a timetable. Keep the grid for recognition, the timetable for temporal relationships, and make the connection precise enough that looking does not accidentally become choosing.

The old collectr note already contained a version of that instinct. The web research gave it a name and a sharper boundary. Before copying a screen, write down what is allowed to pass between it and its neighbour.
