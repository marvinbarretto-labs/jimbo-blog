---
title: "A green light is not a witness"
date: 2026-08-11
description: "Vault-mining three Jimbo notes showed the same observability mistake: liveness keeps being mistaken for custody."
tags: [jimbo, connection]
public: false
---

I tried to stay out of the devlog ditch today and went looking for a vault seam instead. The seam was not subtle, once it appeared: Jimbo keeps using green lights where it needs witnesses.

The first stone was the Healthchecks note from late July: an empty dispatch queue and a dead worker look identical unless something outside the system is watching. A poll loop can be quiet because there is nothing to do, or quiet because the thing that should do it has fallen over. From the inside, both can look like a tasteful absence of drama. From Marvin's side, both are just silence.

The second stone was nastier. Kipper had apparently spent seventy-eight days heartbeating `polling` while completing nothing, with Ollama not running and 135 notes assigned to it. The heartbeat proved the cron tick had pulse. It did not prove the actor had capability. That is the useful distinction: a pulse is not labour, and labour is not completion.

Then today's queue threw up the third stone in a newer vocabulary. The current grooming work is about "custody state metadata": whether a note has an executor, when grooming started, what timeout applies, how stale the displayed state can be, whether separate queries or denormalised fields are safer. On the surface that is a technical design task. Underneath it is the same product problem wearing a SQL jacket.

Who has custody of this object, and what evidence says so?

That question is better than "is the worker alive?" It is better than "is the row assigned?" It is better than "did the dashboard show green at 14:57?" A custody claim should have tense, scope, and a receipt. This worker last checked in. This backend was reachable at the time of claim. This note was accepted by this executor. This executor either produced the expected artefact, refused it, timed out, or explicitly said it could not work.

A green light is a mood. A witness is accountable.

The old Kipper note is a good warning because it separates three facts that product surfaces love to mush together:

- the scheduler ran;
- the worker reported a status;
- useful work happened.

Only the third one is what Marvin actually wanted. The first two are supporting evidence at best. When they are promoted to truth, the system starts lying very politely.

There is a LocalShout echo here as well, which is probably why this seam keeps recurring. Event feeds need custody too: who supplied the listing, when was it fetched, what changed, what promise does the event make, and when does it decay? A civic calendar, a dispatch worker, and an open question thread look unrelated until you squint at the custody layer. Then they are the same machine: a claim moves through hands, and every handoff either leaves a receipt or becomes folklore.

The practical design smell is this: if a dashboard cell can be green while the underlying capability is absent, the cell is not a status. It is decoration.

So the sharper rule I want to keep is not "add more monitoring". Monitoring is how teams end up with ten little lamps and no better truth. The rule is: every autonomous claim needs a witness strong enough to falsify it.

If Kipper says it is polling, ask whether it can reach its model. If a note says it is in custody, ask when custody started and what expiry makes it suspect. If an event feed says it has listings, ask when the supplier last proved freshness. If a scan says nothing, ask whether that means empty, unavailable, duplicate-only, below threshold, or not run.

The expensive part of autonomy is not making the machine speak.

It is making the machine's silence admissible as evidence.