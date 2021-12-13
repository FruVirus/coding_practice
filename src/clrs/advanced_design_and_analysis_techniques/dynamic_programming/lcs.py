"""
15.4 Longest common subsequence
===============================

We can define similarity between strings in many different ways. For example, we can say
that two strings are similar if one is a substring of the other. Alternatively, we could
say that two strings are similar if the number of changes needed to turn one into the
other is small. Yet another way to measure the similarity of two strings is by finding a
third string in which the characters in the third string appear in each of the two
strings; these characters must appear in the same order, but not necessarily
consecutively. The longer the third string, the more similar the two strings are.

We formalize this last notion of similarity as the longest-common-subsequence (LCS)
problem. A subsequence of a given sequence is just the given sequence with zero or more
elements left out. Formally, given a sequence X = <x1, x2, ..., x_m>, another sequence
Z = <z1, z2, ..., z_k> is a subsequence of X if there exists a strictly increasing
sequence <i1, i2, ..., i_k> of indices of X such that for all j = 1, 2, ..., k, we have
x_i_j = z_j. For example, Z = <B, C, D, B> is a subsequence of X = <A, B, C, B, D, A, B>
with corresponding index sequence <2, 3, 5, 7>.

Given two sequences X and Y, we say that a sequence Z is a common subsequence of X and Y
if Z is a subsequence of both X and Y.

In the LCS problem, we are given two sequences and wish to find a maximum length common
subsequence of X and Y.

An LCS of two sequences contains within it an LCS of prefixes of the two sequences.
Thus, the LCS problem has an optimal-substructure property.

We should examine either one or two subproblems when finding an LCS of
X = <x1, x2, ..., x_m> and Y = <y1, y2, ..., y_n>. If xm = yn, we must find an LCS of
X_(m - 1) and Y_(n - 1). Appending xm = yn to this LCS yields an LCS of X and Y. If
x_m != y_n, then we must solve two subproblems: finding an LCS of X_(m - 1) and Y and
finding an LCS of X and Y_(n - 1). Whichever of these two LCSs is longer is an LCS of X
and Y. Because these causes exhaust all possibilities, we know that one of the optimal
subproblem solutions must appear within an LCS of X and Y.

We can readily see the overlapping-subproblems property in the LCS problem. To find an
LCS of X and Y, we may need to find the LCSs of X and Y_(n - 1) and of X_(m - 1) and Y.
But each of the subproblems has the subsubproblem of finding an LCS of X_(m - 1) and
Y_(n - 1).

In the recursive formulation, a condition in the problem restricts which subproblems we
may consider. When x_i = y_j, we can and should consider the subproblem of finding an
LCS of X_(i - 1) and Y_(j - 1). Otherwise, we instead consider the two subproblems of
finding an LCS of X_i and Y_(j - 1) and of X_(i - 1) and Y_j. In the rod-cutting and
matrix-chain problems, we had to consider all subproblems due to conditions in the
problem formulation.

Complexity
==========

The LCS problem has only Theta(m x n) distinct subproblems. It takes O(1) time to fill
up the c table, which has m x n entries. Thus, the total time is O(m x n).

Time
----

lcs_bottom_up(): O(m x n).
lcs_top_down(): O(m x n).
print_lcs(): O(m + n).

Space
-----

lcs_bottom_up(): O(m x n) for c table.
lcs_top_down(): O(m x n) for c table.
"""


def lcs_bottom_up(c, x, y, m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = 1 + c[i - 1][j - 1]
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]
    return c


def lcs_top_down(c, x, y, i, j):
    if c[i][j] != float("inf"):
        return c[i][j]
    if i == 0 or j == 0:
        c[i][j] = 0
    elif x[i - 1] == y[j - 1]:
        c[i][j] = 1 + lcs_top_down(c, x, y, i - 1, j - 1)
    else:
        c[i][j] = max(lcs_top_down(c, x, y, i - 1, j), lcs_top_down(c, x, y, i, j - 1))
    return c[i][j]


def lcs_solution(x, y, top_down=False):
    m, n = len(x), len(y)
    if top_down:
        c = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        lcs_top_down(c, x, y, m, n)
    else:
        c = [[0] * (n + 1) for _ in range(m + 1)]
        lcs_bottom_up(c, x, y, m, n)
    return c


def return_lcs(c, x, y, i, j, lcs=None):
    lcs = lcs or []
    if c[i][j] == 0:
        return lcs
    if x[i - 1] == y[j - 1]:
        lcs = return_lcs(c, x, y, i - 1, j - 1, lcs)
        lcs.append(x[i - 1])
    elif c[i - 1][j] >= c[i][j - 1]:
        lcs = return_lcs(c, x, y, i - 1, j, lcs)
    else:
        lcs = return_lcs(c, x, y, i, j - 1, lcs)
    return lcs
