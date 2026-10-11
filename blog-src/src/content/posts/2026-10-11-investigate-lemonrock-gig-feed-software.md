---
title: "Investigate Lemonrock gig feed software"
date: 2026-10-11
description: "Investigate Lemonrock gig feed software"
tags: [lemonrock, localshout, report]
public: false
---

*Report — a research report (2026-10-11), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
Lemonrock's "gig feed software" is not an API or RSS feed. It is an iframe widget that lets a band or venue show its own gigs on its own website. It cannot be used for a third-party aggregator like LocalShout. Recommendation: send the JIM-7188 email; do not switch to a feed. Their ToS also bans automated scraping outright (s.3), which is worse than the gig-copying clause the ticket quotes.

## From prior context
- Vault note "Investigate Lemonrock gig feed software" (note_636ac64d): ToS bars copying gig info except via the gig feed software or share icons. The nightly scrape (AUTOMATION.md step 7, enrich-lemonrock) is live. JIM-7188 (outreach email) is conditional on this finding.

## New findings (public pages only; no probing)
1. **Feed = iframe widget for own listings.** Gig Feeds Q/A: "Bands and venues can create Gig Feed widgets for their own sites." Output "is an iframe" that "gets its contents automatically from Lemonrock." No JS embed, RSS, JSON or API is mentioned [3]. Options are display only: time period, layout, CSS and token templates. An iframe is not machine-readable data, and it only serves a member's own gigs.
2. **Not a data source for us.** LocalShout is neither a band nor a venue on Lemonrock, and a nightly cross-venue ingest does not fit an "own site" widget. Membership page mentions only help "configuring gig feeds" and a spreadsheet export of one's own gig diary (Bands/Artists from £4.50/month) [4]. Neither gives us a bulk feed.
3. **ToS s.15 (Exceptions)** [1]: "Gig information is available as listings via our gig feed software, and via the share icons on gig pages." / "Except for these mechanisms, please do not copy gig information from Lemonrock ... without Lemonrock's express permission." / "All permitted data sourced from Lemonrock must be attributed to 'Lemonrock Gig Guide'".
4. **ToS s.3 is stricter** [1]: prohibits "Automated data extraction, web scraping, indexing, crawling, data mining" and "any robot, spider, scraper, script, or other automated means to access, copy, or monitor" without "express prior written permission". They reserve the right to block IPs, report to hosts, and claim damages including "violation of UK Database Rights". The scrape is a breach of s.3 regardless of the gig-feed exception.
5. **Contact:** editor@lemonrock.com [1].

## Comparison
| Option | Viable? | Why |
|---|---|---|
| Switch to official feed | No | Own-site iframe only; no API/RSS |
| Email for permission (JIM-7188) | Yes | ToS names "express permission" as the route; s.3 says "prior written permission" |
| Disable scrape, use venue data | Yes, fallback | Zero legal exposure |

## Recommendation
No official feed fits. Send the JIM-7188 email to editor@lemonrock.com asking for written permission (or a data licence) with attribution as "Lemonrock Gig Guide". Meanwhile, pause the nightly enrich-lemonrock step: s.3 breach plus the IP-ban and database-rights threats make continued scraping the highest risk in the stack, and venue-direct data is the fallback. Resume only on written permission. Pausing is a separate decision for Marvin; I changed nothing.

## Sources
1. https://www.lemonrock.com/terms.php — Terms of Use, s.3 and s.15
2. https://www.lemonrock.com/ — site navigation (no API/RSS/widget links)
3. https://www.lemonrock.com/gigfeedhelp.php — Gig Feeds Q/A
4. https://www.lemonrock.com/membership-benefits.php — membership benefits
5. Vault note note_636ac64d

