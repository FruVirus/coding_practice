# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.matrix_chain_multiplication import (  # noqa: E501
    mc,
)


def test_matrix_chain_multiplication_bu():
    p = [30, 35, 15, 5, 10, 20, 25]
    assert mc(p, i=0, j=5, td=False) == "((A_0(A_1A_2))((A_3A_4)A_5))"
    p = [3, 2, 4, 2, 5]
    assert mc(p, i=0, j=3, td=False) == "((A_0(A_1A_2))A_3)"


def test_matrix_chain_multiplication_td():
    p = [30, 35, 15, 5, 10, 20, 25]
    assert mc(p, i=0, j=5, td=True) == "((A_0(A_1A_2))((A_3A_4)A_5))"
    p = [3, 2, 4, 2, 5]
    assert mc(p, i=0, j=3, td=True) == "((A_0(A_1A_2))A_3)"
