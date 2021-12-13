# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.knapsack import (
    ks_solution,
    return_ks,
)


def test_knapsack_bottom_up():
    c = 5
    p = [4, 5, 3, 7]
    w = [2, 3, 1, 4]
    v = ks_solution(p, w, c, False)
    assert v == [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 4, 4, 4, 4],
        [0, 0, 4, 5, 5, 9],
        [0, 3, 4, 7, 8, 9],
        [0, 3, 4, 7, 8, 10],
    ]
    assert return_ks(p, v) == [0, 0, 1, 1]


def test_knapsack_top_down():
    c = 8
    p = [1, 2, 5, 6]
    w = [2, 3, 4, 5]
    v = ks_solution(p, w, c, True)
    assert v == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 2, 2, 0, 0, 0, 3],
        [0, 0, 0, 2, 0, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 8],
    ]
    assert return_ks(p, v) == [0, 1, 0, 1]
