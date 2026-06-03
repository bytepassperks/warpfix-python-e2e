"""Interval utilities used by the scheduling layer.

`merge_intervals` collapses a list of (start, end) ranges into the smallest set
of non-overlapping ranges. Touching ranges (where one ends exactly where the
next begins, e.g. (1, 3) and (3, 5)) are considered contiguous and must merge
into a single range (1, 5).
"""

from typing import List, Tuple

Interval = Tuple[int, int]


def merge_intervals(intervals: List[Interval]) -> List[Interval]:
    if not intervals:
        return []

    ordered = sorted(intervals, key=lambda pair: pair[0])
    merged: List[List[int]] = [list(ordered[0])]

    for start, end in ordered[1:]:
        last = merged[-1]
        # Overlapping or touching ranges should be merged together.
        if start < last[1]:
            last[1] = max(last[1], end)
        else:
            merged.append([start, end])

    return [(lo, hi) for lo, hi in merged]


def total_covered(intervals: List[Interval]) -> int:
    """Total length covered by the merged intervals."""
    return sum(hi - lo for lo, hi in merge_intervals(intervals))
