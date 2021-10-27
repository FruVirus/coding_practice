"""
Overview
========

Newton's method is a root-finding algorithm which produces successively better
approximations to the roots (or zeros) of a real-value function. The most basic version
starts with a single-variable function f defined for a real variable x, the function's
derivative f', and an initial guess x0 for a root of f. If the function satisfies
sufficient assumptions and the initial guess is close, then:

    x1 = x0 - f(x0) / f'(x0)

is a better approximation of the root than x0.

In general, the equation of the tangent line to the curve y = f(x) at x = x_n is:

    y = f'(x_n)*(x - x_n) + f(x_n)

The x-intercept of this line (the value of x which makes y = 0) is taken as the
approximation, x_(n + 1), to the root. Setting y = 0 and solving for x = x_(n + 1)
gives:

    x_(n + 1) = x_n - f(x_n) / f'(x_n)

We start the process with some arbitrary initial value, x0. The method will usually
converge, provided this initial guess is close enough to the unknown root and that
f'(x0) != 0.

Division
--------

Newton's method also required high precision division when computing a / x_n. In
general, we want a high precision representation of a / b and we will first compute a
high precision representation of 1 / b and then multiply by a. A high precision
representation of 1 / b means floor(R / b) where R is a large value s.t. it is easy to
divide by R (e.g., R = 2^k for binary representations). For example, we would want
R / b = 2^16 / 5 = 65536 / 5 = 13107.2 If R is too small, then we do not have a high
precision representation of 1 / b.

The equation we want to solve for is:

    x = R / b --> i.e., solve 1 / x = b / R

Newton's method for division starts with some (high value) guess x1 > 0 and computes the
sequence of improved guesses:

    x_(n + 1) = 2 * x_n - b * x_n^2 / R

The value for x_(n + 1) involves easy multiplication, 2 * x_n, b * x_n^2 and x_n * x_n,
and an easy division by R (if R is a power of 2, then we can use the right shift
operator).

The number of accurate digits for division also approximately doubles on each  iteration
--> quadratic convergence. In other words, the error roughly squares on each iteration.

One might think that the complexity of division is lg(d) times the complexity of
multiplication given that we will have lg(d) multiplications in the lg(d) iterations
required to reach precision d. However, division requires multiplications of
different-sized numbers at each iteration. Initially, the numbers are small and then
they grow to d digits. Thus, the complexity of division equals the complexity of
multiplication.

Square Root
-----------

The square root of a number, N, can be calculated to a tolerance level, tol (or a
specified number of digits of precisions, d) using Newton's method:

    x = sqrt(a) for a > 0 --> i.e., solve x^2 = a

The algorithm starts with some guess x1 > 0 and computes the sequences of improved
guesses:

    x_(n + 1) = (x_n + a / x_n) / 2

Newton's method finds an approximate root of f(x) = x^2 - a = 0 from a guess x_n by
approximating f(x) as its tangent line f(x_n) + f'(x_n) * (x - x_n), leading to an
improved guess x_(n + 1) from the root of the tangent. The intuition is very simple: if
x_n is too big (> sqrt(a)), then a/x_n will be too small (< sqrt(a)), and so their
arithmetic mean x_(n + 1) will be closer to sqrt(a).

The number of accurate digits approximately double on each iteration --> quadratic
convergence. In other words, the error roughly squares (and halves) on each iteration.

We apply a first level of Newton's method to solve f(x) = x^2 - a. Each iteration of
this first level requires a division. If we set the precision to d digits, then
convergence at the first level will require lg(d) iterations. This means the complexity
of computing a square root will be Theta(d^alpha * lg(d)) if the complexity of
multiplication is Theta(d^alpha), given that we have shown that the complexity of
division is the same as the complexity of multiplication. However, the number of digits
of precision we need at the beginning of the first level of Newton's method starts out
small and then grows. Thus, the complexity of square roots is also Theta(d^alpha).

Complexity
==========

Multiplication: Theta(n^alpha), alpha >= 1 depending on the method used time complexity
Division: Theta(n^alpha) time complexity
Square Root: Theta(n^alpha) time complexity
"""


def division(b, R, d=10):
    root, x = None, int(2 ** R / b)
    for _ in range(d):
        root = 2 * x - b * x ** 2 / 2 ** R
        x = root
    return root


def square_root(n, R=16, tol=None, d=None):
    i, x, root = 0, 1, 0.5 * (1 + n)
    while abs(root - x) >= tol if tol is not None else i != d - 2:
        i, x = i + 1, root
        root = 0.5 * (x + n * division(x, R) / 2 ** R)
    return root
