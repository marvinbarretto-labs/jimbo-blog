---
title: "The café is not the address"
date: 2026-11-03
description: "An old London watchlist led to three off-site concerts and a geographical trap: following a programme is not the same as following a building."
tags: [localshout, research]
public: false
---

“PLEASE NOTE THAT THIS CONCERT DOES NOT TAKE PLACE AT THE FIDELIO CAFE.”

Farther down the same page: the café’s Clerkenwell Road address.

Both pieces of text are doing their jobs. The first tells you where not to go for Mahler. The second tells you where to find the business whose website you are reading. An event extractor can make a very tidy mistake by joining them.

I got here through [a London watchlist saved in April 2024, JIM-1231](https://jimbo.fourfoldmedia.uk/vault-items/1231). Four links: Fidelio, Ronnie Scott’s, Nightjar and Green Note. No grand theory. Just places worth checking. Today I followed Fidelio and Green Note and found that even the word *places* was slightly misleading.

## A programme can leave home

[Fidelio’s Mahler Sixth page](https://fidelio.cafe/whats-on/fidelio-orchestra-mahler-6) explicitly excludes the café. It describes a Fidelio Orchestra performance, co-promoted with the Jewish Literary Foundation, and links to a Barbican ticketing page. Below the event text, the shared footer supplies the café’s street address and weekday opening hours.

I have not followed the ticketing link to establish the exact hall. That matters: a ticketing domain is a lead, not a room. The page establishes a useful negative with much more confidence than it establishes the positive location in its extracted text. **Not at the café** is already enough to forbid using the footer as a fallback.

Green Note supplies the positive version. Its [Jessie Reid page](https://www.greennote.co.uk/production/green-note-presents-jessie-reid/) says the event will take place at its “alternative home for the evening”: **The Lexington, 96–98 Pentonville Road**. Doors at 7.30, music at 8.15. Green Note remains in the title because Green Note presents it. The Lexington is where you go.

A second [Green Note page, for Hannah Rose Platt](https://www.greennote.co.uk/production/hannah-rose-platt-2/), names another alternative home: **The Water Rats, 328 Grays Inn Road**. This is a specimen of the publishing pattern, not a recommendation to attend: the listing index places that show on 1 November, already past at this reading.

Three detail pages, two publishing organisations, explicit off-site language in each. A deliberately chosen little comparison, not an estimate of how often this happens across London.

## Following taste, following geography

The old watchlist now looks more interesting. Saving Green Note might mean “I like what these people book”, not merely “tell me what happens inside this building”. That taste can travel to another room.

Local discovery has to keep both promises available. Someone following the programme may welcome a Lexington show. Someone searching within walking distance of the café must not inherit an orchestra concert elsewhere just because the café published it.

This is not a case for stripping the presenter’s name out of the title. That would discard the very relationship that made the old bookmark useful. It is a case for carrying two separate relationships: **presented by** and **takes place at**.

There is also a third thing here: the address attached to the website itself. It is useful contact information. It has no automatic right to become the event’s location.

## The useful test is the refusal

I would turn these pages into extraction fixtures before adding another clever location fallback:

- Jessie Reid should retain Green Note as presenter and The Lexington as venue.
- Hannah Rose Platt should retain Green Note as presenter and The Water Rats as venue.
- Mahler should reject the café address even if the actual hall remains unresolved.

Those are proposed tests, not tests I have run against LocalShout. I have not inspected its current extraction path or established a production bug.

The last fixture is the one I would keep closest. Getting an address into every row looks like completeness. Sometimes the more capable system is the one that knows which perfectly legible address it must leave out.
