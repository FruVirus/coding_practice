# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.lcs import lcs


def test_lcs_bu():
    x = "ABCBDAB"
    y = "BDCABA"
    assert lcs(x, y, td=False) == ["B", "C", "B", "A"]


def test_lcs_td():
    x = "ABCBDAB"
    y = "BDCABA"
    assert lcs(x, y, td=True) == ["B", "C", "B", "A"]
