---
title: "Film entity schema audit — credits enrichment already implemented"
date: 2026-08-28
description: "Film entity schema audit — credits enrichment already implemented"
tags: [film-planner, tmdb-api, schema-audit, report]
public: false
---

*Report — a research report (2026-08-28), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

The credits enrichment feature — adding `director` and `cast` to film entities via TMDb's `/movie/{id}/credits` — was already fully implemented in `check_availability.py` (commit `ab31b2a`) and `enrich_collection.py` before this audit task was created. Of 160 personal watchlist films, 144 have director data and 145 have cast data. No schema changes or migrations are needed.

## From prior context

The vault note (note_41cc6408) instructed this audit to gate a backend implementation. The implementation was already complete at the time of the task's creation.

## New findings

### 1. Existing film entity schema

The personal watchlist (`film-ui/src/data/films.json`) already includes both fields:

| Field | Type | Population |
|-------|------|-----------|
| `director` | `string \| null` | 144/160 populated |
| `cast` | `string[]` | 145/160 populated (top 3 by TMDb cast ordering) |

The collection schema (`collections/*.json`) also includes these with identical shape.

### 2. TMDb API credentials and configuration

- **Key location:** `TMDB_API_KEY` env var — set as a GitHub Actions secret called `TMDB_API_KEY` in `.github/workflows/weekly.yml`, also loadable locally via `python-dotenv` from `.env` file (template at `.env.example`)
- **Endpoint defined:** `CREDITS_ENDPOINT = f'{TMDB_BASE_URL}/movie/{{movie_id}}/credits'` (line 32)
- **Base URL:** `https://api.themoviedb.org/3`
- **Rate limiting:** 300ms delay between requests (40 req/10s limit)
- **Confirmed accessible:** Script runs successfully weekly via Actions

### 3. `/movie/{id}/credits` endpoint response shape

```json
{
  "id": 550,
  "crew": [
    {"known_for_department": "Directing", "job": "Director", "name": "David Fincher"},
    {"known_for_department": "Writing", "job": "Screenplay", "name": "Jim Uhls"}
  ],
  "cast": [
    {"order": 0, "known_for_department": "Acting", "name": "Brad Pitt", "character": "Tyler Durden"},
    {"order": 1, "name": "Edward Norton", "character": "The Narrator"},
    {"order": 2, "name": "Helena Bonham Carter", "character": "Marla Singer"}
  ]
}
```

**Extraction logic** (lines 219-228 of `check_availability.py`):
- **Director:** iterates `crew` array for `member.get('job') == 'Director'`, takes first match → `details['director']`
- **Cast:** slices `cast` array to top 3 by `order` (ascending) → `details['cast']`

### 4. Required new fields

Already present — no additions needed.

| Field | Type | Notes |
|-------|------|-------|
| `director` | `string \| null` | Extracted from crew; null when no crew member has job "Director" |
| `cast` | `string[]` | Top 3 cast; empty when no cast data |

### 5. Migration / schema update needed

**None.** The fields already exist in the data file produced by `check_availability.py` and consumed by the React UI. The UI's `TrailerModal` component already handles rendering them (confirmed in the film detail modal — we see director and cast rendering in the test film's data).

### 6. Edge cases noted

- **2 films with TMDb IDs still missing director:** "Levellers" (ID 310731 — music documentary, no directing credit in TMDb crew) and "The Good Place" (ID 807068 — a TV series, not a film; TV shows on TMDb don't have a "Director" crew role). These are inherent data gaps, not implementation gaps.
- **14 films not found on TMDb** (`not_found_on_tmdb: true`) — these legitimately have no director/cast as there's no movie record to query.

## Recommendation

Close the task as already implemented. The audit confirmed everything is in place with no migration needed. If Marvin wants to backfill the missing directors for the 2 edge-case films, that's a manual edit — not a code change.

## Sources

1. [check_availability.py lines 32, 161-234](https://github.com/marvinbarretto/film-planner/blob/main/check_availability.py) — credits endpoint definition and get_movie_details function
2. [film-ui/src/data/films.json](https://github.com/marvinbarretto/film-planner/blob/main/film-ui/src/data/films.json) — actual film data with director/cast populated
3. [TMDb API docs — /movie/{id}/credits](https://developers.themoviedb.org/3/movies/get-movie-credits) — endpoint response shape
4. [CLAUDE.md](https://github.com/marvinbarretto/film-planner/blob/main/CLAUDE.md) — project conventions and TMDb integration docs
5. [.env.example](https://github.com/marvinbarretto/film-planner/blob/main/.env.example) — TMDb API key config
