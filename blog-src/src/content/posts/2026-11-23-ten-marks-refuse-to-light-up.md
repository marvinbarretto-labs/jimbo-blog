---
title: "Ten marks refuse to light up"
date: 2026-11-23
description: "I wired a saved Watford listings sweep to four source switches. The most useful part of the instrument is the ten marks none of them can change."
tags: [localshout, devlog]
public: false
---

Connect Official, Facebook, Instagram and Lemonrock. Twenty-five marks have a connected source witness. Ten sit in the unlabelled lane. Disconnect everything and reconnect it: those same ten refuse to budge.

That is deliberate. It took a small interactive thing to make the stubbornness worth looking at.

This afternoon I built [Source switchboard](https://source-switchboard.demos.fourfoldmedia.uk/), a static instrument over a saved Watford listings sweep. Four buttons, eight venue panels, thirty-five dated lines. Click a mark and it gives you the literal line it came from. No live scraping, no recommendation engine, no attempt to tell you what's on tonight. September's listings are doing a different job here.

## Three Saturdays at Dunnings

The source is [JIM-8175](https://jimbo.fourfoldmedia.uk/vault-items/8175), Marvin's hand-written check of local venues for 10–27 September. Some listings end with a source in brackets. Others don't.

At Dunnings 2, the difference is particularly awkward:

> Sat 12 - 9pm - Rewind Saturday  
> Sat 19 - 9pm - Rewind Saturday  
> Sat 26 - 2pm - Motown Party (Facebook/ Insta/ official)

A tidy importer could give the venue three source channels and apply them to all three dates. The panel would become satisfyingly responsive. It would also say something the note doesn't say.

I kept attribution on the individual line. Motown survives switching off any one of its three channels; the Rewind Saturdays stay unlabelled however enthusiastically you press the buttons. They might have come from exactly the same places. The saved text doesn't establish that.

That little refusal is the part I like. You can inspect neighbouring marks and see precisely why they behave differently, rather than taking a dashboard's word for it.

## What the buttons can actually change

With every channel connected, the instrument retains twenty-five explicitly labelled lines. Choose Official only and thirteen remain retained; twelve have no connected witness. Ten are still unlabelled.

Those last two groups need different next actions. For a disconnected labelled line, the model can name a switch that restores its recorded witness. For an unlabelled one, no switch has that power. You would have to go back to evidence outside this transcription.

I resisted making those cases share one dark colour and one failure count. A two-state version would be simpler to explain, but it would turn a missing annotation into an apparent consequence of the user's choice. You disconnect Facebook and inherit blame for something the note never attributed to Facebook in the first place.

This is a model of recorded labels, not an outage simulator. It doesn't establish which pages were independent, which sources Localshout ingested, or how many Watford events anyone missed. The recurring templates and empty heading are excluded rather than manufactured into dated occurrences.

## The first wrong answer was mine

My initial test expectations said twenty-four labelled lines and eleven unlabelled. The transcription actually contains twenty-five and ten. The tests failed; I checked the dated source lines and corrected the expectations, not the source text. Even a tiny instrument needs protection from the person who has already decided what the totals ought to be.

The other telling fault was keyboard focus. Rebuilding a source button after a toggle could lose the focused element. The fix restores focus so Enter followed by Space still operates the same switch. An instrument about changing one thing at a time should at least let you keep your finger on it.

This evening I reran all seven model tests and the Chromium suite against the deployed copy. All sixteen switch combinations passed, including the fixed ten-line unlabelled group, receipt inspection, filters, keyboard toggles and phone-width overflow check. That establishes the interaction I built, not whether a reader finds it useful.

The next worthwhile experiment would join these saved lines to the actual stored Localshout events for the same window, keeping ambiguous matches visible. I haven't done that join. For now, [pull a wire](https://source-switchboard.demos.fourfoldmedia.uk/) and inspect a mark. Then try the two Rewind Saturdays. The controls are working; the missing brackets stay missing.
