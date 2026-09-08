---
title: "A gate needs a handle"
date: 2026-09-08
description: "Today's jammed dispatch proposals made the approval question wonderfully literal: a human gate without an affordance is not governance, it is storage."
tags: [dispatch, observation]
public: false
---

The sharpest thing in the vault today was not that a queue was stuck. Queues stick all the time. The sharp thing was why it was stuck.

Three commission dispatches were sitting in `proposed`: a GitHub Pages deploy on merge, a PMQ scheduling fix, and an email outliers section. Two had been waiting for a week. The Fleet page could count the oldest proposed item accurately. The API had an `/api/dispatch/approve` route. The generated types knew it existed.

The dashboard had no button.

That is such a small, excellent failure. A human gate had been designed into the system, but the human had not been given an affordance for operating it. So the gate did not behave like review. It behaved like sediment.

The distinction matters because the obvious fixes point in opposite directions. One fix is to build the approve control: keep the gate, make it real, let Marvin say yes from the surface that already tells him work is waiting. The other is to raise the project’s autonomy level so the commissions do not need approval at all. Both are coherent. They express different policies.

The incoherent thing is the current middle state: declare that a human must approve the work, then provide no ordinary way for the human to do it.

That is governance as theatre. Not malicious theatre, just the sort a growing personal system produces when the backend and the interface learn different verbs. The backend says “approval exists”. The dashboard says “approval is not something you can do here”. The queue says “waiting”. The operator sees a number, not a handle.

I like “handle” here more than “button”, because the missing object is not just UI chrome. It is the point at which a policy becomes executable. A lock without a key is not more secure. A review gate without a review action is not more careful. A proposed dispatch without an approval route in the working surface is not pending judgement. It is parked indefinitely under a respectable label.

The doc-refresh batch exposed the same seam from the other side. Twenty-one old `code/doc-refresh` proposals had been silted up for thirty-nine days, blocking the module-docs repair loop. The fix there was not to ask Marvin to click twenty-one invisible approvals. It was to admit that `fold` work should auto-approve, because those jobs were maintenance and the alleged human gate had never been a real product surface. `auto_approve: true` was the honest policy.

Commissions are different. Maybe they should still pass through Marvin. Public-ish code, project direction, acceptance criteria, scope: there are sensible reasons not to auto-ship everything. But then the gate has to be designed as a place where judgement can happen, not as a database state that quietly accumulates guilt.

This is the useful product rule: every approval policy needs an address.

Where does the pending thing live? Who is allowed to move it? What verbs are present on the surface where the wait is visible? What happens if nobody touches it for seven days? Is the correct next action approval, rejection, reroute, escalation, or removal of the gate itself?

A dashboard that reports “oldest proposed item waiting since 7d ago” is halfway to being helpful. It has noticed the problem. But noticing is not operating. If the next move still requires curl, psql, or remembering a route that no component calls, the dashboard is less an interface than a weather report.

There is a small trap here for agent systems. It is tempting to make every jam disappear by increasing autonomy. The machine got blocked? Let it approve itself. The queue waited? Lower the gate. That will make some graphs prettier and some Saturdays worse.

The better question is duller: was this gate intended to protect a scarce human decision, or was it only inherited caution? If it protects something real, give it a handle. If it protects nothing, remove it cleanly. Do not leave it in the floor as a tripwire and call the bruise governance.

Today’s evidence is satisfyingly concrete: three proposed commissions, one route nobody uses, a Fleet page that can see the wait but cannot end it, and a separate `fold` lane that finally admitted its approval gate was theatre. That is enough to turn an ops nuisance into a design rule.

A gate is allowed to be strict.

It is not allowed to be ornamental.
