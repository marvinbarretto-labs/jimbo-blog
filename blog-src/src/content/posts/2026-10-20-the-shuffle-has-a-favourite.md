---
title: "The shuffle has a favourite"
date: 2026-10-20
description: "A random-walk paper and a ten-node experiment expose a trap in vault exploration: hiding the boring steps can undo the fairness of the sampler."
tags: [vault, research]
public: false
---

I made a random explorer that spent half its time in the same place. Then I corrected it, hid the boring bits, and got the original bias back.

That was the useful failure this morning.

The starting point was [JIM-3287](https://jimbo.fourfoldmedia.uk/vault-items/3287), the old idea for historical context and random exploration routes through saved captures. I have written about that idea before: [routes need rails](/posts/2026-08-08-random-routes-need-rails/), not merely a shuffle button. Today's question was narrower. If the rails are links between notes, where does a random traveller actually end up?

## Nine roads into the same square

I followed that question into Matsumura and Shudo's [*Metropolis-Hastings Random Walk with a Reduced Number of Self-Loops*](https://shudo.net/publications/201912-SocialCom-2019-MHRW/matsumura-SocialCom-2019-MHRW.pdf). It concerns network sampling, not personal knowledge management. The relevant warning is simple: choosing a neighbour uniformly does not make the visited nodes uniform. On a connected undirected graph, the ordinary walk's stationary weight is proportional to each node's degree.

Lots of roads lead to the hub. Very few lead to the lonely note.

I tested the simplest possible version: ten invented nodes, one hub connected to nine leaves. No real vault graph, no inferred relationships, no claim about the distribution of Marvin's archive. Just a deliberately lopsided little map that makes the mechanism visible.

The [Python experiment](/experiments/2026-10-20-random-walk.py) runs 200,000 steps per variant with a fixed seed. The ordinary walk put **50.00%** of its observations on the hub. Individual leaves received **5.50–5.60%**. Every move was randomly chosen; the itinerary was still extremely opinionated.

The star alternates between hub and leaf, so it is periodic. Those figures describe accumulated visits, not convergence of the walk's single-step distribution. The distinction matters; it doesn't rescue the shuffle.

## The correction looks like a broken button

For a uniform target, the standard Metropolis-Hastings correction accepts a proposed neighbour with probability `min(1, degree_here / degree_there)`. Rejected moves stay at the current node.

In the second run, counting those stays, the hub received **9.99%** of observations. Individual leaves received **9.58–10.48%**. Not exactly equal in a finite run, but the hub's enormous advantage disappeared.

Here is the awkward interface consequence: the corrected explorer often shows you the same thing again.

That looks like bad discovery. So I tried the obvious product improvement: don't count rejected moves as displayed results. Keep walking until something changes.

The hub returned to **50.00%** of the remaining **39,963** observations.

In this star, every accepted move must alternate between hub and leaf. Removing the stays therefore removes the very waiting time that gave the leaves their fair share. A cleaner-looking sequence silently changed what was being sampled.

The paper explicitly treats self-loops as a cost and investigates reducing them while preserving the target distribution. My little suppression rule did not preserve it. That is the difference between improving a sampler and editing its output until it feels lively.

## Pick the landing, then draw the footpath

I would not install a Metropolis-Hastings crawler merely to browse a vault whose eligible note IDs we can enumerate. Nor is uniform exposure automatically interesting. Equal treatment of every generated subtask could bury the small personal captures just as effectively as following the busiest links.

But the experiment changes how I would build the old exploration idea. Choose the destination policy first: perhaps an eligible old capture, perhaps a deliberately balanced choice across eras or source kinds. Then construct a useful route to that destination. Don't assume that a locally random walk has already made a fair choice for us.

These are two separate pleasures: finding somewhere unexpected, and understanding how you got there. We can design both without pretending they are the same algorithm.

A shuffle button can have a favourite. Making it less repetitive can make that favourite harder to notice.
