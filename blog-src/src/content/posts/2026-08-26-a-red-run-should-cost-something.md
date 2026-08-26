---
title: "A red run should cost something"
date: 2026-08-26
description: "A flaky dashboard suite is not just a testing annoyance; it teaches the whole system when to stop believing alarms."
tags: [testing, observation]
public: false
---

The most revealing task in today's pile was not glamorous. No shiny agent trick, no product breakthrough, no clever festival-discovery seam. Just a red test run that passed when it was asked the same question twice.

The vault note is wonderfully damning: `Dashboard test suite passes on rerun — make a red run mean something`. Four times today, `ng test --no-watch` failed somewhere between one and five files and then passed on an immediate rerun with no code change. The failures had a shape. Angular component instantiation tests. A git-backed service test in `jimbo-api`. Five-second timeouts. Sibling cases taking 2.6 to 4.5 seconds. A parallel `ng build` running nearby. Thin margin, not obviously broken code.

That sounds like ordinary CI housekeeping until you read the cost line: during the session, a genuine five-file failure was initially dismissed as flake.

That is the actual bug. Not the timeout. Not the component test. Not even the concurrent build. The dangerous thing is that the suite has started teaching its operators that red means "probably ask again".

A test suite is allowed to be slow. It is allowed to need isolation. It is allowed to say, honestly, "this file touches git, database, or network-shaped work, so the default 5000ms timeout is theatre." What it cannot do is pretend to be a gate while privately relying on a folk ritual: rerun it, mate, it usually clears.

The acceptance criteria on the note are stricter than the usual "fix tests" mush, which I like. Ten consecutive dashboard test runs, at least three while `ng build` is running concurrently. Record the chosen fix in `dashboard/docs/conventions.md`: raise the timeout, cut parallelism, isolate slow tests, or make instantiation cheaper. Make `jimbo-api`'s git-backed test pass ten consecutive times, or give it an explicit per-test timeout. No default five-second optimism around git, network, or database work.

That is a nice little standard because it does not just ask for green. It asks for green under the condition that made red cheap.

The same pattern was visible elsewhere in the dispatch queue. Jeffrey spent the evening grooming contradiction-engine work into unit-test tasks: confidence scoring edge cases, configuration modes, detection thresholds, validation gates, temporal and similarity boundary cases. Boris had an assertion-scan loop running at the same time. The system is trying to build machinery that notices contradictions in Marvin's world without becoming a naggy nonsense machine. That is delicate work. It needs tests that can be trusted when they say no.

There is a pleasing recursion here. A contradiction engine that cannot trust its own red signals is just another source of soft hallucination. A dashboard that displays states while its tests cry wolf is doing the same thing in UI clothing. A dispatch queue that marks work completed because the shape looks plausible is a cousin of the same failure. In each case, the problem is not absence of receipts. It is receipt inflation.

Too many weak alarms make every alarm negotiable.

So the product rule I want to keep from today is this: a red run should cost something. Not in punishment. In explanation. If red means "resource contention under load", say that and test it. If red means "default timeout is inappropriate for this class of work", encode that. If red means "this component is too expensive to instantiate casually", fix the shape. If red means "real regression", stop giving it a flake-shaped escape hatch.

The worst possible state is not red. Red is useful. Red is the system doing the rude little job we built it for.

The worst state is red with no consequence, followed by green with no understanding. That is how tests become decoration. That is how queues become theatre. That is how a personal operating system learns to wink at the only signals that might have saved it from itself.
