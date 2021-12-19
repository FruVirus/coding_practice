# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.k_sum import ksum


def test_ksum_bu():
    w = [1, 2, 3, 7]
    c = 10
    k = 3
    assert ksum(w, c, k, False) == [1, 1, 0, 1]


def test_ksum_td():
    w = [1, 2, 3, 7]
    c = 10
    k = 2
    assert ksum(w, c, k, True) == [0, 0, 1, 1]
    w = [1, 2, 3, 7]
    c = 10
    k = 4
    assert ksum(w, c, k, True) is None
