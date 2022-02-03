"""
28.3 Symmetric positive-definite matrices and least-squares approximation
=========================================================================

A matrix is positive definite if it’s symmetric and all its eigenvalues are positive. A
positive-definite matrix is a symmetric matrix with all positive eigenvalues. Since it's
a symmetric matrix, all the eigenvalues are real and they can be positive or negative.
One way to tell if a matrix is positive definite is to calculate all the eigenvalues and
just check to see if they're all positive.

A matrix is positive definite if it’s symmetric and all its pivots are positive. One
equivalent definition can be derived using the fact that for a symmetric matrix the
signs of the pivots are the signs of the eigenvalues.

Another way we can test for if a matrix is positive definite is if all of its upper left
k x k determinants are positive.

    d_k = det(A_k) / det(A_(k-1))

Symmetric positive-definite matrices are non-singular and we can perform LU
decomposition on them without having to worry about dividing by 0.

Least-squares approximation
---------------------------

One important application of symmetric positive-definite matrices arises in fitting
curves to given sets of data points.

Suppose that we are given a set of m data points:

(x_1, y_1), (x_2, y_2), ..., (x_m, y_m)

where we know that the y_i's are subject to measurement errors. We would like to
determine a function F(x) such that the approximation errors

eta_i = F(x_i) - y_i

are small for i = 1, 2, ..., m. The form of the function F depends on the sub-problem at
hand. Here, we assume that it has the form of a linearly weighted sum, where the number
of functions and the specific basis functions are chosen based on knowledge of the
problem at hand. A common choice is:

F(x) = c_1 + c_2 * x + c_3 * x^2 + ... + c_n * x^(n - 1)

which means that F(x) is a polynomial of degree n - 1 in x. Thus, given m data points
(x_1, y_1), (x_2, y_2), ..., (x_m, y_m), we wish to calculate n coefficients
c_1, c_2, ..., c_n that minimize the approximation errors eta_1, eta_2, ..., eta_m.

By choosing n = m, we can calculate each y_i exactly. Such a high-degree F "fits the
noise" as well as the data, however, and generally gives poor results when used to
predict y for previously unseen values of x. It is usually better to choose n
significantly smaller than m and hope that by choosing the coefficients c_j well, we can
obtain a function F that finds the significant patterns in the data points without
paying undue attention to the noise.

Once we choose a value of n that is less than m, we end up with an over-determined set
of equations (since we have more data points than equations) whose solution we wish to
approximate.

A = f1(x1)  f2(x1) ...  fn(x1)
    f1(x2)  f2(x2) ...  fn(x2)
    ...
    f1(xm)  f2(xm) ...  fn(xm)

Ac =    f1(x1)  f2(x1) ...  fn(x1)  * c1
        f1(x2)  f2(x2) ...  fn(x2)  * c2
        ...                           ...
        f1(xm)  f2(xm) ...  fn(xm)  * cn

eta = Ac - y is the m-vector of approximation errors.

To minimize approximation errors, we choose to minimize the norm of the error vector
eta, which gives us a least-squares solution. We can then minimize the norm of the error
vector eta by differentiating the norm squared with respect to each c_k and then setting
the result to 0.

The n equations then are equivalent to a single matrix equation:

(Ac - y).T * A = 0, or

A.T(Ac - y) = 0, which implies

A.T * Ac = A.T * y --> this is the normal equation.

The matrix A.T * A is symmetric and if A has full column rank, then A.T * A is positive
definite as well. Hence, (A.T * A)^(-1) exists, and the solution for the coefficients
is:

c = ((A.T * A)^(-1) * A.T) * y

As a practical matter, we solve the normal equation by multiplying y by A.T and then
finding the LU decomposition of A.T * A. Then, we call lup_solver() with a = A.T * A and
b = A.T * y

If A has full rank, the matrix A.T * A is guaranteed to be non-singular, because it is
symmetric and positive definite.

Intuition
---------

Comparing the normal equation to Ax = b, we have A.T * A = A, c = x, and A.T * y = b.
Thus, we can use lup_solver() to perform linear least squares approximation to find the
vector c.

We can only do this since we chose to minimize the norm of the error vector eta when
minimizing the approximation errors---this gives us a least squares solution. Minimizing
the norm of eta by differentiating the norm of eta w.r.t. c and then setting the result
to 0 gives us the normal equation.

We can change the "deg" parameter to be whatever. We can even change how a[i][j] is
assigned for each element (by hard coding it). However, we will always be performing a
least squares approximation since we are using lup_solver() to approximate the
coefficient vector c.

Complexity
==========

Time
----

is_pos_def(): Theta(n^2).
least_squares(): Theta(n^3).
"""

# pylint: disable=C0200

# Repository Library
from src.clrs.selected_topics.matrix_operations.invert import transpose
from src.clrs.selected_topics.matrix_operations.lup_solver import lu_decomp, lup_solver
from src.clrs.selected_topics.matrix_operations.multiply import mm


def is_pos_def(a):
    for r in range(len(a)):
        for c in range(len(a[0])):
            if r == c and a[r][c] <= 0:
                return False
    return True


def least_squares(data, deg=2):
    a = [[0] * (deg + 1) for _ in range(len(data))]
    for i, (x, y) in enumerate(data):
        for j in range(deg + 1):
            a[i][j] = x ** j
    ata = mm(transpose(a), a)
    lu_decomp(ata)
    assert is_pos_def(ata)
    y = mm(transpose(a), transpose([[y for _, y in data]]))
    return lup_solver(ata, [i[0] for i in y], decomp=False, lup=False)
