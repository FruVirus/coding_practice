"""
Overview
========

Newton's method is a root-finding algorithm which produces successively better
approximations to the roots (or zeros) of a real-value function. The most basic version
starts with a single-variable function f defined for a real variable x, the derivative
function f', and an initial guess x0 for a root of f. If the function satisfies
sufficient assumptions and the initial guess is close, then:

    x1 = x0 - f(x0) / f'(x0)

is a better approximation of the root than x0.

In general, the equation of the tangent line to the curve y = f(x) at x = x_n is:

    y = f'(x_n) * (x - x_n) + f(x_n)

The x-intercept of this line (the value of x which makes y = 0) is taken as the
approximation, x_(n + 1), to the root. Setting y = 0 and solving for x = x_(n + 1)
gives:

    x_(n + 1) = x_n - f(x_n) / f'(x_n)

We start the process with some arbitrary initial value, x0. The method will usually
converge, provided this initial guess is close enough to the unknown root and that
f'(x0) != 0. The for-loop exits when the value of fxn is close enough to 0. f and dfdx
can be easily specified using lambda notation.

Cubic Root
----------

The cubic root of a number, N, can be calculated to a tolerance level, tol (or a
specified number of digits of precisions, d) using Newton's method:

    x = a^(1 / 3) for a > 0 --> i.e., solve x^3 = a --> x^3 - a = 0

The algorithm starts with some guess x1 > 0 and computes the sequences of improved
guesses:

    x_(n + 1) = x_n - (x^3 - a) / (3 * x^2) = (2 / 3) * x_n + (1 / 3) * (a / x_n^2)

The number of accurate digits approximately double on each iteration --> quadratic
convergence. In other words, the error roughly squares (and halves) on each iteration.

Complexity
==========

Time
----

newton(): For multiplication and division operations, Theta(n^alpha), alpha >= 1
depending on the method used for multiplication.
"""


def newton(f, dfdx, x0, eps=1e-10, max_iters=10000):
    xn = x0
    for _ in range(max_iters):
        fxn = f(xn)
        if abs(fxn) < eps:
            return xn
        dfdxn = dfdx(xn)
        assert dfdxn != 0
        xn -= fxn / dfdxn
    return None
