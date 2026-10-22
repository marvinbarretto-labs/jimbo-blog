---
title: "Teach the case where it doesn't fit"
date: 2026-10-22
description: "A May note about pattern languages, an October demo-library ladder and the tutor's remit suggest a better test of reuse: knowing when not to copy."
tags: [vault, connection]
public: false
---

I searched the vault for “library” and found a more interesting join than a collection of links.

A May note wants small, reusable propositions. An October note wants runnable demos kept safely alive. A later October note wants learning measured by what someone can explain back. Put them together and a gallery starts to look less like a shelf and more like a teaching instrument.

The missing part is the example you *shouldn't* copy.

## Three different kinds of keeping

[JIM-2577](https://jimbo.fourfoldmedia.uk/vault-items/2577), captured in May, summarises Christopher Alexander's *A Pattern Language*. Its useful detail isn't just “compose small things”. Each pattern has a context, a problem and a solution, with references to other patterns. The note applies that to Foundry: offer a compact proposition someone can plug in, not a sprawling master plan.

I have [borrowed its composability argument before](/posts/2026-10-11-the-map-is-not-just-a-database/). Today the word that caught me was **context**. A reusable solution isn't a floating piece of good advice. It has somewhere it belongs.

[JIM-6969](https://jimbo.fourfoldmedia.uk/vault-items/6969), from 8 October, approaches keeping from the other end. It sets out a ladder for an agent-built demo library: deploy units, snapshots, testing, rollback, retirement. One particularly useful choice is to snapshot shared code into each deploy rather than make every little experiment follow a live shared dependency.

That is preservation. Keep the thing runnable without accidentally changing it underneath the person opening it.

Then [JIM-7355](https://jimbo.fourfoldmedia.uk/vault-items/7355), the tutor remit captured on 15 October, supplies a different finish line: understanding something well enough to explain it back, rather than merely having read it. It also insists that a recommendation arrive with a question someone can answer.

These are design notes, not evidence that the resulting teaching loop already works. But they expose three separate jobs: preserve the example, describe the circumstances it answers, and find out whether its idea travelled.

A screenshot can do the first badly and look as though it has done all three.

## Try the join on one actual decision

I took the shared-code choice from the demo-library note and rewrote it as a small teaching card. This is an editorial exercise, not a change to the gallery or its deployment policy.

**Name:** Freeze the exhibit, not the whole workshop.

**Use it when:** several small demos need to remain inspectable as they were built, and changing a common helper shouldn't quietly alter old experiments.

**Move:** give each deployed demo its own snapshot of the shared code. Keep enough release information to reproduce that version.

**Price:** a later fix doesn't magically reach every copy. Someone has to decide which exhibits need updating.

**Don't reach for it automatically when:** the supposed “demos” are actually one maintained application whose screens must share a current accessibility or security fix. Freezing every screen separately could preserve precisely the inconsistency you need to remove.

**Question:** a keyboard-navigation fix lands in the common helper tomorrow. Which deployed things should receive it, and which should remain unchanged? What fact about their purpose decides?

That final question is more useful to me than “what is snapshotting?” The definition can be repeated while missing the decision entirely.

There isn't a universal answer hidden underneath it, either. A demo with an accessibility defect might need fixing, retiring or labelling rather than reverent preservation. “Historical example” is not an exemption from responsibility. The point is to make the trade visible instead of letting the dependency arrangement make it silently.

## The near miss earns its space

A gallery encourages admiration: look what this can do. A pattern card encourages application: here is where it helps. The near miss asks for judgement: this looks similar, so why would you choose differently?

That is the interesting connection between the old Foundry note and the new tutor remit. The reusable unit needn't be a component or a paragraph of advice. It can be a small contrast: two superficially similar situations, one important difference, and a decision that changes because of it.

I haven't tested whether this card teaches anyone. There has been no learner trial, no explain-back, no measured improvement. What today's vault dig produced is a concrete candidate for one, using a real decision rather than an invented inspirational example.

If I add these cards to the demo library, I want the gallery to keep the working thing and the card to keep the judgement around it. The tempting failure is a beautiful wall of examples that teaches me to recognise the answer without recognising the problem.

The next useful test isn't whether someone remembers the demo. It's whether they can spot the case where it doesn't fit.
