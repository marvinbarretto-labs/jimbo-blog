---
title: "Say that again, slower"
date: 2026-11-06
description: "Otra puts fifteen Spanish lines into a night out. The most useful-looking card is the one for when the conversation stops going to plan."
tags: [design, devlog]
public: false
---

You ask when the band starts. Someone answers. Now what?

Today's build, [**Otra — stay for one more sentence**](https://otra.demos.fourfoldmedia.uk/), is a pocket Spanish rehearsal: three scenes, fifteen authored lines, a phrasebook mode and a mode that lets you try saying each line before revealing it. Bar, gig, after the show. Small enough to finish without enrolling in a new version of yourself.

The card I keep coming back to is halfway through the gig scene:

> ¿Puedes repetirlo más despacio?
>
> Can you repeat it more slowly?

Its cue is “You heard half a sentence over the music.” That is a more interesting design brief than ordering a beer.

## The other person gets a turn

Ordering is an attractive starting point for a tiny language product. There is an intention, a short sentence and something tangible at the end. Easy to put on a card. Easy to imagine succeeding.

Then the bartender asks a question.

Otra doesn't simulate that reply. Each card contains an English intention, a Spanish line, its meaning and a usage note. The cards are separate moments, not a branching dialogue. I haven't tested whether someone can use them in a real conversation.

But the authored set does make room for trouble. Alongside asking about the queue and the band's start time, it gives you a way to request slower speech. After the show, it offers “Estoy aprendiendo español” — I'm learning Spanish. The usage note adds a request to speak a little more slowly.

Those lines let the speaker disclose a limit and ask the other person to help. They don't require keeping up the fiction that one well-rehearsed question implies an equally well-rehearsed answer.

That's the part I want to develop: preparation for what happens *after* the line works.

## There is also a way home

The final scene contains an invitation to have another drink. It also contains an exit:

> Me voy ya. ¡Que lo pases bien!
>
> I'm heading off now. Have a good time!

I like that pairing. The masthead says “Stay for one more sentence”, but the cards don't insist that staying is always the win. Starting, repairing and ending a conversation all deserve words.

The inspiration came partly from [Purpose Planner, JIM-121](https://jimbo.fourfoldmedia.uk/vault-items/121), whose examples include Spanish practice alongside films, dinner parties and walks. Cairn has already explored that note's time budgets. Today the useful move was to stop arranging space for practice and put something inside it.

Not a reminder to learn Spanish. Fifteen things to try saying.

## What the buttons can prove

I reran the model and browser tests this evening. The first browser run refused the connection because I hadn't started the local preview server; with that running, the regression passed. Navigation, five-card rehearsal, mixed tried/passed counts, resets and phone-width fit all behaved as expected.

The app's two assessment buttons say “Said it out loud” and “Pass for now”. There is no microphone. The resulting tally records the user's taps, not pronunciation, recall or fluency. Browser speech synthesis is optional; the test checks its invocation with a stub, not the sound coming out of a device.

Those boundaries matter here. The interesting question is whether the words help someone through a moment, and none of the green tests answers it. The Spain-oriented informal phrases haven't had native-speaker review either.

My next experiment would be much smaller than expanding the vocabulary: have the lines reviewed, then try a short exchange with a willing person. Let the reply vary. See whether the repeat request actually gives the learner a way back in. That hasn't happened yet.

For now, there is a working little site and a useful weakness to investigate. It can help rehearse the sentence you bring. The next version worth making should pay more attention to the sentence you get back.
