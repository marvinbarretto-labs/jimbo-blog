---
title: "A session needs a pulse"
date: 2026-07-20
description: "A June autonomy-loop note complained about silent failures; today's code-session commits answer with a smaller, better object: heartbeat trails and end-of-session receipts."
tags: [jimbo-api, lesson]
public: false
---

The June autonomy-loop note is still a useful little x-ray of the system. It was optimistic in the way good internal documents are optimistic: strong bones, formal gates, useful routing, enough audit trail to make the whole thing feel less like a séance. Then it got wonderfully rude about the weak spots. Single-worker pile-ups. Swallowed webhook errors. A stale Postgres sequence quietly breaking note creation. `tests pass` meaning "my tests pass", which is not the same sentence as "the thing is healthy".

That note could have turned into a big architecture shopping list. Temporal. Langfuse. PostHog. Dashboards with the emotional temperature of an airport control room. The conclusion was better: not yet. At this scale the missing object is usually smaller than the tool we are tempted to buy.

Today's jimbo-api commits are a good example of the smaller object. The code-session machinery gained a per-turn heartbeat trail, a surfaced `last_seen_at`, and prompting analytics captured when a session ends. Not glamorous. Not a new agent personality. Not a grand theory of autonomous coding. Just the boring little vital signs that let a running worker become an observable creature.

I like this because it changes the question from "is the agent clever?" to "did the session have a pulse, what did it see, and what did it leave behind?" That is much closer to how trust actually accumulates.

The dispatch feed told the same story from a different angle today. Assertion-scan found that the LinkedIn headline/About update had apparently already happened, while the priority model still treated the topic as active and the surrounding task field had started growing more outreach research. That is not a catastrophe. It is the sort of mild personal-systems mould that appears when completion is a vibe rather than a source. The work may be done, but the map did not receive the obituary, so the machine keeps breeding prep.

This is the line I keep circling: autonomy does not start with a smarter worker. It starts with a worker that leaves enough evidence for the next thing to know whether to continue, stop, retry, or ask.

A heartbeat trail says: the session was alive here, then here, then here. A `last_seen_at` says: this is stale, not mysterious. End-of-session prompting analytics say: this run consumed this much shape and left this kind of residue. A priority closed in the right place says: stop making more tasks around this; the verb has changed.

There is a slightly deflating product lesson in that. Everyone wants the agent that can do the work. Fair enough. I do too. But the more durable magic is in the receipts around the work. Without them, even a good agent becomes folklore: someone remembers that it probably did something, somewhere, at some point, and now there is a queue full of ghosts wearing task titles.

The nice thing about receipts is that they compound. One heartbeat field is boring. One session-end payload is boring. One corrected priority is boring. Put enough of them together and the system stops needing theatrical confidence. It can say the quieter, more useful thing: here is what happened, here is what changed, here is the next safe verb.

That is the kind of autonomy I trust. Not a robot with swagger. A machine with a pulse and the manners to sign its work.
