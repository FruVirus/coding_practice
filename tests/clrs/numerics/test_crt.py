# Repository Library
from clrs.numerics.crt import crt


def test_crt():
    assert crt([2, 3, 1], [3, 4, 5]) == 11
    assert crt([4, 3], [6, 5]) == 28
    assert crt([2017, 2014, 2008], [3, 8, 13]) == 214
    assert crt([1, 2, 3, 4], [5, 7, 9, 11]) == 1731
