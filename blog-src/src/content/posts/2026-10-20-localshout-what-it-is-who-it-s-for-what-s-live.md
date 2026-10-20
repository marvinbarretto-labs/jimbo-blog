---
title: "LocalShout: what it is, who it's for, what's live"
date: 2026-10-20
description: "LocalShout: what it is, who it's for, what's live"
tags: [localshout, report]
public: false
---

*Report — a draft (2026-10-20), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

This is the cold-read version of LocalShout: what it is, who it's for, how it's built, and what is live today. It isn't a launch post. I haven't launched, and I'll say why further down.

You can use it now at [localshout.co.uk](https://localshout.co.uk).

## What it is

LocalShout tells you what's on near you. Gigs, comedy, theatre, community stuff, in Watford first. It's a curated list, not a firehose. The reader can play a track from an act before deciding to go, and can save or follow things so the good ones come back to them.

The sentence I keep coming back to is "I stop missing local events I'd have wanted to go to." That's the whole product. The rest is machinery in service of it.

## Who it's for

A busy local who'd rather be told than dig. Not someone who lives on social media, and not someone who has to follow the right account on the right day to find out about a gig.

That's the problem. Discovery on social platforms fails even for heavy users, because you have to already follow the account, catch the post before the algorithm buries it, and be on the app that day. Missing things is the default.

It's worse for small acts. I counted in August: of 3,667 artists on published events, 40% had no link of any kind. That's an upper bound, since "we found nothing" can't tell an act with no presence from our matcher giving up. But it's enough to say that for a lot of local acts there's no feed to miss. Unknown bands are where this does the most good.

LocalShout isn't trying to beat Facebook or Instagram. It indexes the facts (what, when, where, still on) and links out to the act's own channels for video and photos. Linking out is a feature. It's better for the reader and sends traffic to the act.

## How it's built

Next.js 15 and React 19 on Vercel, Supabase for Postgres and auth, Capacitor wrapping it for Android and iOS. Nothing exotic.

The interesting part is the data layer, because the moat isn't the UI. Listings come from messy, inconsistent sources. A pipeline on my VPS scrapes them, an LLM extracts the structure, and the results are deduplicated and enriched with links and media. Extraction is per platform, never per venue, so I'm not writing a bespoke scraper for every pub with a Facebook page. Two years ago that wouldn't have been affordable. In an early test of reading events out of emails, Haiku got 102 out of 102.

The first commit was 17 January 2026. The repo is at roughly 3,000 commits and version 0.4.375. A lot of that is me working with AI agents on a codebase with real rules: PR standards, a vision doc with numbered claims, a rubric a feature proposal has to pass, and an ADR-style log of what's been decided and rejected. Writing down what the product won't do has saved more time than any tooling.

## What's live

- The site, at localshout.co.uk, with curated event feeds and sections you can switch on and off. Civic and support content is fully indexed but off by default on a first visit, so equal coverage, unequal prominence.
- Save and follow on events and followable entities.
- Previews, so you can hear an act before you commit. About half the artists on the site have playable media, which means precision and coverage matter a lot here.
- In-app account deletion and one-click unsubscribe on email.
- The ingest pipeline running continuously: a five-minute scrape scheduler, a fifteen-minute batch dispatcher, a daily heavy batch.

## What isn't

I'm not calling it shipped. My own launch checklist still has every box unchecked: ICO registration, privacy policy and terms, analytics, error monitoring, a soft launch with testers. The ship window has slipped twice. It's now November 2026.

And the plain risk: the persona is a mirror. Right now I'm the only confirmed user. That's only disproved when someone who isn't me uses it twice. The north-star metric is weekly readers who save or follow something they didn't already know about, and I can't yet measure the "didn't already know" part.

The site is live and used, and I'm still building it. I'd rather say that than claim a launch I haven't earned.

## Next

Clear the launch checklist, get a handful of testers who aren't me, then find out whether anyone else wants this. The unglamorous bits are the ones that decide it, and one flat-wrong listing costs more trust than ten good ones earn, so correction and freshness get as much attention as the front page.

[Try it](https://localshout.co.uk). If it shows you something you'd otherwise have missed, that's the point.

