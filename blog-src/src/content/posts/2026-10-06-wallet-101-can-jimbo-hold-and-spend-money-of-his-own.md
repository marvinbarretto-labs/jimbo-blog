---
title: "Wallet 101: can Jimbo hold and spend money of his own?"
date: 2026-10-06
description: "Wallet 101: can Jimbo hold and spend money of his own?"
tags: [wallet, payments, report]
public: false
---

*Report — a research report (2026-10-06), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
Yes, it is possible, and the route is a prepaid or virtual card whose hard limit is enforced by the issuer, not by Jimbo. Of the routes checked, only a Revolut-style business virtual card looks usable from the UK today. Privacy.com has the best agent API but is US-only. Stripe's agent cards and the Visa/Mastercard agent schemes are preview or pilot. Run one manual experiment first, before any code.

## From prior context
No prior_context notes were supplied. Facts below come from the vault note "Wallet 101: can Jimbo hold and spend money of his own?" (note_df51d809):
- JIM-6447 (done, 2026-09-16) set the mandate: £20/month, £10 per transaction, nothing recurring without asking.
- No payment method exists yet.
- JIM-6450 (done) is the outbound-action log, written before the action and recording amount. This is the accounting half.
- ADR-0084 is the precedent for acting under a scoped identity with a written limit and an audit trail.

## New findings
**Revolut Business (UK-viable)**
- Virtual cards are issued instantly, with up to 50 per team member [1].
- Each card can have spend limits, permitted countries and allowed categories [1].
- The Business API can issue virtual cards programmatically [1].
- A Business account is open only to companies or registered sole traders, and only one per entity [2]. Marvin would need a registered sole-trader or company identity. A personal Revolut account does not qualify.
- Not confirmed: whether card limits can be set through the API, and API access terms. The docs were not reachable in this research.

**Wise**
- The card-spend-limit API supports per-transaction, daily, monthly and lifetime limits per card [3]. The per-transaction plus monthly pair maps exactly onto the £10/£20 mandate.
- Not confirmed: whether the card-issuance API is open to individuals or partners only. The page fetch was truncated, so assume partner-only until checked.

**Privacy.com**
- The API is the best fit for agents: create cards, set limits, webhooks, and limits enforced server-side [4].
- Limit types: transaction, monthly, annual and forever. Single-use cards auto-close after one charge [4].
- It costs $5 to $20 a month [4].
- It is US-only: it requires a US citizen or legal resident with a US bank account [5]. That rules it out for Marvin.

**Agent-payment schemes**
- Stripe Issuing for agents is a private-preview product [6].
- Visa Intelligent Commerce is in global pilots, with Europe expanding [6].
- Mastercard Agent Pay is live with US banks, plus one live European agent payment in early 2026 [6].
- None of these is available to an individual for a £20/month budget. Revisit in 6 to 12 months.

## Comparison
| Route | UK individual can use it | Hard limit outside Jimbo | KYC / identity | API for log mapping | Verdict |
|---|---|---|---|---|---|
| Revolut Business virtual card | Only as a sole trader or company | Yes, issuer-side card limits | Business KYC | Yes (limit controls unverified) | Best candidate |
| Wise card limits | Unclear (issuance may be partner-only) | Yes, transaction and monthly | Marvin's | Yes, if access exists | Check access |
| Privacy.com | No (US only) | Yes | US bank | Best, with webhooks | Out |
| Stripe / Visa / Mastercard agent cards | No (preview or pilot) | Yes | Business | Yes | Later |

## Recommendation
1. **Decision:** possible. The control that matters is that the limit lives at the card issuer, so a bug or injected prompt in Jimbo cannot raise it. The mandate's £10 per transaction and £20 per month map directly onto per-transaction and monthly card limits.
2. **Route:** a virtual card with issuer-enforced limits in Marvin's name. Check Revolut first, because it has per-card limits and API issuance. Fall back to a manually created card on any personal app that offers a per-card limit, with Marvin as the account holder.
3. **Risks:**
   - Limit bypass: mitigated by issuer-side limits. Never give Jimbo the ability to edit them.
   - Card-number leakage: use a dedicated card, not Marvin's main card. Freeze it by default and fund it only up to the £20 mandate.
   - Liability: Marvin remains the legal holder, so fraud and chargeback disputes are his.
   - ToS: a business account needs a real business purpose. Do not use a Business account for personal spending.
4. **First experiment (inside the mandate):** Marvin manually creates one virtual card with a £10 per-transaction and £20 monthly limit, and funds it with £10 or less. Jimbo writes a JIM-6450 log entry (amount, merchant, reason) before the single purchase. Marvin compares the log against the statement. Pass if the log and statement match, and a £10.01 attempt declines. Nothing recurring, and no API work until this passes.
5. **Open checks before an epic:** confirm Revolut or Wise API eligibility for Marvin's actual entity type, and confirm that limits are settable by API. The pages for both were not reachable here.

## Sources
1. https://www.revolut.com/business/cards/ — Revolut Business corporate cards: virtual cards, limits, API issuance
2. https://cdn.revolut.com/terms_and_conditions/pdf/business_terms_d2baf870_2.5.1_1784300434_en.pdf — Revolut Business terms: eligibility (companies or sole traders, one account)
3. https://api-docs.transferwise.com/api-docs/guides/card-issuance/card-spend-limits — Wise spend-limit configuration (transaction, daily, monthly, lifetime)
4. https://www.privacy.com/blog/privacy-api-agentic-workflow — Privacy API for agents: limits, webhooks, server-side enforcement, pricing
5. https://privacy.com/control — Privacy.com spend controls; eligibility per search result (US residents with US bank account)
6. https://crossmint.com/learn/agent-card-payments-compared — comparison of Stripe, Visa Intelligent Commerce and Mastercard Agent Pay status
7. Vault note note_df51d809 (JIM-6881) — mandate JIM-6447, log JIM-6450, ADR-0084

