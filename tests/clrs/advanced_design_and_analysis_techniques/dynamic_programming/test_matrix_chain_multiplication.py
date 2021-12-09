# Repository Library
from clrs.advanced_design_and_analysis_techniques.dynamic_programming.matrix_chain_multiplication import (  # noqa: E501
    matrix_chain_order,
    return_optimal_parens,
)


def test_matrix_chain_order():
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    assert m == [
        [0, 15750, 7875, 9375, 11875, 15125],
        [0, 0, 2625, 4375, 7125, 10500],
        [0, 0, 0, 750, 2500, 5375],
        [0, 0, 0, 0, 1000, 3500],
        [0, 0, 0, 0, 0, 5000],
        [0, 0, 0, 0, 0, 0],
    ]
    assert s == [
        [0, 1, 1, 3, 3, 3],
        [0, 0, 2, 3, 3, 3],
        [0, 0, 0, 3, 3, 3],
        [0, 0, 0, 0, 4, 5],
        [0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0],
    ]
    p = [3, 2, 4, 2, 5]
    m, s = matrix_chain_order(p)
    assert m == [[0, 24, 28, 58], [0, 0, 16, 36], [0, 0, 0, 40], [0, 0, 0, 0]]
    assert s == [[0, 1, 1, 3], [0, 0, 2, 3], [0, 0, 0, 3], [0, 0, 0, 0]]


def test_return_optimal_parens():
    p = [30, 35, 15, 5, 10, 20, 25]
    m, s = matrix_chain_order(p)
    assert return_optimal_parens(s, 0, 5) == "((A_0(A_1A_2))((A_3A_4)A_5))"
    p = [3, 2, 4, 2, 5]
    m, s = matrix_chain_order(p)
    assert return_optimal_parens(s, 0, 3) == "((A_0(A_1A_2))A_3)"
