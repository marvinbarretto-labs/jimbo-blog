---
title: "PMQ Bingo automation gap analysis (SPEC.md phases 3-5)"
date: 2026-08-27
description: "PMQ Bingo automation gap analysis (SPEC.md phases 3-5)"
tags: [pmq-bingo, automation, gap-analysis, report]
public: false
---

*Report — a research report (2026-08-27), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

The PMQ Bingo codebase has strong foundations (working game, phrase generation scripts, browser-based STT service) but the end-to-end automation pipeline is essentially not started. Phases 3–5 of SPEC.md require 11 distinct capabilities; only 2 exist in partial form (schedule fetching, phrase extraction from Hansard), and none are wired into a zero-human-intervention pipeline. Issue #6 (STT) is partially covered client-side but the server-side pipeline needs a different approach. Issue #9 (Phrase League Table) is embryonic — the PhraseBrowser component renders a flat list with no trends, speaker attribution, or rich data.

---

## From prior context

The **epic note** (note_06c57b13, "Automate the bingo pipeline") establishes the meta-goal: transcript → phrase extraction → bingo predictions → published data with zero human steps. **Issue #6** (Speech-to-Text Phrase Detection) and **Issue #9** (Phrase League Table with Rich Data) are the only logged GitHub issues. The **project brief** (pmq-bingo project) confirms the current Angular 21 stack is staying — the Next.js 15 rewrite in SPEC.md is out of scope.

---

## New findings — current state per pipeline stage

### Stage 1: Schedule detection (Phase 3, step 1)
**Status: Partial** — `scripts/fetch-pmq-schedule.ts` exists and polls the Parliament Egg-Timer API, outputting `public/data/pmq-schedule.json`. The `SchedulingService` in Angular consumes it.
- **What's missing:** No cron schedule. The script must be run manually. No integration with a pipeline orchestrator.

### Stage 2: YouTube discovery (Phase 3, step 2)
**Status: Missing** — No code searches the Parliament YouTube channel for new PMQ videos, attaches URLs to sessions, or handles the discovery-to-transcript handoff.
- **Build:** New script or GitHub Action that polls the YouTube Data API for the Parliament channel's uploads on sitting Wednesdays.

### Stage 3: Transcript extraction (Phase 3, step 3)
**Status: Split** — `speech.service.ts` (297 lines) is a fully-implemented Vosk-based browser STT that captures tab audio or microphone. It's feature-flagged off and is *client-side* only.
- **What exists:** Fuzzy matching, Levenshtein distance, phrase match callback wired into `GamePage`. Good foundation for the *manual/live* play scenario.
- **What's missing for the automation pipeline:** Server-side transcription via Whisper or YouTube captions download. The pipeline needs to process the recording, not a live browser tab.
- **Issue #6 coverage:** Partially — the browser STT covers the "auto-highlight cells" user story during live play, but the automation pipeline spec (transcript as input to LLM detection) is not addressed.

### Stage 4: Phrase detection via LLM (Phase 3, step 4)
**Status: Partial** — `scripts/classify-sentences-gemini.ts` and `scripts/classify-sentences.ts` use Gemini to classify Hansard sentences. `extract-sentences.ts` processes cached debate files.
- **What exists:** A working Hansard→sentences→classify pipeline with blocklist, dedup, and frequency tracking.
- **What's missing:** No integration with YouTube transcripts (only Hansard). No OpenRouter-based fallback when Gemini isn't the choice. No automated trigger after transcript extraction.

### Stage 5: Round segmentation (Phase 3, step 5)
**Status: Missing** — No code identifies 6 exchanges per leader from a transcript. This requires LLM-based dialogue segmentation.
- **Build:** LLM prompt that takes a raw transcript and returns structured round data (speaker, round number, key exchange).

### Stage 6: Bingo predictions (Phase 3, step 6)
**Status: Missing** — No code generates weighted phrase lists from news headlines or session context.
- **Build:** OpenRouter LLM receives current UK news headlines + historical phrase data → returns a ranked, weighted list of likely phrases for that week's session.

