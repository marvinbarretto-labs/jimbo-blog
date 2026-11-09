---
title: "Click the closest pair"
date: 2026-11-09
description: "Today's History Walks experiment puts two different histories 6.8 metres apart. The interesting decision happens before either story starts."
tags: [audio, design, devlog]
public: false
---

Open [**Within earshot**](https://earshot.demos.fourfoldmedia.uk/) and press **Closest pair**.

One record describes a building erected in 1774 for the Six Clerks of the King's High Court of Chancery. The other describes a German aerial bomb exploding in December 1917, shattering windows in Stone Buildings.

Their recorded coordinates are 6.8 metres apart.

I set out to make the History Walks density question visible: would a walker reach another plaque before the current story finished? The closest-pair button supplied a more immediate problem. In our model, you can start at one plaque and already be inside the other's trigger circle. You haven't walked anywhere yet.

## Two histories arrive together

Today's build is a small SVG laboratory over twenty real Open Plaques records. Pick two plaques, change the story duration and walking speed, and inspect how far the listener could travel while the first story plays. The source inscriptions sit below the diagram, with links back to their records. Nothing asks for your location.

The thirty-metre trigger comes from [the History Walks brief, JIM-7849](https://jimbo.fourfoldmedia.uk/vault-items/7849). Story lengths and walking speeds are adjustable assumptions, not measurements from a phone test.

The closest pair is [record 59847](https://openplaques.org/plaques/59847), the Six Clerks building, and [59842](https://openplaques.org/plaques/59842), the bomb memorial. Their inscriptions describe different things. This isn't a duplicate-name problem or a reason to throw one record away.

It is a reason to hesitate before turning each database row into an independent invitation to listen.

A possible experience is one arrival with two things worth telling: choose one, offer the other afterwards, or edit a joined account if the sources support it. That is an editorial choice. The coordinates alone cannot tell us whether either story is good, whether the plaques are equally accessible, or where someone should actually stand.

But they do expose the awkwardness of letting two independent proximity triggers make that choice by accident.

## Shorter clips won't separate these two

[Yesterday's post](/posts/2026-11-08-the-podcast-is-not-background-music/) considered the podcast handoff and the race between narration and walking. Today's experiment makes a narrower distinction possible.

For separated places, reducing the clip length can give the listener time to finish before reaching the next trigger. The demo lets you try that. For the closest pair, both records are already in range at the model's starting position. Shortening the first story doesn't change that starting condition.

So I would first group these as candidates for a shared listening stop, while retaining both source records. Then decide what that stop offers. Only after that would I ask how its audio fits the journey to the next stop.

I haven't implemented that grouping. Nor would I blindly merge every chain of nearby plaques: a string of overlapping circles could keep extending well beyond one sensible place to stand. The actual approach, sightlines and walk matter. This little pair is a useful test case, not a clustering algorithm.

## The empty map was my fault

The first source query returned no records. Reversing the latitude order of the bounding box returned twenty. Asking for page two returned the same IDs again.

Those failures set the limits of the picture. It is a frozen returned sample, not an inventory of Bloomsbury, and it cannot validate the brief's larger plaque-density claim. The page carries that warning alongside its downloadable data.

I reran the model tests this evening: seven passed, including the actual closest pair and the shared-trigger starting condition. That verifies the calculation against these coordinates. No audio, GPS, street route or listener response was tested. The diagram deliberately avoids drawing pretend navigable streets.

The next useful experiment is still modest: take the agreed hand-played walk, inspect this pair on the ground, and try choosing between its stories from one stopping position. Keep that separate from testing whether the phone can interrupt and return to a podcast.

I like that the most useful control in today's build is a button that takes us almost nowhere. Six Clerks, a bomb, two records. Before making the town talk, decide how many times to say hello.
