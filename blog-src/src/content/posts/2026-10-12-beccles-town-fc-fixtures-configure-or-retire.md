---
title: "Beccles Town FC fixtures: configure or retire?"
date: 2026-10-12
description: "Beccles Town FC fixtures: configure or retire?"
tags: [localshout, report]
public: false
---

*Report — a research report (2026-10-12), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**Retire.** Beccles Town FC does have a fixtures listing (becclestownfc.org.uk, a TeamExpert site with home and away fixtures in plain HTML), but its `robots.txt` has `User-agent: * / Disallow: /`, and LocalShout's own discovery probe refuses every URL on it. Scraping it would break LocalShout's ethical-fetcher rules. There is no iCal, RSS or JSON feed to use instead.

## From prior context
- Vault note `note_030bf5a4` ("Fix empty-URL scrape source: Beccles Town FC Fixtures"): source `0ea73da3-f9de-4e66-87ba-b70c710fc279` has `url: null` and `scrape/no-config`, and was auto-parked after 10 failures. The venue `beccles-town-fc` has no URL either. The default is to retire if nothing is scrapable.
- The note says Marvin applies the verdict, so nothing was edited, unparked or deleted.

## New findings
- **Club site:** https://www.becclestownfc.org.uk/. The footer says it is built on the TeamExpert Football Club website builder.
  - Fixture pages: `/fixtures/1025` (seniors), `/results/1038` (all teams, with unplayed matches as fixtures), `/gct/1039` (youth home fixtures).
  - The pages list date, time, competition and team in HTML, with home and away both shown. Examples: Wed 30 Sep 26 7:30pm Beccles Town v Easton FC (Anglian Combination Premier League, home); Sat 26 Sep 26 2:15pm Beccles Town v Norton Athletic (home). Reserves and A-team fixtures are mixed in.
  - No iCal, RSS or JSON feed, and no embedded FA Full-Time, Pitchero or ClubSpark widget was found on the homepage.
  - The dates have inconsistencies. One match dated 29 Aug 26 has a URL slug containing 20260816.
- **Robots.txt** (fetched 2026-10-12): the named crawlers (Googlebot, bingbot, Teoma, facebookexternalhit) are allowed with a 20-second crawl delay, but the catch-all group is `User-agent: *` / `Disallow: /`. A custom scraper falls under the catch-all.
- **Discovery probe evidence** (`discoverSource` from `localshout-next/scripts/scraper/discovery/discover-source.ts`, run read-only with no DB writes; the batch `probe-sources --live` was not used because it persists to `source_discovery_candidates`):

| Candidate URL | Probe result |
|---|---|
| https://www.becclestownfc.org.uk/ | `URL disallowed by robots.txt` |
| https://www.becclestownfc.org.uk/fixtures/1025 | `URL disallowed by robots.txt` |
| https://www.becclestownfc.org.uk/results/1038 | `URL disallowed by robots.txt` |

- **Other presence:** the club has an X account (@BecclesFC) and Facebook, which are not scrapable. FA Full-Time lists the club's teams (e.g. "Beccles Town FC 'A'", Ladies) but is a league-wide system, and I did not probe it. It would need its own terms and robots review, and it mixes in away games and non-home venues.
- **Footnote on the venue:** the home ground is College Meadow, Beccles. The first team plays in the Anglian Combination Premier Division, and the reserves in Division 2.

## Comparison
| Option | Result |
|---|---|
| Configure on the club site | Blocked by robots `Disallow: /`. Not allowed by LocalShout's ethical fetcher. |
| Configure on FA Full-Time | Unprobed. It would need a separate compliance review and brings noisy league-wide data. |
| Retire | Clean. Removes the red venue-health entry. |

## Recommendation
**Retire.**
1. Delete source `0ea73da3-f9de-4e66-87ba-b70c710fc279` from `/admin/sources` or `/admin/venue-health`.
2. **Venue:** delete `beccles-town-fc` as well, provided it has no other sources and no events attached. It has no URL and no data feed, so it would sit red again. If you want it kept as a manual or editorial venue, keep it and set its status so it doesn't show on venue-health. I did not check for events attached to the venue.
3. Revisit only if the club emails permission or changes its robots.txt. A request to the club would be the route to a feed. If that ever happens, the config would be `scrape/generic-template-html` on `/results/1038`, but only with permission and at the 20-second crawl delay.

## Sources
1. https://www.becclestownfc.org.uk/ — club site (TeamExpert), fixtures and results pages
2. https://www.becclestownfc.org.uk/robots.txt — catch-all `Disallow: /`
3. https://en.wikipedia.org/wiki/Beccles_Town_F.C. — club and league background
4. https://fulltime.thefa.com/displayTeam.html?id=874985125 — FA Full-Time team page (Beccles Town FC 'A'), not probed
5. Vault note note_030bf5a4 — task scope and prior context
6. localshout-next `scripts/scraper/discovery/discover-source.ts` — probe output above

