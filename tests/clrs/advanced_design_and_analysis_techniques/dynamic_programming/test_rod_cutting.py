# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.rod_cutting import (  # noqa: E501
    rod_cut,
)


def test_rod_cut_solution():
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    assert rod_cut(p, 7) == [1, 6]
    assert rod_cut(p, 7, True) == [1, 6]
