from src.intervals import merge_intervals, total_covered


def test_merges_overlapping_intervals():
    assert merge_intervals([(1, 4), (2, 5), (7, 9)]) == [(1, 5), (7, 9)]


def test_merges_touching_intervals():
    # (1, 3) ends exactly where (3, 5) begins -> they are contiguous and must
    # collapse into a single (1, 5) range.
    assert merge_intervals([(1, 3), (3, 5)]) == [(1, 5)]


def test_total_covered_counts_touching_ranges_once():
    # 1..3 and 3..5 cover 1..5 == 4 units with no double-counting.
    assert total_covered([(1, 3), (3, 5)]) == 4


def test_handles_empty():
    assert merge_intervals([]) == []
