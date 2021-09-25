# Repository Library
from clrs.arrays.random_select import random_select


def test_random_select():
    a = [2, 1, 3, 4, 5, 6, 44, 46, 29, 0, 11, 12]
    b = sorted(a)
    for i, item in enumerate(b):
        assert random_select(a, 0, len(a) - 1, i + 1) == item
    assert random_select(a, 0, 1, 1) == 0
