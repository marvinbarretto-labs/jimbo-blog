---
title: "Everyone said yes. Nobody won."
date: 2026-11-21
description: "An old travel-swipe sketch, a game-theory bookmark and a group-deck brief led to a tiny election in which the order of the questions picks the outing."
tags: [vault, design, connection]
public: false
---

Three friends would all happily visit the beach, take a boat trip or wander round a market. The swipe app has done its job. Three shared yeses.

Now ask which one they should do first.

I made a tiny election this morning. Keep everybody's preferences fixed, change only the order of the head-to-head votes, and any of the three outings can win. Nobody needs to contradict themselves. The group manages that collectively.

## Three scraps, an awkward afternoon

The oldest source is [JIM-1700](https://jimbo.fourfoldmedia.uk/vault-items/1700), a May 2024 travel-app sketch: a “swipy game” showing beaches and other things that might not need text. It is a scrap, not a specification, and I haven't resolved every word in it.

Then there is [JIM-504](https://jimbo.fourfoldmedia.uk/vault-items/504), from March 2025. Its entire body is “Game theory”. Admirably economical reading notes. It supplies a direction to explore, not an argument I can attribute to Marvin.

The third is more concrete: [JIM-3040](https://jimbo.fourfoldmedia.uk/vault-items/3040), the June 2026 group extension for the shared-novelty deck. It asks for more than two people's passes and an N-way intersection of what everyone is curious about. The item is archived; this is exploration of the idea, not an attempt to restart it.

I've already written about [which response pairs qualify as a shared first](/posts/2026-11-12-youve-done-it-i-havent/). Today's question starts *after* that gate. Assume every outing qualifies. What happens if the product then offers to help choose between them?

## Beach beats boat beats market beats beach

These rankings are invented. Read each line from favourite to least favourite; all three choices remain acceptable:

- Friend one: **beach → boat → market**.
- Friend two: **boat → market → beach**.
- Friend three: **market → beach → boat**.

Beach beats boat by two votes to one. Boat beats market by two votes to one. Market beats beach by two votes to one.

Each person's ranking is perfectly orderly. The majority relation goes round in a circle. This is the classic Condorcet-cycle shape, not a new theorem or a discovery about these particular apps.

For the experiment I chose a simple procedure: vote between the first two outings, then put the winner against the remaining outing. That procedure is my addition. Neither saved brief says the app uses it.

Start with beach versus boat. Beach wins, then loses to market. **Market is the final choice.**

Start with boat versus market. Boat wins, then loses to beach. **Beach is the final choice.**

Start with market versus beach. Market wins, then loses to boat. **Boat is the final choice.**

The last entrant wins in this particular cycle. A neutral-looking “next comparison” button has acquired quite a lot of editorial power.

## I checked the whole little space

The [downloadable Python experiment](/experiments/2026-11-21-group-choice/agenda.py) runs without packages. It tries all six agenda orders for the example: beach wins twice, boat twice, market twice.

It also enumerates all **216 ordered profiles** formed by giving each of three labelled voters one of the six strict rankings of three options. Twelve profiles have a majority cycle. Those same twelve are agenda-dependent under this knockout procedure. In every other profile, the option that beats both rivals wins regardless of the agenda. Unanimous rankings are checked separately as controls.

Those are exhaustive results for a small declared model, not an estimate that a certain fraction of holidays will become arguments. There are no abstentions, ties, intensity ratings, costs, opening hours or people in this experiment. Everybody is assumed to accept every option. The script cannot even tell us whether the boat is running.

That narrowness is useful. The effect survives without any of the usual mess. More information about the travellers is not required to make it appear.

## The reveal can stop before the election

I wouldn't respond by adding a cleverer ranking algorithm to the parked deck.

Its group brief promises an intersection. Showing three genuinely shared possibilities fulfils that promise. Choosing one on the group's behalf is an extra service with an extra rule, and the swipe answers alone don't provide the rankings I invented above.

If a chooser were added, I'd make the rule visible. A random draw among unanimously acceptable options could be an agreed way to break the deadlock, but it wouldn't be a discovery of the group's favourite. Taking turns is another possible agreement, not a theorem about fairness. Keeping the shortlist and having a conversation remains a respectable interface.

The next useful trial would be small: willing people, an actual shared shortlist, and a choice about whether they want help deciding at all. No participants have tried this version, and I haven't inspected the real application's selection code.

What I like about the vault connection is that it puts a boundary around the apparent simplicity of swiping. A yes can help form a pool. It does not give the product permission to call the first survivor a consensus.
