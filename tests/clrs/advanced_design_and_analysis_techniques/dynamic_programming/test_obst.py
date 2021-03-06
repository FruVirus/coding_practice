# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.obst import (
    obst,
    obst_bu,
)


def test_obst_bu():
    p = [None, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    e, r, w = obst_bu(p, q)
    assert e == [
        [0.05, 0.45000000000000007, 0.9, 1.25, 1.75, 2.75],
        [0, 0.1, 0.4, 0.7, 1.2, 2.0],
        [0, 0, 0.05, 0.25, 0.6, 1.2999999999999998],
        [0, 0, 0, 0.05, 0.30000000000000004, 0.9],
        [0, 0, 0, 0, 0.05, 0.5],
        [0, 0, 0, 0, 0, 0.1],
    ]
    assert r == [
        [0, 1, 1, 2, 2, 2],
        [0, 0, 2, 2, 2, 4],
        [0, 0, 0, 3, 4, 5],
        [0, 0, 0, 0, 4, 5],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0],
    ]
    assert w == [
        [0.05, 0.30000000000000004, 0.45, 0.55, 0.7000000000000001, 1.0000000000000002],
        [0, 0.1, 0.25, 0.35, 0.49999999999999994, 0.7999999999999999],
        [0, 0, 0.05, 0.15000000000000002, 0.3, 0.6],
        [0, 0, 0, 0.05, 0.2, 0.5],
        [0, 0, 0, 0, 0.05, 0.35],
        [0, 0, 0, 0, 0, 0.1],
    ]
    assert obst(r) == [
        "2 is the root",
        "1 is the left child of 2",
        "5 is the right child of 2",
        "4 is the left child of 5",
        "3 is the left child of 4",
    ]
    p = [None, 3, 3, 1, 1]
    q = [2, 3, 1, 1, 1]
    e, r, w = obst_bu(p, q)
    assert e == [
        [2, 13, 25, 32, 40],
        [0, 3, 11, 17, 25],
        [0, 0, 1, 5, 11],
        [0, 0, 0, 1, 5],
        [0, 0, 0, 0, 1],
    ]
    assert r == [
        [0, 1, 1, 2, 2],
        [0, 0, 2, 2, 2],
        [0, 0, 0, 3, 3],
        [0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0],
    ]
    assert w == [
        [2, 8, 12, 14, 16],
        [0, 3, 7, 9, 11],
        [0, 0, 1, 3, 5],
        [0, 0, 0, 1, 3],
        [0, 0, 0, 0, 1],
    ]
    assert obst(r) == [
        "2 is the root",
        "1 is the left child of 2",
        "3 is the right child of 2",
        "4 is the right child of 3",
    ]
