"""
15.2 Matrix-chain multiplication
================================

In matrix chain multiplication, we are given a sequence of n matrices to be multiplied
and we wish to know the optimal parenthesization of the sequence so that the number of
multiplies are minimized. Matrix multiplication is associative, and so all
parenthesizations yield the same product; however, different parenthesizations require
different number of multiplies (unless all matrices in the sequence are square). A
product of matrices is fully parenthesized if it is either a single matrix or the
product of two fully parenthesized matrix products, surrounded by parentheses.

We can multiply two matrices A and B iff they are compatible: the number of columns of A
must equal the number of rows of B. If A is a p x q matrix and B is a q x r matrix, the
resulting matrix C is a p x r matrix. The time to compute C is dominated by the number
of scalar multiplications, which is p x q x r.

Note that in the matrix-chain multiplication problem, we are not actually multiplying
matrices. Our goal is only to determine an order for multiplying matrices that has the
lowest cost.

Counting the number of parenthesizations
----------------------------------------

Exhaustively checking all possible parenthesizations yields to an exponentially growing
algorithm and the total number of possible parenthesizations is given by the Catalan
numbers. The number of solutions is thus exponential in the number of matrices using a
brute force method.

Applying dynamic programming
----------------------------

Consider the following sequence:

A x B x C

If we wish to compute the cost for multiplying (A x B) x C, then we have to compute the
cost of m[A, B] + m[C, C] + the cost of multiplying the result of (A x B) by C.

Intuition
---------

If the problem is non-trivial, i.e., i < j, then to parenthesize the product, we must
split the product between A_k and A_(k + 1) for some integer k in the range i <= k < j.
That is, for some value of k, we first compute the matrices A_i...k and A_(k + 1)...j
and then multiply them together to produce the final product A_i...j. The cost of
parenthesizing this way is the cost of computing the matrix A_i...k plus the cost of
computing A_(k + 1)...j, plus the cost of multiplying the results together. We must
ensure that when we search for the correct place to split the product (i.e., the integer
k), we have considered all possible places, so that we are sure of having examined the
optimal one. Thus, the procedure iterates k through the range [i, j) to consider all
possibilities and we pick the k that gives the minimum cost. In addition, we only want
to iterate/recurse through subproblems where the matrix chain has length greater than 1
(otherwise, the problem is trivial). In the bottom-up approach, the outer-most for-loop
iterates l through chains of length 2 and greater and the top-down approach does not
recurse if i == j.

The values in the m matrix determine how many multiplies are required for all
combinations of multiplications. The diagonal elements are 0 since m[1][1] means that we
are "multiplying" matrix 1 with itself, which is a free operation. m[i][j], where i and
j are consecutive numbers (e.g., i = 2 and j = 3 or i = 3 and j = 4) is the number of
multiplies for multiplying matrix i with matrix j. m[i][j], where i and j are NOT
consecutive numbers (e.g., i = 1 and j = 3) is the MINIMUM number of multiplies among
all possible combinations of multiplies between i and j.

For example:

    A1      *   A2      *   A3      *   A4
   5 x 4       4 x 6       6 x 2       2 x 7

m[1][1] = m[2][2] = m[3][3] = m[4][4] = 0
m[1][2] = A1 * A2 = 5 x 4 x 6 = 120
m[2][3] = A2 * A3 = 4 x 6 x 2 = 48
m[3][4] = A3 * A4 = 6 x 2 x 7 = 84
m[1][3] = min(A1 * (A2 * A3), (A1 * A2) * A3)
        = min(m[1][1] + m[2][3] + 5 x 4 x 2, m[1][2] + m[3][3] + 5 x 6 x 2)
        = min(88, 180)
        = 88
The last addition in min() corresponds to the number of multiplies between A1 and the
result of (A2 * A3) (or between the result of (A1 * A2) and A3).

Thus, the m matrix holds the minimum number of multiplies for every single possible
parenthesization.

The m matrix gives the costs of optimal solutions to subproblems, but they do not
provide all the information we need to construct an optimal solution. The s matrix holds
the k value which obtained the minimum m[i][j] value for a given i, j combination. If
k = 1 gives the minimum value for m[1][2], then k[1][2] = 1, and so on.

Complexity
==========

Time
----

mc_bu() and mc_td(): O(n^3).

Space
-----

mc_bu() and mc_td(): O(n^2) for m table and O(n^2) for s table.
"""


def mc_bu(p, m, s, n):
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[j + 1] * p[k + 1]
                if q < m[i][j]:
                    m[i][j], s[i][j] = q, k + 1


def mc_td(p, m, s, i, j):
    if m[i][j] == float("inf"):
        if i == j:
            m[i][j] = 0
        else:
            for k in range(i, j):
                m1 = mc_td(p, m, s, i, k)
                m2 = mc_td(p, m, s, k + 1, j)
                q = m1 + m2 + p[i] * p[j + 1] * p[k + 1]
                if q < m[i][j]:
                    m[i][j], s[i][j] = q, k + 1
    return m[i][j]


def mc(p, i=None, j=None, s=None, td=False):
    if s is None:
        n, val = len(p) - 1, float("inf") if td else 0
        m, s = [[val] * n for _ in range(n)], [[0] * n for _ in range(n)]
        if td:
            mc_td(p, m, s, i, j)
        else:
            mc_bu(p, m, s, n)
    if i == j:
        sol = "A_" + str(i)
    else:
        sol = "(" + mc(p, i, s[i][j] - 1, s) + mc(p, s[i][j], j, s) + ")"
    return sol
