# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.lcs import (
    lcs_solution,
    return_lcs,
)


def test_lcs_bottom_up():
    x = ["A", "B", "C", "B", "D", "A", "B"]
    y = ["B", "D", "C", "A", "B", "A"]
    c = lcs_solution(x, y, 7, 6, top_down=False)
    assert c == [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 2, 2],
        [0, 1, 1, 2, 2, 2, 2],
        [0, 1, 1, 2, 2, 3, 3],
        [0, 1, 2, 2, 2, 3, 3],
        [0, 1, 2, 2, 3, 3, 4],
        [0, 1, 2, 2, 3, 4, 4],
    ]
    assert return_lcs(c, x, y, 7, 6) == ["B", "C", "B", "A"]


def test_lcs_top_down():
    x = ["A", "B", "C", "B", "D", "A", "B"]
    y = ["B", "D", "C", "A", "B", "A"]
    c = lcs_solution(x, y, 7, 6, top_down=True)
    assert c == [
        [float("inf"), 0, 0, 0, float("inf"), float("inf"), float("inf")],
        [0, 0, 0, 0, 1, float("inf"), float("inf")],
        [float("inf"), 1, 1, 1, 1, float("inf"), float("inf")],
        [0, 1, 1, 2, 2, float("inf"), float("inf")],
        [float("inf"), 1, 1, 2, 2, 3, float("inf")],
        [float("inf"), float("inf"), 2, 2, 2, 3, float("inf")],
        [float("inf"), float("inf"), float("inf"), float("inf"), 3, float("inf"), 4],
        [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 4, 4],
    ]
    assert return_lcs(c, x, y, 7, 6) == ["B", "C", "B", "A"]
