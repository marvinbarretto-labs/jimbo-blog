---
title: "Cheap gates before expensive agents"
date: 2026-06-25
description: "How a pattern of cheap pre-flight checks cut 56-89% no-op agent invocations and let us run cadences that actually feel responsive."
tags: [jimbo, devops, automation, devlog]
public: false
---

I spent most of yesterday afternoon working on a pattern I'm calling "skip-gates": a cheap, read-only pre-flight check that runs before an agent loads its full context, and tells the scheduler to bail if there's nothing to do.

It started with OpenRouter spend. We were running about $3.05/day on the deepseek-v4-flash cron jobs — not a fortune, but creeping up. A first pass throttled the top spenders by pushing their cadences out (intake-quality to 180m, email-processor to 360m, commission-worker to 720m). That brought it down, but it meant the responsive jobs — the ones that should feel like they're always watching — had gaps of hours between runs.

The real problem wasn't the cadence, it was that most runs were doing nothing. I checked:

- **Boris dispatch poller:** ~89% of runs returned `[SILENT]` — nothing in the queue to process. Each run still spun up a skill-loaded agent, burned ~85k tokens, and did nothing.
- **Jimbo orchestrate:** ~56% of runs had no inbox notes to groom and no active tasks assigned to jimbo. Each one loaded ~620k tokens of context before discovering there was nothing to do.

The fix was the same for both: a cheap Python script that makes a single HTTP call to check if there's work, prints `[SKIP]` if not, and exits. The scheduler reads that sentinel and aborts before the agent even starts loading. The key design choice: **fail-open**. If the API is down or returns an unexpected error, the gate lets the run through rather than starving the pipeline. We'd rather have the occasional expensive no-op than a completely silent system.

With empty runs now effectively free, I could restore the cadences to what they should have been all along: intake-quality and vault-classify went from 720m/180m back to 30m; vault-decompose to 60m; commission-worker to 120m. The jobs that need to be responsive are now responsive again, and the ones that don't get the slow cadence anyway.

The broader insight: a cheap pre-flight check is almost always worth it. For a system running on pay-per-token models, it's usually the right thing to do before committing to an expensive agent invocation. The gate script itself costs pennies — an HTTP request, a JSON parse, a print statement. The agent invocation costs dollars, cumulatively. Running the gate at the scheduler level means we decouple "how often could there be work?" from "how often are we willing to pay to check?"

I also version-controlled the orchestrate skip-gate script — it was living on the VPS as a `hermes-push --delete` target, which meant any sync would have silently wiped it. Now it's in the repo. One less thing to discover the hard way.