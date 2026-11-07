"""Synthetic fixtures only. Run with python3 -m unittest -v."""
import unittest
import route_probe

class RouteProbeTests(unittest.TestCase):
    def test_shortest_walk_and_most_complete_sets_are_different_routes(self):
        score = getattr(route_probe, 'score', None)
        self.assertTrue(callable(score), 'route scoring is not implemented')
        self.assertEqual(score(('A', 'B', 'C')), {'walk': 20, 'sets': ['A'], 'finish': 120})
        self.assertEqual(score(('C', 'B', 'A')), {'walk': 40, 'sets': ['C', 'B', 'A'], 'finish': 100})

if __name__ == '__main__':
    unittest.main()
