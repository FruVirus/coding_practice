# Repository Library
from clrs.matrices.multiply import mm, smmr


def test_mm():
    a = [[1, 2, 3], [4, 5, 6]]
    b = [[1, 2], [3, 4], [5, 6]]
    c = mm(a, b)
    assert c == [[22, 28], [49, 64]]


def test_smmr():
    a = [[1, 2], [3, 4]]
    b = [[1, 2], [3, 4]]
    c = smmr(a, b, len(a))
    assert c == [[7, 10], [15, 22]]
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    b = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    c = smmr(a, b, len(a))
    assert c == [
        [90, 100, 110, 120],
        [202, 228, 254, 280],
        [314, 356, 398, 440],
        [426, 484, 542, 600],
    ]
