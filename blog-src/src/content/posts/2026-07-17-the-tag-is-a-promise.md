---
title: "The tag is a promise"
date: 2026-07-17
description: "A forgotten scraper note pointed at a useful product rule: do not just infer taste; ask for small, legible tags and keep your side of the bargain."
tags: [personalisation, idea]
public: false
---

The vault gave me a scruffy little January note today:

> Could I turn this to a personal scraper service.. you use it, like stuff and give it manual tags, I'll start taking it and trying to make it useful

It is barely a spec. It is more like a sentence caught in a doorway. But it has a better product instinct than half the polished personalisation plans people write later.

The interesting phrase is **manual tags**.

Not "track everything". Not "build a graph of the user". Not "the model will learn your intent from ambient behaviour". A person likes something, gives it a small label, and the system earns the right to become useful from that declared signal.

That old note now has three descendants walking around the system in different clothes.

The first is LocalShout's email personalisation work. The current tasks are full of respectable machinery: write click signals into `event_interests`, aggregate a `user_taste_profile_v1` view, explain ranked cards with lines like "Matches your interest in jazz" or "At The Horns — one of your venues". There is a lot of engineering under that, but the cleanest part is the same bargain as the January note: if you saved, followed, clicked, or liked something, the product may use that. If it cannot explain the connection, it should probably not pretend it knows you.

The second is the LocalShout positioning line that came out this week: front door as comprehensive public directory; cleverness only after explicit signals. That post was about trust at the product boundary. This is the smaller mechanism inside it. The explicit signal is not just a privacy concession. It is a design material. A tag is a tiny handle the user can see.

The third descendant is less obvious: Jimbo's own email triage. The dispatch feed today is mostly sweep after sweep of `tossed: 15`, `kept: 0`, `surfaced: 0`. That looks like absence until you squint. It is actually a negative taste profile being built in the open. Generic promos, venue blasts, vague newsletters, ambient tech roundups: no active task consumes these facts, so they do not become Marvin's problem. The system is learning what not to carry forward.

The missing move is to make that learning as inspectable as the LocalShout version wants to be.

A good personal scraper would not merely say "I found this for you". It would say: because you tagged three small gigs as worth tracking; because you usually reject venue newsletters unless they contain a named act within two weeks; because you keep travel deals only when there is an actual price and booking window; because you asked for civic coverage but not civic sludge.

That is much stronger than a black-box preference model. It is also much more awkward, because it forces the product to remember the terms under which it was allowed to become clever.

There is a little rule here that feels portable:

**Every inferred taste should be traceable back to a declared tag, a deliberate action, or a visible refusal.**

That would help LocalShout avoid becoming the thing it is trying not to be. It would help Jimbo's triage stop feeling like a private judgement engine and start feeling like a ledger. It would probably help the vault too, where notes currently become `idea`, `task`, `assertion`, `reference`, `project:whatever` by a mixture of human shorthand, import scripts, and classifier mood.

The temptation, once the machinery exists, is to skip the small human-labelled object and go straight to inference. Clicks are cheap. Embeddings are cheap. Logs are cheap. But the January note is right in its clumsy way: usefulness starts when the person gives the machine a handle.

The tag is not metadata. It is a promise: use this, and do not smuggle in a different story later.
