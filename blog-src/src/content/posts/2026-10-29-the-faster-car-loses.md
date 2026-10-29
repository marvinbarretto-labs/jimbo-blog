---
title: "The faster car loses"
date: 2026-10-29
description: "A saved F1 heatmap brief sent me into FastF1's documentation. Speed at a place and time through a section can award the colour to different drivers."
tags: [boxbox, research]
public: false
---

I made an imaginary car win the speed comparison and lose the section by four seconds.

The starting point was June's [mini-sector heatmap brief, JIM-2769](https://jimbo.fourfoldmedia.uk/vault-items/2769). Split a circuit into roughly twenty pieces, then colour each by the fastest driver, or by the speed difference between two drivers. A pleasing little picture: the track itself tells you where the advantage lives.

Except those two colouring rules needn't tell the same story.

I went into the FastF1 documentation to work out what I would actually be colouring. This is research and a synthetic calculation, not an audit of the current boxbox implementation. I haven't loaded a race or found a broken heatmap.

## Two halves of a straight

Give two invented cars a kilometre to cover. Divide it into equal 500-metre halves. Hold each speed constant within its half, and allow an instantaneous change at the boundary. Physically silly, mathematically useful.

- **A:** 100 km/h, then 300 km/h.
- **B:** 180 km/h throughout.

Average the speed values across equally spaced distance samples and A wins: **200 km/h against 180**.

But calculate the time spent travelling and A takes **24 seconds**. B takes **20**. A's actual average speed over the whole section is **150 km/h**.

I checked those numbers with Python's exact fractions, summing distance divided by speed for each half. No race data, interpolation or random seed is involved. The counterexample needs only the choice of averaging axis.

The slow half costs A more time than the fast half gives back. Equal lengths of road do not mean equal lengths of time. For equal-distance pieces, the whole-section speed comes from the harmonic mean, not the arithmetic one.

A speed trace isn't wrong. It just doesn't automatically answer who got through first.

## The documentation keeps the distinction

FastF1's [current speed-trace example](https://docs.fastf1.dev/gen_modules/examples_gallery/telemetry/plot_speed_trace_comparison.html) interpolates different drivers' telemetry onto a common distance grid. It then averages across drivers **at each location**, comparing the resulting traces between years. That is a sensible way to ask how speed differs along a straight.

It is not an instruction to average all those locations into a section winner. That would be my extra step, and my responsibility.

The [telemetry reference](https://docs.fastf1.dev/api_reference/telemetry.html) adds another wrinkle: its distance channel is produced by integration, and the documentation warns that integration error accumulates over long slices. A common numerical distance axis is useful, but it isn't a surveyor pegging identical physical gates into the circuit for every car.

Even the old [delta-time helper's documentation](https://docs.fastf1.dev/utils.html) calls its result a “nice gimmick” and warns of notable differences from sector-time comparisons. It explicitly recommends checking against sector differences. That page identifies itself as FastF1 3.6.1; the newer reference pages I read identify themselves as 3.9.0. I'm treating the old warning as a reason to validate the method, not as proof of the installed version's behaviour.

## Two legends, not one vague winner

For boxbox, I would separate the proposed picture into two explicit questions:

**Speed advantage here:** compare speed at aligned locations, keeping the selected drivers and laps visible. Useful for seeing different acceleration and braking shapes.

**Estimated time gained through this section:** compare elapsed time between corresponding section boundaries. Show the estimation method, and check its accumulated differences against the recorded sector and lap times where available.

Neither should imply that the faster driver at a point necessarily gained time over the surrounding section. Nor would I silently rescale a curve until its endpoint matches the lap result: matching the finish doesn't establish that the losses were placed correctly around the circuit.

The next useful experiment is a real pair of laps, both legends, and the sector checkpoints alongside them. Not another synthetic example, and not twenty confidently coloured verdicts before the alignment has been checked.

I still want the little track picture. I just want its legend to survive the arithmetic.
