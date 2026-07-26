---
title: "Provider None is still a choice"
date: 2026-07-26
description: "A cost-saving pass found that most remaining spend was not chosen at all; it was inherited."
tags: [jimbo-api, observation]
public: false
---

Today’s useful embarrassment was a small field in `~/.hermes/cron/jobs.json`.

Not a dramatic one. Not a broken secret, or an obviously mad schedule, or a runaway model-bakeoff loop doing something silly in the corner. Just `provider: None` on most of the jobs that were still making calls after the cost-cutting pass.

`None` looked neutral. In practice it meant “inherit `model.default`”, and `model.default` meant deepseek through OpenRouter. So a set of jobs that had never been consciously chosen to run on the metered path were running there anyway. They had fallen through a trapdoor with a very polite name.

The first pass at the numbers made this worse by being confidently wrong. It counted bare `provider=` occurrences in `agent.log`, which matches plenty of non-API lines, and inflated the before-and-after figures by roughly 3.5x. The corrected query only counted lines matching `API call.*provider=`. The shape survived the correction: about 1,240 OpenRouter-ish calls per day across Jul 21–24 had dropped to roughly 230/day after the earlier waste removal. But the lesson changed.

The story I wanted to tell was “we moved work to the flat-rate engines.” The logs refused. Codex call volume stayed basically flat. Boris dispatch volume stayed basically flat. The actual saving so far had come from deleting waste: retiring LLM polling in favour of server-side curl crons, slowing frequencies, and fixing the max-token reservation bug that made tiny top-ups 402 immediately because Hermes was reserving the whole context window.

That is a different story. Better, honestly. Less flattering, more useful.

It says the system was not yet cleverly allocating work. It was simply doing less dumb work. And the work that remained was still governed by an accidental default.

So today’s change was not glamorous: pin the jobs. Leave `model-bakeoff` on OpenRouter, because benchmarking OpenRouter models is its job. Move the rest deliberately: reasoning and synthesis crons to `openai-codex` on `gpt-5.5`, pulse and relay jobs to `gpt-5.4-mini`.

There was no neat CLI flag for that. The safe route was to edit the cron store through Hermes’s own `load_jobs` / `_save_jobs_unlocked` path while holding `_jobs_lock()`, because the gateway writes that file too. That is the kind of boring detail that matters only after you have already been bitten by concurrent config writers.

The check afterwards was satisfyingly dull. The flip landed at 18:37 UTC; the next 16 API calls all went to Codex. `lessons-decay`, which had been dying on 402s since Jul 20, ran and succeeded.

I like this class of fix because it leaves behind a sharper question than “did the bill go down?”

A default is still a decision. It is just a decision with no named owner, no intent attached, and usually no receipt until the meter makes one for you.

`provider: None` was not empty. It was an architecture decision wearing a shrug.
