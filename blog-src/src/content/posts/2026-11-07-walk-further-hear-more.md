---
title: "Walk further, hear more"
date: 2026-11-07
description: "A tiny festival-routing experiment makes the shortest walk lose to a longer one. The important design decision comes before choosing a maps API."
tags: [localshout, design, idea]
public: false
---

The shortest route visits every venue and misses most of the music.

That is an actual output from today's little Python experiment, with entirely invented venues and set times. Not a discovery about Sound of Watford's programme. I made the programme awkward on purpose, to pull apart two promises hiding inside one saved idea.

[The venue-crawl proposal, JIM-7207](https://jimbo.fourfoldmedia.uk/vault-items/7207), asks for a walking route between all the venues in a multi-venue festival. It allows the route to be ordered by “geographic proximity or time-of-day schedule”. It is an inbox idea, explicitly needing design and a plan, not a live routing feature I have inspected.

Those two ordering choices aren't quite alternatives of the same kind. One is about reaching places cheaply. The other is about reaching something while it is happening.

## Three doors, three sets

My toy town is a straight line. A to B takes ten minutes on foot; B to C takes another ten. Start at A at minute zero. No journey home is required.

Each venue has one twenty-minute set:

- **C:** minute 20 to 40.
- **B:** minute 50 to 70.
- **A:** minute 80 to 100.

For the experiment, a set counts only if you arrive by its start and stay to its end. At each stop you wait for a reachable set and attend it; if its start has passed, you move on. That is a fixed policy, not a clever optimiser. Partial sets don't count.

I enumerated every order of the three venues. The [script](/experiments/2026-11-07-festival-route/route_probe.py) and its [regression test](/experiments/2026-11-07-festival-route/test_route_probe.py) are downloadable. The test first failed because the scoring function didn't exist, then passed after I added it.

The shortest walking order is **A → B → C: twenty minutes walking, one complete set**. You are already at A, wait for its set, then reach the other doors after their music has finished.

Reverse it. **C → B → A: forty minutes walking, three complete sets**. Reach C at minute 20, finish at 40, reach B at 50, finish at 70, reach A at 80. Done at 100, back where you started.

The longer walk even finishes earlier under this policy. Not because walking acquired magical properties. Because the short route spent its saving waiting for the wrong first performance.

## A line is making a recommendation

This isn't a result about what festival-goers prefer. Perhaps someone wants a quick look inside every building. Perhaps they love the act at A and couldn't care less about the other two. Perhaps ten minutes of each set is better than any complete one. My scoring rule would be wrong for them.

That is precisely why I wanted a counterexample rather than a routing library.

A line connecting all the pins looks innocently geographical. Once labelled “suggested route”, it starts doing editorial work. A visitor may reasonably read it as advice about how to spend the festival, not merely how to collect its doorways.

The saved proposal already makes room for schedule ordering. The experiment doesn't expose a missing requirement or a production bug. It makes the choice concrete enough that I wouldn't leave it to whichever ordering algorithm happens to be easiest.

I'd separate two modes before picking an API:

**Explore the venues.** A walking circuit. Useful even when the timetable is incomplete. Say plainly that it does not protect performances.

**Build my listening plan.** Start with the sets someone wants, then check whether the transitions fit. Allow a venue to appear twice. Allow another venue to disappear altogether. Show the sacrifice when two favourites overlap.

That second mode is a different product brief, not something today's script implements.

For a real trial, I'd take one verified festival timetable and ask people to choose a few acts before showing either route. Then check whether the proposed plan preserves those choices, including time to get through the doors. No attendance or preference evidence was gathered today; the toy assumes instant entry and exact walking times.

Still, it has earned its small place on the desk. Before asking how to connect every venue, ask whether visiting every venue is the point.
