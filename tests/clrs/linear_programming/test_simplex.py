# Repository Library
from clrs.linear_programming.simplex import initialize_simplex, pivot, simplex


def test_initialize_simplex():
    A = [[2, -1], [1, -5]]
    b = [2, -4]
    c = [2, -1]
    N, B, A, b, c, v = initialize_simplex(A, b, c)
    assert N == [1, 4]
    assert B == [2, 3]
    assert A == [[-0.2, -0.2], [1.8, -0.19999999999999996]]
    assert b == [0.8, 2.8]
    assert c == [1.8, -0.2]
    assert v == -0.8


def test_pivot():
    N = [1, 2, 3]
    B = [4, 5, 6]
    A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
    b = [30, 24, 36]
    c = [3, 1, 2]
    e = 1
    l = 6
    v = 0
    Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l, v)
    assert Nhat == [2, 3, 6]
    assert Bhat == [1, 4, 5]
    assert Ahat == [[0.25, 0.5, 0.25], [0.75, 2.5, -0.25], [1.5, 4.0, -0.5]]
    assert bhat == [9.0, 21.0, 6.0]
    assert chat == [0.25, 0.5, -0.75]
    assert vhat == 27.0
    N = [2, 3, 6]
    B = [1, 4, 5]
    A = [[0.25, 0.5, 0.25], [0.75, 2.5, -0.25], [1.5, 4.0, -0.5]]
    b = [9.0, 21.0, 6.0]
    c = [0.25, 0.5, -0.75]
    e = 3
    l = 5
    v = 27.0
    Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l, v)
    assert Nhat == [2, 5, 6]
    assert Bhat == [1, 3, 4]
    assert Ahat == [
        [1 / 16, -1 / 8, 5 / 16],
        [3 / 8, 1 / 4, -1 / 8],
        [-3 / 16, -5 / 8, 1 / 16],
    ]
    assert bhat == [33 / 4, 3 / 2, 69 / 4]
    assert chat == [1 / 16, -1 / 8, -11 / 16]
    assert vhat == 111 / 4
    N = [2, 5, 6]
    B = [1, 3, 4]
    A = [[1 / 16, -1 / 8, 5 / 16], [3 / 8, 1 / 4, -1 / 8], [-3 / 16, -5 / 8, 1 / 16]]
    b = [33 / 4, 3 / 2, 69 / 4]
    c = [1 / 16, -1 / 8, -11 / 16]
    e = 2
    l = 3
    v = 111 / 4
    Nhat, Bhat, Ahat, bhat, chat, vhat = pivot(N, B, A, b, c, e, l, v)
    assert Nhat == [3, 5, 6]
    assert Bhat == [1, 2, 4]
    assert Ahat == [[-1 / 6, -1 / 6, 1 / 3], [8 / 3, 2 / 3, -1 / 3], [0.5, -0.5, 0.0]]
    assert bhat == [8, 4, 18]
    assert chat == [-1 / 6, -1 / 6, -2 / 3]
    assert vhat == 28


def test_simplex():
    A = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
    b = [30, 24, 36]
    c = [3, 1, 2]
    assert simplex(A, b, c)[0] == [8, 4, 0, 18, 0, 0]
    A = [[1, 1, 0], [0, -1, 1]]
    b = [8, 0]
    c = [1, 1, 1]
    assert simplex(A, b, c)[0] == [0, 8, 8, 0, 0]
    A = [[2, -1], [1, -5]]
    b = [2, -4]
    c = [2, -1]
    assert simplex(A, b, c)[0] == [0, 1.5555555555555554, 1.1111111111111112, 0, 0]
    A = [[1, 2], [-2, -6], [0, 1]]
    b = [4, -12, 1]
    c = [1, -2]
    assert simplex(A, b, c) == "Infeasible!"
    A = [[-1, 1], [-1, -1], [-1, 4]]
    b = [-1, -3, 2]
    c = [1, 3]
    assert simplex(A, b, c) == "Unbounded!"
    A = [[1, -1], [-1, -1], [-1, 4]]
    b = [8, -3, 2]
    c = [1, 3]
    assert simplex(A, b, c)[0] == [
        0,
        11.333333333333334,
        3.3333333333333335,
        0,
        11.666666666666668,
        0,
    ]
    A = [[4, -1], [2, 1], [-5, 2]]
    b = [8, 10, 2]
    c = [1, 1]
    assert simplex(A, b, c)[0] == [2.0, 6.0, 6.0, 0, 0]
    A = [[2, -8, 0, -10], [-5, -2, 0, 0], [-3, 5, -10, 2]]
    b = [-50, -100, -25]
    c = [-1, -1, -1, -1]
    assert simplex(A, b, c) == "Unbounded!"
