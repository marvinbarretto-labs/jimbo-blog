"""A counterexample, not a model fitted to LocalShout users.

Run: python3 worlds.py
Three invented binary gates: likes kind, free tonight, price acceptable.
Keep iff all three gates hold. A pass alone cannot identify which failed.
No dependencies, user data or production integration.
"""
from itertools import product
import json
import unittest


def worlds() -> list[dict[str, bool]]:
    return [dict(zip(('likes_kind', 'free_tonight', 'price_ok'), row))
            for row in product((False, True), repeat=3)]


def action(world):
    return 'keep' if all(world.values()) else 'pass'


def compatible(observed, **known):
    return [w for w in worlds() if action(w) == observed
            and all(w[key] == value for key, value in known.items())]


class Checks(unittest.TestCase):
    def test_full_space(self):
        self.assertEqual(len(worlds()), 8)
        self.assertEqual(len(compatible('keep')), 1)
        self.assertEqual(len(compatible('pass')), 7)

    def test_pass_does_not_identify_taste(self):
        self.assertEqual({w['likes_kind'] for w in compatible('pass')}, {False, True})
        self.assertEqual(sum(w['likes_kind'] for w in compatible('pass')), 3)

    def test_known_constraints_change_inference(self):
        self.assertEqual(compatible('pass', free_tonight=True, price_ok=True),
                         [dict(likes_kind=False, free_tonight=True, price_ok=True)])

    def test_unavailable_preserves_both_tastes(self):
        self.assertEqual({w['likes_kind'] for w in compatible('pass', free_tonight=False)},
                         {False, True})

    def test_same_trace_opposite_tastes(self):
        likes_but_busy = dict(likes_kind=True, free_tonight=False, price_ok=True)
        dislikes_but_free = dict(likes_kind=False, free_tonight=True, price_ok=True)
        self.assertEqual([action(likes_but_busy)] * 5, [action(dislikes_but_free)] * 5)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    print(json.dumps({'worlds': len(worlds()), 'keep_worlds': len(compatible('keep')),
                      'pass_worlds': len(compatible('pass')),
                      'pass_worlds_that_like_kind': sum(w['likes_kind'] for w in compatible('pass')),
                      'warning': 'Counts are logical possibilities, not probabilities.'}, indent=2))
