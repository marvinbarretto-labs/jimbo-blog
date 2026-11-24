# Curiosity cells — archive descriptor counterexample

Question: given the same scored candidates, can sector niches retain only one mechanism while mechanism niches retain alternatives?

Run `python3 archive.py` for the complete authored fixture and results. Run `PYTHONDONTWRITEBYTECODE=1 python3 archive.py --test` for seven tests, including both archive selections over all 40,320 permutations.

Everything is synthetic. Scores are chosen, not evaluated. Origin=published and distance=far are constant. Each archive retains the strictly highest-scoring candidate per descriptor value. There are no ties in this fixture. This is NOT a MAP-Elites search: no mutation, crossover, generation, adaptive loop, live data, quality judge or production integration.

## Verdict: VALIDATED (counterexample only)

Sector winners A,C,D,E all screen. Mechanism winners A,F,H cover screen, coordinate and maintain. With a separate illustrative quality floor of 75, only A survives the mechanism archive. Empty input and lower-scored replacement checks pass.

This does not establish better ideas, preference, a superior taxonomy, or a defect in actual concept batches. Next: with authorisation, independently annotate one real batch by mechanism while preserving its sector labels and original text; compare surviving alternatives before changing the selector.

Grounding: JIM-8227 names the proposed grid. Mouret and Clune (2015), https://arxiv.org/abs/1504.04909, defines the distinct descriptor and performance roles. The script isolates only archive retention.
