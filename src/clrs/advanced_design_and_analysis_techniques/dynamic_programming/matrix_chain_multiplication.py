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
algorithm and is given by the Catalan numbers. The number of solutions is thus
exponential in the number of matrices using a brute force method.

Applying dynamic programming
----------------------------

Consider the following sequence:

A x B x C

If we wish to compute the cost for multiplying (A x B) x C, then we have to compute the
cost of m[A, B] + m[C, C] + the cost of multiplying (A x B) by C.

Complexity
==========

Time
----

matrix_chain_order(): O(n^3).

Space
-----

matrix_chain_order(): O(n^2) for m table and O(n^2) for s table.
"""


def matrix_chain_order(p):
    n = len(p) - 1
    m, s = [[0] * n for _ in range(n)], [[0] * n for _ in range(n)]
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j], s[i][j] = q, k + 1
    return m, s


def return_optimal_parens(s, i, j):
    if i == j:
        str_ = "A_" + str(i)
    else:
        str_ = "("
        str_ += return_optimal_parens(s, i, s[i][j] - 1)
        str_ += return_optimal_parens(s, s[i][j], j)
        str_ += ")"
    return str_
