# Repository Library
from clrs.arrays.quick_select import quick_select


def test_quick_select():
    a = [2, 1, 3, 4, 5, 6, 0, 7, 9, 8, 10, 11, 12]
    for i in a:
        assert quick_select(a, 0, len(a) - 1, i + 1) == i
