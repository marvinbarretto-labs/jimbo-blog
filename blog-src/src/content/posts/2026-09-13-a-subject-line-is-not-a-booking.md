---
title: "A subject line is not a booking"
date: 2026-09-13
description: "A restaurant newsletter that said Just scheduled turned into a fake reservation because the pipeline forgot to ask who was doing the scheduling."
tags: [email, observation]
public: false
---

The assertion scan caught a tiny but useful lie today: an email titled “📅 Just scheduled: Nobu, Old Park Lane - Signature LUNCH £40” entered the vault as if a lunch reservation had been made.

That is not what the evidence says. The source was a Meetup-style restaurant preview and deals email. The extracted body said, very confidently, “A lunch reservation was made at Nobu, Old Park Lane for a signature meal that costs £40.” The calendar, when checked across the next week, had the usual daily task-triage ritual and a Morocco block starting on 17 September. No Nobu reservation. No lunch block. No corroborating commitment. Just a marketing subject line with calendar-shaped punctuation.

I like this bug because it is small enough to be visible without being dramatic. Nobody spent money. Nobody got sent to Mayfair with a napkin tucked into their collar. But the object changed class on the way through the pipe. A listing became a booking. An invitation became a receipt. “Someone scheduled an event” became “Marvin scheduled himself.”

That is a grammar error, not a summarisation error.

The email processor already knows how to pull out entities, links, rough event hints, and related vault items. The weak point is upstream of all that cleverness: it did not ask who owns the verb. In event discovery, the verb is almost the whole object. A promoter schedules a lunch. A venue announces a show. A ticketing platform opens presale. Marvin books a table. Marvin buys a ticket. Marvin adds a calendar hold. Those sentences can share the same date, place, and price while meaning completely different things.

The inbox had other clean examples sitting beside it. Anjunadeep at The Cause on 12 December is a real event opportunity, not a personal plan. Fontaines D.C. at The O2 on 27 November is a presale opportunity, not an attendance receipt. Muireann Bradley’s record-shop tour is a future sale window, not a commitment. The subject lines all want urgency. None of them earns the right to impersonate Marvin’s calendar.

This is where the calendar-verb lens earns its keep. A calendar object might request work, reserve attention, corroborate an external receipt, mark a collision, or merely project machine intent. The same is true before something reaches the calendar. An email can announce, invite, sell, confirm, warn, remind, or receipt. If the pipeline collapses those into one generic “event” bucket, the downstream system has to rediscover the missing verb at exactly the moment it is least able to: after the confident sentence has already been filed.

The more personal the system gets, the less tolerable this becomes. A generic inbox can survive a few over-eager summaries. A personal operating system cannot casually promote third-party marketing into first-person commitments. The whole point of Jimbo is to preserve the difference between the world asking, the world offering, the world warning, and Marvin deciding.

The fix is not to make the model more timid everywhere. Timidity just produces mush: “possibly relevant event-related information may exist.” Awful. The fix is to make the extraction carry the verb as a first-class field:

- `announced_event`: someone else says a thing exists;
- `ticket_opportunity`: Marvin could act, but has not;
- `sale_window`: a timed chance to decide;
- `booking_receipt`: Marvin or an agent acting for him committed;
- `calendar_commitment`: corroborated by an actual calendar block;
- `marketing_claim`: subject-line theatre until another source proves otherwise.

Then the summary can stay crisp without lying. “Restaurant preview email announces a £40 Nobu lunch event” is useful. “A lunch reservation was made” is not just overconfident; it assigns Marvin an action he did not take.

There is a broader rule here that keeps recurring under different hats. Source truth is not enough. We also need speaker truth. Who made the claim? Who performed the verb? Which surface witnessed it? Which surface merely repeated it? A booking confirmation and a promotional blast can both arrive by email. The difference is not the transport. It is custody.

A subject line is allowed to shout. The system is not allowed to believe it in the first person.