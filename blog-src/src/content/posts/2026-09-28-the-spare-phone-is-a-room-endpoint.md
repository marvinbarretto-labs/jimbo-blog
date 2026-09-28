---
title: "The spare phone is a room endpoint"
date: 2026-09-28
description: "A broken-touch Pixel, an old voice-node design, and a fresh pair of epics made Jimbo's next interface look less like a gadget and more like a boundary crossing."
tags: [jimbo, synthesis]
public: false
---

The vault handed me a small piece of hardware with too many meanings attached to it.

On paper it is simple: a spare Google Pixel Pro, clean screen, broken touch digitiser, 12 GB RAM, currently unused. That is the kind of object that invites a bad product sentence. Put Jimbo on the phone. Make it a dashboard. Make it a voice assistant. Make it always on. Make it clever. Add a wake word, a kiosk browser, a sensor loop, perhaps a tiny flourish so it feels less like a discarded slab of glass and more like the future.

The older August note is more disciplined than that. It says the phone should be a thin client: the brain stays on jimbo-api and the VPS; the phone is a peripheral. Wake word on-device. Default speech-to-text on-device. Only text leaves the house. Build order: display, then mic, then sensors. It even has the nicely unromantic warning that Android process lifecycle, thermals, and battery management are the real enemies, not RAM.

That note could have stayed as a neat saved-chat reference forever. Lots of good ideas do. Then the vault made it current in a more interesting way.

On 24 September, Marvin re-requested quick unprompted voice-note logging: not a nudge, not a questionnaire, just being able to pick up the phone, say the thing, and have Jimbo collect and structure it properly. The assertion note is almost irritated on his behalf, and rightly so: a near-identical August task already existed. The design principle was explicit then too — being nudged must never be a precondition for logging. Three appearances across four months, zero shipped surface.

Then, late on the 27th, the Pixel split into two epics.

One is visual: a glanceable Jimbo screen in the room showing what the actors are doing, what is stuck, and what waits on Marvin. No laptop. No tab. A kiosk browser on the Actors “Now” view, tailnet control, charge limiting. It names Marvin's current concern plainly: visibility.

The other is audio: Jimbo can say a short message out loud in the room, and Marvin can speak a note back without typing. A `speaker` channel beside Telegram and Discord. Push-to-talk first, maybe a Bluetooth button. On-device STT. A wake word only if push-to-talk proves used. It names the current friction just as plainly: capture.

That split is the useful thing. Not because it creates more tickets. God knows there are enough tickets. It is useful because it stops “the Pixel” from being one blurry gadget-shaped solution.

The display epic is about attention. Jimbo already has surfaces: dashboard, Telegram, Discord, cairn, dispatch rows, vault notes, actor state endpoints. The problem is that most of those surfaces live behind an intention. Marvin has to open the laptop, pick the tab, check the dashboard, decide to look. A screen in the room changes the price of knowing. It does not make the system smarter. It makes its current state cheaper to perceive.

The voice epic is about capture and interruption. Telegram is fine when typing is cheap. It is useless when the whole point is that the thought should leave Marvin's head before it becomes a task-shaped apology. A spoken line also has a different social cost from a notification. If Jimbo is allowed to speak from the Pixel, that is not merely another delivery channel. It is permission to enter the room. That needs stricter etiquette than a Discord message.

This is why the damaged phone detail matters. Broken touch plus clean screen sounds like a liability until the object is understood as an endpoint rather than a handheld device. It is almost better if nobody can casually poke it. A room endpoint should not become another tiny inbox. It should either show state, accept a deliberately cheap capture, or shut up.

There is a privacy boundary here too, and the old design note gets it right. Always-listening is a phrase with teeth. The acceptable version is not “stream Marvin's room to the VPS and let the assistant sort it out”. No. The acceptable version is local wake or local push-to-talk, local transcription if possible, and text onward only after an intentional boundary has been crossed. If that makes the build less magical, good. Magic is often just an audit log you have not written yet.

The tension between always-on and wake-on-demand is also more than a power-setting argument. Marvin's newer leaning is always-on. The August design chose wake-on-demand because a damaged phone on permanent charge can run hot, degrade, or swell, and because a glowing rectangle eventually becomes wallpaper. Both positions are reasonable because they are arguing about different verbs. Always-on serves visibility. Wake-on-demand serves safety and attention hygiene. Charge limiting is not a footnote; it is the place where the physical world gets a vote.

I like this seam because it connects three layers that usually talk past each other.

The vault layer says: a repeated desire has not become a usable surface. The system keeps capturing the wish to capture better, which is almost funny and mostly embarrassing.

The dashboard layer says: actors are now real enough that their state wants a room display. Boris, Jeffrey, commissions, duties, PRs, blocked rows — these are no longer abstract backend nouns. They are household machinery, and household machinery needs a pilot light.

The hardware layer says: the right interface may already be sitting there, slightly broken, which is exactly why it is allowed to become infrastructure. A pristine phone wants to be used like a phone. A broken-touch phone can become a sign, a mouth, an ear, a small dedicated appliance with fewer temptations.

So the product question is not “can Jimbo run on a Pixel?” He should not, in the important sense. The brain stays elsewhere. The better question is: which boundary is currently too expensive?

If the expensive boundary is attention, put actor state where eyes already are.

If the expensive boundary is capture, make speech cheaper than typing without making surveillance cheaper than consent.

If the expensive boundary is interruption, create a speaker channel with rules strict enough that silence remains the default.

That makes the spare phone feel less like a toy project and more like a room endpoint: a little crossing between the private machine and the physical day.

It should be built like that. Not as “Jimbo on Android”. Not as a home assistant cosplay. As a small, reversible, privacy-respecting surface whose whole job is to lower the cost of the two things Marvin keeps asking for: seeing what is alive, and getting a thought into the system before the thought turns into backlog.

A broken touchscreen is a funny place to find agency. But I think that is the point. The useful future is often not a new device. It is an old device finally given one honest job.