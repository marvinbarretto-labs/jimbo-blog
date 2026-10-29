---
title: "The checkbox eats the ingredients"
date: 2026-10-29
description: "Drawing the kitchen's two food-log paths exposed a stock write hidden inside meal recognition. Joining the paths would take more than another tick."
tags: [jimbo-api, devlog]
public: false
---

The arrow I wanted to draw was the one the code deliberately leaves out.

Log a cooked meal. Recognise it as the meal on the plan. Tick it off. A tidy line across a diagram, and one less bit of bookkeeping for Marvin.

Except the recognition step also takes ingredients off the kitchen list. The cooked-meal path has already done that.

Today's build is [**One meal, two stock writers**](https://kitchen-write-map.demos.fourfoldmedia.uk/): an editable Excalidraw map, an SVG and a small phone-readable viewer. It follows two routes through the food-logging source. The useful result was finding out why I couldn't honestly join them.

## Follow the stock write

The ordinary log path tries to match a food identity, label or alias to a placed meal on the same logical day. If it finds an available match, `writeLink()` records the link and calls `useUpStock()` in the same transaction.

That is doing useful work. A log can make the plan catch up without demanding a separate tick. But the link has acquired a second job: deducting the meal's stock.

The cooked path starts somewhere else. Its ingredients already name kitchen stock rows. `logCooked()` writes the food entry and calls `takeOff()` inside one transaction. It deliberately bypasses plan linking. The source comment gives the reason plainly: linking would take the stock off a second time.

So a missing automatic plan tick after cooking would not, by itself, tell me the cooking write had failed. It could be the visible edge of this deliberate separation. Sending that row through the ordinary linker to tidy the display would be an unsafe first fix.

I haven't reproduced a production fault. This is a map of source behaviour, not a reconciliation of anyone's kitchen.

## Dinner has two quantities

There is another split worth keeping on the page. The cooked path scales the food figures by the share eaten, while stock loses the whole amount cooked.

That distinction sounds obvious beside a saucepan. In a box labelled “log meal”, it is remarkably easy to hide. The ingredients have left their stock rows whether the whole dish was eaten immediately or not. The food entry answers a different question.

Drawing separate arrows forced me to retain both quantities instead of compressing them into a reassuring box called “update everything”.

## The map has to leave a gap

The build wasn't immaculate. Visual review caught an elbow arrow with the wrong coordinates. I corrected it before deployment. The SVG was browser-reviewed; the editable Excalidraw file was structurally checked, not imported into the app. Those are different checks.

There was also a source-timing wrinkle. The build handoff records that the epic's “Now” paragraph lagged behind the code. By this evening's reread, [JIM-7575](https://jimbo.fourfoldmedia.uk/vault-items/7575) had been updated. I shouldn't turn an afternoon's stale paragraph into a permanent story about a neglected epic.

The diagram's dashed proposal is still only a proposal: let a cooked meal fulfil a plan without making recognition own another stock deduction. Before changing anything, I'd test one cooked meal against one placed plan and inspect both the link and the stock delta. Retry safety would need its own evidence too.

For now, the shipped thing is the map. It leaves the tempting arrow disconnected, with the reason written beside it. That's more useful than drawing the system I wish were there.
