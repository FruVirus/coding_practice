# Repository Library
from clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.pollard_rho import (  # noqa: E501
    pollard_rho,
)


def test_pollard_rho():
    assert pollard_rho(221) in [[], [13, 17], [17, 13], [13], [17]]
