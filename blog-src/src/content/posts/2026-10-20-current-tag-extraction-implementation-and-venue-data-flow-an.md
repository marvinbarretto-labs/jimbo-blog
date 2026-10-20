---
title: "Current tag extraction implementation and venue data flow analyzed"
date: 2026-10-20
description: "Current tag extraction implementation and venue data flow analyzed"
tags: [localshout, report]
public: false
---

*Report — a research report (2026-10-20), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

Verified against `localshout-next` master as checked out locally (13 commits behind origin; file history checked with `git log`). Line numbers are from that checkout.

## Summary

The vault note's premise is stale. Commit `262522c5` ("give extractTags venue hints for title-only events (#649)", 2026-10-05) already added `venue?: VenueMetadata` to `ExtractTagsInput` and a venue lookup to the gate. The remaining gap is the **batch pre-extraction path**, which runs before the pipeline and never passes a venue. Most events are tagged there, so the gate's hint rarely fires. JIM-5485 should target that path, not re-add the hint.

## From prior context

The vault note (*Current tag extraction implementation and venue data flow analyzed*, groomed 2026-10-02) says `extract-tags.ts` has "no venue references" and the gate "calls it near line 90". Both were true at 2026-10-02 and are false after #649 landed on 2026-10-05. Its pointers to `match-venue-by-name.ts` as the venue source and to `gates/index.ts` for gate order are still correct.

## New findings

### 1. Prompt and `ExtractTagsInput` (`lib/ai/extract-tags.ts`)
- `ExtractTagsInput` (L102-107): `title`, `description?`, `artistNames?`, `venue?: VenueMetadata`.
- `VenueMetadata` (L97-100): `name?`, `tags?: string[]`. The comment at L93-96 says the `venues` table has no genre/type column, so `tags` are the venue's most common event tags.
- Static rules prompt is built by `buildBasePrompt` (L36-90) with the top-200 preferred tag slugs from `getPreferredTagSlugs()` (L141).
- Per-event text is `Title: … \nDescription: … [\nArtists: …][venue hint]` (L161).
- The venue hint is added only when `isSparse = !description && no artists` (L149) and the venue has a name or tags (L151-159). It is worded as a weak hint that defers to the title.

### 2. Venue fields available before the gate
- The pipeline context has only `venue_id` and `venue_name` on the event. No genre or type field exists.
- `venue_id` is set by `matchVenueByNameGate` (`gates/match-venue-by-name.ts` L117-122 when confidence >= 0.95, shell venues L165, nulled at L151/178/197). Single-venue scrapers get it from the executor instead (L43). `applyDefaultRulesGate` fills an empty venue (`apply-default-rules.ts` L46-59).
- Gate order, `pipeline/config.ts` L51-55: `matchVenueByNameGate` → `applyDefaultRulesGate` → `propagateSiblingTagsGate` → `extractTagsGate` → `applyTagRulesGate`. So venue is resolved before tagging inside the pipeline.

### 3. Gate call site (`gates/extract-tags.ts`)
- `loadVenueHint` (L40-68) queries `venues.name` plus the last 50 non-cancelled events' tags for that venue and keeps the top 5 (`VENUE_HINT_TAG_LIMIT`, L34). Errors become no hint.
- Call site: sparse check and lookup at L126-129, `extractTags({... venue})` at L132-137.
- Early returns at L77-111 skip the LLM entirely when `event.tag_slugs` is already populated (`skippedReason: 'pre-tagged-in-batch'`).

### 4. The gap: batch pre-extraction runs first, without venue
- `SourceExecutor` Phase 3 (`executor/SourceExecutor.ts` L629-636) calls `extractTagsBatch` (L803) before the pipeline, unless `skipBatchTagExtraction` is set. `BatchEventInput` carries only title, description and artistNames (`lib/ai/extract-tags-batch.ts`; `grep venue` finds nothing in the file).
- The single-event branch (L187) and the per-event fallback (L307) call `extractTags` with no `venue`.
- Result: a title-only event gets tagged in batch from the title alone, `tag_slugs` is set, and the gate returns `pre-tagged-in-batch` at L77-86. The venue hint only runs for events the batch skipped (those with `baseTags`, L811-814) or when batch extraction is disabled.
- At batch time, multi-venue events have no `venue_id` yet, because venue matching happens later in the pipeline. Only single-venue sources could supply a venue there.
- Scripts `scripts/backfill-untagged-events.ts` (L116, L135) and `scripts/backfill-tag-reextract.ts` (L125) also call `extractTags` without a venue.

### Integration points for JIM-5485
| Option | Change | Catch |
|---|---|---|
| A. Defer title-only events from batch | In `SourceExecutor.extractTagsBatch`, skip sparse events so the gate tags them after venue matching | Loses batching for those events, so more LLM calls |
| B. Pass venue into batch | Add `venue?` to `BatchEventInput`, render it in the batch prompt | Only works for single-venue sources; multi-venue has no `venue_id` yet |
| C. Re-tag sparse events post-venue | After matching, rerun the LLM for sparse events only | Extra calls, same cost as A |
| D. Backfill scripts | Pass `loadVenueHint` result in both scripts | Does not affect new scrapes |

## Recommendation

Do A. It reuses the gate's existing `loadVenueHint` and sparse check unchanged, and it is the only option that works for multi-venue aggregators, where venue is unknown until after batch. Export `loadVenueHint` and share it with the backfill scripts (D) as a follow-up. Before starting, measure how many recent title-only events show `skippedReason: 'pre-tagged-in-batch'` in `tag_extraction_outcomes`. If the count is small, the gap is not worth fixing. Also update the vault note and JIM-5485 text, which still describe the pre-#649 state.

Not done: this is a read-only analysis. No code was changed. I did not save a doc in the `localshout-next` repo (the AC asks for `docs/architecture/extract-tags-venue-flow.md`); this report is the publishable copy, and the repo is 13 commits behind origin.

## Sources
1. `localshout-next/lib/ai/extract-tags.ts` L36-161: prompt, input types, sparse venue hint.
2. `localshout-next/lib/scraper/pipeline/gates/extract-tags.ts` L34-137: `loadVenueHint` and gate call site.
3. `localshout-next/lib/scraper/pipeline/config.ts` L51-55: gate order.
4. `localshout-next/lib/scraper/executor/SourceExecutor.ts` L629-636, L803-830: batch pre-extraction.
5. `localshout-next/lib/ai/extract-tags-batch.ts` L177-200, L295-320: batch calls without venue.
6. `localshout-next` git commit `262522c5` (2026-10-05): added the venue hint.
7. Vault note `note_6599bf3c`: the original task and its stale premise.

