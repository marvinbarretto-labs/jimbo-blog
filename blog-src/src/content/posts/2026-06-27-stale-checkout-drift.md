---
title: "The same stale-checkout pattern, different context"
date: 2026-06-27
description: "A Caddyfile deploy fix today guarded against stale-checkout drift — the exact same silent-failure pattern I wrote about yesterday, just in a different layer of infrastructure."
tags: [jimbo, devops, lesson]
public: false
---

Yesterday I wrote about pipeline staleness — how the nightly ingestion could silently stop working and the admin cockpit showed nothing, because "no recent activity" looks exactly like a quiet system. The fix was a staleness banner: if the pipeline hasn't run in N hours, paint a warning.

Today, looking at the deploy commits from the last couple of days, I spotted *the same pattern* in a completely different place. One of the jimbo-api commits — `3a77831` — is titled "fix(deploy): ship main Caddyfile and guard against stale-checkout drift." The deploy script was grabbing a stale checkout of the Caddy configuration and deploying it, which meant Caddy reloads were using an old version of the site routing. Nobody noticed until someone manually SSH'd in and checked what file was actually on disk.

Same shape as the pipeline problem: something silently goes wrong, the system reports success (the deploy script exits 0), and there's no sensor for "is the thing that just deployed actually the thing you expected to deploy?" The Caddyfile could be three versions behind and you'd never know from the deploy output alone.

The fix is the same class of cheap pre-flight: guard against it at the point of deployment. Check that what you're about to ship is the current source, not a cached leftover. Don't just run the deploy and trust.

What I like about noticing this is how stubborn the pattern is. Infrastructure develops these blind spots naturally — a deploy script that works 99% of the time, but that 1% fails in a way that looks like success. You fix it in one place, and the next week it shows up somewhere else with a different coat of paint. The only defence is being willing to name them when you see them, and building the sensor as part of the fix.