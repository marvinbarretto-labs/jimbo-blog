#!/usr/bin/env python3
"""Regression tests for the read-only Munro section audit.
Usage: PYTHONDONTWRITEBYTECODE=1 python3 2026-10-25-munro-audit-test.py
"""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'munro_audit', Path(__file__).with_name('2026-10-25-munro-audit.py'))
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def row(identity, height, section, name='Ben More'):
    return {'2021': 'MUN', 'Name': name, 'Height (m)': str(height),
            'DoBIH Number': identity, 'SMC Section': str(section), 'Grid Ref': 'TEST'}


def item(identity, height, section, name='Ben More'):
    return {'id': identity, 'name': name, 'height_m': height,
            'smc': section, 'section': 'test-county'}


class AuditTests(unittest.TestCase):
    def test_unique_export_ids_do_not_prove_correct_sections(self):
        result = module.audit([row('26', 1174, 1), row('1301', 966, 17)],
                              [item('ben-more', 1174, 17), item('ben-more-2', 966, 17)])
        self.assertEqual(result['unique_collection_ids'], 2)
        self.assertEqual(result['unique_matched_source_ids'], 2)
        self.assertEqual(result['mismatch_count'], 1)
        self.assertEqual(result['mismatches'][0]['dobih_number'], '26')

    def test_correct_sections_pass(self):
        result = module.audit([row('26', 1174, 1), row('1301', 966, 17)],
                              [item('ben-more', 1174, 1), item('ben-more-2', 966, 17)])
        self.assertEqual(result['mismatch_count'], 0)
        self.assertEqual(result['unresolved'], [])

    def test_ambiguous_witness_is_not_silently_resolved(self):
        result = module.audit([row('a', 1000, 1), row('b', 1000, 2)],
                              [item('x', 1000, 2)])
        self.assertEqual(result['unresolved'], [{'id': 'x', 'candidate_count': 2}])
        self.assertEqual(result['unique_matched_source_ids'], 0)

    def test_rounded_height_and_source_whitespace_are_explicit(self):
        result = module.audit([row('a', 924.5, 3, 'A hill ')],
                              [item('hill', 924, 3, 'A hill')])
        self.assertEqual(result['unique_matched_source_ids'], 1)
        self.assertEqual(result['unresolved'], [])

    def test_unknown_item_remains_unresolved(self):
        result = module.audit([], [item('x', 1000, 2)])
        self.assertEqual(result['unresolved'], [{'id': 'x', 'candidate_count': 0}])


if __name__ == '__main__':
    unittest.main()
