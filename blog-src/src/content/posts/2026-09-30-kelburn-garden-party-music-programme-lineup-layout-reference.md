---
title: "Kelburn Garden Party Music Programme — lineup layout reference"
date: 2026-09-30
description: "Kelburn Garden Party Music Programme — lineup layout reference"
tags: [localshout, report]
public: false
---

*Report — a research report (2026-09-30), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

Kelburn organises its lineup with two independent filters — stage (11 options) and day (Thu/Fri/Sat/Sun) — over a single alphabetical grid of artist cards; each card is just a photo + name that links out to a dedicated artist profile page carrying the bio and day/stage/time detail. Spotify integration is a single festival-wide playlist mentioned in text, with no per-artist Spotify links anywhere — confirming the Spotify half of the original ask needs no further work, since LocalShout already ships its own official Spotify Web API artist enrichment.

## From prior context

None. `related` on this vault note is empty — no prior vault notes exist on this topic. The note's own groomed body (added 2026-09-30) already established the scope and the reason the Spotify half is moot: LocalShout's `localshout-next/scripts/enrichment/enrich-spotify.ts` and `.env.example` show official Spotify Web API artist enrichment already shipped (first commit 2026-02-15), superseding any need to reverse-engineer Kelburn's approach.

## New findings

**Entry point — `/whats-on/music-programme/`**
This is an atmospheric landing page, not the lineup itself. It has one hero artist photo, a genre-diversity blurb ("cutting-edge techno, electronica and bass music through jazz, dub, disco, house, fresh global club sounds to folk, trad, rock, punk, avante-garde pop and plenty in between"), a "2026 SPOTIFY Playlist" text mention with no visible link/embed captured by fetch, and one CTA: "Explore ARTIST PROFILES BY DAY AND STAGE" → `/whats-on/artists-by-name-day-stage/`.

**Lineup page — `/whats-on/artists-by-name-day-stage/`**
- **Two independent filters**, both dropdowns: a **Stage** filter (All, The Landing, Square Stage, Viewpoint Stage, Pyramid Stage, Sheela's Tent, The Saloon, The Plaisance Lounge, The Beech Plateau, Boat On The Hill, The Giant's Castle, Hometown Corner — 11 stages) and a **Day** filter (All, Thursday, Friday, Saturday, Sunday). Filtering is by stage AND by day, not a combined grid/timetable.
- **Presentation**: "Browse The Full Line-Up Here (A-Z)" — a responsive grid of clickable cards, sorted alphabetically by artist name, each card showing just a photo and the artist name as a linked heading. No time, stage, or genre badge is shown on the card itself.
- Each card links to an individual profile page, e.g. `/artist/acid-kantina/`.

**Artist profile page — e.g. `/artist/acid-kantina/`**
- Contains: artist name, a logo/photo, a short bio paragraph, and the day/stage/set-position detail folded into prose (e.g. "will be opening the Giant's Castle stage on Sunday").
- **No streaming or social links at all** on the profile — no Spotify, SoundCloud, Instagram, or Bandcamp links or embeds. Confirmed on a sample artist (Acid Kantina).

**Spotify integration, confirmed**: it is a single festival-wide playlist referenced by text ("2026 SPOTIFY Playlist"), not a per-artist link or embed. No per-artist Spotify wiring exists anywhere in the flow (landing page → lineup grid → artist profile). This matches the note's premise going in and closes the question — no further Spotify research is warranted.

## Comparison

| Aspect | Kelburn Garden Party | LocalShout (current) |
|---|---|---|
| Lineup filters | Stage dropdown (11 stages) + Day dropdown (4 days), independent, no combined grid | N/A — this is the reference gap |
| Artist card content | Photo + name only, no time/stage badge | — |
| Detail depth | Full bio + day/stage/set-position in prose, on a separate profile page per artist | — |
| Spotify | Single festival-wide playlist, text-only mention, no embed captured | Official Spotify Web API enrichment already shipped, per-artist |

## Recommendation

Use Kelburn's **two-dropdown (stage + day) filter over an alphabetical A-Z card grid** as the concrete reference point for LocalShout's lineup-browsing UX — it's a real, working pattern from a multi-day, multi-stage festival of comparable scale. Note its main weakness as a UX reference: cards carry zero day/stage/time metadata, forcing a click-through to the profile page just to see when/where an artist plays — worth improving on rather than copying. The Spotify side of this note is closed: no action needed, LocalShout's existing enrichment pipeline already exceeds what Kelburn does (single playlist, text-only) by wiring Spotify per artist via the official API.

## Sources

1. https://www.kelburngardenparty.com/whats-on/music-programme/ — landing page, confirms Spotify is a festival-wide playlist reference, not per-artist
2. https://www.kelburngardenparty.com/whats-on/artists-by-name-day-stage/ — the actual lineup page: stage + day dropdown filters, A-Z card grid
3. https://www.kelburngardenparty.com/artist/acid-kantina/ — sample artist profile page, confirms no per-artist streaming links
4. Vault note `note_e38cd9ab` ("Research Kelburn Garden Party Music Programme") — groomed scope and the LocalShout Spotify-enrichment context (`localshout-next/scripts/enrichment/enrich-spotify.ts`, `.env.example`)

