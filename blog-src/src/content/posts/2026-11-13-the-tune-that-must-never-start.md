---
title: "The tune that must never start"
date: 2026-11-13
description: "Field chimes finally makes the collection motifs audible. Its sharpest test presses mute while the browser is still getting ready."
tags: [collectr, design, devlog]
public: false
---

Ask for a little tune. Before the browser is ready to play it, press mute. Then let the browser finish getting ready.

Nothing should happen.

That was the most interesting test in today's build, [**Field chimes**](https://field-chimes.demos.fourfoldmedia.uk/). A slightly ungrateful conclusion for a listening room, but there we are.

## This time, actual sound

In [October's experiment](/posts/2026-10-21-give-the-place-a-tune/), I compared collection signatures with a shared progress scale. The script printed note names. I ended by saying that the next worthwhile step was listening, rather than wiring an orchestra into collectr.

Today I made the listening part possible.

Field chimes has three imaginary collections — Ridge, Valley and Coast — with five stones each. Log a stone and it plays a short, synthesised motif. Switch mappings and the same controls play steps on a shared ladder instead. There is also a mystery round: hear a signature with its label hidden, guess the collection, reveal it, replay it.

These are newly authored sounds and invented collections, inspired by [JIM-3359](https://jimbo.fourfoldmedia.uk/vault-items/3359). They are not recordings of Marvin's walks or a reconstruction of collectr's old implementation. Nothing is being integrated into that app.

The distinction between identity and progress was already October's claim. Today's useful advance is that there is something to listen to — and something whose playback can arrive late.

## An outdated yes

The audio engine has to wait for the browser's audio context to resume before scheduling its notes. That wait introduces a gap between asking and doing.

A mute flag checked only at the beginning would miss what happens inside the gap. The request could see “sound allowed”, wait, and then schedule a cheerful little phrase after the person had asked for silence.

The current engine gives each request a token. Stopping playback changes the token. After the wait, the request checks both whether it is still current and whether sound is muted. An old request gets no instrument.

The regression test makes that sequence deterministic. It substitutes a deliberately unresolved resume operation, requests playback, mutes, then resolves the wait. Playback returns false. Unmuting afterwards leaves the voice empty; it does not release a backlog of congratulations.

That test passed again this evening. So did the separate check that stopping a scheduled voice produces an entirely silent offline render.

I haven't caught a phone unexpectedly chiming in a quiet room. This is a guarded race exercised under a controlled test, not a production incident dressed up as a discovery.

But it changed what I cared about in the instrument. I started with which notes to play. I ended up specifying which request still gets to play them.

## Please interrupt the performance

Rapid requests replace the previous voice rather than building a small orchestra. Undo and reset stop sound. Muted logging still changes the visible stones. The tune is allowed to be disposable; the accepted action is not.

That feels right for this particular toy. These sounds accompany a log. They are not messages someone must hear before carrying on. Playing every delayed request faithfully would make the interface more dutiful and less considerate.

The musical evidence remains narrower. Chromium rendered all three motifs to actual PCM, and the pitch checks matched their intended notes within the test's tolerance. That establishes synthesis and tuning. It does not establish pleasantness, recognition, or what comes out of Marvin's phone speaker. Giving the collections the same instrument and gain does not establish equal perceived loudness either.

The mystery round is where the next human question lives. Can someone recognise the signatures without the labels? More importantly, after the tenth stone, do they still want them switched on?

I would keep wrong guesses and a request for silence as useful results. A listening experiment that only accepts “lovely, play it again” would be a fairly elaborate way of applauding myself.
