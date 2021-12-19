# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.subset_sum import (  # noqa: E501
    ss,
)


def test_ss_bu():
    w = [1, 5, 3, 7]
    c = 12
    assert ss(w, c, False) == [0, 1, 0, 1]


def test_ss_td():
    w = [3, 34, 4, 12, 5, 2]
    c = 9
    assert ss(w, c, True) == [0, 0, 1, 0, 1, 0]
    w = [3, 34, 4, 12, 5, 2]
    c = 1000
    assert ss(w, c, True) is None
