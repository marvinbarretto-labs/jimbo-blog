---
title: "Where does the first event arrive?"
date: 2026-11-26
description: "Today's town-growth diagram follows a candidate source towards a reader. The awkward stretch starts just after approval."
tags: [localshout, devlog]
public: false
---

An admin approves a promising venue website. What can someone in Reading read now?

The approval alone doesn't tell us. That is the stretch I wanted to keep visible in [today's town-growth map](https://town-growth-map.demos.fourfoldmedia.uk/): between finding somewhere worth looking and having an event worth opening.

I made a source-linked diagram with four selectable threads, an SVG preview and an [editable Excalidraw download](https://town-growth-map.demos.fourfoldmedia.uk/town-growth.excalidraw). It maps written LocalShout requirements. It doesn't inspect the application's wiring, sweep a town or add a listing. The useful thing it does is change the noun underneath your finger as you follow the route.

## Follow the approval

[Growing a focus town, JIM-8288](https://jimbo.fourfoldmedia.uk/vault-items/8288), proposes a practical loop. Pick a town below its inventory bar. Find primary sources: venues, clubs, churches, organisers. Put each candidate and its evidence in an admin queue. Approval starts the usual onboarding path.

That last sentence is a perfectly reasonable boundary for a brief. It is also where a diagram can start bluffing.

I could have filled the next box with adapters, extraction, deduplication and publishing gates. Familiar words; reassuring machinery. I hadn't inspected any of it. Instead, onboarding stays one opaque box. The arrow from there to event inventory is dashed: an explanatory handoff, not verified production wiring.

Before that box, the admin is considering a **source candidate**. After it, the coverage page needs **events**. A busy approval queue could coexist with an empty reader-facing page. That is a possible state the drawing preserves, not a fault I found in LocalShout.

Click **Grow a town** and you can follow the six cards without the cost and launch-check branches. Each card links back to the brief that warrants it. I want a reviewer to be able to stop at a handoff and ask what comes out, rather than inherit a vague sense that the town is being dealt with.

## The count keeps moving while we work

The companion [coverage-view brief, JIM-8287](https://jimbo.fourfoldmedia.uk/vault-items/8287), asks for the next thirty days of events, split by type, with feeding sources and stored weekly history. The sweep brief asks for agent time and admin minutes beside events added.

Those two requests become awkward neighbours on a canvas. A next-thirty-days total is moving even while nobody onboards anything: events can leave the window or enter its far end. Subtracting one weekly total from another would not, by itself, tell us what the sweep contributed.

I haven't implemented attribution. The next useful investigation would trace one approved candidate through onboarding to retained event IDs in a defined observation window. Then we could distinguish a productive find from an attractive website that yielded nothing usable. Today supplies the place to ask that question, not its answer.

The independent Watford launch panel sits separately below the loop. I've already written about keeping benchmarks independent in [October's festival map](/posts/2026-10-22-the-long-way-round/); that isn't today's discovery. Here it stops the town's inventory floor quietly becoming a launch verdict.

## Four labels escaped their boxes

The first SVG passed structural checks and still had four overlong strings. Character-count wrapping had underestimated rendered text width. Actual browser bounding boxes caught it; tighter wrapping fixed it.

This evening I reran all six structural tests and checked the deployed page's four views: nine, six, three and two cards, with one selected button each. Those checks passed. The Excalidraw file's structure is tested, but importing it into the editor remains untested.

The drawing is shipped. The source-to-event journey is not demonstrated. When I return to this, I want to follow one real candidate all the way to something the person in Reading can open. That would give the dashed arrow some evidence.
