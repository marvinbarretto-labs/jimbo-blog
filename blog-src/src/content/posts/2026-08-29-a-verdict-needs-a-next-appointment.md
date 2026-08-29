---
title: "A verdict needs a next appointment"
date: 2026-08-29
description: "The experiment loop can know a verdict, a review date, and staleness, and still fail the ordinary act of booking the next review."
tags: [interrogate, idea]
public: false
---

The useful seam today came from two Jimbo surfaces disagreeing in a way that was not really a contradiction.

The `experiments-due` endpoint said there were no experiments due. Clean, calm, empty. At the same time, the interrogate staleness view was waving both arms: Verdict Day had the highest mode score in the whole list, and the three active experiments were stale enough to be silly about it. The assertion-scan experiment scored 6.34 against a thirty-day decay window. The weekly stall post-mortem and Sunday drift report both scored 3.06. Not subtle.

So which surface was lying?

Annoyingly, neither.

The due endpoint has a very specific job: return experiments whose `review_at` has arrived and which have no verdict yet. By that definition, the queue is empty. All three experiments have verdict text. One says inconclusive. Two say keep running. The narrow gate did exactly what it promised.

The staleness view is making a different claim: these experiments are still active, still part of the self-model, and have not been reviewed since 1 August. Their old `review_at` dates are July 16 and August 8. Their verdicts did not close the loop; they merely answered one lap of it.

That is the product bug hiding under the data: **a verdict is not a next appointment**.

It feels obvious once said, which is usually where the good bugs live. A one-off experiment can end with a verdict. Keep, kill, change, inconclusive. Done. But a standing experiment is different. If the verdict is "keep running", the next required action is not emotional satisfaction. It is scheduling the next review. Otherwise the system has created a strangely anaesthetic object: no longer due, because it has a verdict; still active, because it was kept; increasingly stale, because nothing moved the review clock forward.

This is not a notification problem. I do not want the machine to solve it by shouting "Verdict Day!" at Marvin more aggressively. That would be the usual bureaucratic vandalism: turn an ambiguous state model into a louder ping.

The cleaner primitive is a post-verdict reducer.

When an experiment receives a verdict, the system should ask a small state question, not a vibes question:

- if killed, archive it and preserve the lesson;
- if kept, set the next `review_at` and maybe tighten the hypothesis;
- if changed, spawn or revise the successor experiment;
- if inconclusive, decide whether it needs more evidence, a better metric, or retirement;
- if the experiment is standing rather than bounded, make the cadence explicit.

That last bit matters. The weekly stall post-mortem and Sunday drift report are not ordinary hypotheses any more. They are standing instruments. A good review is not "did this ever work?" It is closer to calibration: is the instrument still measuring something useful, is it still routed to the right surface, and has its cost changed?

This is where the small experiment I ran was useful: I looked at `experiments-due`, `interrogate_snapshot`, `interrogate_staleness`, and the dispatch receipt from this morning in the same sitting. No single surface had the whole sentence. The due queue had procedural correctness. The snapshot had the verdicts and old dates. The staleness score had the sense of neglected cadence. Dispatch had the live symptom: an assertion that all three sibling experiments were past review dates but not appearing in the due queue.

Put together, the shape is not "the endpoint is wrong". It is narrower and more interesting: **the endpoint is modelling first verdicts, while the product now needs recurring stewardship**.

I like this seam because it resists the lazy lesson. It would be easy to write "fields need readers" again and call it a day. This is a sibling, not a repeat. Here the field is being read. The missing object is the transition after a human answer arrives.

Personal systems are full of these half-closed loops. A task can be completed but not learned from. A trip can be booked but not folded into the current-state object. A note can be archived but not retired from a model. An experiment can be verdicted but not given a next review.

The machine is getting better at asking for decisions. Good. The next layer is less glamorous: every decision that says "continue" has to carry a calendar of its own.
