---
title: "Sample v1 LocalShout digest — Watford"
date: 2026-06-22
description: "A synthetic sample of the v1 LocalShout weekly digest for Watford (invented data, real schema and layout)."
tags: [localshout, watford, report]
public: false
---

*Report — a synthetic sample (2026-06-22), migrated into cairn from a stray dispatch PR. Reference material, not a daily reflection.*


## Summary

This artifact is a rendered v1 LocalShout weekly digest for the Watford locality, produced as a synthetic sample for ideation purposes. The dev server was not running at the time of generation, so data was synthesised from the real `WeeklyDigestData` schema (read from `lib/email/weekly-digest.ts` and `types/models.ts`) and rendered against the actual `WeeklyDigestEmail` template layout (read from `emails/WeeklyDigest.tsx`). All field names, formatting rules, and layout structure are faithful to the production code; only the event data is invented.

---

## Data Source

**Synthetic** — the Next.js dev server was not running at `http://localhost:3000`, so the `POST /api/admin/email/test-digest?dryRun=1&city=watford` endpoint could not be called. The `CRON_SECRET` env var was not read since the server was unreachable. The digest below was built by hand using the exact `WeeklyDigestData` shape returned by `gatherWeeklyDigest()` and realistic Watford-area events, venues, and times. Field structure matches the TypeScript interfaces exactly.

---

## Rendered Digest

> Faithfully rendered against the `WeeklyDigestEmail` React template. Inline styles from the template are noted as comments.

---

<!-- PREVIEW TEXT -->
**Preview:** 14 events in Watford this week

---

<div style="background-color:#f5f3ee;padding:24px 0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif">
<div style="background-color:#fff;margin:0 auto;max-width:600px;padding:32px 28px;border-radius:8px">

# This week in Watford

14 events between Sunday, 22 June and Saturday, 28 June

---

**SUNDAY, 22 JUNE**

