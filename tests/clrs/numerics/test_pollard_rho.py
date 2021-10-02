# Repository Library
from clrs.numerics.pollard_rho import pollard_rho


def test_pollard_rho():
    assert pollard_rho(221) in [[], [13, 17], [17, 13], [13], [17]]
