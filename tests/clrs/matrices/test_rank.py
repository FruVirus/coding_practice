# Repository Library
from clrs.matrices.rank import rank


def test_rank():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rank(a) == 2
    a = [[1, 2], [2, 4]]
    assert rank(a) == 1
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [101, 102, 99, 77]]
    assert rank(a) == 3
    a = [[1, -2, 0, 4], [3, 1, 1, 0], [-1, -5, -1, 0], [3, 8, 2, -12]]
    assert rank(a) == 2
