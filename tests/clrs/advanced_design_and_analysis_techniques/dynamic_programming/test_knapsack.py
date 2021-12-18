# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.knapsack import ks


def test_ks_bu():
    c = 5
    p = [4, 5, 3, 7]
    w = [2, 3, 1, 4]
    assert ks(p, w, c, False) == [0, 0, 1, 1]


def test_ks_td():
    c = 8
    p = [1, 2, 5, 6]
    w = [2, 3, 4, 5]
    assert ks(p, w, c, True) == [0, 1, 0, 1]
