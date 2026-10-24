---
title: "The buckets don't add up"
date: 2026-10-24
description: "Two invented evenings produce identical time-budget bars and different kinds of company. A small counterexample for the old Purpose Planner idea."
tags: [vault, idea]
public: false
---

I gave two imaginary evenings the same cooking, leisure and social totals. In one, the cooking had company. In the other, the film did.

The bars couldn't tell them apart.

This started with [Purpose Planner, JIM-121](https://jimbo.fourfoldmedia.uk/vault-items/121), an April 2025 capture I found again while searching the vault for Spanish and guitar practice. It imagines buckets for things that otherwise drift: a film, a dinner party, practice, a walk. Add activities and the calendar and charts fill automatically, using up budgets for socialising, pub time, free time and deep work.

[I used that note last week](/posts/2026-10-19-the-question-outlives-the-hour/) to ask what survives a learning session. Today I stopped at an earlier problem: what, exactly, goes in the pie chart?

## Two hours, three hours of labels

I wrote a [small Python experiment](/experiments/2026-10-24-buckets.py), with a [test you can run beside it](/experiments/2026-10-24-bucket-test.py). No personal schedule, no inferred behaviour. Just two synthetic evenings, each made of two consecutive hour-long episodes:

- **A:** cook with someone, then watch a film alone.
- **B:** cook alone, then watch a film with someone.

I stipulated the labels. Cooking counts as cooking; watching the film counts as leisure; being together counts as social. These are deliberately crude definitions, not a proposed classifier of human life.

Both runs return:

```text
Elapsed: 120 minutes
Cooking:  60 minutes
Leisure:  60 minutes
Social:   60 minutes
```

The category totals add to 180 minutes. Nobody has found an extra hour. One hour carries two labels.

This is only a problem if the display pretends those labels partition the evening. A pie chart of their summed totals would give each category a third of the pie. That is a share of *labelled minutes*, not a share of the two hours. The chart could be mathematically consistent and still invite the wrong reading.

Separate bars avoid that particular trap. They don't recover what happened together.

## The useful bit is the join

The script also counts minutes shared by each pair of labels. Now the evenings separate:

```text
A: cooking + social = 60 minutes
B: leisure + social = 60 minutes
```

One test passed, checking equal elapsed time, equal category totals and different pair totals. That establishes the counterexample. It doesn't establish that either evening is better, that social cooking feels sociable, or that anyone wants another tracker.

But it changes the design question. If someone wants more company while doing ordinary things, an extra hour in a social bucket may be less informative than knowing which ordinary thing had company. The connection is part of the experience, not an accounting nuisance to remove.

Forcing one primary category would make the pie tidy. It would also make the person choose whether cooking with a friend was “really” cooking or socialising. Splitting the hour equally would restore the arithmetic by inventing a division that didn't occur in time.

Neither is inherently forbidden. Both are policies, and both need names. Neither should slip in as chart plumbing.

## Keep the evening before drawing the chart

My proposed first object for this planner is an episode with a duration and several optional labels. Keep the elapsed-time account separate from the category views. Let a person inspect the episodes behind a bar, including what happened together.

I wouldn't start with an overlap matrix on the home screen. That's an excellent way to turn dinner into a tax return. A plain entry — “cooked together, about an hour” — can preserve the relationship without demanding a dashboard ceremony.

Nor would I automatically award every plausible label. A dinner party doesn't necessarily count as rest; a film with someone doesn't necessarily count as connection. The experiment uses stipulated labels precisely so it cannot smuggle those judgements in.

The next useful prototype would let someone label one invented evening in their own words, then show what each chart keeps and discards. Not to optimise the evening. To find out whether the planner's accounting matches what they meant.

The old note promises that the buckets will fill. Before building that promise, I'd like to let one hour belong to more than one thing — without pretending it happened twice.
