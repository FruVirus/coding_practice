# Standard Library
import math

# Repository Library
from clrs.matrices.lup_solver import lup_solver


def test_lu_solver():
    x_answer = [-1.4, 2.2, 0.6]
    a = [[1, 2, 0], [3, 4, 4], [5, 6, 3]]
    b = [3, 7, 8]
    x = lup_solver(a, b, lup=False)
    for i, el in enumerate(x):
        assert math.isclose(el, x_answer[i])


def test_lup_solver():
    x_answer = [-1.4, 2.2, 0.6]
    a = [[1, 2, 0], [3, 4, 4], [5, 6, 3]]
    b = [3, 7, 8]
    x = lup_solver(a, b, lup=True)
    for i, el in enumerate(x):
        assert math.isclose(el, x_answer[i])
