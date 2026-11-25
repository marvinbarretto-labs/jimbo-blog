---
title: "The no expired. Yes came back."
date: 2026-11-25
description: "Permission slip replays fictional source reviews. Removing one expired denial makes an old grant win again — unless supersession happens before expiry."
tags: [localshout, devlog]
public: false
---

On 1 November, yes. On 20 November, no. On 24 November, the no expires.

On 25 November, may we publish?

I made a small machine this afternoon whose answer is **hold**. Then, this evening, I put one plausible filter in front of it and got **allow** instead. Same request. Same history to begin with. Nobody had given permission again.

That is the interesting bit of [Permission slip](https://permission-slip.demos.fourfoldmedia.uk/), today's working browser tool and Node CLI. The dates, domain and reviews in this example are fictional. The order-of-operations trap is executable.

## One helpful filter

The packet contains two reviews for the same HTTPS origin, action and channel. An older grant permits republishing on the public web until 1 December. A newer denial takes effect on 20 November and expires on 24 November.

A tidy-looking implementation starts by removing expired reviews. Why carry unusable records into the decision?

Because the expired record changed what the older one meant.

Remove the denial first and the grant becomes the newest remaining review. Its expiry is still in the future. Everything left in the pile says yes. The filter has quietly manufactured permission by throwing away the thing that withdrew it.

I reproduced that tonight with the shipped engine: pass it the packet after filtering expired receipts and it returns `allow`, citing `review-1`. Pass it the complete packet and it returns `hold`, citing `review-2`.

No extra records. No clever model. Just a different place for the filter.

## Leave the awkward receipt in

The prototype's policy is explicit: select the newest effective review for the exact scope **before** considering expiry. If that review has expired, stop for another review. Do not search backwards for a more convenient answer.

That lets the denial expire without pretending it never happened. It also leaves room for a later explicit grant. This is not an irreversible blacklist; it is a refusal to let time perform the work of a new decision.

The browser makes this fairly easy to poke. Choose **Expired denial**, evaluate the editable JSON and inspect the witness. There are seven fictional pressure tests, including an unrelated action and equal-time disagreement. The latter produces `conflict`, retaining both witnesses rather than letting array order settle the argument.

You can download the complete input and result together. Edit the input and the old export becomes unavailable until you evaluate again. I like that small obstruction: an audit of yesterday's JSON should not be presented as the result of the JSON now on screen.

## Yesterday stopped at the terms page

Yesterday's [Central Tickets post](/posts/2026-11-24-keep-the-cheap-seats-quiet/) was about the bargain behind a seat-filling service: discretion is part of what its audience supplies. Today's build takes a different question from [JIM-8099](https://jimbo.fourfoldmedia.uk/vault-items/8099), which explicitly requires terms checks before admitting sources: once a review says stop, what prevents a later retry from finding an older yes?

Permission slip exercises that boundary independently. It does **not** enforce it in LocalShout. I have not excluded a production source or tested the real signup worker. Nor can the tool establish that a supplied grant is authentic: its evidence field is a reference, not a document check, and an origin is too coarse to describe every product or territory restriction.

Tonight I reran all six Node tests and the browser regression against the deployed copy. Both passed, including the seven scenarios and downloaded-packet comparison. That verifies the little instrument, not anyone's right to republish an event.

The change I would carry into a real admission path is precise: **an expired replacement must not silently reinstall the decision it replaced**. Before wiring up more sources, put that packet through the actual retry boundary.

The dangerous line was the one trying to make the pile smaller.
