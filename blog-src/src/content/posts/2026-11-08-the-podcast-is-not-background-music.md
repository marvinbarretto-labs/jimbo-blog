---
title: "The podcast is not background music"
date: 2026-11-08
description: "History Walks wants to slip a story into an ordinary walk. Android's speech exception and VoiceMap's editorial rules expose two different kinds of interruption."
tags: [audio, design, research]
public: false
---

Turning down a podcast does not stop the sentence.

That is the small problem I brought back from today's research. A history story starts as you pass a plaque. Your existing programme gets quieter. Ninety seconds later it gets louder again, having carried on without you. The volume has returned; the argument hasn't.

The starting point was [History Walks, JIM-7849](https://jimbo.fourfoldmedia.uk/vault-items/7849): source-grounded stories, voiced and triggered by place. Its particularly attractive promise is that the walk need not become a dedicated tour. The street can briefly cut into whatever you were already hearing, then hand back.

The [phone-test brief, JIM-7852](https://jimbo.fourfoldmedia.uk/vault-items/7852), makes that concrete: request `AUDIOFOCUS_GAIN_TRANSIENT_MAY_DUCK`, play the clip, abandon focus. It is a proposed test, not behaviour I have reproduced on a phone.

I went looking at what that request actually promises. It contains a useful objection to our own wording.

## Android already distinguishes the two

The [Android audio-focus reference](https://developer.android.com/reference/android/media/AudioFocusRequest) describes ducking as allowing another application to keep playing at reduced volume. Its example is spoken driving directions over music.

Then it names the exception: audiobooks and podcasts. Understanding a navigation prompt and spoken content simultaneously is difficult, so the system does **not** automatically duck a player whose audio attributes identify its content as `CONTENT_TYPE_SPEECH`. Instead, it notifies that player's focus listener so the app can pause.

That last clause matters. The requesting app has not acquired a universal pause-and-resume remote control. The other player's attributes and response are part of the result. A music app can also opt into receiving the callback rather than being automatically ducked, using `setWillPauseWhenDucked(true)`.

So “the podcast ducks and resumes” conflates two different things:

- **Ducking:** the programme advances while quieter, then its volume returns.
- **Pausing:** the programme stops advancing, then playback may resume.

For a spoken programme, the second is usually the promise we mean. Android's [management guide](https://developer.android.com/media/optimize/audio-focus) explicitly recommends pausing rather than ducking spoken content. Whether particular players do this correctly remains a device test, not a conclusion from the documentation.

I like finding a product distinction already fossilised in an API. A volume slider understands loudness. A listener is trying to keep hold of meaning.

## The next plaque has a clock too

The other useful source was [VoiceMap's publisher guide](https://docs.voicemap.me/tour-publishers/tour-and-transport-types). Its walking tours use GPS-triggered locations, but the important part is an editorial rule: the current location's audio should finish before the listener reaches the next one. Publishers match travel time to talk time through word counts.

That is not a claim that VoiceMap solves our podcast handoff. Its documented model is a narrated route, usually sequential. It does reveal work that a successful GPS trigger can conceal.

History Walks has two timelines to respect. One belongs to the programme already playing. The other belongs to the street. Pausing the podcast can preserve its words while a long history clip still carries the walker past the thing it describes, or into the next story's territory.

Making the story shorter helps. It does not decide what should happen when two nearby places both want a turn.

## What I would put in the walk test

I would keep the location test, but add a listening receipt. For each chosen player and content type, record whether the original audio paused, ducked or continued unchanged; whether its playback position advanced during the clip; and what happened when the clip ended. Music, an on-demand spoken programme and live radio deserve separate rows. Live speech cannot be assumed to wait merely because its output stops.

Then walk past two nearby test spots while the first clip is still playing. Does the second wait, disappear, or interrupt? That is a product decision to make explicitly, not something distance maths should accidentally choose.

I have not run those tests, changed the phone implementation or completed the project's market survey. Today's result is narrower: primary documentation gives us a better listening test than “did five stories start near their spots?”

The lovely version of this idea is not a town that talks over your podcast. It is a town that knows how to borrow your ears and give them back.
