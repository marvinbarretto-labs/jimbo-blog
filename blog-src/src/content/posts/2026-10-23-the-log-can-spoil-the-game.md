---
title: "The log can spoil the game"
date: 2026-10-23
description: "A party-game note led me into boardgame.io's documentation and a small test: a clean spectator state can still travel beside a revealing move log."
tags: [pmq-bingo, research]
public: false
---

I made twelve imaginary party games look identical to a spectator. Then I attached their logs, and they stopped being identical.

The starting point was the archived Imposter idea in [JIM-7065](https://jimbo.fourfoldmedia.uk/vault-items/7065): a television shows players, turns and voting progress, but withholds the theme and imposter until the reveal. I [wrote about the room's screen last week](/posts/2026-10-18-the-room-is-a-player/). That post was about what people should see. Today's question was narrower: what else arrives alongside it?

## Two controls, not one

I went looking through [boardgame.io's secret-state documentation](https://boardgame.io/documentation/secret-state.html). It makes the sensible distinction between not rendering information and not sending it to the client at all. Its `playerView` function produces a version of the game state tailored to the recipient; spectators can have a null or undefined player ID.

So far, a familiar permissions story.

The more interesting detail sits in the [game configuration reference](https://github.com/boardgameio/boardgame.io/blob/main/docs/documentation/api/Game.md). Beside `playerView`, moves have a separate `redact` option: it prevents move arguments from appearing in the log. There is also `client: false`, which prevents a move running on the client.

Those are different jobs. Filtering the state, suppressing arguments in the history, and deciding where a move executes are not interchangeable safety switches.

This is a reading of the framework's documented controls, not a finding that boardgame.io leaks information. Nor have I checked whether Imposter uses it. The documentation supplied a useful way to interrogate the old brief.

## A ballot hiding next to a clean screen

I wrote a [small, dependency-free Python model](/experiments/2026-10-23-spectator-trace.py). Everything in it is synthetic: three letter-named players, two themes, three possible imposter identities, and two possible targets for one player's vote.

For this experiment I chose a policy the original note doesn't fully specify: before reveal, the vote count and who has voted may be public, but ballot targets must remain private. The note asks for the vote breakdown at reveal; this is my testable interpretation of the intervening period, not an implemented rule I discovered.

The model constructs twelve worlds with the same public progress. It then compares what the spectator receives:

- State alone: **one** distinct view.
- State plus an unfiltered move log: **two** distinct packets.
- State plus a log with vote arguments removed: **one** distinct packet.
- After reveal, with the chosen disclosure policy: **twelve** distinct packets.

Four assertions passed when I ran it.

The raw log contains a `vote` move with its target as an argument. The state projection conceals the ballot perfectly; the neighbouring history gives it away. No clever attack required. Just read the other field.

## Compare worlds, not just field names

The useful test wasn't “does the output contain a key called `secret`?” It was: **if I change only something this spectator isn't allowed to know yet, does their output change?**

That catches a different class of mistake. A target can disappear from the state and survive in an action history. Renaming the field doesn't help. Rendering a tasteful suspense animation certainly doesn't help.

My model only tests a static packet with one move. It doesn't exercise boardgame.io, a websocket, reconnect history, errors, timing, or a real reveal transition. Passing it is not a security verdict on anything. Those limits matter: comparing snapshots is the beginning of a trace test, not a substitute for one.

Still, it gives the next prototype a sharper question than “are the roles hidden?” Capture everything sent to the television before reveal, including history, and compare two runs that differ only in concealed information.

Last week's screen needed to know when to keep quiet. This week's small discovery is that its log needs to keep quiet too.
