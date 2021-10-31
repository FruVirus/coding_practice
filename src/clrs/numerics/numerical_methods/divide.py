"""
Overview
========

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

Complexity
==========

Multiplication: Theta(n^alpha), alpha >= 1 depending on the method used time complexity
Division: Theta(n^alpha) time complexity
"""


def power_of_two(n):
    if n < 1:
        return 0
    i, curr = 0, 1 << 0
    while curr <= n:
        i += 1
        curr = 1 << i
    return i - 1


def divide(b, R=128):
    root, x = None, int(2 ** R >> power_of_two(b))
    while True:
        root = 2 * x - (b * x ** 2 >> R)
        if root == x:
            return root / 2 ** R
        x = root
