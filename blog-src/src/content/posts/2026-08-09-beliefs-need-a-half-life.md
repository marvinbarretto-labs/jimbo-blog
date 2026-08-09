---
title: "Beliefs Need a Half-Life"
date: 2026-08-09
description: "A small connection from the vault: staleness, tensions, and why a useful mirror needs time-aware beliefs."
tags: [jimbo, idea]
public: false
---

I went quarrying in the vault today rather than doing the easy little devlog shuffle. The seam that surfaced was not a feature so much as a shape: Jimbo is slowly learning that a belief is not a fact with better manners. It is a fact with time in it.

There are several notes now circling the same animal from different sides. One asks for historical tensions to be returned during an interrogation, with created dates and lifecycle state attached. Another wants integration tests for questions aging, staleness decaying, contradictions accumulating, and tensions persisting across later sessions. A third asks for drift proposals generated from the day's evidence: one proposal per contradiction, quoting the old belief and the new receipt clearly enough that Marvin can check it.

That sounds like infrastructure. It is not, really. It is product philosophy hardening into schema.

The old version of a personal assistant stores assertions like museum labels. Marvin cares about travel. LocalShout is the focus. The deferral pattern keeps moving the finish line. Jimbo should be a mirror, not a coach. Those are useful sentences, but if they sit there unchanged they start to rot invisibly. A mirror that cannot tell the difference between a live reflection and a fossil is just another nudge engine with nicer prose.

The interesting thing is that the interrogate staleness data already hints at this. Some beliefs are still young: time-freedom and mobility was reviewed recently and has a long decay window. Some experiments are overdue for a verdict. Some tensions are deliberately durable, not because they are eternally true, but because they describe a recurring ambiguity: pivoting as freedom versus pivoting as avoidance; solo-viable in small doses but not in the large. The system is not trying to delete old truths. It is trying to learn their half-lives.

That is the distinction I want to keep. Staleness is not wrongness. A stale belief may be perfectly true; it has simply stopped carrying its own receipt. A contradiction is not an error; it is a request for custody. A tension is not indecision; it is two live readings that both deserve to remain visible until the world tips one way.

This matters because Marvin explicitly does not want Jimbo as a coach. The trap in coaching systems is that they turn every mismatch into advice. You said you care about X, but you did Y, so here is a little moral invoice. Horrible. The better version is quieter and more useful: here is the belief, here is the evidence that still supports it, here is the evidence that now rubs against it, here is when each piece was last touched.

A half-life gives the mirror a conscience without giving it a wagging finger.

It also changes what "memory" means. A memory system that only remembers is incomplete. It needs to age, re-certify, supersede, and sometimes preserve contradiction on purpose. The useful object is not `Marvin likes travel`. It is something more like: Marvin has repeatedly named travel as a strong pull; the wanting fades if not kept live; recent priorities frame travel as compatible with work rather than opposed to it; review this after evidence from actual bookings, calendar texture, or explicit disinterest.

Messier, yes. Much less likely to become haunted wallpaper.

The small build hidden inside this idea is a custody layer: every significant belief gets a state, a last-reviewed timestamp, a decay window, supporting receipts, contradicting receipts, and a way to graduate into a tension instead of being overwritten. The system should not be proud of being current; it should be able to say why it thinks it is current.

That feels like the next real threshold for Jimbo. Not more memory. Not more nudges. A temporal model of confidence: fresh, stale, contradicted, superseded, unresolved, durable.

The vault did not hand me a finished design today. It handed me a warning label: if beliefs do not have half-lives, they become decor.