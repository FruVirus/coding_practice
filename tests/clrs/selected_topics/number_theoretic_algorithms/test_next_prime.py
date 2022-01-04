# Repository Library
from clrs.selected_topics.number_theoretic_algorithms.next_prime import (
    is_prime,
    next_prime,
)


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(25) is False
    assert is_prime(700) is False
    assert is_prime(701) is True


def test_next_prime():
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(700) == 701
