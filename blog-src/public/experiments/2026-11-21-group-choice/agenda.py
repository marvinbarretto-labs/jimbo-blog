"""Synthetic group-choice experiment. No personal preference data.
Run: PYTHONDONTWRITEBYTECODE=1 python3 agenda.py
Three voters, three options, strict rankings, simple majority, sequential agenda.
All options are assumed acceptable to everyone. Acceptability is not ranking.
"""
from collections import Counter
from itertools import permutations, product
import json

OPTIONS = ("beach", "boat", "market")
ORDERS = tuple(permutations(OPTIONS))


def duel(profile, a, b):
    votes = sum(rank.index(a) < rank.index(b) for rank in profile)
    return a if votes >= 2 else b


def choose(profile, agenda):
    return duel(profile, duel(profile, agenda[0], agenda[1]), agenda[2])


def condorcet(profile):
    return next((a for a in OPTIONS if all(a == b or duel(profile, a, b) == a
                                         for b in OPTIONS)), None)


def run():
    profile = (("beach", "boat", "market"),
               ("boat", "market", "beach"),
               ("market", "beach", "boat"))
    assert duel(profile, "beach", "boat") == "beach"
    assert duel(profile, "boat", "market") == "boat"
    assert duel(profile, "market", "beach") == "market"
    assert condorcet(profile) is None
    outcomes = [{"agenda": agenda, "winner": choose(profile, agenda)} for agenda in ORDERS]
    counts = Counter(row["winner"] for row in outcomes)
    assert counts == Counter({a: 2 for a in OPTIONS})
    cycles = 0
    dependent = 0
    total = 0
    for p in product(ORDERS, repeat=3):
        total += 1
        winners = {choose(p, agenda) for agenda in ORDERS}
        best = condorcet(p)
        cycles += best is None
        dependent += len(winners) > 1
        assert (best is None) == (len(winners) > 1)
        if best is not None:
            assert winners == {best}
    for order in ORDERS:
        assert {choose((order, order, order), a) for a in ORDERS} == {order[0]}
    assert total == 216
    assert cycles == dependent == 12
    return {"assumptions": "Three labelled voters; three unanimously acceptable options; strict complete rankings; majority knockout; no abstention or indifference. Enumeration is not a population model.",
            "invented_rankings": profile,
            "agenda_outcomes": outcomes,
            "winner_counts": dict(counts),
            "exhaustive_check": {"profiles": total, "majority_cycles": cycles,
                                 "agenda_dependent_profiles": dependent},
            "checks": "Pairwise cycle, six agendas, exhaustive equivalence, Condorcet preservation and unanimous controls passed."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