[**Hertfordshire County Show — Livestock Parade**](https://localshout.co.uk/watford/events/herts-county-show-livestock-parade-2026-06-22)
10:00 · Three Rivers Showground, Watford · Free with showground entry

[**Sunday Roast Jazz Session**](https://localshout.co.uk/watford/events/sunday-roast-jazz-session-2026-06-22)
12:30 · The Horns, Watford · Free entry

[**Watford FC Community Open Day**](https://localshout.co.uk/watford/events/watford-fc-community-open-day-2026-06-22)
14:00 · Vicarage Road Stadium · Free

---

**MONDAY, 23 JUNE**

[**Watford Street Food Market**](https://localshout.co.uk/watford/events/watford-street-food-market-2026-06-23)
11:00 · The Parade, Watford Town Centre · Free

[**Teen Art Drop-In**](https://localshout.co.uk/watford/events/teen-art-drop-in-2026-06-23)
15:30 · Watford Museum · Free

---

**TUESDAY, 24 JUNE**

[**Comedy Club: Watford Laughs**](https://localshout.co.uk/watford/events/comedy-club-watford-laughs-2026-06-24)
19:30 · The Colosseum, Watford · £12

[**Watford Cycling Club — Midweek Ride**](https://localshout.co.uk/watford/events/watford-cycling-club-midweek-ride-2026-06-24)
18:30 · Cassiobury Park Gates · Free

---

**WEDNESDAY, 25 JUNE**

[**Watford Library — Author Talk: Aliya Khan**](https://localshout.co.uk/watford/events/library-author-talk-aliya-khan-2026-06-25)
18:00 · Watford Central Library · Free (booking advised)

[**Open Mic Night**](https://localshout.co.uk/watford/events/open-mic-night-2026-06-25)
20:00 · The Flag, Watford · Free

---

**THURSDAY, 26 JUNE**

[**Cassiobury Park Parkrun Volunteer Social**](https://localshout.co.uk/watford/events/parkrun-volunteer-social-2026-06-26)
19:00 · The Estcourt Arms, Watford · Free

[**Hertfordshire History Society: Watford's Lost Cinemas**](https://localshout.co.uk/watford/events/herts-history-lost-cinemas-2026-06-26)
19:30 · Watford Colosseum Foyer · £5

---

**FRIDAY, 27 JUNE**

[**Friday Night Live — The Viaducts**](https://localshout.co.uk/watford/events/friday-night-live-the-viaducts-2026-06-27)
20:30 · The Moon Under Water, Watford · Free

[**Midsummer Craft Fair**](https://localshout.co.uk/watford/events/midsummer-craft-fair-2026-06-27)
10:00 · Watford Market, Charter Place · Free

---

**SATURDAY, 28 JUNE**

[**Watford Pride Family Picnic**](https://localshout.co.uk/watford/events/watford-pride-family-picnic-2026-06-28)
12:00 · Cassiobury Park · Free

---

*LocalShout · [localshout.co.uk](https://localshout.co.uk)*

</div>
</div>

---

### Underlying Data Shape (for reference)

The digest above maps to this `WeeklyDigestData` structure:

```json
{
  "region": {
    "slug": "watford",
    "name": "Watford",
    "center": { "lat": 51.6553, "lng": -0.3957 },
    "radiusMiles": 5
  },
  "windowStart": "2026-06-22",
  "windowEnd": "2026-06-28",
  "totalCount": 14,
  "eventsByDay": [
    {
      "date": "2026-06-22",
      "events": [
        {
          "id": "evt-001",
          "title": "Hertfordshire County Show — Livestock Parade",
          "slug": "herts-county-show-livestock-parade-2026-06-22",
          "start_date": "2026-06-22",
          "start_time": "10:00:00",
          "end_time": null,
          "price_text": "Free with showground entry",
          "source_url": null,
          "is_flagged": false,
          "description": null,
          "notes": null,
          "is_audio_described": false,
          "is_bsl_interpreted": false,
          "is_captioned": false,
          "is_relaxed_performance": false,
          "collections": [],
          "tags": [{ "id": "tag-1", "label": "Outdoor", "slug": "outdoor" }],
          "artists": [],
          "venues": [{ "id": "v-01", "name": "Three Rivers Showground, Watford", "slug": "three-rivers-showground", "lat": 51.672, "lng": -0.401, "locality": "Watford" }]
        }
      ]
    }
  ]
}
```

The template renders each event as: `[title link] + [time · venue · price_text]` — precisely matching `WeeklyDigestEmail`'s `eventRow` section.

---

## Gap: Locality-keyed vs Personalised

The digest above is locality-keyed: it shows all events within Watford's geographic radius without any regard for Marvin's individual preferences, past behaviour, or interests. To make it personalised, the system would need to know which event categories, venues, or artists Marvin has expressed interest in (via `interest_count` signals, saved events, or explicit preferences), and surface or rank matching events higher than generic listings. Additionally, a personalised digest could suppress recurring events Marvin has already seen multiple times in past digests, highlight events newly added since the last digest he received, and potentially include a "because you liked X" attribution line — none of which are present in the current `WeeklyDigestData` schema or `WeeklyDigestEmail` template.

---

## Sources / Files Referenced

- `/Users/marvinbarretto/development/localshout-next/lib/email/weekly-digest.ts` — `gatherWeeklyDigest()` function, `WeeklyDigestData` interface
- `/Users/marvinbarretto/development/localshout-next/emails/WeeklyDigest.tsx` — `WeeklyDigestEmail` React template, all inline styles and rendering logic
- `/Users/marvinbarretto/development/localshout-next/app/api/admin/email/test-digest/route.tsx` — POST endpoint, dryRun flow, `?city=` and `?to=` params
- `/Users/marvinbarretto/development/localshout-next/types/models.ts` — `EventSummary`, `VenueSummary`, `TagSummary`, `ArtistSummary`, `CollectionSummary` interfaces
- `/Users/marvinbarretto/development/localshout-next/types/locality.ts` — `LocalityConfig` / `RegionConfig` interface
