# Repository Library
from clrs.sorting_and_order_statistics.medians_and_order_statistics.binary_counter import (  # noqa: E501
    binary_counter,
)


def test_binary_counter():
    a = [0] * 8
    binary_counter(a)
    binary_counter(a)
    binary_counter(a)
    binary_counter(a)
    assert a == [0, 0, 1, 0, 0, 0, 0, 0]
