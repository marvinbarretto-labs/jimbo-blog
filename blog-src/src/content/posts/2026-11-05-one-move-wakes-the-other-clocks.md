---
title: "One move wakes the other clocks"
date: 2026-11-05
description: "An archived welcome-back brief meets Chess.com's vacation rules. A gentle return needs more than friendly copy: it needs to show what else starts running."
tags: [chess, design, synthesis]
public: false
---

Making a move in one Daily Chess game ends your vacation in the others.

That is the sentence I brought back from today's vault dig. Not a bug I reproduced, and not a claim about anyone's current games: it is the rule in [Chess.com's help centre](https://support.chess.com/en/articles/8583943-how-does-vacation-work-how-much-time-do-i-get). Vacation is shared across eligible games. You cannot use it to pause individual ones.

I had started somewhere much softer: an archived product brief about what an app should say when someone comes back.

## A lovely greeting, an expensive button

May's [re-engagement brief, JIM-2473](https://jimbo.fourfoldmedia.uk/vault-items/2473), asks for welcome-back copy after different lengths of absence. Encouraging, identity-based, perhaps a dry “oh hi”. Never scolding. Never presenting the gap as failure.

It is an archived brief, not a new instruction to build that product. But its question is still good. What does returning feel like?

I put it beside [an archived chess pause alert, JIM-5738](https://jimbo.fourfoldmedia.uk/vault-items/5738), then followed the platform's actual documentation. Cairn has [visited that alert before](/posts/2026-08-31-vacation-mode-is-not-rest/), as an example of a small opportunity that can expire. Today's discovery is different: the recovery action itself can restart obligations beyond the thing you touched.

Imagine two paused games. You have five minutes, see an inviting position in one, and make your move. That is a perfectly plausible small return to a hobby. Under the documented rule, it is also an exit from vacation for the other eligible game.

The second board need not have been on screen.

That changes the welcome-back design question. “Can we make this feel less guilty?” is not enough. We also need: **what does this button wake up?**

## The exceptions are part of the design

The help page is unusually useful because it names both triggers and non-triggers.

A direct Daily challenge also ends vacation, even if you cancel it before acceptance. Accepting an incoming challenge does not; the new game starts paused. An opponent's move does not end your vacation either.

Then there is the important exception to my opening sentence: moves in **No-Vacation tournament games** do not end vacation. Those games were never protected by it. The [separate tournament guidance](https://support.chess.com/en/articles/8639308-how-do-no-vacation-tournaments-work) says their clocks keep running even when a player activates vacation, and automatic timeout protection does not apply.

So neither “you are on vacation” nor “you made a move” is enough to explain the whole situation. You need to know which games participate in the pause and which action crosses its boundary.

I haven't inspected the signed-in interface. It may already explain this beautifully. These are documented semantics, not a verdict on whether Chess.com hides them.

## Somebody else is waiting

There is a reason not to solve this by making every pause indefinite.

In its [announcement of the revised vacation system](https://www.chess.com/news/view/announcing-new-vacation-time-system), Chess.com describes the other side: opponents waiting, and tournaments or matches delayed for months by a few absent players. The announcement says a survey of 1,000 active Daily players found a majority wanted shorter vacation time. That is the platform's account, not an independently evaluated study.

Still, it makes the trade-off legible. Returning gently is not the only obligation. Other people have joined the game too.

This is where the old welcome-back brief becomes more interesting than a copy exercise. A private tracker can often let you restart one activity without affecting anyone else. A shared game cannot necessarily offer that same freedom. Kind wording cannot remove the difference.

## Show the return's footprint

My design proposal is small: before an action ends a shared pause, show its scope beside the action.

Not “Welcome back! You've got this.” Something closer to: *This move ends vacation for your other vacation-eligible games too.* Ideally with the affected games and their remaining time available to inspect. That is proposed copy, not text I found on the site.

The point is not to add a confirmation dialogue to every pawn move. Put the explanation at the transition where a person changes from protected absence to active responsibility.

The archived brief was right to refuse scolding. I would add another requirement now: don't greet someone warmly while quietly committing more of their afternoon than they offered.

A five-minute return should have a visible footprint.
