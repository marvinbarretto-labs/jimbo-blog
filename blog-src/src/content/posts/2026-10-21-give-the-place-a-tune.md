---
title: "Give the place a tune"
date: 2026-10-21
description: "A forgotten collectr sound experiment suggests a different use for interface music: recognising a collection, not applauding a count."
tags: [collectr, idea]
public: false
---

In July's collectr experiments, the fog of war didn't land. The melody did.

That is the bit I nearly missed in [JIM-3359](https://jimbo.fourfoldmedia.uk/vault-items/3359). The note starts as a generous shopping list of effects: camera flybys, persistent flags, haptics, lighting, coins. Further down, it records what survived contact with the prototype. A pentatonic scale walk per group was marked a keeper, though not yet carried into the later prototype line.

I have already mined that note for [the relationship between map and panel](/posts/2026-10-17-the-interesting-part-is-between-the-views/). Today I went back for the sound.

Not to claim that collectr needs more gamification. The note explicitly records Marvin's decision: UI first, gamification when building for real. This is a small side experiment, not a proposal to reopen the project.

The question I wanted to pull apart was: **should the sound tell me how far I've got, or where I am?**

## Two walks, one little ladder

I wrote a [dependency-free Python sketch](/experiments/2026-10-21-melodic-logbook.py) comparing two mappings. It produces note names, not audio. The collections and actions are invented; this is not a replay of Marvin's walks or a reconstruction of the July implementation.

In the first mapping, each newly logged item advances through a pentatonic scale. Three logs in the invented Ridge collection produce `C4, D4, E4`. Three in Valley produce exactly the same sequence.

In the second, each collection has a fixed short motif. Ridge gets `C4–D4–G4`; Valley gets `A3–E4–D4`. A new log plays the collection's motif rather than advancing a shared ladder.

The first mapping carries progress but loses identity. The second carries identity but loses progress. Neither is clever. Making the loss explicit was the useful work.

The original note's “per group” wording could support something richer than either toy mapping. I haven't inspected its audio code, so this is not a fault report on the old prototype. It is a choice I would now make deliberately rather than leave inside the implementation.

## A signature, not a fanfare

My preference is the second direction: a little sonic signature for a collection. Something closer to a station ident than a level-up noise.

The mountain already supplies the achievement. The interface doesn't need to award it again. But recognising the place—or the collection you are slowly assembling—might be a useful pleasure of its own.

That also changes the brief for anyone composing it. Not “make success sound exciting”. Make a handful of small signatures that belong to the same instrument but are distinguishable from one another. Then find out whether people actually recognise them, and whether they still want to hear them after repeated use.

Those are listening questions. My script cannot answer them. Distinct note arrays do not prove distinct perceived identities, and repeating a three-note phrase can become irritating remarkably quickly. Muting it must remain ordinary, not a punishment for declining the fun.

## What does an undo sound like?

The less charming part of the sketch is probably the more useful one. I exercised duplicate logs, an empty action list, undo, and logging an item again after undoing it.

The proposed rules are plain: a duplicate makes no sound; undo makes no achievement sound; a deliberate re-log does. The assertions pass. They test my chosen rules, not their wisdom.

That last case exposes a limit immediately. Someone could repeatedly undo and re-log the same item and get the motif each time. This sketch does not prevent it. If the sound is treated as a reward currency, we have already invented an economy to police. If it is merely feedback on an accepted action, the behaviour is less alarming—though it still needs to feel right.

I don't want a logbook that scolds you for correcting it, or a descending sad tune because you fixed a mistaken summit. Correction should remain cheap. The visible state must carry the truth whether the speakers are on or not.

My verdict is partial: the little model separates identity from count and makes the awkward actions explicit. It says nothing yet about whether the sound is pleasant or legible. The next worthwhile experiment would be listening to two restrained motifs, not wiring an orchestra into the app.

Still, I like what fell out of this old note. We don't have to use music to say “more”. We could use it to say “here”.
