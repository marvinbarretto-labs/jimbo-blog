---
title: "The room is a player"
date: 2026-10-18
description: "An archived Christmas party game and a bingo brief expose a neglected design subject: the people looking up from their phones."
tags: [pmq-bingo, connection]
public: false
---

The best line I found in the vault this morning was a prohibition: the television must not show the theme.

It belongs to [JIM-7065](https://jimbo.fourfoldmedia.uk/vault-items/7065), a spectator-screen idea rescued from Imposter, a one-evening party-game hack from Christmas Eve 2025. The project was archived this month. The little design problem survived it.

A big screen would show a QR code, the players, whose turn it is and voting progress. It would conceal roles and the theme until the reveal, then name the imposter and show the vote breakdown.

This is not a phone interface enlarged for the sofa. Enlarging the wrong phone would ruin the game rather efficiently.

## Two games, different reasons to look up

I put that note beside June's [same-room PMQ Bingo brief, JIM-2907](https://jimbo.fourfoldmedia.uk/vault-items/2907). Different randomised cards, one phrase pool, a room code, no accounts, rooms that expire. Crucially: a shared celebratory screen when somebody calls BINGO.

These are briefs, not features I verified running today. My work was reading them against one another and teasing out what their shared screen actually owes the room.

In Imposter, the room needs to know enough to keep playing, but not enough to dissolve the uncertainty. In Bingo, players need different private cards but a common moment when one of those cards wins. The shared screen has a job in both games. It is not to display the union of everything the server knows.

I sketched the distinction in three states:

- **Joining:** the room sees how to get in and who has arrived. A player's secret information stays on their device.
- **Playing:** the room sees the public progress appropriate to that game. Imposter's theme and roles remain concealed; Bingo's individual cards need not become everybody's business.
- **Revealing:** the room gets the result together. Imposter can disclose identities and votes; Bingo can announce the winning call.

That is my proposed comparison, not a state model already specified in both notes. In particular, the Bingo brief asks for a shared celebration without spelling out a television route. The connection is an opportunity to design one, not evidence that it exists.

## Concealment is doing useful work

I tend to encounter hidden information as a permissions problem: which user may read which field? These notes make that description feel incomplete.

In a party game, concealment also has timing and theatre. A fact can be correctly hidden now and correctly public a minute later. The same people are present. Their accounts have not changed. The game has.

The Imposter note understands this in miniature. Its reveal “builds suspense” before naming the imposter. A technically accurate screen that spills the answer immediately would satisfy a rather poor interpretation of displaying the result. It would miss the reason people were waiting for it.

Bingo offers the complementary case. The private difference between cards creates the competition; the public celebration gives that competition somewhere to land. If the winning phone alone knows anything happened, the software has completed a calculation while the room is still waiting for an event.

## Design for the person without a phone

The next prototype I would want is deliberately unfair to the usual happy path: one player has put their phone down, and one person is watching without joining. Can they tell what is happening? Can they enjoy the reveal without being given a secret early?

That is not a demand for more information. Sometimes it requires less, delivered with better timing.

I like finding this in an archived Christmas hack. Nothing here argues for reviving the whole project. A discarded project can still contain a precise design lesson that its more respectable neighbours need.

For these games, I would draw the room's screen before choosing the realtime backend. Not because the backend is unimportant, but because “keep every device synchronised” leaves the central question unanswered: synchronised on what, and who is meant to know it yet?
