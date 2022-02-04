# Repository Library
from clrs.selected_topics.number_theoretic_algorithms.modular_arithmetic.gcd import (
    gcd,
    gcd_binary,
    gcd_multi,
)


def test_gcd():
    assert gcd(-30, -21) == (-3, -2, 3)
    assert gcd(30, 21) == (3, -2, 3)
    assert gcd(21, 30) == (3, 3, -2)
    assert gcd(99, 78) == (3, -11, 14)
    assert gcd(30, 24) == (6, 1, -1)
    assert gcd(24, 12) == (12, 0, 1)
    assert gcd(25, 15) == (5, -1, 2)


def test_gcd_binary():
    assert gcd_binary(30, 21) == 3
    assert gcd_binary(21, 30) == 3
    assert gcd_binary(99, 78) == 3
    assert gcd_binary(30, 24) == 6
    assert gcd_binary(24, 12) == 12
    assert gcd_binary(25, 15) == 5


def test_gcd_multi():
    assert gcd_multi(30, 20, 12) == (2, [1, 7, -14])
    assert gcd_multi(20, 12, 30) == (2, [1, 6, -3])
    assert gcd_multi(30, 24, 12) == (6, [1, 0, -2])
    assert gcd_multi(12, 24, 30) == (6, [0, -1, 1])
    assert gcd_multi(30, 21) == (3, [-2, 3])
    assert gcd_multi(99, 78) == (3, [-11, 14])
    assert gcd_multi(30, 24) == (6, [1, -1])
    assert gcd_multi(24, 12) == (12, [0, 1])
    assert gcd_multi(24, 12, 30, 20, 78) == (2, [0, 0, 0, 4, -1])
