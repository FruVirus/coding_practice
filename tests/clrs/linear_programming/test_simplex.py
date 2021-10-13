# Repository Library
from clrs.linear_programming.simplex import pivot


def test_pivot():
    N = [0, 1, 2]
    B = [3, 4, 5]
    A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
    b = [30, 24, 36]
    c = [3, 1, 2]
    e = N.index(0)
    l = B.index(5)
    Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l)
    assert Nhat == [1, 2, 5]
    assert Bhat == [0, 3, 4]
    assert Ahat == [[0.25, 0.5, 0.25], [0.5, 2.75, -0.25], [1.0, 4.5, -0.5]]
    assert bhat == [9.0, 21.0, 6.0]
    assert chat == [0.25, 0.5, -0.75]
    assert vhat == 27.0
