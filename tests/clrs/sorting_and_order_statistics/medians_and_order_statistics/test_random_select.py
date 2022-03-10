# Repository Library
from clrs.sorting_and_order_statistics.medians_and_order_statistics.random_select import (  # noqa: E501
    random_select,
)


def test_random_select():
    a = [2, 1, 3, 4, 5, 6, 44, 46, 29, 0, 11, 12]
    b = sorted(a)
    for i, num in enumerate(a, 1):
        assert random_select(a, i) == b[i - 1]
    assert random_select(a, 100) is None
