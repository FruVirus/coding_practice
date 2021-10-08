# Repository Library
from clrs.matrices.gaussian_elimination import gaussian_elimination


def test_gaussian_elimination():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert gaussian_elimination(a)[1] == 2
    a = [[1, 2], [2, 4]]
    assert gaussian_elimination(a)[1] == 1
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [101, 102, 99, 77]]
    assert gaussian_elimination(a)[1] == 3
    a = [[1, -2, 0, 4], [3, 1, 1, 0], [-1, -5, -1, 0], [3, 8, 2, -12]]
    assert gaussian_elimination(a)[1] == 2
