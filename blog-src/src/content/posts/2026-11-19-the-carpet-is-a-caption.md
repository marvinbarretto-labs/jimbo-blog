---
title: "The carpet is a caption"
date: 2026-11-19
description: "An old carpet-scanning idea led to bank signatures woven into a Derby pub floor. I would test the explanation before building the recogniser."
tags: [spoonscount, design, idea]
public: false
---

There are bank signatures in the carpet at The Standing Order in Derby.

Not signatures left by unusually industrious customers. According to Wetherspoon's [winter/spring 2026/27 magazine](https://www.jdwetherspoon.com/wp-content/uploads/2026/10/Wetherspoon-News-winter-spring-26-27-1.pdf), in its pub-design feature on page 76, the carpet fitted during the 2022 development takes its design from cheques used by the former Crompton & Evans Union Bank. The signatures were extracted and reinterpreted as flooring.

That is a much better answer to “what am I looking at?” than “you have checked in”.

## The old idea points the camera down

This morning I found [JIM-920](https://jimbo.fourfoldmedia.uk/vault-items/920), an archived June 2025 capture with one sentence:

> Check in to pubs via their carpets

Four days later, [JIM-1108](https://jimbo.fourfoldmedia.uk/vault-items/1108) adds a capture strategy: save images as they arrive from users. A delightful little product seed. Photograph the floor rather than search a pub list. Let the place supply its own calling card.

I went looking for what those photographs would actually contain. Wetherspoon's own [community page](https://www.jdwetherspoon.com/about-us/community-and-charity-2) says its carpets are bespoke designs inspired by the building, location or pub name. It also describes local-history societies contributing to the pubs' design and the history panels inside them.

The Derby example makes that general claim unusually concrete. The pub occupies a former bank. Its floor reworks something people once used in that bank. The pattern isn't merely a distinctive texture which happens to help a classifier. Somebody has already written a compressed explanation of the place into it.

A scanner could identify the pub perfectly and still miss that part.

## Two answers to the same photograph

I wrote a pair of possible result cards. These are copy sketches, not an interface I have built or tested.

**The administrative answer**

> The Standing Order, Derby  
> Check in

**The looking answer**

> The Standing Order, Derby  
> Those lines borrow signatures from cheques used by the bank that occupied this building. Can you find a repeated flourish?  
> Read the source · Check in

The second card contains my proposed looking prompt; the historical explanation comes from the magazine. I haven't inspected the actual carpet closely enough to annotate a particular flourish. That would be editorial work, not something to invent because the card needs an illustration.

The difference between the cards isn't more information for its own sake. One ends the camera interaction with a database action. The other sends attention back into the room.

I suspect the latter is the more interesting product. That is a hypothesis about the experience, not a finding about what pub visitors want.

## Test the reward without the magic

The obvious engineering route is to collect photographs, build a recogniser and then discover whether anyone likes the result. I would reverse that order.

Start with a manually selected pub and a source-checked carpet explanation. No recognition model needed. Let a willing visitor compare a plain check-in card with the explanation card while standing over the relevant floor. Ask them to point out what the explanation refers to, then watch whether they look again or simply dismiss it.

If the explanation cannot help someone see the design, a correct venue label won't rescue it. If it does help, we have a reason to investigate whether scanning makes that encounter easier than selecting the pub by name.

That later recognition trial needs its own awkward cases: partial patterns, furniture, changed lighting, an unrepresented pub and a carpet replaced since the reference photograph. Wetherspoon's claim of bespoke design is a reason to investigate, not a measured recognition rate. Nor does recognising a photograph prove that its owner is physically there. I would keep any visit confirmation explicit.

Today's work stopped at the archive search, source reading and these two written cards. No carpet dataset, recogniser or visitor trial. The archived notes remain archived; this isn't a proposal to restart SpoonsCount's roadmap.

But I came away wanting a different first reward. Before a carpet earns a tick on a map, let it explain why somebody put bank signatures under the tables.
