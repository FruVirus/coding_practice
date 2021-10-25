"""
Overview
========

The square root of a number, N, can be calculated to a tolerance level, tol, using
Newton's Method:

    x = sqrt(a) for a > 0 --> i.e., solve x^2 = a

The algorithm starts with some guess x1 > 0 and computes the sequences of improved
guesses:

    x_(n + 1) = (x_n + a / x_n) / 2

Newton's Method finds an approximate root of f(x) = x^2 - a = 0 from a guess x_n by
approximating f(x) as its tangent line f(x_n) + f'(x_n) * (x - x_n), leading to an
improved guess x_(n + 1) from the root of the tangent. The intuition is very simple: if
x_n is too big (> sqrt(a)), then a/x_n will be too small (< sqrt(a)), and so their
arithmetic mean x_(n + 1) will be closer to sqrt(a).

The number of accurate digits approximately double on each iteration --> quadratic
convergence. In other words, the error roughly squares (and halves) on each iteration.
"""


def newtons_method(n, tol=None, d=None):
    root, x = None, n
    if tol is not None:
        root = 0.5 * (x + (n / x))
        while abs(root - x) >= tol:
            x = root
            root = 0.5 * (x + (n / x))
    else:
        for _ in range(d - 1):
            root = 0.5 * (x + (n / x))
            x = root
    return root
