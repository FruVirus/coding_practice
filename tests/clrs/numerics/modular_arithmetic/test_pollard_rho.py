# Repository Library
from clrs.numerics.modular_arithmetic.pollard_rho import pollard_rho


def test_pollard_rho():
    assert pollard_rho(221) in [[], [13, 17], [17, 13], [13], [17]]
