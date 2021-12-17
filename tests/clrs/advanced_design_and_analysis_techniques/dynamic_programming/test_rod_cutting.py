# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.rod_cutting import (  # noqa: E501
    rc,
)


def test_rod_cut():
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    assert rc(p, 7) == [1, 6]
    assert rc(p, 7, True) == [1, 6]
