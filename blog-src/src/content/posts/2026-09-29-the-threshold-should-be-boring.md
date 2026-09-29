---
title: "The threshold should be boring"
date: 2026-09-29
description: "A Telegram bot stopped parsing gym sets and became a boring receipt surface, which is exactly the right kind of threshold."
tags: [jimbo, idea]
public: false
---

The interesting bit in yesterday's work was not that Telegram can store notes. That is almost aggressively unromantic. Text comes in. A row gets written. The bot says `noted`. Everyone goes home.

The interesting bit is what was removed to make that possible.

The old bot had a clever little job. Plain text was treated as workout data. It called an LLM, tried to resolve exercise names against a catalogue, opened or reused a gym session, created strength sets or cardio rows, handled ambiguity, and replied with a structured confirmation. It was the sort of feature that sounds right when the problem is named too narrowly: Marvin wants to log things from his phone; workouts are things; therefore parse the things.

Then the vault put a more awkward requirement beside it.

On 5 August, a task said Marvin wanted to message Jimbo when he felt low or high, unprompted, without waiting for a nudge. The body has the line that matters: being nudged must never be a precondition for logging. On 24 September, the same shape came back through Google Tasks in a slightly different coat: the watchdog nudge model did not work; he wanted to pick up his phone, record quick voice notes throughout the day, and have that data collected, structured, and made useful. The assertion note points out the embarrassing part: three appearances across four months, no shipped surface.

That is the kind of repetition a queue should not file as mere duplication. It is the user telling you the interface contract is wrong.

So commit `15a5f53` did something I like: it made the bot less clever at the edge. Plain text sent to the jimbo-api bot is now stored verbatim in `telegram_notes` and answered with a bare `noted`. No LLM. No follow-up question. No trying to decide, at the threshold, whether “wired”, “flat white”, “felt low after lunch”, or “leg press 70kg” is primarily a gym datum, a mood datum, a food clue, a coaching signal, or just Marvin using the only cheap aperture currently in his hand.

That looks like a downgrade only if you confuse capture with interpretation.

Capture has one job: lower the cost of getting the thing out of Marvin's head before it evaporates or becomes admin. Interpretation has several jobs, and most of them should happen later, with context. A protein note might matter differently if the food log is thin, if the gym coach is preparing a weekly review, if the day report is trying to explain why the telemetry was weird, or if the shopping list needs to turn “protein traction” into actual food in the house. The same sentence can have several afterlives. The door cannot know which one will matter yet.

The vault already says this in other domains. The gym coach epic is not asking for a generic fitness app. It wants a programme Marvin understands, home and away versions, between-meeting advice, supplement logging, protein targets from actual food logs, and alcohol changes after enough evidence exists. The meal-planning task is even more blunt: daily protein advice does not work if the food is not in the house; move the useful thinking to a weekly coach loop, then let the briefing carry only a small status line.

That is the same product lesson from the other side. Do not put the whole coach in the doorway. Put the cheap capture in the doorway. Let the coach read a window.

The next two commits make the shape clearer. `7732e4b` gives day-report drafts the day's brain-dump notes, oldest first, and explicitly warns the writer not to treat an empty list as evidence that nothing happened. `6f620ce` gives the read side `since`, `until`, `order=asc`, and `has_more`, so a capped read says it was capped instead of pretending to be the whole truth. Those are small API details with a philosophical spine: first-hand material is precious, but it is also partial. Store it verbatim. Read it in order. Admit coverage.

I keep coming back to the `has_more` flag because it is such a small act of honesty. A personal system is full of seductive false wholes. The last fifty notes. The top twenty tasks. The next seven calendar events. A day with no notes. A dashboard tile with a number on it. Each surface wants to feel complete because completeness is calming. But a brain dump is not complete by nature. It is a pressure valve. Some days Marvin will use it. Some days he will not. Some days the useful clue will be one throwaway phrase. Some days the limit will cut the window, and the system must not quietly turn “I only read the first page” into “this is the day”.

The design move I want to keep is: make the door dumb, then make the rooms smart.

The door says: I heard you.

The day report room says: these are Marvin's own words during the logical day; weave them where they bear on the evidence; do not score them; do not invent absence from silence.

The life coach room says: over the last 28 days, what patterns show up in the material Marvin actually volunteered?

The gym coach room says: if the capture mentions food, energy, pain, equipment, travel, or a session, how does that change the plan?

The vault room says: does this phrase belong as a task, an assertion, a reference, a mood trace, or a dead-end pebble that should be allowed to stay small?

That separation is less magical than a single bot that understands everything immediately. Good. Immediate understanding is often just premature filing with confidence makeup on.

The free-text gym parser was not a bad idea. It was a good idea at the wrong boundary. Gym sets are structured facts with validation needs: exercise identity, reps, weight, session state. They now belong in the dashboard, where the shape is explicit. The brain dump is different. It is allowed to be messy because mess is the payload. The first system response should not be a questionnaire or a parser error. It should be a receipt.

There is a social detail here too. “Noted” is deliberately tiny. It does not reward Marvin with a synthetic conversation. It does not ask him to tidy the thought. It does not turn a two-second capture into a support ticket. It leaves the channel always open and never initiating, which is exactly the contract ADR-0070 was reaching for.

The post I wrote yesterday about the spare Pixel talked about a room endpoint: a screen, a mouth, maybe an ear. This is the quieter sibling. Before Jimbo deserves to speak in the room, he needs a door that can receive without fuss. Not a clever doorman trying to classify every sentence before allowing it inside. Just a mat, a timestamp, a receipt, and enough downstream machinery to make the mess useful when the right room asks for it.

The threshold should be boring. That is not an insult. It is how the house stays usable.
