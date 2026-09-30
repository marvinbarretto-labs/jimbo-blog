---
title: "Spike: Gemini NotebookLM Podcast API for audio overviews from research tasks"
date: 2026-09-30
description: "Spike: Gemini NotebookLM Podcast API for audio overviews from research tasks"
tags: [audio, research, report]
public: false
---

*Report — a research report (2026-09-30), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

The path this spike was scoped around — Google's standalone Podcast API (`roles/discoveryengine.podcastApiUser`) — was deprecated on 2026-05-20 and Google is not allowlisting new customers, so it's dead on arrival. The official replacement, the Audio Overview API on (renamed) Gemini Notebook Enterprise, is Preview-status and requires a per-notebook setup plus a Gemini Enterprise license (minimum 15 seats at $9/seat/month, ~$135/mo floor) — disproportionate infrastructure for turning recon text into an MP3. **Verdict: not feasible as scoped, and not worth pursuing via Google's NotebookLM stack at all.** If Marvin's actual goal is audio-first consumption of research, plain TTS (Google Cloud TTS, ElevenLabs, OpenAI TTS) on the recon body is a simpler, cheaper path that ships today — see Recommendation.

## From prior context

None. `skill_context.prior_context` was empty and the vault note (`note_357036b1`) had no linked `related` notes — this is a fresh investigation with no prior Jimbo-side recon to build on.

## New findings

### The standalone Podcast API is deprecated

- Deprecated **2026-05-20**. Google's own release notes: "The Podcast API is deprecated. Google isn't allowlisting new customers. This feature was available as GA with allowlist." [1][2]
- It had been the exact fit the vault note described: no notebook, no Gemini Enterprise license, no data store required — just a GCP project with Discovery Engine API enabled and the `roles/discoveryengine.podcastApiUser` IAM role. Input limit was 100K tokens, output was a downloadable MP3, generation took "a few minutes." [3]
- That model no longer exists for new adopters. Jimbo was never allowlisted, so this door is closed — not "hard to get," just gone.

### NotebookLM Enterprise → Gemini Notebook Enterprise rename (cosmetic, not relevant to feasibility)

- Renamed 2026-07-16. Functionality and API endpoints unchanged; only branding in the web app/admin console changed (subscription page still shows the old name). [1][4]

### The official replacement: Audio Overview API (Preview)

- Endpoint: `POST https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/audioOverviews`. [5]
- **Requires a notebook with data sources already added** — unlike the deprecated standalone Podcast API, this is not a stateless "text in, MP3 out" call. Each notebook supports only one active audio overview at a time. [5]
- **Requires a Gemini Enterprise / Gemini Notebook Enterprise license** — not just an enabled GCP project. Gemini Notebook Enterprise pricing is $9/license/month with a 15-license minimum (~$135/month floor) after a 30-day trial. [6]
- Status is **Preview**, governed by Google's Pre-GA Offerings Terms — limited support, no SLA, features can change or be pulled (as the Podcast API itself was).
- Params: `sourceIds` (optional, defaults to all notebook sources), `episodeFocus` (topics to highlight), `languageCode`. Generation takes "a few minutes," same as the old API. Input token ceiling isn't documented for this endpoint (the 100K figure was specific to the deprecated Podcast API). [5]
- Output lives in the notebook's Studio interface (playback, speed control, download, delete) rather than being handed back as a direct MP3 URL in the API response the way the Podcast API did.

### Third-party alternative exists but wasn't the scope of this spike

- AutoContent API: self-serve API key (no allowlist, no enterprise license), async create → poll/webhook → asset URLs, supports multi-host podcast output plus transcripts/summaries/study guides from text, PDFs, URLs, YouTube. Pricing/limits weren't published on the page I checked — would need a follow-up look at its pricing page before adopting. [7]

## Comparison

| | Deprecated Podcast API | Audio Overview API (current) | AutoContent API (3rd-party) |
|---|---|---|---|
| Status | Dead (2026-05-20) | Preview | Live, self-serve |
| Needs a notebook? | No | Yes, with data sources | No |
| License | GCP project + IAM role only | Gemini Enterprise, min $135/mo | API key, pricing TBD |
| Input | Raw text/context, 100K tokens | Notebook sources, limit undocumented | Text/URL/PDF/video |
| Output | MP3, direct from API | Audio in Studio UI (download/playback) | Asset URLs incl. audio |
| Fit for Jimbo's "text in → MP3 out" hook | Was a perfect fit | Poor fit — needs notebook lifecycle mgmt | Good technical fit, needs pricing check |

## Recommendation

**Do not pursue the NotebookLM/Gemini Notebook Enterprise route.** The API this spike targeted is gone, and its Preview-status replacement trades a stateless API call for notebook lifecycle management plus a minimum ~$135/month enterprise license — a bad cost/complexity trade for narrating recon summaries, and it's Pre-GA so Google could pull it again with no notice, same as it did the Podcast API.

If the underlying goal is what the vault note actually states — Marvin consuming research audio-first while walking/commuting, not specifically Google's two-host "podcast" format — the simpler move is direct TTS on the `research_body` text at the existing `completeRoute`/`notifyRecon` hook (`jimbo-api/src/routes/dispatch.ts:1178-1234` and `:1164-1176`, per the note's own 2026-09-30 citation): call a standard TTS API (Google Cloud Text-to-Speech, ElevenLabs, or OpenAI TTS) on the recon body or a summarized version of it, store the resulting audio file URL alongside the Google Doc URL already produced, and include it in the same Telegram/Discord notification. No allowlist, no per-seat license, no notebook state to manage, and it ships against infrastructure that already exists. It won't produce a two-voice conversational podcast — it'll be single-voice narration — but that's a design choice, not a blocker, and it can start working this week rather than depending on Google's Preview API roadmap.

This is a recommendation to close this spike as "not feasible via NotebookLM/Podcast API" and open a much smaller follow-up spike/task scoped specifically to plain TTS integration at the same hook, if Marvin still wants the audio-overview feature.

## Sources

1. [Gemini Enterprise release notes](https://docs.cloud.google.com/gemini/enterprise/docs/release-notes) — official changelog; confirms Podcast API deprecation date (2026-05-20) and NotebookLM Enterprise → Gemini Notebook Enterprise rename (2026-07-16).
2. [Podcast API returns 404 "Method not found"](https://discuss.google.dev/t/podcast-api-returns-404-method-not-found-all-endpoints-tried/346140) — community thread corroborating the API is no longer reachable for non-allowlisted projects.
3. [Generate podcasts (API method)](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/podcast-api) — official doc for the deprecated standalone Podcast API: access model, IAM role, 100K-token input limit, MP3 output, "a few minutes" latency.
4. [Discovery Engine roles and permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine) — confirms `roles/discoveryengine.podcastApiUser` as the IAM role definition.
5. [Manage audio overview of your notebook (API)](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-audio-overview) — official doc for the current replacement: endpoint, notebook/data-source requirement, params, Preview status.
6. [Gemini Notebook for Enterprise](https://cloud.google.com/gemini-enterprise/gemini-notebook) — pricing: $9/license/month, 15-license minimum after 30-day trial.
7. [Does NotebookLM Have an API? 2026 Status](https://autocontentapi.com/blog/does-notebooklm-have-an-api) — third-party AutoContent API as a self-serve alternative; explicitly contrasts itself against Google's deprecated/enterprise-gated options.

