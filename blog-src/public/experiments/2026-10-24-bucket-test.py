"""Synthetic counterexample; no personal schedules or observations.
Run beside 2026-10-24-buckets.py with Python 3.
"""
import importlib.util
from pathlib import Path
import unittest

class BucketTest(unittest.TestCase):
    def test_same_totals_can_hide_different_company(self):
        path = Path(__file__).with_name('2026-10-24-buckets.py')
        self.assertTrue(path.exists(), 'the bucket experiment is not implemented')
        spec = importlib.util.spec_from_file_location('buckets', path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        a = module.summarise([(60, ('cooking', 'social')), (60, ('leisure',))])
        b = module.summarise([(60, ('cooking',)), (60, ('leisure', 'social'))])
        self.assertEqual(a['elapsed_minutes'], 120)
        self.assertEqual(a['elapsed_minutes'], b['elapsed_minutes'])
        self.assertEqual(a['category_minutes'], b['category_minutes'])
        self.assertEqual(sum(a['category_minutes'].values()), 180)
        self.assertEqual(a['pair_minutes'], {'cooking + social': 60})
        self.assertEqual(b['pair_minutes'], {'leisure + social': 60})
        self.assertNotEqual(a['pair_minutes'], b['pair_minutes'])

if __name__ == '__main__':
    unittest.main()
