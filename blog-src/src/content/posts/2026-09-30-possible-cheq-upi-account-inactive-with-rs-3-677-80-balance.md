---
title: "Possible CHEQ UPI account inactive with Rs. 3,677.80 balance — verify safely"
date: 2026-09-30
description: "Possible CHEQ UPI account inactive with Rs. 3,677.80 balance — verify safely"
tags: [phishing, report]
public: false
---

*Report — a research report (2026-09-30), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**Verdict: probably legitimate sender, not a scam by sender identity — inconclusive on this specific email. Confidence: medium. Recommended action: escalate to Marvin, do not archive as spam.** `terrafin.tech` is not a generic third-party domain: it is the real operating domain of Terrafin Solutions Pvt Ltd, which runs CHEQ UPI, and `contactus@terrafin.tech` is CHEQ's published support address [1][2][3]. The grooming premise ("generic third-party domain, matches the Binance scam") is contradicted by public sources. The deciding question only Marvin can answer: did he ever load a CHEQ wallet (e.g. on a trip to India)?

## From prior context
- Vault note *Possible CHEQ UPI account inactive with Rs. 3,677.80 balance — verify safely* (note_74ce839c): groomed as likely phishing because UPI is Indian-only, no Indian banking footprint in the vault, and the sender looked generic. Its own extraction flagged "generic customer wording".
- *binance-scam--note_3fc5504* / *note_d77d3e4c* (cited in the note's intake rationale): the scam-pattern comparison. Treated as settled for Binance, but it does not transfer here because the domain check fails.

The "no Indian banking footprint" point is weaker than assumed: CHEQ is built for **foreigners and NRIs visiting India** [1][4], so a UK-based holder with no Indian bank account is exactly its customer profile. Absence of Indian banking in the vault is not evidence against.

## New findings
- **Sender identity matches.** Terrafin Solutions Private Limited is the publisher of the Cheq:UPI app; the Play Store/App Store listings and the company's support pages list `contactus@terrafin.tech` as support and `admin@terrafin.tech` as admin [1][2][3].
- **Transcorp link is real.** CHEQ UPI is powered by Transcorp International Limited, an RBI-regulated PPI/AD2 licence holder, based in Jaipur [2][5]. A notice naming "CHEQ/Transcorp" is consistent with the actual corporate structure.
- **Unused balance is a real scenario.** CHEQ's FAQ says unused funds can be withdrawn by contacting customer care via the in-app help section, and refunds go to the source account within 10–12 days via `contactus@terrafin.tech` [3]. An "inactive wallet holds a balance" notice fits a real wallet operator's dormant-balance process.
- **No scam reports found.** Searches for "terrafin.tech", "CHEQ UPI inactive account" and related scam/phishing terms returned no phishing report, fraud advisory, or news item about this notice or domain. Only vague user complaints about the service exist, nothing about impersonation [3]. This is absence of evidence, not proof.
- **Gaps:** CHEQ's FAQ has no fraud/impersonation warning and no inactive-account policy page [3]. The two published support phone numbers differ between sources (+91 98455 63750 vs +91 72044 58787) [2][3], so **numbers or links inside the email must not be trusted as verification**.
- I could not inspect the email's headers (SPF/DKIM/DMARC). A spoofed `From:` on a real domain is possible, and real-domain mail can still carry a malicious link. Sender identity is therefore plausible, not authenticated.

## Comparison
| Signal | Phishing-shaped | Legit-shaped | Found |
|---|---|---|---|
| Sender domain | unrelated/lookalike | operator's own domain | **Operator's own domain** |
| Service exists and does this | no | yes | **Yes** (wallet, refunds, dormant balance) |
| Customer profile fits | Marvin has no Indian banking | foreigners/NRIs are the target | **Fits** |
| Public scam reports | present | absent | **None found** |
| Urgency / verify-to-access | typical | — | Claimed in note; unverified, email not opened by this run |
| Generic wording | typical | typical of bulk notices | Ambiguous |

## Recommendation
1. **Escalate to Marvin; do not archive as spam.** Ask one question: "Did you ever install CHEQ UPI / load money into it?" If **no** → archive (an unsolicited mail from a real operator you never used is at worst misdirected or spoofed). If **yes** → the balance (Rs. 3,677.80) is plausibly real.
2. **If yes, never use anything from the email.** Open the CHEQ app or type chequpi.com yourself and use the in-app help to request a withdrawal; the FAQ says refunds return to the source account [3]. Optionally check SPF/DKIM in the original message's "Show original" headers before trusting it.
3. Keep the no-touch rules: no links, no reply, no personal or financial details.
4. Fix the grooming premise: the "domain mismatch" and "Binance pattern" rationale in the note should be corrected so it is not reused.

**Handling confirmation:** this research was open-source only. No reply was sent to the sender, no link from the notice was opened, and no verification was attempted. The email itself was not opened by this run; only the vault note text was read.

## Sources
1. https://play.google.com/store/apps/details?id=com.acecredit.android&hl=en_IN — Cheq:UPI for Foreigners & NRIs listing (publisher Terrafin Solutions)
2. https://appadvice.com/app/cheq-upi-for-foreigners-nris/1667625083 — App listing naming Terrafin Solutions Private Limited
3. https://www.chequpi.com/faqs/ — CHEQ FAQ: refund email contactus@terrafin.tech, unused-fund withdrawal via in-app help
4. https://yourstory.com/companies/cheq-upi — Company profile (foreigners/NRIs product)
5. https://www.chequpi.com/jaipur/ — CHEQ page; Transcorp International Ltd partnership (via search summary)

