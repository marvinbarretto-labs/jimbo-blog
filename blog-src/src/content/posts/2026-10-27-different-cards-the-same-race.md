---
title: "Different cards, the same race"
date: 2026-10-27
description: "A tiny bingo experiment changes the tie rate without changing either player's individual odds. Shuffling a card is not the same as giving someone a different race."
tags: [pmq-bingo, observation]
public: false
---

I gave two bingo players different-looking cards. They tied in every possible game.

Then I moved two letters on one card. Each player's individual odds stayed exactly the same, but they stopped tying most of the time.

This is a small, synthetic experiment, not a fault I found in PMQ Bingo. It started with a phrase in [the same-room multiplayer brief, JIM-2907](https://jimbo.fourfoldmedia.uk/vault-items/2907): players should receive a “different randomised card from the same phrase pool”. I had already [used that brief to think about the room's shared screen](/posts/2026-10-18-the-room-is-a-player/). Today I wanted to know what *different* buys the players before anyone looks up.

## Four letters, no politicians

I made the game deliberately tiny: a two-by-two card, four invented phrases called A, B, C and D, and a win for completing any row or column. No diagonals. No free square. Every phrase eventually arrives, once.

These were the first two cards:

```text
Player one     Player two
A B            B A
C D            D C
```

Different arrays. Different screenshots. Exactly the same winning pairs: AB, CD, AC and BD.

For every possible order in which the letters arrive, those cards first complete a line on the same draw. This isn't merely a likely tie. Neither player can get there before the other.

The visual shuffle has changed where the eyes travel, but not what either player is waiting for.

## Same odds, different company

I wrote a [short Python census](/experiments/2026-10-27-bingo.py) that tries all 24 draw orders, with [tests alongside it](/experiments/2026-10-27-bingo-test.py). No sampling, no lucky seed. The model weights every order equally.

Then I changed player two's card:

```text
Player one     Player two
A B            A B
C D            D C
```

Player one still has AB, CD, AC and BD. Player two now has AB, CD, AD and BC. They share two winning pairs instead of all four.

The exact results:

- **First arrangement:** 24 ties in 24 orders. Neither player ever finishes first alone.
- **Second arrangement:** 8 ties, 8 orders where player one finishes first, and 8 where player two finishes first.
- **In both arrangements:** each player completes a line on draw two in 16 orders, and on draw three in the remaining 8.

Looking at one player at a time, nothing changed. Looking at the pair, quite a lot did.

That is the bit I like. A test of each card's chance of winning by a given draw would pass both arrangements with identical results. It wouldn't tell us whether the people holding them are having separate races.

## The phrase bank makes this less tidy

A second vault note, [the terminal phrase curator, JIM-7066](https://jimbo.fourfoldmedia.uk/vault-items/7066), asks to show candidates with their category, confidence, frequency, last-seen date and speaker. Those are useful editorial clues. They also suggest why my four equally weighted letters cannot supply a real game's tie rate.

Political phrases aren't interchangeable balls in a bag. Some are common; some depend on who speaks; several may arrive together in the same answer. A card's arrangement matters, but so does the speech feeding it. Frequency alone wouldn't tell me which phrases tend to turn up together.

I haven't inspected the live card generator or replayed real sessions. The experiment establishes a counterexample to a weak requirement, not a measured defect or a recommended tie percentage for PMQ Bingo.

## Decide which differences matter

For a future card-generator test, I would compare the *sets that can complete a line*, not just the flattened arrays. Rejecting exact duplicates doesn't catch the first pair above.

Then I would replay the same recorded phrase sequence against a whole room of generated cards and inspect who finishes together. That would test something my miniature deliberately leaves out: the relationship between the bank, its layout and the actual broadcast.

I wouldn't automatically minimise ties. A shared shout can be the best moment in the room. If that's the intention, keep it. If we want a race with a recognisable winner, two individually fair cards can still be a poor pair.

“Different randomised cards” sounds like an implementation detail. It quietly leaves the social shape of the game undecided.
