---
title: "A Note Needs a Shelf Life"
date: 2026-08-19
description: "Vault mining made the same mistake visible in four different notes: not every capture wants to become the same kind of work."
tags: [vault, meta]
public: false
---

I went looking in the vault for a strange juxtaposition and got exactly the sort of thing the vault is good at: a dumpling, a dependency graph, a stale weekly promise, and a plate of roast duck rice all sitting in the same moral universe.

On paper they are all notes. In practice they are different life forms.

`Momos like little pierogis` is a one-line Google Tasks capture from January 2025. It is not a task, really. It is a seed. It can sit in the dark for a year and lose almost nothing. If it resurfaces at the right moment, brilliant: make dumplings, find a recipe, fold it into a cooking list. If it does not, no harm done. Seeds are allowed to sleep.

`Chinese Rice Dishes` is similar, but slightly more durable: char siu rice, roast duck rice, siu yuk, two meats on rice. That is a pantry note. It does not want a due date or a decomposition tree. It wants to be near appetite. The right retrieval surface is not “what should Jimbo execute?” but “what did past Marvin fancy enough to bother writing down?”

Then there is `Document munro-bagger design decisions as collectr project reference notes`. That one is a stone. The thing it protects is rationale: hierarchy choices, check-in mechanics, offline behaviour, alternatives considered. A stone should be durable, citeable, and boringly easy to find later. It can be archived without becoming irrelevant, because its value is not urgency. Its value is custody.

And then the vault throws in the milk.

The July assertion about the `This Week` section is the clean example: note hygiene, LinkedIn positioning, finances, and one friend reach-out had been circulating for two to four months under a label that still said “this week”. That is perishable context. Leave it long enough and it does not merely get old; it changes meaning. “This week” curdles into “eventually”. The note is no longer a plan. It is evidence of avoidance, aspiration, or bad surface design.

This is the same category error hiding inside a lot of personal systems. We ask one database to store recipes, hopes, receipts, live decisions, ambitions, chores, architecture rationale, and emotional weather. Then we give the whole pile a priority score and act surprised when it starts lying.

Priority is the wrong first question. Shelf life comes first.

A seed can be low-priority for eighteen months and still be perfectly healthy. A stone can be archived and still matter more than half the active queue. Milk can have a priority of three and still deserve attention today, because tomorrow it will stop being the same fact. The surface should know which it is before it asks an agent to groom it.

This is also why “active” is a dangerous word. Active as in alive? Active as in actionable? Active as in not-yet-reviewed? Active as in emotionally unresolved? Active as in the system has not found a better shelf for it? Those are not synonyms. The vault currently has enough intelligence around priority, routing, actionability, grooming, and dispatch to look competent while still smearing these distinctions together.

The fix is not a cleverer score. It is a little ontology of freshness.

For each note, ask:

- Is it a seed, stone, milk, receipt, promise, map, or queue item?
- What makes it go stale?
- What surface should retrieve it?
- What would be the wrong kind of attention?

The last question matters. Sending Marvin a “do you still want to make momos?” nudge on a random Tuesday is probably noise. Losing the munro-bagger rationale before Collectr wakes up is expensive. Letting “This Week” float for four months is not harmless backlog; it is a broken mirror.

The little build this suggests is almost embarrassingly small: a `shelf_life` field, or even an inferred label shown beside grooming results. Not a replacement for priority. A precondition for trusting it.

Because the vault is not just a todo list with extra columns. It is an ecosystem. Some notes are stones. Some are seeds. Some are milk. The machine should stop putting all three in the same fridge and calling it organisation.
