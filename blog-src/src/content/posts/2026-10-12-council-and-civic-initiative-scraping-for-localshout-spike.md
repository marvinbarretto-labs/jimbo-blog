---
title: "Council and civic initiative scraping for LocalShout (spike)"
date: 2026-10-12
description: "Council and civic initiative scraping for LocalShout (spike)"
tags: [localshout, scraper, report]
public: false
---

*Report — a research report (2026-10-12), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
Don't build a `source_type: 'council'`. The Healthy Hub is not an event feed. It is one prose page with three weekly drop-ins, and Watford's own `/events` list is empty. Treat it as a hand-curated, snapshot-backed aggregator source feeding a `series` collection. The discovery probe confirms that: both Watford URLs come back as snapshot only, at 20% confidence. Council and NHS sites are CMS-driven and fetchable, but none exposes structured event data (no JSON-LD, no iCal).

## From prior context
No prior-context notes were supplied. The only input was the vault note "feat: [Scraper] explore council/civic initiative scraping" (note_5aa442b5, groomed 2026-10-11). Its scope was to audit, probe, recommend and draft one config without enabling it.

## New findings
Fetched 2026-10-12 with a polite bot UA. These are static fetches only. No browser rendering except via the probe.

| Site | CMS | Fetch | robots.txt | Structured events? |
|---|---|---|---|---|
| watford.gov.uk | Jadu | 200, no blocking | None (returns the 404 page) | No. `/events` renders "Sorry, no content available" (`<body class="event-list">`, filter form, "Submit a new event"). Only RSS is `/rss/news`. No JSON-LD found on the Healthy Hub page |
| hertfordshire.gov.uk | Contensis 17.1 | 200 | Allow-list style, no blanket `Disallow: /` | Not found. Guessed events/news URLs 404; I didn't locate a real events section |
| hct.nhs.uk (Herts Community NHS Trust) | VerseOne v5 | 200 | `crawl-delay: 10` | `/events` 404s. No event listing found |
| westhertshospitals.nhs.uk | Concrete CMS | 200 | `crawl-delay: 10` | Not audited beyond the homepage |
| dacorum.gov.uk (bonus, neighbouring) | Sitefinity 15 | 200 | Not checked | Has some `ld+json`; not examined |
| hertsmind.org.uk, hertsfs.org.uk (charities) | — | Connection failed (HTTP 000) from here | — | **Not audited.** Retry from another network before drawing conclusions |

**Healthy Hub content.** The news article (Jul 2025) and `/healthy-hub` both carry the same prose schedule:
- Tue 10:00–14:00, Cussans House (Conservatory), WD18 6PJ
- Wed 10:00–14:00, Watford Town Hall, WD17 3EX
- Fri 09:00–13:00, Meriden Community Centre (Meriden Foodbank), WD25 9ET
- Free and no booking needed. Phone 01923 278445.

It is a page of text, not event cards.

**Probe output** (`onboard-source.ts`, dry-run, which wraps `discover-source.ts`; nothing written):
- `/healthy-hub` → `scrape/generic-snapshot`, 20%: "no structured source found — snapshot floor… drop-in times listed in `<ul>` but not structured as event cards."
- `/events` → `scrape/generic-snapshot`, 20%: alert "no content", no repeating event elements.
- The probe used a free OpenRouter model after a 404 on its first-choice model (`nvidia/nemotron-3-nano-30b-a3b:free`). The fallback worked, but the model slug needs updating.

**`source_type`.** `ScraperSourceStatus.source_type` is `'venue' | 'aggregator'` (`lib/scraper/types.ts:777`). A third value would ripple through the executor and admin UI for no extraction benefit.

## Recommendation
1. **No `council` source_type.** Use the existing `aggregator` pattern (`is_multi_venue: true`). Councils differ by CMS, not by extraction shape. Strictly speaking, snapshot extraction of one page is a source, not a pipeline.
2. **Healthy Hub = snapshot source plus a `series` collection.** Draft config below. The snapshot extractor must turn the prose into three weekly events (one per venue). It needs checking against a real run before enabling.
3. **Don't generalise from Watford.** The CMS differs on every site (Jadu, Contensis, VerseOne, Concrete). Onboard civic sources one by one via snapshot, not through a shared "council" template.
4. **Ask Watford directly.** Their `/events` has a "Submit a new event" form, and the list is empty. Submitting the Healthy Hub there, or asking the comms team, may yield a feed.
5. **NHS trusts: low priority.** No event listings, and `crawl-delay: 10` means a slow, polite fetch.
6. **Follow-ups.** Retry the charity audit from another network, and fix the stale OpenRouter slug in the page-analyzer.

### Draft config (DO NOT ENABLE) — from the probe's own output
```json
{
  "name": "Watford Healthy Hub",
  "slug": "watford-healthy-hub",
  "is_multi_venue": true,
  "config": {
    "source": "snapshot",
    "url": "https://www.watford.gov.uk/healthy-hub",
    "snapshot": { "originalUrl": "https://www.watford.gov.uk/healthy-hub" }
  }
}
```
Proposed event/collection shape (not created): collection `type=series`, "Watford Healthy Hub drop-ins", with three weekly recurring events (venues, times above), free and no booking.

## Sources
1. https://www.watford.gov.uk/news/article/790/watford-s-healthy-hub-drop-in-for-free-health-and-wellbeing-support — Healthy Hub announcement (schedule, venues)
2. https://www.watford.gov.uk/healthy-hub — Healthy Hub page
3. https://www.watford.gov.uk/events — empty events list (Jadu)
4. https://www.watford.gov.uk/rss/news — news RSS (Jadu CMS)
5. https://www.hertfordshire.gov.uk/robots.txt — Herts CC robots (Contensis meta on homepage)
6. https://www.hct.nhs.uk/robots.txt and https://www.westhertshospitals.nhs.uk/robots.txt — crawl-delay 10
7. localshout-next `scripts/scraper/discovery/discover-source.ts`, `scripts/scraper/onboard-source.ts`, `lib/scraper/types.ts:777`, `lib/scraper/templates/README.md` — local tooling, probe run 2026-10-12
8. Vault note note_5aa442b5 — scope and constraints

