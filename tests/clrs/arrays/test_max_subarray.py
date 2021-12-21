# Repository Library
from clrs.arrays.max_subarray import find_max, find_max_iterative


def test_find_max():
    a = [
        100,
        113,
        110,
        85,
        105,
        102,
        86,
        63,
        81,
        101,
        94,
        106,
        101,
        94,
        106,
        101,
        79,
        94,
        90,
        97,
    ]
    assert find_max(a) == (7, 10, 43)


def test_find_max_iterative():
    a = [
        100,
        113,
        110,
        85,
        105,
        102,
        86,
        63,
        81,
        101,
        94,
        106,
        101,
        94,
        106,
        101,
        79,
        94,
        90,
        97,
    ]
    assert find_max_iterative(a) == (7, 10, 43)
