# Repository Library
from clrs.numerics.mod_linear_solver import mod_linear_solver


def test_mod_linear_solver():
    assert mod_linear_solver(14, 30, 100) == [95, 45]
    assert mod_linear_solver(14, 30, 40) == [5, 25]
    assert mod_linear_solver(14, 32, 40) == [8, 28]
    assert mod_linear_solver(1, 32, 40) == [32]
    assert mod_linear_solver(4, 33, 40) is None
