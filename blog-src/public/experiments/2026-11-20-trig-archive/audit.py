"""Audit an unmodified OS CompleteTrigArchive.zip; no coordinate conversion.
Usage: python3 audit.py /path/to/CompleteTrigArchive.zip
Source: https://www.ordnancesurvey.co.uk/geodesy-positioning/legacy-data/trig-search
Contains Ordnance Survey data © Crown copyright and database right 2026.
Source data available under Open Government Licence v3.0.
"""
import collections
import csv
import hashlib
import io
import json
from pathlib import Path
import sys
import zipfile


def audit(path):
    data = Path(path).read_bytes()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        rows = list(csv.DictReader(io.StringIO(archive.read('CompleteTrigArchive.csv').decode('utf-8-sig'))))
    types = collections.Counter(row['TYPE OF MARK'] for row in rows)
    pillars = [row for row in rows if row['TYPE OF MARK'] == 'PILLAR']
    groups = collections.defaultdict(list)
    for row in rows:
        groups[row['New Name']].append(row)
    examples = []
    for key in ['TL74T011', 'HY52T024', 'SD80S003']:
        examples.append({'new_name': key, 'records': [{field: row[field] for field in ['Trig Name', 'TYPE OF MARK', 'DESTROYED MARK INDICATOR', 'COMMENTS']} for row in groups[key]]})
    result = {
        'source': 'https://www.ordnancesurvey.co.uk/documents/gps/CompleteTrigArchive.zip',
        'zip_sha256': hashlib.sha256(data).hexdigest(),
        'row_count': len(rows),
        'type_of_mark_counts': dict(sorted(types.items())),
        'pillar_rows': len(pillars),
        'pillar_destroyed_indicator_counts': dict(sorted(collections.Counter(row['DESTROYED MARK INDICATOR'] for row in pillars).items())),
        'examples': examples,
        'limits': ['Archive rows are not unique currently visitable pillars.', 'Raw indicator values are preserved, not interpreted.', 'No access, current condition, or coordinate conversion checked.'],
    }
    assert sum(types.values()) == len(rows)
    assert sum(result['pillar_destroyed_indicator_counts'].values()) == len(pillars)
    return result


if __name__ == '__main__':
    print(json.dumps(audit(sys.argv[1]), indent=2, ensure_ascii=False))
