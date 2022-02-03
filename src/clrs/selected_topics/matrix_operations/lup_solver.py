"""
28.1 Solving systems of linear equations
========================================

LUP Solver
----------

We can formulate a linear system as a matrix equation in which each matrix or vector
element belongs to a field, typically the real numbers.

We start with a set of linear equations in n unknowns x_1, x_2, ..., x_n:

a_11 * x_1 + a_12 * x_2 + ... + a_1n * x_n = b_1,
...
a_n1 * x1 + a_n2 * x_ 2 + ... + a_nn * x_n = b_n.

A solution to the equations is a set of values for x_1, x_2, ..., x_n that satisfy all
of the equations simultaneously.

If A is non-singular, it possesses an inverse A^(-1), and x = A^(-1) * b is the unique
solution vector.

If the rank of A is less than n, then the system is under-determined and the system will
typically have infinitely many solutions, although it may have no solutions at all if
the equations are inconsistent. This corresponds to the situation of having more
unknowns than equations.

If the rank of A is greater than n, then the system is overdetermined and there may not
exist any solutions. This corresponds to the situation of having more equations than
unknowns.

If we have exactly n equations in n unknowns, then we could compute A^(-1) and then
solve for x using A^(-1) * b. This approach suffers in practice from numerical
instability. LUP decomposition is numerically stable and has the further advantage of
being faster in practice.

Rank
----

The diagonal elements of the matrix returned by lu_decomp() can be used to determine the
rank of the passed in matrix.

Rank is the number of independent columns/rows of a matrix. If a column/row is a
multiple of another column/row or is a combination or other columns/rows, then that
column/row is not independent and does not contribute to the rank of a matrix.

Rank can be found by performing Gaussian elimination on the input matrix and then
counting the number of non-zero elements on the diagonal. After we perform Gaussian
elimination, the resulting matrix is in row echelon form.

A matrix is full row rank when each of the rows of the matrix are linearly independent
and full column rank when each of the columns of the matrix are linearly independent.
For a square matrix these two concepts are equivalent and we say the matrix is full rank
if all rows and columns are linearly independent. A square matrix is full rank iff its
determinant is nonzero.

For a non-square matrix with m rows and n columns, it will always be the case that
either the rows or columns (whichever is larger in number) are linearly dependent. Hence
when we say that a non-square matrix is full rank, we mean that the row and column rank
are as high as possible, given the shape of the matrix. So if there are more rows than
columns (m > n), then the matrix is full rank if the matrix is full column rank.

Overview of LUP decomposition
-----------------------------

The idea of LUP decomposition is to find three n x n matrices L, U, and P such that:

    PA = LU (28.4)

where:
    L is a unit lower-triangular matrix
    U is an upper-triangular matrix
    P is a permutation matrix

We call matrices L, U, and P satisfying equation (28.4) an LUP decomposition of the
matrix A. Every non-singular matrix posses such a decomposition.

Computing an LUP decomposition for the matrix A has the advantage that we can more
easily solve linear systems when they are triangular, as is the case for both matrices L
and U. Once we have found an LUP decomposition for A, we can solve the system of
equations, Ax = b, by solving only the triangular linear systems, as follows.
Multiplying both sides of Ax = b by P, which yields the equivalent equation PAx = Pb,
which amounts to permuting the system of equations. Using our decomposition (28.4), we
obtain:

    PAx = Pb
    LUx = Pb --> define y = Ux, where x is the desired solution vector

    Ly = Pb --> solve for y using forward substitution
    Ux = y --> solve for x using back substitution

Because the permutation matrix P is invertible, multiplying both sides of equation
(28.4) by P^(-1) gives P^(-1)PA = P^(-1)LU so that A = P^(-1)LU

Hence, the vector x is our solution to Ax = b:

    Ax = P^(-1)LUx
       = P^(-1)Ly
       = P^(-1)Pb
       = b

Computing an LU decomposition
-----------------------------

If A is a non-singular matrix, then we can factor A = LU using Gaussian elimination. We
start by subtracting multiples of the first equation from the other equations in order
to remove the first variable from those equations. Then, we subtract multiples of the
second equation from the third and subsequent equations so that now the first and second
variables are removed from them. We continue this process until the system that remains
has an upper-triangular form---in fact, it is the matrix U. The matrix L is made up of
the row multipliers that cause variables to be eliminated.

The elements by which we divide during LU decomposition are called pivots, and they
occupy the diagonal elements of the matrix U. The reason we include a permutation matrix
P during LUP decomposition is that it allows us to avoid dividing by 0. When we use
permutations to avoid division by 0 (or by small numbers, which would contribute to
numerical instability), we are pivoting.

An important class of matrices for which LU decomposition always works correctly is the
class of symmetric positive-definite matrices. Such matrices require no pivoting, and
thus we can employ LU decomposition without fear of dividing by 0.

Each iteration of lu_decomp() works on a square sub-matrix, using its upper leftmost
element as the pivot to compute the v and w vectors and the Schur complement, which then
becomes the square sub-matrix worked on by the next iteration.

A standard optimization of the procedure is that we store the significant elements of L
and U in place in the matrix A.

A = (a_11,  w.T)
    (v,     A')
  = (1      0)      (a_11    w.T)
    (v/a_11 I_n-1)  (0      A' - vw.T/a_11)

A' - vw.T/a_11 is the Schur complement of A. Because A is non-singular, then the Schur
complement of A is also non-singular. Because the Schur complement of A is non-singular,
we can recursively find an LU decomposition for it.

Define A' - vw.T/a_11 = L'U'

A = (1      0)      (a_11    w.T)
    (v/a_11 I_n-1)  (0      A' - vw.T/a_11)
  = (1      0)  (a_11   w.T)
    (v/a_11 L') (0, U')
  = LU

Computing an LUP decomposition
------------------------------

Generally, in solving a system of linear equations Ax = b, we must pivot on off-diagonal
elements of A to avoid dividing by 0. We also want to avoid dividing by a small value,
even if A is non-singular, because numerical instabilities can result. We therefore try
to pivot on a large value.

We are given an n x n non-singular matrix A, and we wish to find a permutation matrix
P, a unit lower-triangular matrix L, and an upper-triangular matrix U such that PA = LU.

Before we partition the matrix A, as we did for LU decomposition, we move a non-zero
element, say a_k_1, from somewhere in the first column to the (1, 1) position of the
matrix. For numerical stability, we choose a_k_1 as the element in the first column with
the greatest absolute value. In order to preserve the set of equations, we exchange row
1 with row k, which is equivalent to multiplying A by a permutation matrix Q on the
left.

QA = (a_k1  w.T)
     (v     A')
   = (1      0)      (a_k1    w.T)
     (v/a_k1 I_n-1)  (0      A' - vw.T/a_k1)

P'(A' - vw.T/a_k1) = L'U'

Define P = (1   0)Q
           (0   P')

PA = (1   0)QA
     (0   P')
   = LU

Complexity
==========

Time
----

lu_decomp(), lup_decomp(): Theta(n^3).
lup_solver(): Theta(n^2) for forward substitution, Theta(n^2) for backward substitution,
Theta(n^2) for solving the system of equations.

Space
-----

lup_solver(): O(n) for x array and O(n) for y array.
"""


def lu_decomp(a):
    for k in range(len(a)):
        schur_complement(a, k, len(a))


def lup_decomp(a):
    n = len(a)
    p = list(range(n))
    for k in range(n):
        k_new = p_new = 0
        for i in range(k, n):
            if abs(a[i][k]) > p_new:
                k_new, p_new = i, abs(a[i][k])
        assert p_new != 0
        p[k], p[k_new] = p[k_new], p[k]
        for i in range(n):
            a[k][i], a[k_new][i] = a[k_new][i], a[k][i]
        schur_complement(a, k, n)
    return p


def lup_solver(a, b, p=None, decomp=True, lup=True):
    if decomp:
        p = lu_decomp(a) if lup is False else lup_decomp(a)
    n = len(a)
    b, x, y = [b[i] if p is None else b[p[i]] for i in range(n)], [0] * n, [0] * n
    for i in range(n):
        y[i] = b[i] - sum(a[i][j] * y[j] for j in range(i))
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]
    return x


def schur_complement(a, k, n):
    for i in range(k + 1, n):
        a[i][k] /= a[k][k]
        for j in range(k + 1, n):
            a[i][j] -= a[i][k] * a[k][j]
