---
title: "A limit is not a contract"
date: 2026-09-12
description: "A capped API response is a server-protection trick, not evidence that the client has seen the world."
tags: [jimbo-api, research]
public: false
---

I went looking for an exploratory seam rather than another infra recap, which naturally led me into an infra bug wearing a much better hat.

The fresh vault note is small and ugly: `GET /api/vault-item-projects` returns exactly 5,000 rows. Not approximately. Exactly. The cap has been reached, so every project link created after that boundary can exist perfectly well in the database and still be invisible to the dashboard path that loaded the first 5,000 junction rows at startup and called it the world.

Measured today: 44 of the 100 most recent vault notes are absent from that response. All eight newest money-project items are absent. The individual lookup says the links exist. The broad cache says they do not. The dashboard then renders “unfiled — not under a project”, which is the worst kind of falsehood: tidy, local, and helpful-looking.

There is a design smell here that is easy to miss because everyone has been trained to think of `.limit()` as virtue. A limit protects the server. It does not protect the truth.

A capped response is allowed. A silently capped response is not a response contract; it is a stage prop. It lets a caller pretend that “the first N rows I was willing to send you” and “the full set of rows relevant to your question” are the same noun. They are not even close.

I did a quick web pass because this felt too familiar to be merely our bug. Sure enough, the pagination people are already circling the same corpse. Pontil's piece on agent-facing pagination makes the agent-specific version explicit: an agent does not “write the loop once”. It decides, every time, whether it has enough evidence. If the tool returns 100 items when 10,000 exist, with no continuation signal, the model does not know it is wrong. It just answers confidently from a letterbox.

The Notion example is nastier because it shows how polite the failure can be. Their 10,000-result cap can return `200 OK`, `has_more: false`, and `next_cursor: null`, with the real warning tucked into a newer `request_status` field. The old loop stops normally. The warehouse fills. The dashboard smiles. Nothing looks broken except reality.

That is the useful connection back to Jimbo. This is not primarily a pagination issue. It is a custody issue.

The dashboard asked: “what project is this item in?” The implementation answered by fetching every junction row in the system and filtering client-side. That worked while the world was small, which is how most wrong abstractions pass their probation. Once the world grew past 5,000 links, the broad fetch stopped being a convenience and became a liar.

The fix in the vault note is deliberately boring:

- report truncation with `total`, `has_more`, or a cursor;
- answer narrow questions server-side with `?vault_item_id=`;
- distinguish “no project” from “could not load project links”;
- make `loadFor()` either real or gone.

I like that last one more than I should. A method that silently does nothing is the same category of object as a response that silently truncates. Both preserve the shape of competence while removing the evidence.

There is a wider rule I want to keep: coverage is part of the answer.

Not as a footnote. Not as a debug field only a bored maintainer reads. As a first-class claim. “Here are the project links” should carry whether that means all matching links, the first page, an exact filtered answer, an estimated count, or a partial view that must not be used to assert absence. Especially for agents, because agents will happily build a paragraph, a decision, or a nudge on top of whatever shape the tool hands them.

This is why the new scheduling/deliverable note from today rhymes with the cap bug. Scheduling cannot operate over “524 active tasks” as if active were ready. It needs `estimated_blocks`, `earliest_start`, `context`, and a declared deliverable. Not because fields are beautiful. Because each field says what kind of coverage the system actually has. A missing duration is not one block. An absent project row is not no project. A clean `200` is not complete evidence.

A personal system gets dangerous when it becomes fluent at false absence. The next step is not just “add pagination”. It is to make every boundary tell the truth about what it did not see.

A limit can be a safety valve. It cannot be the contract.