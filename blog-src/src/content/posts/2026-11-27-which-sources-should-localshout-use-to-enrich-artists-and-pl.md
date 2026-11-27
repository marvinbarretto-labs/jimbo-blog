---
title: "Which sources should LocalShout use to enrich artists and play previews?"
date: 2026-11-27
description: "Build an ID spine on MusicBrainz and Wikidata first, then choose preview sources by their terms."
tags: [research, localshout, report]
public: false
---

*Report — a research report (2026-11-27), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

LocalShout should build an ID spine first and pick audio previews second. Use [MusicBrainz](https://musicbrainz.org/doc/MusicBrainz_API) as the hub, because it lists an artist's own site, Wikidata, Bandcamp, SoundCloud, socials, Apple and Deezer pages. Use Wikidata as the second hop. Match an artist only on a single exact-name hit, or on a link we already hold. For previews, Apple's iTunes lookup (30 seconds, no key, stream only, with a badge) is the best sanctioned source. Put Bandcamp, SoundCloud, YouTube and Spotify embeds beside it. Don't build on Deezer previews or Last.fm unless LocalShout earns no revenue or a licence is agreed. The terms below are my reading, not legal advice, and "not checked" means I could not confirm it from an official page.

## Where LocalShout stands

The `artists` table already has columns for most links: YouTube, Spotify, Apple Music, Bandcamp, SoundCloud, a website, socials, and a blurb. It has no column for any external ID, such as a MusicBrainz ID, a Wikidata ID, or a Deezer or Apple artist ID. That gap is what the spine fills. I did not check the genre and bio tables or the enrichment queue table.

Coverage is thin. Of 7,192 published artists in the 22 November check, 2,896 have a YouTube channel, 35 have Spotify, one has SoundCloud, one has Apple and none has Bandcamp. That leaves 3,713 artists (52 per cent) with nothing playable.

The existing enrichers live in `scripts/enrichment/`. The YouTube one searches with Playwright and scores matches with an LLM. The Spotify one is built but unscheduled since 6 August, because its LLM match check spends the shared 1,000-a-day OpenRouter free pool, and 4,763 artists are pending. No code today calls MusicBrainz, Wikidata, Deezer, Apple, Discogs, Last.fm, Bandsintown or Songkick.

## Why names are not enough

Earlier Jimbo checks settled this, so I did not repeat them. Name clashes with MusicBrainz were wrong four times out of eight. On preview coverage, 59 per cent of music acts have one exact match with a preview (Apple 53 per cent, Deezer 38 per cent). But precision was only 17 of 30 clearly right, which is 57 to 81 per cent depending on how you count. Every wrong match was a covers act or a DJ. That is under the 90 per cent bar, so matches should rest on IDs, not names.

One more finding shapes the scope. Of 239 email "artists", 118 were speakers. So enrichment should look up music and comedy acts only.

## The hub: MusicBrainz and Wikidata

MusicBrainz gave links for most matched music acts in the 22 November sample of 73: a site for 39, Wikidata for 35, Spotify for 24, Deezer for 15, YouTube for 13, Apple for 11, SoundCloud for 6 and Bandcamp for 2. It is good for gigging acts with releases and thin for covers bands and open-mic acts. Only 73 of 121 music acts matched at all.

It needs no key, but it allows [one request a second per IP](https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting), wants a contact User-Agent, and returns 503s if you go faster. The 22 November check suggests about 1.6 seconds in practice. A useful trick is the reverse lookup, `/ws/2/url?resource=`, which takes up to 100 links per call. Where we already hold a trusted link, it finds the MusicBrainz ID from the link rather than from a name.

The [licence](https://musicbrainz.org/doc/About/Data_License) matters. Core data is CC0. Tags, ratings and annotations are CC BY-NC-SA. Commercial use of the API needs a [MetaBrainz tier](https://metabrainz.org/supporters/account-type), and the "Stealth Start-Up" tier starts at $0. Whether LocalShout's links-only use counts as commercial: not checked.

[Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing) adds an official site, an image, genre and country, under CC0 for structured data. Commons images carry their own licences, which I did not check. Coverage is poor for small acts, since only notable ones have an item. The [query service](https://www.mediawiki.org/wiki/Wikidata_Query_Service/User_Manual) gives 60 seconds of processing per 60 seconds per client. The Wikidata property that holds the MusicBrainz ID: not checked.

## Where previews can come from

| Source | Preview? | Terms in short | Verdict |
|---|---|---|---|
| Apple iTunes lookup | 30 s `previewUrl`, no key | Stream only: no download, save or cache. Attribution plus an Apple Music badge and link. About 20 calls a minute. | Best sanctioned source |
| Deezer | 30 s MP3, URLs expire in about 15 min | [Terms](https://developers.deezer.com/termsofuse): non-commercial only, no revenue even from ads without a written agreement, no local database of content | Skip unless licensed |
| Spotify | Not from the API for new apps (removed 27 Nov 2024) | Embed instead; embed rules not checked | Embed only |
| Bandcamp | Embed only, pasted by the act or a fan | No public API. Embedding a third party's track: not checked | Embed where we hold a link |
| SoundCloud | Embed widget | API terms: no caching, no ads around content. Widget terms: not checked | Embed where we hold a link |
| YouTube | Embedded video player | Player must not be covered by overlays | Already our biggest set |

Apple's [Search API](https://performance-partners.apple.com/search-api) says previews are for streaming only and not for "independent entertainment value". A tap-to-play taster that links out looks fine, but Apple has not ruled on it. One forum report of `/search` returning 404s in April 2026 is unconfirmed.

Spotify has changed a lot. Its [November 2024 changes](https://developer.spotify.com/blog/2024-11-27-changes-to-the-web-api) removed preview URLs, recommendations, related artists and audio features for new apps. [Development mode](https://developer.spotify.com/documentation/web-api/concepts/quota-modes) now allows 5 allowlisted users, and the owner needs Premium. The older 25-user figure is out of date. The [February 2026 guide](https://developer.spotify.com/documentation/web-api/tutorials/february-2026-migration-guide) says batch endpoints and `popularity` went and search `limit` is now 10. One Jimbo vault note still says 25 users and needs fixing. Its conclusion holds, because a playlist written only to our own account never hits the cap.

The [Bandcamp developer page](https://bandcamp.com/developer) says registration is for labels and merch partners only, and [embedding](https://get.bandcamp.help/hc/en-us/articles/23020711574423-How-do-I-embed-a-player-on-my-site) is the act's or fan's job. Don't scrape. Bandcamp has real small-act presence, but we hold none of the links, and MusicBrainz has Bandcamp for only 2 of 73.

## What to leave for later

Discogs, Last.fm, Bandsintown and Songkick add facts or tour dates, not audio, and each has a licence gate. Last.fm is [non-commercial only](https://www.last.fm/api/tos) without an agreement. Songkick is gated behind a partner agreement and fee, and Wikipedia says from $500 a month. That is secondhand, and I did not check Songkick's own page. I could not open Discogs' terms (403), and I only saw Bandsintown's [data terms](https://corp.bandsintown.com/data-applications-terms) as a search snippet. Coverage for all four is not measured. Revisit them when a specific feature needs one.

## The suggested order

First, add `musicbrainz_id` and `wikidata_id` to `artists`, and the Deezer and Apple IDs as they appear, with no new behaviour. Then write a MusicBrainz enricher on the YouTube enricher's queue pattern. It should take only one exact match, or one that shares a link we already hold, and send clashes to the existing link check. It would fill the existing columns for Bandcamp, SoundCloud, Apple, website and socials. Wikidata comes next, for image, genre and a verified website, using CC0 data only.

Only then add previews, one provider at a time, keyed by ID. Apple goes first, fetching a fresh preview URL at play time and never storing audio. Embeds follow for links that now exist. After that, re-run the two 23 November checks on ID-based matches, against the 90 per cent bar, and re-count the 3,713 with nothing playable.

## What to do next

Seven questions need Marvin's answers. Three decide the most. Will LocalShout carry ads, sponsorship or sales? That decides Deezer outright and changes how MusicBrainz and Apple read. Is an embed acceptable, given that it carries the provider's terms but looks like the "unprofessional YouTube treatment" one vault note complains about? Or does he want a custom 30-second Apple player with the badge, the link and no caching?

Then two small actions. Approach MetaBrainz about a tier before the first production run, since the Stealth Start-Up tier is $0. And consider emailing Apple to confirm preview-only use, since they have not ruled on it.

The remaining questions are lesser. Should a preview show only when an ID or the act's own link confirms it? Does Jimbo's "Sound of Watford" playlist replace in-app previews or sit beside them as marketing? Should speakers and authors stay out of enrichment entirely?

