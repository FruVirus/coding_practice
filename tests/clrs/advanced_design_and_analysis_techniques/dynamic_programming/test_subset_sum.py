# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.subset_sum import (  # noqa: E501
    return_ss,
    ss_solution,
)


def test_ss_bottom_up():
    w = [1, 5, 3, 7]
    c = 12
    v = ss_solution(w, c, False)
    assert v == [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    assert return_ss(w, c, v) == [0, 1, 0, 1]


def test_ss_top_down():
    w = [3, 34, 4, 12, 5, 2]
    c = 9
    v = ss_solution(w, c, True)
    assert v == [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]
    assert return_ss(w, c, v) == [0, 0, 1, 0, 1, 0]
    w = [3, 34, 4, 12, 5, 2]
    c = 1000
    v = ss_solution(w, c, True)
    assert return_ss(w, c, v) is None
