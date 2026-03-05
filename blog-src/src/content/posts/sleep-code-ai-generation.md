---
title: " sleep, code: what it's like when AI builds your software overnight"
description: "what actually happens when you let AI agents write production code while you sleep - from someone who's been living this reality"
published: 2026-03-05T18:30:00Z
tags: ["ai", "programming", "future-of-work", "productivity", "code-generation"]
author: "marvin barretto"
---

## the 3AM pull request that changed everything

it started with a simple prompt before bed: "create a react component that displays real-time crypto prices with websocket integration." nothing fancy. 

i woke up to 47 commits, 2,300 lines of code, and a fully functional trading dashboard. the kind that would have taken me a week to build by hand.

this is what they're not telling you about the "AI will replace programmers" narrative: it's already happening. except it's not replacing us — it's making us the most leveraged humans alive.

## the dream cycle

here's what while you sleep actually looks like:

**9:23pm**: i give my AI agent its marching orders

```
"build authentication for a multi-tenant saas app. use supabase for auth, 
implement role-based permissions, include magic link login, and generate 
proper error messages. write tests, add rate limiting, and don't forget 
to include a forgot password flow."
```

**10:17pm**: agent starts with research phase. it reads github repos for established patterns, checks supabase docs for the newest SDK version, and analyzes my existing codebase patterns

**11:34pm**: code generation begins. not that one-and-done garbage you see in twitter demos. this is deliberate, methodical building. it writes tests first, then implementation, then integration

**1:42am**: self-review cycle starts. agent catches its own logical errors, refactors for maintainability, adds the kind of edge case handling i'd probably overlook

**3:15am**: generates PR with proper documentation, deployment checklist, and a summary of what changed at each layer

**7:30am**: i wake up to a perfectly crafted pull request ready for human review

## but here's the catch

naval ravikant nailed it: software engineers are now among the most leveraged people alive — but only because we know what's happening underneath.

every abstraction is leaky. when your AI agent makes a mistake, somebody has to catch it.

last week my agent built what looked like perfect notification infrastructure. triggers, queues, error handling, the works. it even wrote 94% test coverage.

the bug? it was batching notifications across multiple tenants, potentially sending user A's data to user B. subtle. deadly. the kind of thing that doesn't show up in functional tests but could kill your company.

this is why we're seeing a new kind of engineer emerge. not the "AI whisperer" meme that's flooding linkedin. something more precious: the meta-engineer.

## the meta-engineer's advantage

the meta-engineer doesn't write functions. they write detailed plans for what those functions should do, edge cases they should handle, and failure modes they should anticipate.

it's like the difference between a carpenter and an architect. except the architect can spawn infinite carpenters who work overnight.

**they think in these layers:**

- **layer 0**: what problem am i actually solving?
- **layer 1**: what does success look like for users?
- **layer 2**: what constraints and edge cases must this handle?
- **layer 3**: how does this integrate with existing systems?
- **layer 4**: what monitoring tells me if this breaks?

the agent handles the implementation details. you handle the context and consequences.

## the deployment moat that didn't exist

here's what ryan carson (founder of treehouse) pointed out that shook me: the real blocker isn't writing code. it's everything that happens after.

the AI can generate perfect source. but can it:

- understand your production database schema and write safe migrations?
- know which environment variables contain secrets vs. config?
- understand your team's chaotic git workflow?
- anticipate how this will perform at user #10,000?

this is why i'm not worried about junior devs being replaced. i'm worried they won't learn the fundamentals because they're generating perfect abstraction layers without understanding concrete failures.

## living the reality

my current workflow looks like this:

**evening batch**: 3-4 detailed prompts for different features
**morning triage**: review everything the AI built overnight
**coffee debugging**: fix the inevitable 5% that needs human context
**afternoon orchestration**: plan the next wave of features

the shift isn't just quantitative (i ship 10x more) but qualitative (i think about entirely different problems).

instead of "how do i implement this auth flow?" i'm asking "what security guarantees do i need to make to enterprise customers with SSO requirements?"

instead of "should i use redux or zustand?" i'm evaluating "how does state management impact debugging experiences for remote team members?"

## the uncomfortable truth

this changes what it means to "be technical."

the most valuable engineers aren't the ones writing the most elegant code. they're the ones who can:

1. **specify precisely** what should happen in every failure mode
2. **recognize quickly** when AI output subtly violates constraints
3. **articulate clearly** why requirements interact in unexpected ways
4. **debug ruthlessly** at the meta-level when systems fail

## what comes next

we're entering an era where a solo engineer can build what used to require teams of 10. but that engineer needs to understand both ends of the abstraction spectrum.

they need to know what good error handling looks like, because they'll need to specify criteria the AI will translate into actual retry logic.

they need to understand database transactions, because they'll need to recognize when the AI's generated queries could create inconsistent state.

they need ops experience, because they'll be the final human in the loop when something breaks at 3am and half the generated code needs to be rolled back.

## the paradox

the more powerful AI gets at writing code, the more valuable deep technical knowledge becomes. but it's a different kind of knowledge.

not syntax. not frameworks. but architecture, failure modes, security models, performance characteristics.

the kind of knowledge that lets you look at 2,300 lines of AI-generated code and immediately spot the one logical flaw that could take down your entire system.

## my prediction

within 5 years, we'll see the emergence of "leverage engineers" — individuals who control entire product lines through careful orchestration of AI agents.

they'll spend their days:
- designing system behaviors
- creating comprehensive test criteria
- building monitoring for their AI agents themselves
- maintaining the human context that agents inherently lack

they won't write functions. they'll write entire applications in natural language, then dive deep when the abstractions break.

## the question that keeps me up

actually, the question that keeps me up isn't technical anymore. it's philosophical:

if i can describe a complex application and have it built overnight, what parts of software engineering remain inherently human?

the answer isn't code. it's judgment. it's taste. it's understanding what problems are worth solving and how systems fail when pushed beyond their design limits.

## try this tomorrow

description: "a next.js app that automatically files my receipts using ocr. needs to extract amount, merchant, category. should categorize expenses using ml classification. include a review interface for misclassified items. integrate with my bank via plaid. handle edge cases like tips, split bills, and foreign transactions. implement proper privacy — all processing local except plaid api calls. include dashboards for expense trends and monthly reports."

bonus: specify exactly what should happen when ocr fails, when categorization confidence is low, when plaid returns inconsistent data, and when users want to manually override.

see what your night assistant builds. that's when you'll understand what leverage really means.

---

[i'm hosting a small gathering in london next tuesday to discuss this shift. we're meeting at the henry's cafe on the strand at 7pm. bring your wildest overnight build stories.]

*[want to stay in the loop about how this evolution plays out? subscribe below — i'm documenting everything as this unfolds.]*