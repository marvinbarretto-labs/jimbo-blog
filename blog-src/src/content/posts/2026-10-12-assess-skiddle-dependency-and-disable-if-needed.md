---
title: "Assess Skiddle dependency and disable if needed"
date: 2026-10-12
description: "Assess Skiddle dependency and disable if needed"
tags: [localshout, skiddle, report]
public: false
---

*Report — a research report (2026-10-12), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
The ticket's premise is wrong. Skiddle is **not** mostly duplicated: all 491 events with a Skiddle sighting have no sighting from any other source, and only 3 of 491 fuzzy-match a non-Skiddle event on the same venue and date. Disabling it is not "little coverage cost", but I still recommend disabling it. It is a single source row, the scrape only works by defeating Skiddle's WAF with a stealth browser, and the events are mostly outside Watford. Disabling is one flag flip on one row, with no code change.

## From prior context
No `prior_context` was supplied. The vault note (*Assess Skiddle dependency and disable if needed*) supplies the terms and risk framing:
- Skiddle's Promotion Centre terms protect content with "copyright and database rights" and allow only personal non-commercial retrieval. The note quotes them. I did not re-fetch the terms, and this is not legal advice.
- The note's claim that "most events are available via direct venue scraping" is the premise tested below.

## New findings (read-only queries against the LocalShout Supabase, 2026-10-12)

**The source.** There is exactly one Skiddle source row, in `sources`:

| Field | Value |
|---|---|
| `id` | `0bf28c64-4d40-459e-91b8-9709b70d0bac` |
| `slug` | `skiddle-watford` |
| `integration_slug` | `scrape/skiddle` |
| `url` | `https://www.skiddle.com/whats-on/Watford/` |
| `is_active` | true |
| `publish_immediately` | true |
| `scrape_frequency_days` | 3 |
| `last_scraped_at` | 2026-10-09 |
| `last_scrape_status` | success |

**The counts.**

| Measure | Count |
|---|---|
| Events with a Skiddle sighting (all `scrape/skiddle`; 1,433 sightings in total) | **491** |
| Also sighted by another source (`event_sightings`) | **0** |
| Fuzzy match to a non-Skiddle event (same `venue_id` and `start_date`, ≥50% title-word overlap, against 13,780 other events from 2026-03-01 onward) | **3** |
| Skiddle-only | **488 (99%)** |
| Published / draft / archived | 333 / 155 / 3 |
| Upcoming (from 2026-10-12) | 99, of which 77 are published |
| Skiddle events with a venue, at venues with no non-Skiddle events | 43 of 79 upcoming |
| Venues touched | 157; 35 of them also have events from other sources |

- The 961 sightings flagged `corroborates_existing=true` are Skiddle re-sighting its own events on repeat scrapes. They are not cross-source corroboration, because no other `integration_slug` appears on any of these events.
- The 3 fuzzy hits are:
  - a World Cup screening;
  - "Kaleidoscope Festival 2026";
  - "The Bracknall".
- The fuzzy match needs `venue_id`, so the 155 venue-less drafts could not be matched. Even counting them as duplicates would not change the verdict.
- The method is conservative about matching. A looser match would find a few more duplicates. It would not find hundreds.

**Sample of upcoming Skiddle-only published events:**
- 2026-10-15, International Stand Up Comedy, Soho Comedy At 7 Dials.
- 2026-10-16, Rent, Duke Of York's Theatre.
- 2026-10-17, Oktoberfest on the Common, Clapham Common.
- 2026-10-17, The Halloween Special, The Benidorm Bar (Liverpool).
- 2026-10-23, Terminal V, Drumsheds.
- 2026-10-25, Halloween Extravaganza, Kew Little Pigs Farm (10 upcoming rows alone).

The "Skiddle Watford" listing is mostly London and national events, not Watford.

**Scraping state.** The earlier doc claim that Skiddle is "a hard 403" (`2026-09-09-launch-plan.md`) is stale or incomplete.
- Capture history shows plain HTTP failing daily from 2026-09-20 to 09-29 with `Page returned status 403`, and a "0 items… JS-rendered" error on the first tier.
- Since 2026-09-29 the source has succeeded through `firefox-playwright`, a stealth browser run by `m2-batch`. It returned 50 items on 09-29 and 49 on 10-06.
- Sightings are still arriving: 41 on 2026-10-09.
- The WAF is therefore being deliberately worked around, which makes the terms issue worse, not better.

## Verdict
**Disable.** The ticket's reason (it is duplicated) is false, but there are three better ones:
1. The terms prohibit commercial retrieval, and the scrape works by evading a WAF that actively blocks it.
2. The source row is fragile: it failed daily for roughly 10 days before the browser tier was added.
3. The coverage it adds is mostly out-of-area London and national ticketed events. Watford coverage is already corroborated by venue sites (`2026-07-28-recall-baseline.md`, via the vault note).

The cost is real: about 77 upcoming published events, 43 of them at venues with no other source.

**What to change (nothing was changed here):**
- Set `sources.is_active = false` on `0bf28c64-4d40-459e-91b8-9709b70d0bac` (`skiddle-watford`).
- No code change is needed. `lib/scraper/sources/skiddle.ts` and `lib/scraper/configs/providers/skiddle.ts` only run for active rows. Leave them in place so the decision can be reversed.
- Decide separately what to do with the 333 existing published rows. Keeping scraped content already held is a different question from continuing to retrieve it. That is Marvin's call, and this audit did not touch it.

## Recommendation
Disable the source before the November launch, and tell yourself the real trade: you are giving up around 77 upcoming events, mostly London. If that coverage matters, replace it with Skiddle's official partner API or DICE, Lemonrock and TownSpot, which the launch plan already lists as in. Do not keep the stealth-browser scrape as the long-term route.

## Sources
1. Vault note `note_771d6c50`: task, quoted Skiddle terms, risk framing.
2. LocalShout Supabase (read-only REST), 2026-10-12. Tables: `sources`, `event_sightings`, `events`, `venues`. The audit data is in `/tmp/skid_sight.json`, `/tmp/ev.json` and `/tmp/allev.ndjson`; these are ephemeral.
3. `localshout-next/docs/live/2026-09-09-launch-plan.md`: Skiddle recorded as a hard 403.
4. `localshout-next/docs/live/2026-07-28-recall-baseline.md`: Watford listings corroborated by venue sites.
5. `localshout-next/supabase/migrations/20260516092008_create_event_sightings.sql`: provenance model.
6. `localshout-next/lib/scraper/configs/providers/skiddle.ts`: snapshot source and `isMultiVenue`.

