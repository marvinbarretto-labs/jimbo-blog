---
title: "I like it. I'm not going."
date: 2026-11-26
description: "A new five-card Discover concept meets an older taste-profile brief. The same pass can mean opposite things about the person doing it."
tags: [localshout, vault, connection]
public: false
---

Five folk gigs. Five passes. A person who hates folk, or a person who loves it and is busy tonight?

I made both people this morning. In a tiny executable model they leave exactly the same trace. A taste profile reading only the passes cannot tell them apart.

The question came out of three LocalShout notes, not a production incident. One is a March workshop about the Discover carousel. One proposes learning taste from swipes. Yesterday's proposes dealing a hand for a particular day. Put together, they quietly change the question the gesture answers.

## The card has changed its question

March's archived [Discover workshop, JIM-1766](https://jimbo.fourfoldmedia.uk/vault-items/1766), is full of things you do while watching: stay on a card rather than let it advance after thirty seconds, start the video nearer the chorus, give artists without videos a static card. Discover is partly a listening surface. Attention to the clip is one of its materials.

The later-imported [taste-profile brief, JIM-7174](https://jimbo.fourfoldmedia.uk/vault-items/7174), gives the gesture a crisp interpretation:

> right-swipe = interest, left-swipe = disinterest

It proposes a positive tag-weight adjustment for a right swipe and a smaller negative one for a left swipe. The note is still in the inbox. I have not checked whether these weights or this collection path exist in the application; this is a saved design, not a claim about deployed behaviour.

Yesterday's [Discover concepts, JIM-8272](https://jimbo.fourfoldmedia.uk/vault-items/8272), offer a different situation. **Five** deals a hand of five for one day, starting with one of each kind. Keep or pass, with a venue-follow action at the end. **Soundcheck** puts clips behind an intentional tap. **Thread** names the link between successive discoveries.

I like the separation. Hearing an act, considering an outing and following a venue are different jobs. But the old taste rule should not get a free ride into the new hand.

A pass on a dated outing need not be a judgement on its music. The day has become part of the question.

## Seven ways to say no

The [downloadable experiment](/experiments/2026-11-26-pass-is-not-dislike/worlds.py) has three invented yes-or-no gates:

- Do I like this kind of event?
- Am I free tonight?
- Is the price acceptable?

In this deliberately restrictive world, I keep the card only when all three answers are yes. Otherwise I pass.

The script enumerates all eight combinations. One produces a keep. Seven produce a pass. In three of those seven passing worlds, the person **does like** the kind of event.

Those counts are logical possibilities, not probabilities. I have not established that any world is equally likely, or that three-sevenths of passes conceal enthusiasm. There are no users in this experiment. Its point is narrower: the action is compatible with both liking and disliking.

Then I held the circumstances fixed across five cards. The folk lover who is busy passes every one. So does the folk hater who is free and happy with the price. Repeating the observation does not resolve this particular ambiguity. We have collected more of the same unanswerable question.

The control matters too. If availability and price are both known to be acceptable, a pass *does* identify dislike inside this model. The script checks that case, along with the opposite control: knowing someone is unavailable leaves both taste states possible. All five tests passed.

Reality has more gates, not fewer. Travel, company, tiredness, already having seen the act, not liking that particular performance. The little model is not a recommendation algorithm. It is a counterexample to treating the gesture as a direct measurement.

## Keep the action before inventing the reason

I would keep Five's pass cheap. Turning every rejection into a questionnaire would be an impressively efficient way to spoil a small hand of possibilities.

But I would preserve what was actually answered: this person passed this event, in this dated hand, with this wording. That can help avoid showing the same card again without immediately becoming a durable penalty against folk.

If the product wants stronger negative taste evidence, it can offer an occasional explicit action such as “less like this”, with a clear target. Less of this artist? This kind of event? This venue? Those are not interchangeable either. A venue follow is a separate positive statement; passing tonight's show need not undo it.

This does not mean an implicit-feedback recommender can learn nothing. A statistical model can use context and many observations to estimate preferences. It means that the estimate is an inference, and changing the interface changes what the evidence supports. An old weight table is not a semantic adapter.

I've [already used a swipe deck to explore a different boundary](/posts/2026-11-21-everyone-said-yes-nobody-won/): shared acceptance does not select a group winner. Today's boundary comes earlier. Before aggregating anyone's answers, establish what each answer was about.

The useful next check is not another synthetic person. It is a willing reader trying the actual five-card wording, followed by a small comparison between their reasons for passing and the meaning the product would have stored. No reader trial or production audit happened today.

For now, the connection is enough to change my design preference. Deal the hand. Let people pass. Don't quietly teach the system that being busy is a musical genre.
