#!/usr/bin/env python3
"""Compare saved Munro section assignments with a named source CSV.
Usage: python3 2026-10-25-munro-audit.py SOURCE.csv COLLECTION.json
Read-only: prints JSON; never changes the collection. No dependencies.
"""
import csv
import json
import sys
from collections import Counter, defaultdict


def audit(source_rows, items):
    source = [row for row in source_rows if row['2021'] == 'MUN']
    candidates = defaultdict(list)
    for row in source:
        candidates[(row['Name'].strip(), round(float(row['Height (m)'])))].append(row)
    mismatches, unresolved = [], []
    seen_source_ids = []
    for item in items:
        # A diagnostic witness, NOT a production identity scheme.
        matches = candidates[(item['name'], float(item['height_m']))]
        if len(matches) != 1:
            unresolved.append({'id': item['id'], 'candidate_count': len(matches)})
            continue
        row = matches[0]
        seen_source_ids.append(row['DoBIH Number'])
        if int(item['smc']) != int(row['SMC Section']):
            mismatches.append({
                'id': item['id'], 'name': item['name'],
                'height_m': item['height_m'], 'county_in_collection': item['section'],
                'dobih_number': row['DoBIH Number'],
                'source_grid_ref': row['Grid Ref'],
                'collection_smc': item['smc'],
                'source_smc': int(row['SMC Section']),
            })
    names = Counter(row['Name'] for row in source)
    return {
        'source_munros': len(source), 'collection_items': len(items),
        'unique_collection_ids': len({item['id'] for item in items}),
        'unique_matched_source_ids': len(set(seen_source_ids)),
        'reused_source_ids': sorted(k for k, n in Counter(seen_source_ids).items() if n > 1),
        'missing_source_ids': sorted({r['DoBIH Number'] for r in source} - set(seen_source_ids)),
        'repeated_source_names': {k: n for k, n in sorted(names.items()) if n > 1},
        'unresolved': unresolved, 'mismatch_count': len(mismatches),
        'mismatches': mismatches,
    }


def main():
    with open(sys.argv[1], encoding='utf-8-sig', newline='') as handle:
        rows = list(csv.DictReader(handle))
    with open(sys.argv[2], encoding='utf-8') as handle:
        items = json.load(handle)
    print(json.dumps(audit(rows, items), indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
