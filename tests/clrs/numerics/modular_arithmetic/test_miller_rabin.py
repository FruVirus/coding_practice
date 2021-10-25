# Repository Library
from clrs.numerics.modular_arithmetic.miller_rabin import miller_rabin


def test_miller_rabin():
    assert miller_rabin(221) is False
    assert miller_rabin(11) is True
    assert miller_rabin(7) is True
    assert miller_rabin(223) is True
    assert miller_rabin(225) is False
    assert miller_rabin(561) is False
    assert miller_rabin(1105) is False
    assert miller_rabin(1729) is False
