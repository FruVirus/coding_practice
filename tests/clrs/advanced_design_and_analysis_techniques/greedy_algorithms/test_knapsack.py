# Repository Library
from clrs.advanced_design_and_analysis_techniques.greedy_algorithms.knapsack import (
    ks_bottom_up,
)


def test_ks_bottom_up():
    p = [10, 5, 15, 7, 6, 18, 3]
    w = [2, 3, 5, 7, 1, 4, 1]
    c = 15
    sol, total_p = ks_bottom_up(p, w, c)
    assert sol == [(4, 1), (0, 1), (5, 1), (2, 1), (6, 1), (1, 0.6666666666666666)]
    assert total_p == 55.333333333333336
