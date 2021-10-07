# Repository Library
from clrs.matrices.multiply import matrix_multiply, smmr


def test_matrix_multiply():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]
    c = matrix_multiply(a, b)
    assert c == [[22, 28], [49, 64]]


def test_smmr():
    pass
