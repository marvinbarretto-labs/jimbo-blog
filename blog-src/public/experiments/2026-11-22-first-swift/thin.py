"""Exact record-thinning sensitivity, NOT an arrival-date estimator.
Run: python3 thin.py data.json
Only the frozen swift records are used. Subsets sample records uniformly,
without replacement, not birds, observers, visits or checklists.
"""
import json
import sys
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path


def minima_histogram(dates, k):
    if not 1 <= k <= len(dates):
        raise ValueError("k must be between 1 and the record count")
    return Counter(min(group) for group in combinations(dates, k))


def audit(data):
    dates = sorted(r["date"] for r in data["records"])
    result = {"record_count": len(dates), "unique_dates": len(set(dates)),
              "earliest": dates[0], "method": "exact uniform record subsets without replacement",
              "warning": "Sensitivity of this archive minimum only; not observer effort or biological arrival.",
              "subsets": []}
    for k in sorted({1, 5, 10, len(dates)}):
        if k > len(dates):
            continue
        hist = minima_histogram(dates, k)
        total = comb(len(dates), k)
        assert sum(hist.values()) == total
        target = (total + 1) // 2
        cumulative = 0
        median = dates[-1]
        for date, count in sorted(hist.items()):
            cumulative += count
            if cumulative >= target:
                median = date
                break
        result["subsets"].append({"kept": k, "subsets": total,
            "earliest_retained_fraction": hist[dates[0]] / total,
            "median_minimum": median,
            "minimum_distribution": dict(sorted(hist.items()))})
    return result


def self_test():
    assert minima_histogram(["01", "02", "03"], 2) == {"01": 2, "02": 1}
    assert minima_histogram(["01", "01", "03"], 2) == {"01": 3}
    assert minima_histogram(["01", "02"], 2) == {"01": 1}
    assert minima_histogram(["01", "02"], 1) == {"01": 1, "02": 1}
    try:
        minima_histogram(["01"], 0)
        raise AssertionError("invalid k accepted")
    except ValueError:
        pass


if __name__ == "__main__":
    self_test()
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("data.json")
    print(json.dumps(audit(json.loads(path.read_text())), indent=2))