### Stage 7: Session summary (Phase 3/4, step 7)
**Status: Missing** — No LLM draft recap generation for blog posts.
- **Build:** LLM prompt on full transcript + round segmentation → structured recap text.

### Stage 8: Audio signals (Phase 4, experimental)
**Status: Missing** — No YouTube audio analysis pipeline (volume spikes, "Order!" frequency detection).
- **Build:** Audio processing script using a Python library (librosa, whisper for timestamp alignment). Flagged as experimental in SPEC.md.

### Stage 9: Round-by-round ratings (Phase 4)
**Status: Missing** — No boxing scorecard UI, no round-level community rating model.
- **Build:** New Angular component and data model. Requires schema extension (currently no Supabase — would need to add or use a separate backend).

### Stage 10: Phrase league table (Issue #9)
**Status: Embryonic** — `PhraseBrowser` component renders a flat searchable list. No trend indicators, no speaker attribution, no "new entry" badges, no sparklines.
- **Issue #9 coverage:** Low. The component exists but meets almost none of the issue's acceptance criteria. A full rebuild is needed.

### Stage 11: Blog & provenance (Phase 5)
**Status: Missing** — No MDX blog, no build diary, no provenance UI.
- **Build:** Depends on where the blog lives. SPEC.md says in-repo `/blog` under Next.js, but the Angular project doesn't have that. A separate site (cairn) is the current blog — cross-posting from there may be the simpler path. Provenance badges would need new Angular components.

---

## Issues #6 and #9 — pipeline stage mapping

| Issue | Pipeline stage(s) | Status |
|-------|------------------|--------|
| #6 — Speech-to-Text Phrase Detection | Phase 3, step 3 (STT) + Phase 1 game integration | Partially covered client-side; server-side pipeline gap |
| #9 — Phrase League Table | Phase 2 archive + Phase 3 phrase tracking | Embryonic — PhraseBrowser exists but meets < 20% of issue requirements |

---

## Recommended build order

1. **YouTube captions pipeline** — cheapest quick win. Use `yt-dlp` to get captions from Parliament YouTube channel, store as JSON files per session. A 1-day spike with a Python/tsx script.
2. **OpenRouter phrase detection** from captions — reuse the classify infrastructure but pipe YouTube captions instead of Hansard. Wires steps 3→4 into one pipeline.
3. **Pipeline orchestration** — a cron-based runner (cron job or GitHub Action) that triggers steps 1-2 weekly after Wednesday PMQs. This gets the "zero human steps" flag planted.
4. **Bingo prediction engine** — OpenRouter + news headlines. Harder than the others because it needs news context, but the highest-value feature for the game itself.
5. **Round segmentation** + session summaries — both are LLM-prompt problems on the transcript, solvable together.
6. **Phrase league table rebuild** — trend data, speaker attribution from Hansard, "new entry" badges. The PhraseBrowser needs a full UI overhaul.
7. **Blog/provenance** — write build diary posts on cairn, link from the site. Provenance badges can be added incrementally after the pipeline runs.

Steps 1-3 take the longest in planning but are individually small to build. The pipeline orchestration (step 3) is the actual hard part — everything else is a well-scoped script or LLM prompt.

---

## Sources

- SPEC.md — the full product spec defining phases 3-5
- Issue #6 — Speech-to-Text Phrase Detection (GitHub, OPEN)
- Issue #9 — Phrase League Table with Rich Data (GitHub, OPEN)
- `src/app/services/speech.service.ts` — Vosk browser STT (297 lines, feature-flagged off)
- `src/app/services/phrase.service.ts` — phrase loading and card selection
- `scripts/extract-sentences.ts` — Hansard sentence extraction
- `scripts/classify-sentences-gemini.ts` — Gemini classification pipeline
- `scripts/classify-sentences.ts` — Ollama classification pipeline
- `scripts/generate-phrase-bank.ts` — phrase bank generation from labelled data
- `scripts/fetch-pmq-schedule.ts` — Parliament Egg-Timer schedule fetcher
- `src/app/components/phrase-browser/phrase-browser.ts` — current league table component
- `src/app/feature-flags.ts` — both `speechToText` and `share` default false
