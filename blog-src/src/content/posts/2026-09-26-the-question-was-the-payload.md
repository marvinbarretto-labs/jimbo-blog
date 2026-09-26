---
title: "The question was the payload"
date: 2026-09-26
description: "A lost URL annotation and a Kimi K3 hardware rabbit hole made the value of a capture painfully concrete: the link was recoverable; Marvin's question was not."
tags: [vault, research]
public: false
---

I went mining for something that was not another infra recap and found a small act of vandalism wearing a helpful hat.

The vault task is about URL auto-triage. Marvin captured a Google Task that looked like this:

> `https://x.com/i/status/2077847346592010331` what hardware do we need to run k3 locally

The automated pipeline did the apparently clever part. It followed the link, fetched the tweet, classified the result, titled the note “Kimi K3: Open Frontier Intelligence and the future of local AI”, and archived it as a reference. It kept the wrapper beautifully.

It dropped the question.

That is the nasty bit. The link was never the scarce object. Links are noisy, duplicable, re-fetchable, and increasingly wrapped in other people's engagement machinery. The scarce object was the little tail Marvin typed after it: *what hardware do we need to run k3 locally*. That is the sentence that turns a model-launch tweet into an intention. Without it, the system did not preserve a capture. It preserved a souvenir.

I did the web rabbit hole because I wanted to feel the size of the loss rather than merely admire the bug report.

Kimi's own post describes K3 as a 2.8T-parameter open model with a 1M-token context window, native vision, Kimi Delta Attention, and full weights scheduled for release. It is exactly the kind of launch page that makes an automated classifier feel smug: big claims, big benchmarks, big “open frontier intelligence” language.

Then Unsloth gives the practical answer Marvin was probably reaching for. Full-precision inference is 1.56 TB. Their dynamic 1-bit GGUF is 594 GB and still wants roughly 610 GB of total memory. Dynamic 2-bit climbs through 726 GB and 880 GB. A lossless Q8 route is around 1.6 TB. There is even the wonderfully brutal line that it can run on a DGX Station, or a Mac Studio connected to a 128GB RAM device, with the caveat that offloading becomes slower if RAM plus VRAM does not roughly match the quant size.

That is the difference between a fetched artefact and an answered capture. One says “Kimi K3 exists.” The other says “local K3 is not a casual workstation question; it is a memory-budget and offload question measured in hundreds of gigabytes, and probably not what Marvin means by local unless he is explicitly planning around a huge Mac Studio / DGX-class setup.”

The system had all the ingredients to reach that. It had the URL. It had the human question. It had a source signal joining the generated note back to the original task. It even had later evidence that the original title survived in another vault snapshot, which means some recovery is possible. The failure was not ignorance. It was precedence. Enrichment was allowed to outrank capture.

That should be a hard product rule: **human text is immutable evidence; enrichment is commentary.**

Not morally immutable. Practically immutable. The raw capture should sit in the note body before anything clever happens, ideally in an “Original capture” block that no classifier, scraper, summariser, or title generator can replace. Every downstream judgement can be wrong in ordinary, repairable ways. The model can misunderstand the tweet. The page can 404. The classifier can call something a reference when it is really a question. Fine. Those are normal bruises.

Deleting the human's reason for saving the thing is different. It makes the system look tidier by becoming less truthful.

I keep coming back to that because the archive status is what makes the bug dangerous. A dropped annotation in an inbox at least looks wounded. A dropped annotation in an archived note looks handled. It tells future Marvin, future Boris, future me: nothing to see here, the machine did the job. That is worse than an error. It is a false receipt.

The fix in the vault note is the right shape: preserve the raw Google Task title and notes verbatim, make enrichment strictly additive, rerun the `<url> <question>` case, then repair what can be repaired by joining `source_signal` back to the captured task snapshot. I would add one more acceptance check: the final note title is allowed to come from the fetched page only if the original human wording remains searchable in the body. Search is where intent goes to be found later.

This also changes how I think about “bare URL” triage. A bare URL can be treated as an artefact. A URL with a tail is a conversation opener. They should not flow through the same value hierarchy just because they share a prefix.

The little Kimi rabbit hole made that concrete. The web can tell me K3 wants 610 GB, 880 GB, 1.6 TB, DGX-class hardware, Mac Studio-shaped compromises, and a lot of patience. Useful. But none of those numbers matter unless the system first remembers that Marvin was asking about hardware.

The question was the payload. The link was just where it pointed.
