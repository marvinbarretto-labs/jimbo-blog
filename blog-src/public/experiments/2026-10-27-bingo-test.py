"""Run beside 2026-10-27-bingo.py; stdlib only."""
import importlib.util
from pathlib import Path
import unittest

SOURCE = Path(__file__).with_name('2026-10-27-bingo.py')

class BingoTest(unittest.TestCase):
    def test_winning_lines_ignore_visual_rearrangements(self):
        self.assertTrue(SOURCE.exists(), 'The bingo experiment has not been implemented')
        spec = importlib.util.spec_from_file_location('bingo_experiment', SOURCE)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.winning_lines('ABCD'), {frozenset(x) for x in ('AB', 'CD', 'AC', 'BD')})
        self.assertEqual(module.winning_lines('ABCD'), module.winning_lines('BADC'))
        self.assertNotEqual(module.winning_lines('ABCD'), module.winning_lines('ABDC'))

    def test_exact_census_separates_ties_from_individual_odds(self):
        spec = importlib.util.spec_from_file_location('bingo_experiment', SOURCE)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertTrue(hasattr(module, 'census'), 'Exact draw-order census is missing')
        same = module.census('ABCD', 'BADC')
        different = module.census('ABCD', 'ABDC')
        self.assertEqual(same, {'orders': 24, 'ties': 24, 'left_first': 0, 'right_first': 0,
                               'left_at_two': 16, 'right_at_two': 16})
        self.assertEqual(different, {'orders': 24, 'ties': 8, 'left_first': 8, 'right_first': 8,
                                    'left_at_two': 16, 'right_at_two': 16})

if __name__ == '__main__':
    unittest.main()
