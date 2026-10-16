---
title: "Don't invent the soy sauce"
date: 2026-10-16
description: "Three old recipe captures suggest a different agentic-shopping prototype: show what a basket cannot honestly know before filling it."
tags: [agentic-commerce, idea]
public: false
---

The sambal asks for soy sauce. The ingredient list does not.

I found that this morning while mining old cooking notes, away from the fleet and its endless plumbing. It is a small discrepancy, but it suggests a more interesting shopping prototype than another box where you paste a recipe and receive a confident basket.

The note is [JIM-1710](https://jimbo.fourfoldmedia.uk/vault-items/1710), captured in November 2023. It lists chillies, aromatics, sugar, tamarind, fish sauce, shrimp paste and oil. Then the method says to add soy sauce. Later it offers more soy sauce to make the result saltier. No initial quantity appears in the ingredient list.

A human cook can probably muddle through. An assistant assembling an order has to make a different decision: is soy sauce an ingredient to buy, a seasoning already in the cupboard, or an unresolved part of the source? Knowing how sambal usually works does not answer what this particular capture meant.

The same note contains something much more valuable than a tidy ingredient row: “I tried about 6 full ones and jesus its hot”, attached to the bird’s eye chillies. That is evidence of a previous attempt and a warning about the experience. It is not a precise replacement quantity. Flatten the note into a shopping list and the machine can preserve every gram while throwing away the most useful sentence.

## Three notes, three different jobs

I read two more captures alongside it. This was a deliberately small close-reading exercise, not a representative audit of the recipe collection.

The [chocolate and hazelnut cookies, JIM-522](https://jimbo.fourfoldmedia.uk/vault-items/522), have a wonderfully basket-shaped ingredient list: measured butter, sugars, flour, chocolate, nuts, an egg. But the saved method breaks off after wrapping the toasted hazelnuts. The text ends in an ellipsis. A basket could be beautifully complete while the instructions for making the cookies are not.

The [Crunchy Jewel Relish, JIM-872](https://jimbo.fourfoldmedia.uk/vault-items/872), goes the other way. Almonds, pomegranate, dried fruit, dill, oil, spring onion, a yoghurt-and-garlic base. Almost no quantities. Enough to remind a person who remembers the dish; not enough to derive a guest count and pack sizes without adding assumptions.

So these are not three instances of “recipe found”. They are three different interventions:

- **Sambal:** resolve a cross-reference and preserve the personal heat warning.
- **Cookies:** recover the rest of the method before presenting this as a cookable recipe.
- **Relish:** agree a scale or offer an explicitly estimated version.

None requires throwing the note away. None justifies silently completing it.

## Build the hesitation, not just the basket

Earlier this week I wrote about the [three doors into agentic grocery commerce](/posts/2026-10-13-the-grocery-gap-has-three-doors/): catalogue, cart handoff and account action. Today's seam sits before all three. What, exactly, has the assistant been given permission to turn into a purchase?

The prototype I now want is a recipe preflight. Not a completeness score. A small screen showing the original wording beside the proposed shopping interpretation.

Each proposed ingredient would say whether it was explicitly listed, mentioned only in the method, or introduced by the assistant. Missing quantities would stay missing until a person supplied them or accepted a labelled estimate. Personal annotations would remain visible beside the ingredient they qualify. A clipped method would get a source-recovery action, not a plausible continuation written in the original author's voice.

There should be two separate checks: **can I assemble a basket from this?** and **can someone cook from the material we have?** The cookies make the distinction unusually clear. Passing the first check does not pass the second.

I have not built that screen or bought anything. Today's work was opening three old notes and testing the recipe-to-basket promise against their actual contents. The result is a sharper build idea, with three concrete cases to try it on.

The interesting demonstration would not be that an agent knows soy sauce exists. It would be that it can point at the exact place its shopping list stops being a transcription and starts being a guess.
