# Repository Library
from clrs.numerics.lcm import lcm_multi


def test_lcm_multi():
    assert lcm_multi(4, 6) == 12
    assert lcm_multi(4, 6, 8) == 24
    assert lcm_multi(1, 7) == 7
