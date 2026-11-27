# Programme roles: an invented search contract

Question: can a small selector keep composition, orchestration, a talk's subject and an unresolved name apart, while explaining a broader musical match?

All four event descriptions are invented. Credits are hand-assigned, not extracted. Real work titles are used for recognisable examples, not advertised concerts. No canonical IDs, dates, locations, source permissions, live MusicBrainz API or LocalShout code are involved.

Run `python3 search.py Ravel --mode composer` or `python3 search.py Ravel --mode music`. Run `python3 search.py --test` for eight contract tests.

## Verdict: PARTIAL

- What worked: composer mode returns A; broader music mode returns A and B with role reasons. D remains review-only; C is excluded. Eight tests passed, including multiple reasons on one event, case handling, original-composer search and an absent-name control.
- What did not: this does not validate extraction, identity resolution, actual source coverage, reader interpretation or a production search implementation.
- Surprise: an orchestration can be musically relevant without becoming a composer match. A useful result need not be a strict result.
- Next: retain actual programme text with permission, annotate credits independently, and compare explicit composer-only versus broader result cards with a willing reader.

Sources consulted: https://musicbrainz.org/doc/Work and https://musicbrainz.org/doc/Style/Classical/Works on 2026-11-27. This is a proposed local display/search policy, not a claim that MusicBrainz encodes every credit at one level or that LocalShout currently loses them.
