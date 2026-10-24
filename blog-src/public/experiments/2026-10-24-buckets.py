"""A synthetic time-budget counterexample, not a tracker.
Inputs are sequential, non-overlapping episodes in integer minutes.
Category labels describe the whole episode; they are stipulated, not inferred.
"""
from collections import Counter
from itertools import combinations
import json


def summarise(episodes):
    categories = Counter()
    pairs = Counter()
    elapsed = 0
    for minutes, labels in episodes:
        elapsed += minutes
        labels = sorted(set(labels))
        categories.update({label: minutes for label in labels})
        pairs.update({' + '.join(pair): minutes for pair in combinations(labels, 2)})
    return {
        'elapsed_minutes': elapsed,
        'category_minutes': dict(sorted(categories.items())),
        'pair_minutes': dict(sorted(pairs.items())),
    }


if __name__ == '__main__':
    print(json.dumps({
        'synthetic': True,
        'A_cook_together_then_solo_film': summarise([
            (60, ('cooking', 'social')), (60, ('leisure',))]),
        'B_solo_cooking_then_film_together': summarise([
            (60, ('cooking',)), (60, ('leisure', 'social'))]),
    }, indent=2))
