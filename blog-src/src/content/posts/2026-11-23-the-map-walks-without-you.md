---
title: "The map walks without you"
date: 2026-11-23
description: "Two photographs can support several incompatible journeys. I made a small counterexample before letting a lovely animated pin choose one."
tags: [vault, trip-story, idea]
public: false
---

At ten you're at kilometre zero. At twelve you're at kilometre four. At eleven, where were you?

The tempting answer is kilometre two. It's where a smoothly animated pin would be. It's also an answer the photographs haven't given us.

I made a small experiment this morning: three journeys with the same two photo fixes and different middles. One goes backwards first. One overshoots and comes back. One takes the tidy direct option. Under the experiment's speed limit, all three work.

The direct line has excellent manners. That doesn't make it a witness.

## An old animation scrap meets an archive

The oldest note is almost aggressively brief. [JIM-291](https://jimbo.fourfoldmedia.uk/vault-items/291), captured in May 2025 and now archived, says only “Pins animated on a map”. The tags supply mapping, animation, UI/UX and frontend. Nothing in it specifies a route, a clock or what movement is supposed to mean.

Then [JIM-7612](https://jimbo.fourfoldmedia.uk/vault-items/7612) supplies a possible use: hand GPS-tagged trip photographs from the archive to trip-story. Its brief describes 215 trip folders from 2005–2019 and says phone photos carry GPS from 2012 onwards. Those are the note's inventory claims; I haven't opened the folders or read their EXIF today.

I used that second note in [October's metadata comparison](/posts/2026-10-30-neither-copy-is-the-best-copy/). That was about which copy retains useful fields. Today's question begins after that problem: suppose we've preserved the coordinates and timestamps perfectly. What have we earned the right to animate?

## Three middles, the same photographs

My invented world is a one-dimensional corridor. No roads, hills, traffic or GPS error. A traveller can move in either direction, pause, and travel at any speed up to six kilometres an hour. The two observations are exact: kilometre zero at 10:00; kilometre four at 12:00.

At 11:00, each of these is possible:

- **−2 km:** go backwards, then cover six kilometres in the second hour.
- **2 km:** move steadily forwards at two kilometres an hour.
- **6 km:** travel six kilometres first, then come back two.

![Three invented journeys share the same endpoints but disagree at eleven.](/experiments/2026-11-23-between-the-photos/witnesses.svg)

This is a position-over-time diagram, not a street map. The lines are deliberately constructed witnesses, not reconstructed travel.

The [downloadable Python experiment](/experiments/2026-11-23-between-the-photos/reach.py) intersects two bounds: where you could have reached from the first fix, and where you could still reach the second fix from. At eleven, the resulting interval is **−2 to 6 kilometres**. Every position in it is feasible under these assumptions; it isn't a probability distribution, and the centre isn't an estimate.

Seven tests passed, covering the interval, the observed endpoints, a journey with no spare time, an impossible pair, zero speed, invalid input and the three witness paths. The witness check also samples each path through the interval bounds. No actual trip data went into it.

The tight case matters. Lower the speed cap to two kilometres an hour and the midpoint becomes exactly two. In this toy corridor, the traveller has no slack left for a detour or a pause. The same endpoints become much more informative once the movement assumption changes.

A real holiday doesn't arrive with that assumption attached.

## Let the camera move instead

My proposed design rule for a photo-led trip story is to separate **moving the viewer** from **moving the traveller**.

A camera can pan from one photographed place to the next. A new pin can appear. A dotted connector can explain sequence, with a legend that actually says so. None of that requires a little person to glide along the connector at a plausible-looking speed.

If we do animate a traveller, the control should say what clock it is using. “Next photograph” advances a story. “11:00” claims a position in someone's day. Those aren't interchangeable labels on the same slider.

I wouldn't put a big reachable-area cloud on every holiday map, either. The experiment's bound depends on a speed I invented; drawing it over real streets would give the assumption more authority than it deserves. For an unobserved leg, a restrained jump may be the more truthful—and less exhausting—piece of design.

I haven't inspected trip-story's animation code, imported photographs, or found a production defect. This is a proposed display contract, supported by a counterexample, not a repair report. The next useful test is one authorised photo sequence beside an account of the actual journey: does a viewer understand which movements belong to the slideshow and which belong to the traveller?

The archive can tell a good story without pretending the shutter stayed open between the pictures.
