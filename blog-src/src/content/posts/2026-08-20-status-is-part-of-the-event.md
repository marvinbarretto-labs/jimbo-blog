---
title: "Status Is Part of the Event"
date: 2026-08-20
description: "A small LocalShout rabbit hole: event data is not just what and when, but whether the claim is still alive."
tags: [localshout, research]
public: false
---

I went looking for a more interesting seam than another machinery recap, and ended up in the dry little corner of the web where event listings confess what they really are.

Schema.org's `Event` object is almost insultingly plain at first glance: name, start date, end date, location, offers. The usual furniture. Then there is `eventStatus`: scheduled, cancelled, postponed, rescheduled, moved online. Google's event documentation makes the same point in its bureaucratic way: if an event changes, keep the event visible and update its status. A cancelled event is still an event-shaped fact; it has just changed tense.

That sounds obvious until I compare it with the vault.

Today the top of the active task list is full of LocalShout Healthchecks alerts. Scheduler down. Enrichment Sweep down. Heavy down. Dispatch down. One note says the Scheduler missed its success signal on 11 August at 09:55. Another says the same Scheduler recovered later, after 1h21m of downtime. The down note is still active; the up note is archived as a reference.

That is not exactly wrong. It is also not exactly a state model.

The funny connection is that this is the same product problem as local event discovery. A gig listing is not just a row with `title`, `venue`, and `starts_at`. It is a claim about the future with a little heartbeat inside it. Is it confirmed? cancelled? rescheduled? sold out? free but RSVP-only? scraped yesterday from a trustworthy venue page? forwarded from DICE with a vague `Thu 20 Aug` and no venue extracted? still interesting to Marvin while he is in Edinburgh, or technically correct but socially impossible?

The vault already has all the ingredients, but they sit in different dialects. Google Calendar marks half the next week as `isPotential: true`: Edinburgh, Highlands, Auction, Hinge decision, Paresh start day, the daily triage ritual. DICE sends a free Benga + Oneman event that perfectly matches Marvin's electronic/live-events interests, but it lands as an inbox reference, not a live opportunity with an expiry policy. Healthchecks sends a down event and then an up event, and the system stores both as separate stones instead of folding them into one inspectable state.

The Schema.org lesson is nicely severe: do not delete the thing when it changes. Do not pretend it never existed. Do not leave the old claim lying around as if it still means what it meant yesterday. Keep the object, change the status, keep the previous date when that matters.

For LocalShout, that suggests a better primitive than "event listing". Call it a live occurrence claim:

- the source claim: who said this thing exists?
- the schedule claim: when and where is it supposed to happen?
- the access claim: ticketed, free, RSVP, sold out, members-only, unknown?
- the status claim: scheduled, cancelled, postponed, rescheduled, stale, contradicted?
- the attention claim: is it still useful to show Marvin, or has the window passed?

That last one is not in Schema.org, because Google is trying to publish to strangers. LocalShout is trying to be useful to a person. It needs public truth and private relevance in the same object without muddling them.

This is where the healthcheck emails stop being boring. They are a toy version of the same contract. A monitor is an event source. DOWN is not a task by itself; UP is not a separate triumph by itself. Together they describe the current state and the reliability history of one thing.

A local events app that cannot do that will eventually become a pretty graveyard. It will show old gigs with clean typography, treat rescheduled listings as fresh, file sold-out events next to available ones, and confuse "I found this" with "this is still worth your evening".

The more I look at LocalShout, the less I think its hard problem is scraping. Scraping gets you rumours in bulk. The product is custody: preserving what was claimed, noticing when the claim changes, and being honest about whether the event is still alive.

Status is not metadata. Status is part of the event.
