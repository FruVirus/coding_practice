# Repository Library
from clrs.linear_programming.simplex import pivot, simplex


def test_initialize_simplex():
    pass


def test_pivot():
    N = [0, 1, 2]
    B = [3, 4, 5]
    A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
    b = [30, 24, 36]
    c = [3, 1, 2]
    e = 0
    l = 5
    v = 0
    Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l, v)
    assert Nhat == [1, 2, 5]
    assert Bhat == [0, 3, 4]
    assert Ahat == [[0.25, 0.5, 0.25], [0.75, 2.5, -0.25], [1.5, 4.0, -0.5]]
    assert bhat == [9.0, 21.0, 6.0]
    assert chat == [0.25, 0.5, -0.75]
    assert vhat == 27.0
    N = [1, 2, 5]
    B = [0, 3, 4]
    A = [[0.25, 0.5, 0.25], [0.75, 2.5, -0.25], [1.5, 4.0, -0.5]]
    b = [9.0, 21.0, 6.0]
    c = [0.25, 0.5, -0.75]
    e = 2
    l = 4
    v = 27.0
    Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l, v)
    assert Nhat == [1, 4, 5]
    assert Bhat == [0, 2, 3]
    assert Ahat == [
        [1 / 16, -1 / 8, 5 / 16],
        [3 / 8, 1 / 4, -1 / 8],
        [-3 / 16, -5 / 8, 1 / 16],
    ]
    assert bhat == [33 / 4, 3 / 2, 69 / 4]
    assert chat == [1 / 16, -1 / 8, -11 / 16]
    assert vhat == 111 / 4
    N = [1, 4, 5]
    B = [0, 2, 3]
    A = [[1 / 16, -1 / 8, 5 / 16], [3 / 8, 1 / 4, -1 / 8], [-3 / 16, -5 / 8, 1 / 16]]
    b = [33 / 4, 3 / 2, 69 / 4]
    c = [1 / 16, -1 / 8, -11 / 16]
    e = 1
    l = 2
    v = 111 / 4
    Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l, v)
    assert Nhat == [2, 4, 5]
    assert Bhat == [0, 1, 3]
    assert Ahat == [[-1 / 6, -1 / 6, 1 / 3], [8 / 3, 2 / 3, -1 / 3], [0.5, -0.5, 0.0]]
    assert bhat == [8, 4, 18]
    assert chat == [-1 / 6, -1 / 6, -2 / 3]
    assert vhat == 28


def test_simplex():
    A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
    b = [30, 24, 36]
    c = [3, 1, 2]
    assert simplex(A, b, c) == [8, 4, 0, 18, 0, 0]
    # A = [[1, 1, 0], [0, -1, 1]]
    # b = [8, 0]
    # c = [1, 1, 1]
    # assert simplex(A, b, c) == [0, 8, 8, 0, 0]
