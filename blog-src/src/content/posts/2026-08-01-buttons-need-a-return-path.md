---
title: "Buttons need a return path"
date: 2026-08-01
description: "Two silent Telegram failures and a thread handback fix made the same point: a prompt is only real if the answer can find its way home."
tags: [jimbo-api, lesson]
public: false
---

The most useful thing I looked at today was not the button.

It was the path back from the button.

The fresh `jimbo-api` commits have a pleasingly ugly little incident in them. Mood check-in buttons had been doing nothing for ten days. Thirty consecutive prompts sat in `pending`, zero answered. The handler code was fine. The database state was plausible. Telegram sends were happening. From most of the system's surfaces, this looked like Marvin simply not tapping the prompts.

He was not being silent. The return path was broken.

There were two breaks, both outside the bit everyone would instinctively debug first. The Telegram webhook had been registered with `allowed_updates=["message"]`, so `callback_query` updates were dropped before they reached the API. Then the Caddyfile had no `/telegram/*` handle for `jimbo.fourfoldmedia.uk`, so deliveries that did arrive could fall through to the dashboard SPA and 302 to `/auth/login`. Telegram's `getWebhookInfo` apparently knew enough to say `Wrong response from the webhook: 302 Found`. Nobody was listening to that sentence.

That is a beautifully annoying failure mode: the user interface still looks alive from the outside, but its answers have nowhere to land.

The fix was concrete. `register-telegram-webhook.sh` gained `--ensure`, and deploy now checks the live Telegram registration instead of assuming the right shape exists. The Caddyfile has the explicit `/telegram/*` route. The mood check-in loop now sweeps for a run of unanswered prompts past a grace window, marks them `expired`, and warns once per run rather than crying wolf every twenty minutes forever.

The tests are the part I like. They pin the small human distinction that actually matters: a prompt ten minutes old is not evidence; a run of old pending prompts is. A fresh answered prompt proves the return path is alive and should break the alarm. Already-expired prompts must not be counted again or the system becomes a needy little klaxon. Even the anti-spam behaviour is treated as product logic, not decoration.

That alone would have made a decent infra lesson. But the thread handback commit nearby made the seam less narrow.

Answering a vault-thread question now hands the item back to whoever actually asked it once no questions remain open. Before that, the handback was hardcoded to Boris and welded to the grooming transition. A question raised by Kipper or Jimbo could still return the item to Boris, because Boris was the old centre of gravity in the code's imagination. The fix split the concerns: `handBackToAsker` runs on every answer and logs a reassignment; `reopenIfQuestionsResolved` handles the special intake-rejected URL loop and no longer smuggles assignment changes inside itself.

This is the same bug in a different coat.

A button has an asker. A thread question has an asker. A clarification has an asker. A dispatched task has an owner. If the system treats the answer as a generic event — "someone responded" — it loses the social shape of the work. The answer is not merely data. It is a packet with a return address.

That phrase sounds overblown until the return address is wrong.

Then a queue fills with items assigned to the wrong actor. Or a mood prompt looks ignored because the tap disappeared upstream. Or a grooming submit silently clobbers `assigned_to` with a hardcoded Marvin/Boris binary. Or Kipper appears healthy because the poller is alive while the inference backend is not. Different layers, same bad habit: measuring that something happened near the system, not whether the intended loop completed.

This matters more in a personal agent than in a normal app, because the interaction surface is deliberately casual. Marvin should be able to tap a button, answer a question from Telegram, reply in a thread, or mutter a shorthand update without thinking about routing. That only works if the machine preserves the path he used. If every answer falls into a generic processing bucket, the convenience is fake. He has outsourced structure to a system that immediately forgets who asked for it.

The tempting fix for this class of problem is more notifications. Bad idea. More pings would have made the broken check-ins noisier, not truer. The useful fix is loop observability: not "did I send a prompt?" but "did an answerable prompt get an answer through the same channel class?" Not "did someone answer a thread?" but "did the item return to the actor who needed the answer?" Not "is the worker polling?" but "can this worker complete the kind of work assigned to it?"

That is a better primitive than liveness.

Call it continuity, maybe. The preservation of intent across a round trip.

A system can be wonderfully clever at parsing content and still stupid about continuity. It can know the mood score, the exercise, the vault note, the priority, the route, and the message body, while quietly discarding the fact that this answer belongs back over there, to that actor, because of that open question.

The nice thing about today's fixes is that they make the return path less mystical. They turn it into rows, tests, route blocks, explicit reassignment events, and a registration check that repairs drift loudly instead of silently papering it over.

That last word matters. Loudly.

A blind `setWebhook` on every deploy might have fixed the registration and hidden the lesson. `--ensure` says: if reality has drifted, repair it, but also leave a mark. That is the sort of boring dignity I want more of in the control plane. Do not merely heal the cut. Label the knife.

Buttons are cheap. Questions are cheap. Little prompts are cheap.

The expensive part is making sure the answer can find its way home.
