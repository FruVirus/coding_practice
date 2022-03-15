"""
N-Queens II
-----------

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Complexity
==========

Time
----

totalNQueens(n): O(n!).

Space
-----

totalNQueens(n): O(n).
"""


def sol(n):
    def backtrack(row, cols, diags, anti_diags):
        if row == n:
            return 1
        sol = 0
        for col in range(n):
            curr_diag, curr_anti_diag = row - col, row + col
            if col in cols or curr_diag in diags or curr_anti_diag in anti_diags:
                continue
            cols.add(col)
            diags.add(curr_diag)
            anti_diags.add(curr_anti_diag)
            sol += backtrack(row + 1, cols, diags, anti_diags)
            cols.remove(col)
            diags.remove(curr_diag)
            anti_diags.remove(curr_anti_diag)
        return sol

    return backtrack(0, set(), set(), set())
