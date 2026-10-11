---
title: "Decide whether Monzo Extra earns its £3/mo, and where cash earns most"
date: 2026-10-11
description: "Decide whether Monzo Extra earns its £3/mo, and where cash earns most"
tags: [money, savings-rates, report]
public: false
---

*Report — a research report (2026-10-11), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**Downgrade to free Monzo.** Extra's only hard-money benefit is +0.25% AER on Instant Access pots (3.00% vs 2.75%). That beats £36/yr only if more than £14,400 sits in Monzo pots, and Monzo's free Select Access pot (3.15%, ≥£500, ≤2 withdrawals) out-earns Extra's instant pot anyway. The bigger lever is Metro: its published rate is 0.90% AER, not the 2.48% in the vault. If that is the real rate, moving ~£11.3k to Monzo gains about £209–£299/yr. Rates were checked 2026-10-11.

## From prior context
- Extra is £3/mo, YNAB payee `Extra`, filed `Desirable · Subscriptions · Monzo` (note *Decide whether Monzo Extra earns its £3/mo…*).
- Personal pots are ~£16.6k with Metro Savings at 2.48% AER (note *Give each pot of cash a job…*). The 2026-09-11 scenarios report puts Metro Savings at £11,266 / 2.48%, and personal sterling (Halifax + Metro + Monzo) at £12,415. Per-account balances for Halifax and Monzo Savings were not available. The money API (`/api/money/summary`) gives only personal total £43,358, which includes Wise USD. `jimbo-money/data/money/CONTEXT.md` does not exist at the path the task names.
- Out of scope: Fourfold company accounts, investment advice.

## New findings

### Plans (Monzo plans page, checked 2026-10-11)
| Plan | £/mo | Instant Access AER | Select Access AER* | Notable features |
|---|---|---|---|---|
| Standard | 0 | 2.75% | 3.15% | 1 connected account, 1 credit score, £200 free ATM abroad |
| **Extra** | **3** | 3.00% | 3.15% | Connected banks/cards, virtual cards, advanced roundups, custom categories, auto-spreadsheet, 2 credit scores, Billsback (prize draw, up to £150), 5% Saving Challenge |
| Perks | 9 | 3.25% | 3.65% | Extra + £600 ATM abroad, 3 free cash deposits, Uber One, Railcard, Greggs, Vue, YouTube Premium Lite, discounted investment fees |
| Max | from 19 | 3.50% | 3.65% | Perks + travel/phone insurance, breakdown cover |

*Select Access: ≥£500, ≤2 withdrawals/yr.

Note: a search summary quoted Perks £7 / Max £17. Monzo's own plans page and savings page both say £9 / £19, so I used those.

### What Marvin uses
I can't see feature usage from the repo. The vault evidence is that he budgets in YNAB, so Extra's custom categories, auto-spreadsheet and spending tools duplicate what he already has. Billsback is a lottery. Connected banks and credit scores are the only features that could matter. Marvin should confirm whether he opens them. Everything else Extra adds is free in YNAB.

### Instant-access rates (checked 2026-10-11)
| Pot | Rate | Source / caveat |
|---|---|---|
| Monzo Savings (free plan) | 2.75% AER var; Select Access 3.15% | monzo.com/features/savings, monzo.com/current-account/plans |
| Monzo Savings (Extra) | 3.00% AER var | same |
| Metro Instant Access Savings | **0.90% AER var** | metrobankonline.co.uk product page; June 2026 Important Information Summary says the same. **Conflicts with the 2.48% measured in the vault** (possibly a different or legacy Metro product, or a figure that has since changed). Marvin to check the Metro app. |
| Halifax Reward Bonus Saver | 3.00% AER var for ≤2 withdrawals/yr, 0.65% from the 3rd | DepositScout (undated). Halifax's own page errored; an older snapshot showed 3.50%. Tied to the Reward current account. Halifax is being folded into Lloyds on 31 Oct 2026. **Unconfirmed.** |
| Halifax Everyday Saver | 1.00% | DepositScout, unconfirmed |
| Monzo current account | no interest | n/a |

### £/year gains (on the £11,266 Metro balance; Halifax/Monzo balances unknown)
| Move | If Metro is 0.90% | If Metro is 2.48% |
|---|---|---|
| Metro → Monzo free instant (2.75%) | +£208 | +£30 |
| Metro → Monzo Select Access (3.15%) | +£253 | +£75 |
| Metro → Monzo Extra instant (3.00%) | +£237 | +£59 (before the £36 fee) |
| Extra vs free, on same £11,266 | +£28, less £36 fee = **−£8** | same |
| Break-even for Extra | £14,400 in Monzo instant pots | |

Even if all ~£16.6k personal cash sat in Monzo instant pots, Extra's uplift is £41.5/yr against a £36 fee, a net gain of about £5.

## Recommendation
1. **Downgrade Extra → free.** The uplift only pays for itself above £14.4k in Monzo pots, and the tools duplicate YNAB. If Marvin does open connected banks or credit scores, that's the one reason to keep it.
2. **Check the Metro rate in the app today.** If it's 0.90%, move Metro Savings to Monzo (free plan). Put ≥£500 into Select Access (3.15%) if he can live with ≤2 withdrawals a year, and the working balance in the 2.75% instant pot. If it really is 2.48%, the move is worth only £30–£75/yr, so it's optional.
3. **Halifax:** leave it alone until the Lloyds migration on 31 Oct settles and the rate can be read from the live page. Don't open anything new for a ~£3k-or-less pot.
4. **YNAB (Marvin does this after reading):** if downgraded, set the `Desirable · Subscriptions · Monzo` budget to £0 (it was £3). Any other Monzo item in that category stays.

Not done by me: no plan change, no money moved, no YNAB edit.

## Sources
1. https://monzo.com/current-account/plans — plan prices, features, savings rates
2. https://monzo.com/features/savings/ — instant access AER by plan
3. https://www.metrobankonline.co.uk/savings/products/instant-access-savings/ — Metro 0.90% AER
4. https://www.metrobankonline.co.uk/globalassets/documents/customer_documents/retailonline-instant-access/inst-access-savings-iis-06-26.pdf — Metro Important Information Summary, 15 Jun 2026
5. https://depositscout.com/banks/halifax/reward-bonus-saver — Halifax Reward Bonus Saver 3.00% (undated)
6. https://halifax.co.uk/savings/easy-access/reward-bonus-saver.html — Halifax page, returned an error when fetched
7. Vault note *Give each pot of cash a job — three pots, ~£118k, none of it working* (note_c6c1748c)
8. `docs/reports/2026-09-11-money-session-2-scenarios.md` — Metro Savings £11,266 at 2.48%; personal sterling £12,415

