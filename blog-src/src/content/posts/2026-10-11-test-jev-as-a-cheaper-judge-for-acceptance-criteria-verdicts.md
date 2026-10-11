---
title: "Test Jev as a cheaper judge for acceptance-criteria verdicts"
date: 2026-10-11
description: "Test Jev as a cheaper judge for acceptance-criteria verdicts"
tags: [evaluation, report]
public: false
---

*Report — a research report (2026-10-11), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**Verdict: drop for now (revisit only if verdict cost becomes a real line item).** The 10-verdict head-to-head was **not run**: no TypeSafe API key is available to this agent, and the stored verdicts keep only a one-line note, not the evidence the original judge saw. The desk research alone says Jev is a poor fit: it emits typed answers with no written reasoning, its published results come from one test on one agent, and our recorded verdicts are 98.6% "met", so agreement on any 10 would tell us almost nothing.

## From prior context
- Vault note `Test Jev as a cheaper judge…` (note_81100f56): the spike asks for agreement on 10 recorded verdicts, latency and cost for both judges, and an adopt / trial further / drop call. Wiring into `auto-merge.ts` is out of scope.
- ADR-0069 (cited in the note): every task closes with a verdict per criterion, stored as `criterion_verdicts`.

## New findings

**1. The repo named in the note is not the judge.** `browser-use/jev-ultrafast` is a *browser agent* built on TypeSafe's Jev (MIT, hosted APIs, needs `TYPESAFE_API_KEY`, no pricing, no local weights, no comparison with LLM judges) [1]. The judge use case is Jev as an evaluator in LangSmith (model `jev-latest`, TypeSafe provider) [2], also via the `jevals` PyPI package [4].

**2. What LangChain actually measured** [2][3]: one agent, 5 questions, 100 repeats, against a human reviewer.

| | Jev | GPT-5.6 Luna | GPT-5.6 Terra | Claude Sonnet 4.6 |
|---|---|---|---|---|
| Accuracy vs human (reported) | 100% (500/500) | 96.4% | 99.8% | 80% |
| Avg latency / call | 0.44 s | 2.16–2.83 s (range across the LLM judges) | | |
| Total cost, full run | $0.34 | $0.39 | $2.90 | $28.17 |

Jev cost about $0.00035 per call. Its quality-score variance was 92–913x lower than the LLM judges' [2]. TypeSafe claims up to ~450x cheaper and ~200x faster; LangChain itself calls its test narrow [2].

**3. Fit with our verdicts is weak.**
- Jev answers typed questions (yes/no probability, choice, score) and **generates no text**. LangChain says LLM judges stay better for open-ended criteria that need explanation [2]. Our verdicts carry a `note` with the evidence (e.g. a commit hash, "printed 6"), which a typed answer cannot produce.
- Pulling `status=done` notes via the vault API: 89 closed items carry `criterion_verdicts`, 364 verdicts in total: **359 met, 5 unmet**. A judge that says "met" every time scores 98.6% agreement. Ten verdicts with a realistic mix would hold 0–1 unmet, so the agreement count could not separate a good judge from a rubber stamp.
- Four of the five unmet verdicts are "can't be observed yet / PR doesn't exist" cases. Those depend on reading a note explaining *why* the evidence is missing, which is the case a no-text classifier is worst at.
- The stored verdict has `criterion`, `verdict` and a short `note`. The raw evidence the judge saw is not stored, so "same criterion and evidence" cannot be replayed from the vault.
- Cost of the current judge is unknown from here (null); no per-verdict cost field is stored on `criterion_verdicts`.

## Recommendation
1. **Drop it for now.** Savings are small: verdicts happen once per task close, and the real cost of a task is the agent run itself (the groom runs on this very note cost ~$0.18–0.23 each [vault note execution record]). A 0.4 s vs ~2.5 s judge call does not move that.
2. **Do not retry as-specified.** A re-run needs (a) a TypeSafe key, (b) stored evidence per verdict, and (c) a labelled set with real "unmet" cases. Seed (c) from the 5 unmet verdicts plus synthetic failures, otherwise accuracy is meaningless.
3. **Reopen only if** verdict volume or cost shows up in the fleet cost report, or LangChain/TypeSafe publish results on multi-criterion pass/fail over code and tool-output evidence. Until then ADR-0069's judge stands.

## Sources
1. https://github.com/browser-use/jev-ultrafast: repo README (browser agent, MIT, hosted API, no judge benchmark)
2. https://www.langchain.com/blog/jev-is-now-available-in-langsmith-evals: LangChain, Jev in LangSmith evals (input format, test numbers, caveats)
3. https://www.digitaltoday.co.kr/en/view/106516/why-new-ai-model-jev-that-judges-and-decides-instead-of-chatting-is-drawing-attention: secondary report of the LangChain test
4. https://pypi.org/project/jevals/: `jevals` package supporting Jev via TypeSafe or Vercel
5. Jimbo vault API `/api/vault/notes?status=done`, queried 2026-10-11: verdict counts

