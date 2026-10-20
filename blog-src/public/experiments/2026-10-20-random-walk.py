"""Synthetic graph experiment, not a measurement of Marvin's vault.
Run with Python 3; standard library only. Counts include repeated states.
"""
from collections import Counter
from random import Random

GRAPH = {0: list(range(1, 10)), **{i: [0] for i in range(1, 10)}}
STEPS = 200_000


def walk(corrected=False, suppress_repeats=False):
    rng = Random(20261020)
    current = 0
    counts = Counter()
    for _ in range(STEPS):
        proposal = rng.choice(GRAPH[current])
        if not corrected or rng.random() < min(1, len(GRAPH[current]) / len(GRAPH[proposal])):
            current = proposal
        else:
            if suppress_repeats:
                continue
        counts[current] += 1
    return counts


if __name__ == '__main__':
    assert len(GRAPH) == 10
    assert all(u in GRAPH[v] for u in GRAPH for v in GRAPH[u])
    for label, corrected, suppress in [
        ('simple walk', False, False),
        ('Metropolis-Hastings, including stays', True, False),
        ('Metropolis-Hastings, stays hidden', True, True),
    ]:
        counts = walk(corrected, suppress)
        total = sum(counts.values())
        hub = counts[0] / total
        print(f'{label}: observations={total}, hub={hub:.2%}, leaf range={min(counts[i] / total for i in range(1, 10)):.2%}..{max(counts[i] / total for i in range(1, 10)):.2%}')
        if not corrected or suppress:
            assert abs(hub - 0.5) < 0.001
        else:
            assert abs(hub - 0.1) < 0.005
            assert all(abs(counts[i] / total - 0.1) < 0.01 for i in GRAPH)
    print('All structural and frequency assertions passed.')
