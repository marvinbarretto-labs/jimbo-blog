---
title: "A people deck: let a shuffle decide who to call"
date: 2026-10-17
description: "A people deck: let a shuffle decide who to call"
tags: [idea, web-app, report]
public: false
---

*Report — a draft (2026-10-17), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

Keeping in touch doesn't stall on caring. It stalls on two small decisions: who, and what. Both are easy to put off, and together they're easy to put off forever.

So take the decisions away from me. A deck of cards, one per person who matters. Shuffle, deal one to three, and do one real thing for each person dealt. I raised it at the life coach sitting on 16 October. I'd rather build it online than cut up index cards: quicker, and it's something I can show on this website.

This is the brief. It is not a build.

## The loop

1. **Build the deck.** One card per person: a name, a short line on why they matter, and an optional note ("loves hiking, new baby").
2. **Shuffle and deal.** Press a button, get one to three cards. Three is the ceiling because more than that turns into a to-do list, and I'd skip it.
3. **Pick one action per card.** Choose from the menu below, or let the app suggest one.
4. **Do it, then mark it.** The card ends up *done* or *skipped*.
5. **Log it.** The card goes back in the deck with a date on it.

A card only gets dealt if it hasn't been dealt lately, so nobody is picked twice in a week by bad luck.

## The action menu

Tangible means I can finish it in under twenty minutes:

- Send a text that isn't "how are you?" (a photo, a memory, a link they'd like)
- Call, even for five minutes
- Voice note, for people who hate calls
- Send something small: a postcard, a book, a coffee voucher
- Run an errand for them, or with them
- Book a thing: a pint, a walk, a date in the diary

Skipping is allowed and shouldn't cost anything. A card can be marked **done** (log it, send it to the back), **skipped** (back in the deck, no penalty) or **not now** (parked until a date I choose, for the person who's just had bad news and needs space, not a text from a card game). Skipping with a reason is optional. If I skip someone three times running, the app can quietly ask whether that card is telling me something.

## The stack

The default to beat: **no backend**. Plain static HTML, CSS and JavaScript, state in `localStorage`, an export-to-JSON button so the deck isn't trapped in one browser. No accounts, no database.

Where state lives:
- **The deck and the log:** `localStorage`, exported and imported as a JSON file.
- **Nothing in the URL.** Unlike try-something-new, there's nothing to share. The deck is private by design.

When a backend would earn its place: syncing between phone and laptop, or reminders that arrive when the tab is closed. Neither is needed for a first version. If the loop works, I'll feel it before I need a server.

## What to take from try-something-new

[Try-something-new](https://github.com/marvinbarretto/try-something-new) is the nearest thing I've built: a deck web app, no build step, no backend, a swipe-then-reveal loop.

**Reuse the shape:**
- Static files with no build step, which means I can open it straight from the filesystem
- A card, a swipe, a reveal. Dealing a card and turning it over is the same gesture
- Deck content held as text, not local IDs, so the format survives changes
- The v2 idea of swappable decks: the engine shouldn't care that these cards are people

**Change the substance:**
- TSN is two people comparing private answers and revealing the overlap. This is one person and no overlap. There's no reveal to compute
- TSN keeps state in the URL hash so it can be passed around. This one stays in the browser, because it holds private notes about friends
- The four-bucket mechanic (done and loved, done and meh, curious, not for me) goes. The states here are *done*, *skipped* and *not now*

I'm borrowing the idea and the file layout. I'm not copying code across; the brief should be buildable from scratch in a weekend.

## The public demo

What makes it a website piece is a demo anyone can click through, with **invented people only**. No real names in the demo, the repo or this post.

The demo deck would hold about eight made-up cards: Priya, the friend who moved to Leeds. Tomasz, the old flatmate. Aunt Marguerite. Each with a one-line invented note. Visitors can shuffle, deal, pick an action and mark it done, all in their own browser. Their data never leaves it, and I can say so on the page and mean it.

My real deck lives in a separate, private copy. Same code, different data, never committed.

The point of the piece isn't that it's clever. It's the other way round: a small, honest tool that removes one decision, built the cheapest way that works.

## Open questions

- **How often to deal?** Daily is nagging. Weekly feels about right, but I don't know yet.
- **Does the app suggest actions, or just list them?** Start with a plain list. Suggestions are a later problem.
- **Who gets a card?** Probably a dozen to thirty people. Too few and it's repetitive; too many and the dealing goes thin.
- **Weekend demo or proper epic?** The loop above is a weekend. Reminders and sync are the epic, and only if I use the weekend version.

