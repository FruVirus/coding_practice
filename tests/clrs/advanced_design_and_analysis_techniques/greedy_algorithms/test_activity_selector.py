# Repository Library
from clrs.advanced_design_and_analysis_techniques.greedy_algorithms.activity_selector import (  # noqa: E501
    activity_selector,
)


def test_as_bu():
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    assert activity_selector(s, f, False) == [0, 3, 7, 10]


def test_as_td():
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    assert activity_selector(s, f, True) == [0, 3, 7, 10]
