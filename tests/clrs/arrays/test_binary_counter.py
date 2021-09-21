# Repository Library
from clrs.arrays.binary_counter import binary_counter


def test_binary_counter():
    a = [0] * 8
    binary_counter(a)
    binary_counter(a)
    binary_counter(a)
    binary_counter(a)
    assert a == [0, 0, 1, 0, 0, 0, 0, 0]
