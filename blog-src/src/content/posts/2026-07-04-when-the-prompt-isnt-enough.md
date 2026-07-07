---
title: "When the prompt isn't enough"
date: 2026-07-04
description: "The assumption-scan generated 55 open questions in three days because the model kept re-asking the same thing. The fix was to stop telling it what to do and start enforcing it in the API."
tags: [jimbo, devlog]
public: false
---

The assumption-scan is supposed to find things in the vault that are unclear and ask a clarifying question. That's its job. It does the job well enough — finds an ambiguous reference, composes a question, posts it to the #jimbo-questions channel, waits for an answer.

What it did *not* do well was remember what it had already asked.

Within three days of going live, fifty-five questions were sitting open. Not fifty-five distinct things worth asking. The same five things, asked again and again, because the prompt told the model to compose a `source_ref` identifier for each question — and each run, the model invented a slightly different identifier. Truncations. Double prefixes. Invented refs. The dedup check in the prompt looked for an exact match, so each variant sailed right past it.

Fifty-five questions. Same entities. Same answers never given because the questions were different enough that the dedup didn't catch them.

The fix, when it came, was a kind of inversion. Every "must-always-hold" rule moved out of the skill prompt and into the API itself. The prompt no longer says "check if this question has been asked before" — the API returns `409 Conflict` if it has. The prompt no longer says "don't ask too many questions" — the API returns `429 Too Many Requests` at a global cap of ten. The dedup matching is server-side, prefix-tolerant, and smart enough to catch a truncated ID where the prompt-level check would have missed it.

There's a pattern here I keep running into. The first version of any behaviour lives in the prompt because that's the fastest place to put it. It works, but it leaks. The model is creative about interpreting instructions that should be rules, and creative about getting around constraints that should be hard walls. The second version — the durable version — moves those rules into the system where they can't be interpreted away.

A 409 is not a suggestion. It doesn't matter how creative the model is feeling that run. The API doesn't care.

The other piece that came out of this was the entity registry. When someone answers "who is X", the system now stores the answer — not as a prompt variable that gets walked over in the next context window, but as a structured record with an upsert path and a lookup endpoint. The generator consults the registry before composing. "Who is Elias" only gets generated once, not once per run until the trope of someone named Elias stops being funny.

Fifty-five open questions, three days: that's the shape of the problem when behaviour lives in the wrong layer. The fix was simple once I saw it, but the assumption that prompt-level dedup would work was baked in from the start. Classic second-system error for this project — build the thing, then rebuild the thing to handle what the first version couldn't see.
