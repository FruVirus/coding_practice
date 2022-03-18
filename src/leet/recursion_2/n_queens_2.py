"""
N-Queens II
-----------

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Intuition
---------

Given a board state, and a possible placement for a queen, we need a smart way to
determine whether or not that placement would put the queen under attack. A queen can be
attacked if another queen is in any of the 4 following positions: on the same row, on
the same column, on the same diagonal, or on the same anti-diagonal.

Each time our backtrack function is called, we can encode state in the following manner:

    1. To make sure that we only place 1 queen per row, we will pass an integer argument
row into backtrack, and will only place one queen during each call. Whenever we place a
queen, we'll move onto the next row by calling backtrack again with the parameter value
row + 1.

    2. To make sure we only place 1 queen per column, we will use a set. Whenever we
place a queen, we can add the column index to this set.

The diagonals are a little trickier - but they have a property that we can use to our
advantage.

    1. For each square on a given diagonal, the difference between the row and column
indexes (row - col) will be constant. Think about the diagonal that starts from (0, 0) -
the i^th square has coordinates (i, i), so the difference is always 0.

    2. For each square on a given anti-diagonal, the sum of the row and column indexes
(row + col) will be constant. If you were to start at the highest square in an
anti-diagonal and move downwards, the row index increments by 1 (row + 1), and the
column index decrements by 1 (col - 1). These cancel each other out.

Whenever we place a queen, we should calculate the diagonal and the anti-diagonal value
it belongs to. In the same way we had a set for the column, we should also have a set
for both the diagonals and anti-diagonals. Then, we can put the values for this queen
into the corresponding sets.

When we are done exploring a path, we backtrack by removing the queen from the square -
this just means removing the values we added to our sets.

Complexity
==========

Time
----

totalNQueens(n): O(n!).

Space
-----

totalNQueens(n): O(n^2).
"""


def sol(n):
    sol, board = [], [["."] * n for _ in range(n)]

    def backtrack(row, cols, diags, anti_diags, board):
        if row == n:
            sol.append(["".join(row) for row in board])
            return 1
        count = 0
        for col in range(n):
            diag, anti_diag = row - col, row + col
            if col in cols or diag in diags or anti_diag in anti_diags:
                continue
            cols.add(col)
            diags.add(diag)
            anti_diags.add(anti_diag)
            board[row][col] = "Q"
            count += backtrack(row + 1, cols, diags, anti_diags, board)
            cols.remove(col)
            diags.remove(diag)
            anti_diags.remove(anti_diag)
            board[row][col] = "."
        return count

    count = backtrack(0, set(), set(), set(), board)
    return count, sol
