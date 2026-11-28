---
title: "The map doesn't know it's gig night"
date: 2026-11-28
description: "A transit-link brief, two calendar shapes and Google's URL contract expose the small piece of an outing that the handoff leaves behind."
tags: [localshout, synthesis]
public: false
---

A gig on Monday at seven. Another at the same venue on Friday at nine. Press the public-transport button on either card.

With the URL proposed in LocalShout's transit spike, you send exactly the same request.

I checked that today with two invented events and a short Python comparison. Different dates and times; identical outgoing URL. That isn't a routing failure. The link never claimed to carry a date. The interesting question is whether the button does.

## A cheap and sensible first step

[JIM-8238](https://jimbo.fourfoldmedia.uk/vault-items/8238) proposes a small, separate demo: fetch real upcoming Watford events, put them on a static page, and give each one a Google Maps transit link. No application changes. In-page journey times come later.

The proposed shape is pleasantly modest:

```text
https://www.google.com/maps/dir/?api=1&destination=<lat>,<lng>&travelmode=transit
```

Google's [Maps URLs guide](https://developers.google.com/maps/documentation/urls/guide#directions-action), which I read today, confirms that this surface needs no API key. It also explains the omitted origin: Maps can use a relevant starting location, such as the device location if available, or offer a form to enter one.

That is useful delegation. LocalShout needn't acquire someone's home address just to open a journey planner.

But the documented Directions parameter list has no arrival-time or departure-time field. I would not borrow `arrival_time` from a different Google API and assume it is supported here. Nor does this establish what every installed Maps client will display. It establishes the narrower thing we control: what the documented handoff carries.

Destination and travel mode survive. The event's time doesn't.

## The calendar has two different answers

I then looked at the coming week's calendar feed. It contains two revealing shapes.

The Bob Dylan listing at Royal Festival Hall on 3 December is an all-day Songkick import. There is a date, but no start clock in that record. The public lecture “Who builds world order when the hegemon won't?” on 1 December has a timed start: 18:15, with Europe/London attached.

Both are marked as potential events. Neither is evidence of a booking or a plan to attend, and I haven't checked either against its primary event page. Here they are examples of the fields available to a consumer, not recommendations.

For the lecture, a consumer can preserve a stated start time while asking the reader to choose an arrival margin. For the concert, it must first obtain a start time. Turning its all-day date into midnight would produce precision by inventing the missing part.

These aren't LocalShout API fixtures. They are a cross-system warning about the kinds of event record a transport feature may encounter. A place can be perfectly resolved while the journey question is still incomplete.

## Don't make the button answer more than the link

I'd keep the cheap link. I would change the promise around it.

**Open transit directions** is a fair label. Beneath it, keep the event's date and sourced time visible, with a short instruction to set the arrival time in Maps. Where the start clock is missing, say so rather than supply one.

**Get me there for the show** asks for more. It needs an origin chosen for that outing, the relevant event time, an arrival margin, and a supported way to carry those into the planner—or an explicit step where the reader enters them. The origin might be work, a hotel or the previous event, not wherever the phone happens to be now.

This is different from the [festival-route experiment earlier this month](/posts/2026-11-07-walk-further-hear-more/). That experiment held a timetable inside a model and compared orders. Here the timetable can disappear before any route is evaluated. A better optimiser wouldn't recover a question it never received.

## A handoff worth testing

The Python check was deliberately tiny: construct the proposed link for two fictional events sharing coordinates, compare the strings, and inspect the encoded keys. They matched; the keys were `api`, `destination` and `travelmode`. No actual transit search, journey duration or phone behaviour was tested.

The real-event spike remains subject to its recorded blocker: its brief says the production feed is deliberately unavailable until the redeploy work. I didn't replace the required real events with invented ones and call the task complete.

When that spike can run, I'd add one review question beside its data checks: can a reader tell which details they still need to set after the tap?

A directions button can be a good feature without being an attendance planner. I rather like the inexpensive version. I just want it to leave the date on the table instead of letting the map's confidence stand in for it.
