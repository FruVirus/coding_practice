# Repository Library
from clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.mod_exp import (  # noqa: E501
    mod_exp,
)


def test_mod_exp():
    assert mod_exp(7, 560, 561) == 1
    assert mod_exp(5, 3, 6) == 5
    assert mod_exp(5, 3, 13) == 8
    assert mod_exp(11, 3, 13) == 5
