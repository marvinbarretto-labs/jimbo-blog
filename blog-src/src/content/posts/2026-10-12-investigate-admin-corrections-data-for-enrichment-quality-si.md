---
title: "Investigate admin corrections data for enrichment quality signals"
date: 2026-10-12
description: "Investigate admin corrections data for enrichment quality signals"
tags: [localshout, report]
public: false
---

*Report — a research report (2026-10-12), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
The table is not a correction log in practice: of 29,556 rows (4 Apr to 12 Oct 2026), 231 (0.8%) are admin edits and 29,325 are enrichment scripts' own writes. Admin corrections are too sparse to rank enrichment sources reliably, and the suspected "YouTube is the worst" hypothesis is not supported (3 of 2,199 YouTube-enriched artists were later touched by admin). The one real signal is venue geocoding: addresses are the most-corrected admin field. `not_artist` never appears in the data.

## From prior context
Vault note "Investigate admin corrections data for enrichment quality signals" (note_744600d8) supplied the five questions, starter SQL, and the hypothesis that YouTube videos lead corrections. It says a later migration "added the source and entity columns". That is slightly off: `source` was in the original `20260403190000_admin_corrections.sql`; `20260624120000_..._source_entity.sql` only widened the `entity_type` check to allow `'source'`. Note: the note says ~2 weeks of data; there are ~6 months (first row 2026-04-04).

## Method
Read-only: `SELECT *` from `admin_corrections` via the Supabase REST API (service role, GET only), paged 1000 rows at a time, 29,556 rows; aggregated locally in Python. Equivalent SQL for each figure is the note's three starter queries plus `GROUP BY` on `entity_type`, `field`, `detail->>'tag_slug'`. The REST route was used because no psql credentials were available. No writes.

## New findings (all counts from the table)

**Volume by source and action**

| source | action | rows |
|---|---|---|
| enrichment_events | field_edit | 13,252 |
| enrichment_youtube | field_edit | 10,371 |
| enrichment_events | tag_add | 3,406 |
| enrichment_venues | field_edit | 1,919 |
| enrichment_lemonrock | field_edit | 322 |
| admin_manual | field_edit / status_change / tag_remove / tag_add / rule_create | 130 / 31 / 24 / 24 / 22 |
| enrichment_spotify | field_edit | 30 |
| purge_foreign_venue_data | field_edit | 25 |

Entities: 16,795 event, 10,752 artist, 2,009 venue rows. Monthly volume is lumpy (3,305 rows on 15 Jul; 2,971 on 21 Jun), which is batch runs. Admin rows: 86 in Apr, 42 May, 21 Jun, 71 Jul, 0 Aug, 11 Sep, none in Oct.

**Q1. Which source is most admin-corrected?** Using the note's self-join (enrichment write followed later by an admin_manual edit to the same entity and field): `enrichment_venues`/address 6, `enrichment_events`/tags 3. Nothing else registers. At entity level: 11 of 510 enriched venues (2.2%), 30 of 7,968 enriched events (0.4%), 3 of 2,199 YouTube-enriched artists (0.1%) were touched by admin. YouTube is the *least* corrected, not the most. Caveat: low admin correction may reflect low admin review, not high quality.

**Q2. Most-corrected fields (admin_manual, 231 rows).** Event tags 70, event status 51, venue address 51, venue status 9, artist status 7, event title 6, venue lat/lng 4, artist video_url_1..5 plus `video_url_*` about 14 (3 of the `video_url_*` rows are "(cleared via report)", driven by `wrong_video_report`). Note 11 of the event status rows are one batch with reason "St Albans City away fixture published at Clarence Park by a single-venue source (DEC-19)", a source-rule problem, not a model problem.

**Q3. Venues/artists with highest correction rates.** No concentration: the most-corrected venue has 3 admin rows, the most-corrected artist 6, the most-corrected event 7. There is no scraper-drift hot spot visible at this volume.

**Q4. `not_artist`.** Zero rows contain the string anywhere (`old_value`, `new_value`, `detail`). Admin artist-status changes total 7 (5 draft to published, 2 published to draft). No quality signal for LLM artist extraction exists in this table; the action is either not logged here or not used.

**Q5. Tag add vs remove.** Enrichment added 3,406 tags (top: music 518, family 154, animation 147, rock 139, covers 129, imax 122, band 119, blues 108). Admin added 24 (music 9, covers 3, quiz 2) and removed 24 (`free` 8, music 3, nightlife 2, club 2). Admin also created 22 tag rules: 11 "block" (`free` 6, theatre, club-night, talks, nightlife, celebration) and 11 "force" (music 3, covers, jazz, quiz, family, walking, talks, science, workshop). Pattern: the model over-applies `free` (8 removals, 6 blocking rules, the clearest repeated miss) and under-applies `music` (9 admin adds + 3 force rules). Only 3 enrichment-written tag rows were later admin-edited, so this is directional, n=24.

## Recommendations
1. **Stop treating this table as a quality score yet; fix what it records.** 99.2% of rows are enrichment writes with no admin follow-up, so source ranking is unanswerable. Log admin review decisions (confirm/reject) on enriched rows, or the table cannot answer Q1 at all. Evidence: 231 admin rows vs 29,325 enrichment rows.
2. **Tighten `free` tagging.** It is the most-removed tag (8 of 24 admin removals) and has 6 block rules, so remove or gate it in the prompt for tag extraction (relevant to the sibling walk/exercise tag note, note_ac786b66). Conversely add a venue-type prior for `music`: 9 admin adds and 3 force rules.
3. **Spot-check venue geocoding before trusting new addresses.** Address is the top admin-corrected field on venues (51 edits; 6 follow an enrichment_venues write, 11/510 venues touched). Do not spend effort on YouTube channel filtering: 3 of 2,199 artists were touched.

## Sources
1. `localshout-next/supabase/migrations/20260403190000_admin_corrections.sql`: schema, actions and constraints.
2. `localshout-next/supabase/migrations/20260624120000_admin_corrections_source_entity.sql`: widened entity_type check only.
3. `localshout-next/lib/admin/queries/corrections.ts`: existing query code.
4. Vault note "Investigate admin corrections data for enrichment quality signals" (note_744600d8): questions and starter SQL.
5. Live `admin_corrections` table, 29,556 rows read 2026-10-12.

