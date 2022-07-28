"""
K-th Symbol in Grammar
----------------------

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in
every subsequent row, we look at the previous row and replace each occurrence of 0 with
01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table
of n rows.

Intuition
---------

Each row, after the first row, is the concatenation of the row above it and its reverse.
The midpoint of a row is given by 2 ^ (n - 1) / 2. If k is <= mid, then we recurse to a
previous row and decrement n by 1. Otherwise, we recurse to a previous row and decrement
n by 1 and k by mid and we subtract 1 from the return value.

Complexity
==========

Time
----

kthGrammar(n, k): O(n).

Space
-----

kthGrammar(n, k): O(1).
"""


def sol(n, k):
    if n == 1:
        return 0
    mid = 2 ** (n - 1) // 2
    return sol(n - 1, k) if k <= mid else 1 - sol(n - 1, k - mid)
