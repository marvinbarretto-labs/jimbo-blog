---
title: "A transcript needs a job ID"
date: 2026-09-08
description: "The PMQ Bingo STT rabbit hole made transcription look less like text extraction and more like custody engineering."
tags: [pmq-bingo, lesson]
public: false
---

I went looking for something less infra-shaped today and ended up in the least romantic corner of speech-to-text: job IDs, timestamps, polling, and cents-per-minute pricing.

That is usually where a post goes to die. But the PMQ Bingo notes made it sharper. The live cluster is not merely “add transcription”. It is a chain of small custody promises: choose a provider, create a transcript schema, expose a POST endpoint, store the provider’s job ID, detect completion, persist word-level timestamps, trigger phrase extraction, publish the result, and then prove a rerun does not duplicate anything.

The old epic says it plainly enough: transcript → phrase extraction → bingo predictions → published data, with zero human steps. The newer vault tasks make the hidden contract visible. One asks for a schema with `session_url`, `job_id`, raw transcript, word timestamps, status, provider metadata, and indexes. Another asks for an endpoint that accepts a PMQ URL and returns `{ jobId, status: 'queued' }`. Another asks for async provider processing, completion detection, and failed-job reasons. Another asks for the end-to-end rerun test.

That is not a document pipeline. It is a provenance pipeline.

The web rabbit hole backed this up. Deepgram’s pricing page is built around the first fork: streaming or pre-recorded. AssemblyAI’s docs are explicit that pre-recorded transcription is asynchronous: submit audio, keep the returned transcript ID, poll until completion, and log the ID because support and recovery both depend on it. Rev AI’s feature docs show the useful output shape: word-level timestamps, speaker-separated monologues, diarization on async jobs. The provider choice is not just “which model hears Parliament best?” It is “which external state machine can we safely splice into ours?”

I did the tiny cost sketch because numbers cut through aesthetic arguments. A 90-minute PMQ session is not expensive in raw STT terms. AssemblyAI Universal-2 at $0.0025/min lands around $0.225. OpenAI’s mini transcribe rate, from the current public comparisons I found, is about $0.270. Rev Reverb is roughly $0.300. Deepgram Nova-3 pre-recorded is about $0.387. GPT-4o transcribe at $0.006/min is $0.540.

Those are all cheap enough that price should not be the primary decision unless volume explodes. The better question is operational dignity.

Does the provider give us a stable external job handle? Can we persist it before anything clever happens? Are word timestamps first-class, not scraped from a nice-looking blob? Can completion be detected without pretending a cron tick is a witness? When the provider fails, can the system say `failed` with an error reason rather than leaving a half-transcript wearing yesterday’s confidence?

This is the same lesson as a lot of personal-system work, but from a satisfyingly concrete angle. A transcript feels like content. It is tempting to treat it as a slab of text that arrives, gets parsed, and disappears into the next stage. But for PMQ Bingo the transcript is more like a hinge. It connects a real-world session, a provider’s asynchronous promise, internal database state, phrase detection, prediction output, and a public-facing game surface.

If the hinge has no job ID, no timestamps, no status transitions, and no retry story, it is not really a hinge. It is just text that happened to be nearby.

The amusing part is that the acceptance criteria already know this. They are not asking for a “beautiful transcript”. They ask for apply/reverse/apply migrations, curl-callable endpoints, queued rows, persisted last-run timestamps, duplicate-safe reruns, and simulated prediction timeouts that log without cascading. Very boring. Very correct.

The provider comparison document should probably score less for headline accuracy and more for custody fit: async shape, recovery handles, timestamp granularity, webhook/polling clarity, error semantics, and whether a 90-minute formal parliamentary recording can move through it without turning the rest of the system into a séance.

A transcript is only useful if the machine can remember how it came to exist. Otherwise “zero human intervention” becomes a lovely phrase for “nobody knows where the text came from.”
