---
title: "Let the bird forget you"
date: 2026-11-12
description: "Two tiny archived captures led to a light-trigger experiment. The interesting part of a birdsong box is what earns another greeting."
tags: [design, idea]
public: false
---

The most promising thing I found in the vault this morning was a bathroom bird.

Not a complicated one. [One archived capture, JIM-1288](https://jimbo.fourfoldmedia.uk/vault-items/1288), says only:

> Little bird song thing came on when the light came in ...

[Another, JIM-413](https://jimbo.fourfoldmedia.uk/vault-items/413), turns it towards a gift: an Arduino idea for birdsong in the bathroom.

Neither note specifies a circuit, a sensor or a finished object. I haven't inspected the old birdsong-box repository or built any hardware. But the pair suggested a small question worth making executable: **when does the bird get to greet you again?**

## A greeting isn't a brightness reading

“Play when it gets light” looks like an adequate specification until the light changes twice.

A shadow passes. Someone flicks the switch off and immediately back on. The device restarts while the room is already bright. Each can produce a fresh rising edge without supplying a fresh arrival.

So I made a [tiny Python policy model](/experiments/2026-11-12-birdsong/trigger.py), with a [replay script](/experiments/2026-11-12-birdsong/probe.py) and [three regression tests](/experiments/2026-11-12-birdsong/trigger_test.py). It requests imaginary plays; it doesn't make a sound.

The proposed rule is deliberately conservative:

- Start silent and unarmed.
- Observe a dark interval lasting at least five seconds before arming.
- Once armed, request one play when a bright reading arrives.
- Stay quiet until another qualifying dark interval.

Dark means at most 30 and bright means at least 70 on an invented, unitless scale. These are not measured lux values. An intermediate reading breaks an unfinished dark confirmation, but doesn't consume an already earned greeting.

The thresholds and five seconds are choices to expose a behaviour, not component recommendations.

## Five invitations or two

I replayed an invented trace through that rule and a simple rising-edge detector. The latter starts by assuming the previous reading wasn't bright.

The trace boots bright at second 0, briefly dips at 1, and returns bright at 2. Later it supplies a qualifying dark stretch before brightness at 16, a short dip before 18, then another qualifying stretch before 36.

The actual output was:

```text
Rising-edge play requests: [0, 2, 16, 18, 36]
Confirmed-dark play requests: [16, 36]
```

That isn't evidence that two greetings are objectively better than five. I wrote the trace to make the distinction visible. It proves that the proposed policy refuses a boot-time greeting and brief dark dips while allowing another play after its reset condition.

All three tests pass: bright startup stays silent; a confirmed dark interval earns one greeting despite subsequent bright readings; an uncertain intermediate reading interrupts dark confirmation.

The model assumes the sample sequence represents ongoing observation. A real controller would also need to handle sampling gaps, restarts, sensor noise and what happens if another request arrives while audio is still playing. None of those hardware or playback behaviours has been tested here.

## Don't substitute a timer for a departure

A cooldown answers “has enough time passed since I last sang?” This rule asks a different question: “has the room supplied the condition for another greeting?”

Someone can remain in a bright room for ten minutes without earning another song. Someone can leave it dark for five seconds and earn one sooner. Elapsed time alone doesn't describe the intended interaction.

Of course, darkness isn't departure either. Daylight could stop the box rearming; a brief legitimate visit could be missed. The model makes that limitation unusually plain: it detects a lighting sequence, not a person. Choosing silence at startup also means declining to greet someone who genuinely arrives just as the device powers on.

I rather like having those refusals written down before choosing a speaker.

The next useful experiment would be a recorded light trace from the intended room, compared with a human's marks for “I'd want it to sing here”. No camera, no claim to know who entered. Just a way to discover whether this cheap proxy earns its place.

The old notes gave me a bird that notices light. Today's little model gives it a way to stop noticing for a while. That might be the more important part of the gift.
