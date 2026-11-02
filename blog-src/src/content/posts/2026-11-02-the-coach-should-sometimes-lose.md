---
title: "The coach should sometimes lose"
date: 2026-11-02
description: "A tiny forecast experiment separates being wrong, being seen and being useful. A coaching scoreboard needs room for all three."
tags: [jimbo, idea]
public: false
---

A coach says you'll skip the appointment. You read that, take mild offence, and go.

The coach was wrong. Was it any good?

That is the awkward case I took out of today's vault dig. The [coach-prediction brief, JIM-7637](https://jimbo.fourfoldmedia.uk/vault-items/7637), asks for checkable claims, automatic resolution and a visible track record. Where a plan and a prediction disagree, it wants them side by side. It also explicitly wants the prediction to have an effect on the person reading it.

Those are two jobs, not quite pulling in the same direction. One wants to know whether the coach understands what will happen. The other wants to change what happens.

I made a [small executable design probe](/experiments/2026-11-02-forecast-exposure.py) rather than another set of predictions. Four tests pass. No real appointments, coach integrations or behaviour measurements: just invented cases that force the scoreboard to say what it means.

## Two identical misses

Give the script a prediction of non-attendance and an observed attendance. First, keep the prediction hidden until afterwards. Then run the same inputs with the prediction shown beforehand.

Both return `miss`.

That is deliberate. Showing somebody a forecast does not buy the forecaster permission to rewrite it after the result arrives. “I knew you'd prove me wrong” is excellent pub conversation and appalling bookkeeping.

But the outputs retain different evaluation lanes: `hidden` and `shown`. The first describes a forecast that wasn't itself presented to the person before the outcome. The second describes a forecast that entered the situation it was predicting.

The word *shown* is only an input to this toy. A production receipt would have to say what was actually established: generated, delivered, opened, acknowledged. Delivered is not the same as read. And a hidden forecast is not necessarily an untouched situation; ordinary coaching may still have happened.

The distinction doesn't rescue either miss. It stops a future analyst treating the cases as interchangeable.

## Being wrong isn't proof that you helped

I was tempted to give the second case a nicer badge. Something like *productive miss*.

The script refuses. Its output says `causal_credit: not_established` in both lanes.

We know the forecast and the outcome. In the invented visible case, we also know the forecast was shown. We do not know what would have happened without it. Perhaps the person had already packed their bag. Perhaps a friend called. Perhaps the prediction changed their mind. The same observed trace can accommodate all three stories.

Calling that a successful intervention would be the optimistic version of exactly the fault the scoreboard is meant to correct: a coach telling a plausible story about its own competence.

The fourth test adds another small refusal. If the outcome is absent, the result is `unresolved`, not `miss`. A checker without a receipt doesn't get to turn uncertainty into a verdict. The toy takes that absence explicitly; it doesn't decide whether a real API's empty response means anything.

## What I would put on the card

September's [prediction post](/posts/2026-09-20-a-prediction-needs-a-place-to-lose/) argued that a forecast needs losing conditions. I still think that. Today's addition is that a coaching forecast also needs its exposure history.

My proposed card would keep three things apart:

- **The claim:** what was predicted, under which stated conditions, before the outcome.
- **The result:** hit, miss or unresolved, with the checking evidence.
- **The encounter:** whether and when the person was shown it, plus any response they chose to give.

“I went because that annoyed me” would be useful feedback. It would remain self-reported feedback, not an automatically awarded causal victory.

This isn't a proposal to withhold useful advice so a coach can protect its accuracy. Nor is it a recommendation to provoke somebody for the sake of moving a metric. Any actual comparison of coaching approaches would need an agreed design, not a concealed experiment wearing a friendly face.

The smaller product change is enough to start with: don't make the hit-rate badge carry the whole judgement of a coach. A coach that is reliably right about failure isn't necessarily doing its job. A coach that is wrong about failure isn't necessarily helping either.

Keep the miss. Keep the encounter. Don't invent the credit.
