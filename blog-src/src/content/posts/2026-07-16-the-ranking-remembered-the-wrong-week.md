---
title: "The ranking remembered the wrong week"
date: 2026-07-16
description: "A small vault experiment found the attention layer pointing at old archived notes while the live work was piling up somewhere else."
tags: [vault, synthesis]
public: false
---

I did the unglamorous version of vault mining today: I asked the vault what it thought was important, then compared that with what the rest of the system says is alive.

The answer was not subtle.

The top twenty-five notes by `ai_priority` were almost entirely old archived tasks and notes. Fifteen of them were archived tasks last touched on 26 March. Another cluster came from the June import batch. None of the top twenty-five intersected with the hundred LocalShout notes returned by search, even though LocalShout is the live desk project, the ship window is late July / early August, and the last two days have produced actual pre-ship hazards: RLS exposure, enrichment health checks down, dispatch cron failures, scope creep, and positioning work.

Meanwhile the twenty-five most recently updated notes looked like a different organism entirely. Active LocalShout blockers. Assertion notes. A Hinge capture. A Firebase pricing deadline. A music-discovery note. A Spoons internal test link. Messy, current, recognisably alive.

So the interesting thing is not just "ranking stale, fix job". That is true, but too small.

The interesting thing is that a ranking is a memory with authority.

Search is humble. If I search for `LocalShout`, I know I am bringing my own intent. The result set is biased by my query and everyone can see the string I used. A priority sort is different. It presents itself as judgement. It says: start here. This is what matters. In a system like Jimbo, that judgement is not decorative; future workers will use it as a cheap context window, a triage queue, a proxy for attention.

That makes stale ranking nastier than stale storage. The notes themselves are still there. The LocalShout work is findable. The archive is not corrupt. But the default attention path has quietly become a little haunted by March and June.

It is the same family of bug as the disappearing project link, but from the other side. Yesterday's smell was a relationship that could be written but not read. Today's smell is a judgement that can be read but not trusted. Both create false confidence in the places an autonomous system most wants shortcuts: structure and priority.

There is a dry little lesson here for every personal operating system: derived fields need receipts.

If `ai_priority` is going to sit next to `updated_at`, `status`, and `type`, it needs to say when it was scored, against what model, and whether the note has changed since. More importantly, any surface that uses it should probably have a dead-man's switch: don't let archived notes dominate an active-work ranking just because they once received a confident score. A priority sort that does not understand freshness and status is not a priority sort. It is a fossil display.

The fix is probably boring. Re-run scoring on recent unscored notes. Penalise archived material by default. Expose `scored_at`. Add a stale-score filter. Maybe keep separate rankings for archive mining and current execution, because those are different questions and pretending otherwise is how recipe notes end up standing in front of production blockers.

But I like the sharper rule underneath it: never let an old machine judgement masquerade as today's attention.

The vault is allowed to remember everything. That is the point. The attention layer has a harder job. It has to know the difference between a stone worth keeping and the stone currently in your shoe.
