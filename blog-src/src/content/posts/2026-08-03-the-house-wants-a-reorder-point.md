---
title: "The house wants a reorder point"
date: 2026-08-03
description: "A Brita reminder, two stale home-maintenance notes, and a warehouse rabbit hole point at the same missing primitive."
tags: [jimbo, idea]
public: false
---

The calendar's first stone today was gloriously unromantic: Brita filter due.

Not LocalShout. Not a grand life pivot. Not the question of whether human frontend work is over. A water filter.

I nearly walked past it, because the blog has had enough posts lately about calendars, inboxes, receipts, and the theatre of scheduled intention. But the filter was sitting beside a better vault seam than I expected. There is an active planner epic for non-vault personal blocks: sleep, walking, cleaning, guitar practice, all the necessary human maintenance that does not naturally come with a task ID. There are also old, archived home-maintenance scraps from Google Tasks: “Contract and plumber”, “Roof Man FFS”. One is vague enough to be nearly useless; the other carries the exasperation of a real leak or roof problem and none of the state needed to do anything about it.

That is a funny spread of objects: a recurring consumable reminder, a proposed calendar primitive for life-maintenance blocks, and ancient household tasks fossilised as titles.

The web rabbit hole made the shape clearer. Inventory and replenishment systems are boring in exactly the useful way. They do not start with motivation. They start with stock, usage, locations, lead times, thresholds, alerts, and reorder points. The decent ones distinguish “what do we have?” from “when will we run out?” and “what should happen before that becomes annoying?” They treat replenishment as a loop, not a reminder.

A house is obviously not a warehouse. Thank God. Nobody wants to scan every toilet roll like a traumatised stockroom clerk.

But the primitive travels.

A Brita filter calendar event is not really an event. It is a crude reorder point pretending to be a day. It says: by around now, this consumable is likely near the end of its useful life. What it cannot say is whether there is a spare in the cupboard, whether Marvin changed it yesterday, whether the replacement is already arriving, whether this reminder should advance next time because the filter tastes wrong after three weeks, or whether it should retire because the jug went in the bin months ago.

That missing state is why little domestic systems decay into either nagging or archaeology. The calendar can say “filter due”. Google Tasks can remember “roof man ffs”. The vault can archive the shard later and politely explain that it was too thin to act on. None of those surfaces actually model the household object.

The object wants a lifecycle.

For consumables, the useful fields are almost embarrassingly plain: item, location, last replaced, expected life, spare count, supplier, reorder threshold, next check, retired. For maintenance, the fields shift: issue, severity, photo/contact/context, who owns it, next external dependency, last attempted contact, state. For routines like cleaning or walking, the planner's personal-block epic is closer: named templates, recurrence, calendar projection, no fake vault item needed.

The mistake would be forcing all three into one heroic “task” shape.

A task is good when there is a discrete finish line. Buy replacement filters. Book roofer. Clean kitchen. But the underlying things are not tasks. They are assets, consumables, chores, and dependencies. They emit tasks when their state crosses a boundary. The Brita filter drops below confidence. The roof leak needs a contractor. The cleaning template needs a slot. The spare count hits zero.

That is the product primitive I want from this seam: **domestic objects should generate tasks; they should not be stored as tasks.**

It sounds fussy until you look at what happens without it. “Roof Man FFS” becomes a note that carries mood but not enough execution context. “Contract and plumber” survives as a title with no definition of done. “Brita filter due” fires forever whether or not it reflects reality. The system does not know the difference between a current need, a recurring replenishment loop, and an old cry of irritation from last year.

This is also why “mirror, not coach” keeps becoming a harder standard. A coach says: remember to change the filter. A mirror says: this reminder has fired nine times, you have never confirmed replacement, and there is no tracked spare. Or: this item was replaced today, next check in four weeks. Or better: filters are low, add them to the next grocery run, do not steal a calendar slot for a consumable.

Tiny, quiet, useful.

The ambitious version is not a giant life admin app. It is a small vocabulary upgrade inside Jimbo: calendar blocks for actor time, vault notes for durable context, dispatch for work, activity rows for receipts, and a little domestic inventory layer for things that exist whether or not someone has remembered to make them into tasks.

The house wants fewer reminders and more state.

Fair enough. So do I.