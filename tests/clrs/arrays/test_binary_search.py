# Repository Library
from clrs.arrays.binary_search import bs_iterative, bs_recursive


def test_binary_search_iterative():
    a = [0, 1, 2, 3, 666]
    assert a[bs_iterative(a, 0, len(a), 666)] == 666
    assert a[bs_iterative(a, 0, len(a), 3)] == 3
    assert a[bs_iterative(a, 0, len(a), 0)] == 0
    assert bs_iterative(a, 0, len(a), -1) is None


def test_binary_search_recursive():
    a = [0, 1, 2, 3, 666]
    assert a[bs_recursive(a, 0, len(a), 666)] == 666
    assert a[bs_recursive(a, 0, len(a), 3)] == 3
    assert a[bs_recursive(a, 0, len(a), 0)] == 0
    assert bs_recursive(a, 0, len(a), -1) is None
