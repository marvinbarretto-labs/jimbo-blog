---
title: "Portfolio: four projects, one thread"
date: 2026-08-27
description: "Portfolio: four projects, one thread"
tags: [portfolio, ai-translator, report]
public: false
---

*Report — a draft (2026-08-27), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

Four projects, one thread: making software that meets the real world halfway and does not fall over when the real world is scruffy.

Most good software engineering is invisible. A background pipeline that never crashes. An enrichment layer that catches up after a messy capture. A notification that arrives at the right moment because the scheduling logic accounted for timezones, weekends, and one slow API. The projects below share a common thread: each solves a concrete problem through systems thinking, solo delivery, and a refusal to treat surface polish as the main event.

## Jimbo / Hermes — personal AI infrastructure

Marvin needed an assistant that could actually act — not a chatbot that talks. The result is Jimbo, running on the Hermes agent platform: a persistent AI system with multi-agent orchestration, a briefing pipeline that digests inbox items before he wakes up, a vault that tracks 1,500+ structured notes with dependency relationships, and a self-updating context model that evolves with his priorities. The orchestration layer dispatches work to specialised agents (coders, researchers, drafters) and routes the output back into his inbox, his blog, or a pull request. A scheduling pipeline handles time-sensitive briefings, dispatch deadlines, and reminder nudges without manual intervention.

What was hard: building a multi-agent system that stays reliable enough to run unattended — every prompt, every fallback, every error path had to work without a human in the loop. What it demonstrates: the ability to design, ship, and operate a production-grade agent infrastructure from scratch, solo, with no prior template.

## LocalShout — community platform

Local events are notoriously fragmented. Facebook Events, Meetup, Instagram stories, pub noticeboards, and local news sites each hold a piece of the picture. LocalShout pulls them together into a unified discovery experience: a weekly email digest, a searchable event feed, and personal taste profiling so the recommendations improve over time.

What was hard: building an event ingestion and deduplication pipeline that handles the chaos of real-world event data — inconsistent formatting, stale listings, multi-source duplicates — without manual curation overhead. Near-launch with the core pipeline running daily, the email digest delivering, and the feedback loop tuned. What it demonstrates: full-stack delivery (Next.js, Postgres, LLM enrichment, email integration) on a tight timeline.

## Browser extension — background service workers

A browser extension that runs background tasks via service workers, managing persistence through the extension lifecycle without a dedicated server. The problem was straightforward: how does a lightweight browser tool maintain state, run periodic checks, and communicate results to a user who may have closed the tab hours ago?

What was hard: navigating the constraints of service worker lifetimes, Chrome extension APIs, and cross-browser compatibility — while keeping the extension small enough that a user would actually install it. What it demonstrates: breadth beyond web applications. The ability to work across platform boundaries — browser internals, background processing, and UX design for the long tail of install-once tools.

## SpoonsCount — mobile app with real-world rhythm

A pub check-in app — Angular, Firebase, Capacitor — that lets people discover where their friends are drinking and join them without the friction of group DMs. Live in production, with magic-link authentication, push notifications, and a real user base.

What was hard: cross-platform mobile development with Angular and Capacitor, real-time data sync via Firebase, and keeping the app lightweight enough for casual use — the kind of quick-open, quick-close experience that means people actually use it rather than just installing it. What it demonstrates: mobile delivery from concept to production, including web hosting, auth flows, and notification infrastructure.

---

Each of these projects started as a question — "can I build that?" — and ended as a running system. Together they trace a line through full-stack web development, mobile, browser extensions, AI orchestration, and data pipeline engineering. The common denominator is not the technology stack; it is the ability to pick up unfamiliar territory, build something that works, and ship it. That is the capability that matters for a team that needs someone who can translate between what AI can do and what a product actually requires.

