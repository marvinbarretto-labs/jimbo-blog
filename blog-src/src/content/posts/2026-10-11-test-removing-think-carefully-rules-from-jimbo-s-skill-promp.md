---
title: "Test removing 'think carefully' rules from Jimbo's skill prompts"
date: 2026-10-11
description: "Test removing 'think carefully' rules from Jimbo's skill prompts"
tags: [prompts, report]
public: false
---

*Report — a research report (2026-10-11), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**Verdict: no difference.** None of the headline effort phrases ("think carefully", "think step by step", "take your time", "ultrathink") appear in any `SKILL.md`; only five mild adverb lines do. In an A/B on two of them, the outputs with and without the wording were substantively the same. Nothing is worth a remove task. This is a smoke test (one run per arm), not proof.

## From prior context
The vault note (note_c45957ea, "Test removing 'think carefully' rules...") already said the headline phrases are absent and named the five adverb lines. I re-ran the grep and confirm it.

## New findings

### Inventory (grep of `skills/**/SKILL.md`, case-insensitive: think carefully, step by step, take your time, ultrathink, think hard/deeply, carefully, thoroughly, deeply, rigorously)
| File:line | Text |
|---|---|
| skills/research/structured-investigation/SKILL.md:14 | "investigate a topic **thoroughly**" |
| skills/research/structured-investigation/SKILL.md:36 | "Read the title and acceptance criteria **carefully**." |
| skills/think/assess/SKILL.md:55 | "Read all the loaded context **carefully**." |
| skills/vault-grooming/review-briefing/SKILL.md:91 | "Read it **carefully**." |
| skills/think/evaluate/SKILL.md:129 | "investigate each one **thoroughly**" |

Absent everywhere: "think carefully", "think step by step", "take your time", "ultrathink", "think hard/deeply", "rigorously".

### A/B (scratch prompts, no tools, same input, model claude-sonnet-5-5; real SKILL.md files untouched)

**think/assess line 55** — input: a tweet summary of the Opus guide, with a fixed mini-context.
- With "carefully": Verdict *Bookmark*; skip the thread, read the original guide; one 30-minute audit pass on a high-traffic prompt; compare before/after. Blind spots: secondhand, unquantified "can hurt", other models in the fleet, over-pruning.
- Without: Verdict *Bookmark (leaning Worth exploring)*; same steps (find source, grep prompts, audit, change one agent at a time); same blind spots. Slightly longer next-steps list.
- Difference: same verdict, same structure, same content. Only the hedge on the verdict label varied, which is ordinary run-to-run variation.

**research/structured-investigation lines 14 + 36** — input: this task's title and criteria; step 1 plus a research plan.
- With "thoroughly"/"carefully": defined the effort-line boundary, a measure fixed up front, a scratch-copy rule, a confidence caveat; 6-step plan ending in a verdict.
- Without: same points (matching rule recorded, ADR check, scratch copies, blind scoring, small-sample caveat); 6-step plan, same shape.
- Difference: none that matters. The no-wording run was, if anything, a little more concrete (ADR check, blind scoring).

Limits: n=1 per arm, partial skill runs (no live context or web), no scoring rubric beyond reading both outputs. A subtle effect on long, tool-using runs is not ruled out.

## Recommendation
Keep the skills as they are and do not open a remove task. Five mild adverbs cost almost nothing, and the test shows no behaviour change either way. The "audit your old rules" idea is better spent on any prompt that does contain real scaffolding, and a grep shows `skills/` has none.

## Sources
1. Vault note note_c45957ea (scope, line list, source link https://x.com/Voxyz_ai/status/2102850122497368464 — not fetched; secondhand claim about Anthropic's Opus guide).
2. Local grep of `skills/**/SKILL.md` on 2026-10-11.
3. `skills/think/assess/SKILL.md` and `skills/research/structured-investigation/SKILL.md` (prompts under test).

