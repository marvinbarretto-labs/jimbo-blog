"""Synthetic 2x2 bingo, rows/columns only, no diagonals or free square.
Letters are invented phrases. Run with Python 3; no dependencies.
"""

def winning_lines(card):
    return {frozenset(card[:2]), frozenset(card[2:]),
            frozenset(card[::2]), frozenset(card[1::2])}


def census(left, right):
    from itertools import permutations
    counts = dict.fromkeys(('orders', 'ties', 'left_first', 'right_first',
                           'left_at_two', 'right_at_two'), 0)
    for order in permutations('ABCD'):
        times = []
        for card in (left, right):
            lines = winning_lines(card)
            times.append(next(n for n in range(2, 5)
                              if any(line <= set(order[:n]) for line in lines)))
        a, b = times
        counts['orders'] += 1
        counts['ties' if a == b else 'left_first' if a < b else 'right_first'] += 1
        counts['left_at_two'] += (a == 2)
        counts['right_at_two'] += (b == 2)
    return counts


if __name__ == '__main__':
    import json
    print(json.dumps({
        'model': 'Synthetic 2x2; rows and columns only; all 24 orders equally weighted',
        'visually_different_same_lines': census('ABCD', 'BADC'),
        'visually_different_changed_lines': census('ABCD', 'ABDC'),
    }, indent=2))
