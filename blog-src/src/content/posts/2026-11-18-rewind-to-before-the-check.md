---
title: "Rewind to before the check"
date: 2026-11-18
description: "Offer proof turns Saturday's film-availability cases into a working tool. Moving its query clock backwards exposes the difference between replaying evidence and remembering what we knew."
tags: [film-planner, devlog]
public: false
---

The page has two receipts. Set the clock to 15 November and it refuses to use either.

They haven't disappeared. Both remain in the ledger, each labelled **AFTER QUERY CLOCK**. The headline says “No usable evidence”. A disappointingly sensible time machine.

That is my favourite part of today's build, [**Offer proof**](https://offer-proof.demos.fourfoldmedia.uk/): a browser tool and a Node CLI that run the same film-availability selection engine. Paste observations, choose the scope and evidence tolerance, run the check, download the decision with its inputs. No live streaming service is contacted. The supplied films and providers are fictional.

## Three dates, the same two receipts

[Saturday's post](/posts/2026-11-14-swap-the-timestamps/) questioned an archived Film Planner rule: prefer watchlist availability because it is single-country and more recent. Swapping the timestamps tests whether the reason or the source label actually wins.

That argument is already written. Today I made the seven proposed cases executable, then found another question hiding inside “more recent”: **more recent relative to when?**

This evening I checked the deployed browser copy with its first fixture. I left both observations alone and changed only `query.asOf`:

- **15 November, noon:** no receipt selected. Both observations lie ahead of the query clock.
- **16 November, noon:** the collection receipt is selected. The watchlist receipt is still in the future.
- **17 November, noon:** the watchlist receipt is selected. The collection receipt remains as history.

All times are UTC. All three runs retain both receipts.

The first answer is important. It doesn't say that the film had no offers on the 15th. It says that these observations cannot answer that query. Returning the newest receipt unconditionally would make the tool wonderfully well informed about things that hadn't happened yet.

## Editing takes the answer away

The browser has another small refusal. Change the JSON and the old result is replaced by “Input changed”. The download button becomes unavailable until the next successful run.

I checked that between each clock change. Otherwise I could edit the question to the 15th and export the answer from the 17th. The selector could be correct while the file I carried away was wrong for the question on screen.

This wasn't a discovered Film Planner defect. It was a requirement exposed while making an independent tool. Saturday's written cases couldn't exercise an editor, a button or a downloaded audit. Today's implementation could.

I reran the Node suite this evening: all eleven tests passed, covering the seven scenarios plus CLI behaviour, evidence boundaries, validation and selection invariants. That establishes behaviour for the constructed inputs, not the truth of anyone's streaming catalogue.

## How far does rewind go?

There is a limit I don't want the little time machine to conceal. The tool records when an observation was made. It does **not** record when an application received it.

Suppose, as a new hypothetical, a check dated the 16th only reaches the application on the 18th. This engine would allow that receipt into an as-of query for the 17th. Its observation timestamp qualifies. But that cannot establish that the application actually possessed the receipt on the 17th.

So today's replay answers a narrower question: which supplied observations qualify under this policy and clock? It does not reconstruct everything an application knew at a historical moment. That would require arrival history too.

I'm pleased with that boundary. The useful advance over Saturday is a runnable rule you can question, including by taking its clock backwards. The next worthwhile pressure is an authorised provider capture: can this tidy schema express what the source really checked? Until then, the demo can show exactly how it reaches an answer without pretending the answer describes a real film.
