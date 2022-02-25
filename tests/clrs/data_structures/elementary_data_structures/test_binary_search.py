# Repository Library
from clrs.data_structures.elementary_data_structures.binary_search import (
    bs_iterative_one,
    bs_iterative_three,
    bs_iterative_two,
    bs_recursive,
)


def test_binary_search_iterative_one():
    a = [0, 1, 2, 3, 666]
    assert a[bs_iterative_one(a, 666)] == 666
    assert a[bs_iterative_one(a, 3)] == 3
    assert a[bs_iterative_one(a, 0)] == 0
    assert bs_iterative_one(a, -1) is None


def test_binary_search_iterative_two():
    a = [0, 1, 2, 3, 666]
    assert a[bs_iterative_two(a, 666)] == 666
    assert a[bs_iterative_two(a, 3)] == 3
    assert a[bs_iterative_two(a, 0)] == 0
    assert bs_iterative_two(a, -1) is None


def test_binary_search_iterative_three():
    a = [0, 1, 2, 3, 666]
    assert a[bs_iterative_three(a, 666)] == 666
    assert a[bs_iterative_three(a, 3)] == 3
    assert a[bs_iterative_three(a, 0)] == 0
    assert bs_iterative_three(a, -1) is None


def test_binary_search_recursive():
    a = [0, 1, 2, 3, 666]
    assert a[bs_recursive(a, 0, len(a) - 1, 666)] == 666
    assert a[bs_recursive(a, 0, len(a) - 1, 3)] == 3
    assert a[bs_recursive(a, 0, len(a) - 1, 0)] == 0
    assert bs_recursive(a, 0, len(a) - 1, -1) is None
