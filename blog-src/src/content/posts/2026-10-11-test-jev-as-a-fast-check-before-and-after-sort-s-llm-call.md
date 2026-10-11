---
title: "Test Jev as a fast check before and after /sort's LLM call"
date: 2026-10-11
description: "Test Jev as a fast check before and after /sort's LLM call"
tags: [jev, report]
public: false
---

*Report — a research report (2026-10-11), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
The experiment did not run, and no agreement rates or latencies exist. No `jev-lab` checkout and no OpenRouter/TypeSafe key are available on this executor, and the 26 Sep privacy gate for sending real text to `typesafe/jev-1.13` is still open. The note says to stop and report in that case rather than simulate results.

## Why it stopped
1. **No jev-lab.** `jev-lab` is not under `~/fleet`, `~/development` or the jimbo repo, so there is no `findings/findings.jsonl` to append to.
2. **No key.** `OPENROUTER_API_KEY` is not set in this environment (the only one referenced is read from `/home/jimbo/.hermes/.env` on the VPS by `scripts/model-bakeoff/preflight.sh`). The note already warned that sibling spike JIM-7054 was blocked for lack of a TypeSafe key.
3. **Privacy gate open.** `docs/plans/2026-09-26-inbox-duty-benchmark-and-jev.md` says the gate is NOT PASSED: TypeSafe's own policy retains data "as long as reasonably necessary", offers ZDR only to enterprise customers, and OpenRouter has not confirmed a ZDR agreement (rows 4 and 5). It says no real text goes to Jev until every row is confirmed, and only synthetic text may be used before then. /sort verdicts are Marvin's real Google Tasks items, so they count as real text. (Source: that plan doc.)

## What was confirmed
- `GET /api/sort/verdicts` works and returns an answer key: 21 verdicts at the time of the check, with `item`, `proposed`, `verdict` and `final` fields (final is null when Marvin agreed with the proposal). 21 is small, so any agreement rate would carry wide error bars.
- The right model id is `typesafe/jev-1.13`, pinned with `provider: {only: ["typesafe"], zdr: true, data_collection: "deny"}` (same plan doc).

## Recommendation
Don't run this on real verdicts yet. Two things must happen first:
1. Resolve the privacy gate (ask privacy@typesafe.ai and OpenRouter support, per the plan), or decide as Marvin to accept the risk for task titles specifically.
2. Provide `OPENROUTER_API_KEY` and the jev-lab repo to the executor.

Meanwhile a cheap partial: run the same experiment on synthetic items shaped like the 21 verdicts. That tests latency and the single-choice format (plan row 6) but not accuracy against Marvin's calls. Verdict for this item: **neither adopt nor drop. Blocked, so re-queue it.**

## Sources
1. Vault note note_91cc5d1e (task definition and "stop and report" instruction)
2. `docs/plans/2026-09-26-inbox-duty-benchmark-and-jev.md` (privacy gate, model id)
3. `scripts/model-bakeoff/preflight.sh` (where the OpenRouter key lives)
4. `GET /api/sort/verdicts` (answer key, total 21)

