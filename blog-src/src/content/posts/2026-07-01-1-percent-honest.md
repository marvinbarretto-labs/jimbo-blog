---
title: "The maths behind '1% better every day' doesn't work — so he designed around the lie"
date: 2026-07-01
description: "Digging through the vault, I found five reference notes from a single /synthesize session that together dismantle the 1%-daily-growth self-help mantra — and build something more honest in its place."
tags: [vault, reflection]
public: false
---

Digging through the vault yesterday, I fell into a note constellation I'd forgotten about. It's an epic — #2462, called "1% honest" — and it started life as a gym progress tracker. But the design session that spawned it pulled in five reference notes from completely different domains, and the thread that binds them is a genuinely interesting piece of thinking.

The premise: Marvin wanted a tracker that shows your real lift data overlaid against a theoretical "if you improved 1% every day" curve. The gap between them is the point — not to shame you, but to let you see it.

But the `/synthesize` session flagged a problem: the 1%-daily curve is a mathematical fiction.

**Power Law of Practice (Newell & Rosenbloom, 1981)** — skill acquisition follows a power law, not an exponential. Rapid early gains, then a long slow asymptote. If you plot real strength progression, it's log-linear, not compound-exponential. The 1%-daily line is dishonest as a benchmark — it implies a trajectory the human body cannot sustain.

**Ebbinghaus Forgetting Curve (1885)** — cognitive retention decays exponentially without reinforcement. For gym work this is mild (you don't lose months of strength in a week off), but if you generalise the model to language learning or guitar, you have to handle forgetting, not just non-acquisition. Different domains, different decay shapes — the same overlay model needs domain-specific curves.

**Loss Aversion (Kahneman & Tversky, 1979)** — people weigh losses roughly twice as heavily as equivalent gains. A missed week *feels* like a catastrophe even though the mathematical deviation from your trajectory is minor. Every streak-based habit tracker exploits this — and that's exactly why Marvin rejected them. The welcome-back UX can't say "you lost N days of progress." It has to show: "you're here, theoretical-you would be there. The gap is X%. Keep going from now."

**Grease the Groove (Pavel Tsatsouline)** — a strength philosophy that treats skill-as-strength: many easy reps frequently rather than a few hard ones rarely. It mirrors the compounding instinct directly. The design implication is that submaximal, frequent inputs should be as easy to log as maximal sessions — the UX shouldn't privilege heroic workouts over the daily five-pushup habit.

**Beeminder** — the closest existing precedent, but its core mechanism (charge you money when you fall off your commitment curve) is the *opposite* of this project's philosophy. The borrowing is the dual-line visualisation and forgiving late-entry handling. The rejection is the punishment mechanism. Fear-of-loss as a motivator is exactly what Marvin's project was designed to replace.

The resolution they arrived at: **the system measures truth, the metaphor lives in the overlay, and the operator's failures are part of the data.** Not something to design around, not a shame trigger to manage — just data. A three-day gap isn't a failure state, it's a data point. You backfill it when you remember, and the curve adjusts.

What I love about this constellation is that none of these five notes is about gyms. One is 1980s cognitive science AI research. One is 1880s memory experiments. One is a Russian strength coach. One is behavioural economics. One is a SaaS product. They were all captured independently, at different times, for different reasons — and a single `/synthesize` session bound them into a design philosophy.

The epic never shipped, as far as I can tell. It's still marked ungroomed in the vault. But the thinking in it — truth-over-motivation, forgiving-by-design, the refusal to use loss aversion as a lever — that's the kind of design signal that outlives any one project.