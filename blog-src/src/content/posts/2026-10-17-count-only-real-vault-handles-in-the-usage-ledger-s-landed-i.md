---
title: "Count only real vault handles in the usage ledger's landed items"
date: 2026-10-17
description: "Count only real vault handles in the usage ledger's landed items"
tags: [ledger, report]
public: false
---

*Report — a research report (2026-10-17), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
The merged fix (jimbo-api PR #221, 85e6a0f) works on live data. `GET /api/usage/ledger?date=2026-10-12` shows session be214619 with only real `JIM-` handles in `landed.items`, and all three dashboard squash commits (#53, #54, #55) attributed to it. Both live criteria pass; nothing is missing.

## From prior context
The vault note (task note_fbb8c61f) records that the handle filter and dashed-separator trailer reader merged in #221, with the two unit-test criteria already marked met. Only the live check was left.

## New findings
Fetched the ledger for 2026-10-12 (page 1: 50 top-level rows, 332 including children; the API reports 20885 total, so other pages were not read). Session `be214619` (kind `session`, repo `marvinbarretto/jimbo`) has 60 landed commits.

- **`landed.items`**: `JIM-7259, JIM-7261, JIM-7260, JIM-7019, JIM-7133, JIM-7238`. No ADR- or SLICE- handle.
- **No ADR-/SLICE- in any `items` list on the page**: checked all 332 rows. ADR-NNNN strings do appear, but only inside commit subjects (e.g. `docs(adr): ADR-0111 background agents from attended sessions use the App`), which is correct. They are not counted as items.
- **Squash commits present** (all `marvinbarretto/jimbo-dashboard`):
  - #53: `fix(week): week, today and balance share one block-state derivation (#53)`
  - #54: `feat(week): week view on FullCalendar with movable blocks, list on phones (#54)`
  - #55: `fix(week): day tabs count a moved block on the day it sits (#55)`
- Earlier squashes #49, #50, #51 and #52 are also on this session, so the pre-fix drop of multi-commit squashes is gone.

No squash commit was missing, so no explanation from `session-landed.ts` / `commit-vault-linking.md` was needed.

## Recommendation
Mark the two live criteria met and close the task. No further code change. Caveat: only the first ledger page was inspected, so other sessions on other pages were not checked for ADR-/SLICE- leaks; the check on this page covered 332 rows with zero.

## Sources
1. Vault note note_fbb8c61f, "Count only real vault handles in the usage ledger's landed items"
2. `GET /api/usage/ledger?date=2026-10-12` (jimbo-api, read 2026-10-17)

