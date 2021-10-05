# Standard Library
import math

# Repository Library
from clrs.matrices.lup_solver import lu_decomp, lup_decomp, lup_solver


def test_lu_solver():
    a_answer = [[1, 2, 0], [3.0, -2.0, 4.0], [5.0, 2.0, -5.0]]
    x_answer = [-1.4, 2.2, 0.6]
    a = [[1, 2, 0], [3, 4, 4], [5, 6, 3]]
    b = [3, 7, 8]
    lu_decomp(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            assert math.isclose(a[i][j], a_answer[i][j])
    x = lup_solver(a, b)
    for i, el in enumerate(x):
        assert math.isclose(el, x_answer[i])


def test_lup_solver():
    a_answer = [[5, 6, 3], [0.2, 0.8, -0.6], [0.6, 0.5, 2.5]]
    x_answer = [-1.4, 2.2, 0.6]
    a = [[1, 2, 0], [3, 4, 4], [5, 6, 3]]
    b = [3, 7, 8]
    p = lup_decomp(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            assert math.isclose(a[i][j], a_answer[i][j])
    assert p == [2, 0, 1]
    x = lup_solver(a, b, p)
    for i, el in enumerate(x):
        assert math.isclose(el, x_answer[i])
