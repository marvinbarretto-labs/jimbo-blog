---
title: "LocalShout Weekly Digest v1 Brief"
date: 2026-08-13
description: "LocalShout Weekly Digest v1 Brief"
tags: [localshout, digest, report]
public: false
---

*Report — a brief (2026-08-13), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Contents

v1 digest includes live music events only. This is a deliberate scope choice, not a proxy for quality.

The vision identifies three content categories in scope: arts (live music, theatre, comedy, visual), civic (community events, health, support), and everything else. v1 ship with arts only. Civic content stays indexed and queryable but doesn't route into the digest; toggling it on comes later per [POS-7].

Live music is chosen first because:
1. It's the remembered miss case that drove [MET-6]'s 90% recall gate. A gig at a local venue is the concrete example.
2. Media previews (Spotify/YouTube) are highest-signal here; an unknown band can be heard before deciding to attend. This locks down [VP-5]'s "previews are decision aids" claim.
3. It's the longest tail — the acts most likely to be under-promoted and absent from the reader's existing follows.

Within arts, filter to confirmed-happening events only. Cancelled, tentative, or "date TBA" events stay in the system but don't ship in the digest; they pollute the curation signal and force readers to read past noise. The UI can show "might happen soon" in a separate treatment later.

## Curation Logic

The digest is sorted by relevance-to-reader, not chronologically.

Relevance is determined by three signals, ranked in order:
1. **Save/follow history.** Events whose artists or venues the reader has previously saved or followed appear first. This is the personalisation signal we get without a profile form. A reader who followed three jazz venues gets jazz events promoted.
2. **Freshness of artist discovery.** Events by artists with no social presence or minimal online footprint rank higher than well-promoted acts. This serves [PROB-2]: raising awareness of under-promoted shows is a first-order goal. A no-name local band ranks above a major touring act, all else equal.
3. **Venue tier.** Venues with a history of booking diverse lineups rank above one-off promoters. The system already tracks this as part of deduplication logic.

The digest caps at 10-12 events per week to stay true to [VP-2]: "curated — a few good things, not a firehose." Events ranked 13+ go unseen; they're available in the full browse. Over time we'll tune the cap based on reader engagement, but starting at 10-12 makes the editorial choice visible.

Hard filter: exclude events already saved by the reader. They've decided; no need to remind them.

## Cadence

Send every Friday at 6 PM local time. Window is Friday through Thursday (7 days forward-looking, as implemented in `gatherWeeklyDigest`).

Rationale: Friday evening is the moment readers start thinking about their week. The 7-day window gives enough time to decide and book without making events feel stale (no "last chance" urgency). Thursday closure keeps Friday's send fresh. If an event is added Thursday evening, it lands in the next week's digest, not this week's.

Send only if there are curated events to show. An empty digest is noise; "check back next week" feels better than "nothing on the books."

## Tone and Voice

The digest is matter-of-fact and assumes the reader knows Watford. No "discover" rhetoric, no "you might like" hedging. The tone is "here's what's actually on, sorted for you." Events speak for themselves; the preview (if available) does the selling.

The email header is "This week in [Region]" — ownership framing. The footer is plain: a link back to the app, nothing else. No tracking pixels, no newsletter signup, no engagement hooks. This is a service, not a growth channel.

## Deliberate Exclusions (v1)

- **Civic and support content.** In scope for the product ([AUD-3]), out of scope for v1 digest. Non-binding commitment: will add as a toggleable second digest or a fold-out section in the same email. Depends on reader feedback about whether civic content helps or distracts.
- **Major commercial entertainment.** Theatre tours, big comedy acts, mainstream bands. [SCOPE-2] is clear: small and niche beats big and commercial. v1 is local-first; touring acts belong in a different product or a section Marvin reads on purpose.
- **Events without venue confirmation.** "Summer music series (dates TBA)" or "TBD venue — artist page" are live in the system but not in the digest. Uncertainty doesn't belong in a curation artifact.
- **Recurring or evergreen events.** Weekly open-mics, standing community dinners. They're in the browse; they're not fresh discovery. Recurring content breeds list-fatigue and doesn't change week to week.
- **Anything beyond 10 miles.** v1 bounds to tight geography. London and surrounding towns come later per [UND-3]; Watford is the beachhead.
- **Reader-submitted content.** Posters scanned by users go straight to the live database but don't appear in curated surfaces until an editor has verified them. Trust is load-bearing per [RISK-3]; a flat-wrong event costs more than ten good ones earn.

## Next Steps

Implementation tasks:
- Retrain the ranking model with the three-signal ranking logic. Currently the database has some venue-tier scores from clustering; use those to validate the model.
- Build the curation admin surface to tag artists as "under-promoted" and tune the freshness signal. Manual tuning until we have 4-6 weeks of reader engagement data.
- Instrument saves and follows by event, so we can measure [MET-1] locally: readers finding events they didn't already know about.
- Ship with a feature flag. Friday sends go to Marvin only. After two weeks of dogfood, expand to test group if the engagement numbers say "this is not noise."

The digest serves [VP-2]'s core claim: "I stop missing local events I'd have wanted to go to" + "It's curated — a few good things, not a firehose." v1 does both in the narrowest possible scope. Everything else waits for data.

