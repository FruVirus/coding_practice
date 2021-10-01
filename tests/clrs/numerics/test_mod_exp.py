# Repository Library
from clrs.numerics.mod_exp import mod_exp


def test_mod_exp():
    assert mod_exp(7, 560, 561) == 1
    assert mod_exp(5, 3, 6) == 5
    assert mod_exp(5, 3, 13) == 8
    assert mod_exp(11, 3, 13) == 5
