# Repository Library
from clrs.advanced_design_and_analysis_techniques.greedy_algorithms.activity_selector import (  # noqa: E501
    as_bottom_up,
    as_top_down,
)


def test_as_bottom_up():
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    assert as_bottom_up(s, f) == [1, 4, 8, 11]


def test_as_top_down():
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    assert as_top_down(s, f, 0, len(s) - 1) == [1, 4, 8, 11]
