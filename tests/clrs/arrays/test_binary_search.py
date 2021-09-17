# Repository Library
from clrs.arrays.binary_search import binary_search


def test_binary_search():
    a = [0, 1, 2, 3, 666]
    assert a[binary_search(a, 0, len(a), 666)] == 666
    assert a[binary_search(a, 0, len(a), 3)] == 3
    assert a[binary_search(a, 0, len(a), 0)] == 0
    assert binary_search(a, 0, len(a), -1) is None
