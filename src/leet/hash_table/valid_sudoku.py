"""
Valid Sudoku
------------

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without
repetition.

Note:

    - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    - Only the filled cells need to be validated according to the mentioned rules.

Complexity
==========

Time
----

isValidSudoku(board): O(n^2), because we need to traverse every position in the board
and each of the four checks is an O(1) operation.

Space
-----

isValidSudoku(board): O(n^2), because in the worst-case scenario, if the board is full,
we need a has set each with size n to store all seen numbers for each of the n rows, n
columns, and n boxes, respectively.
"""


def sol(board):
    n = 9
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]
    for r in range(n):
        for c in range(n):
            val = board[r][c]
            if val != ".":
                idx = 3 * (r // 3) + c // 3
                if val in rows[r] or val in cols[c] or val in boxes[idx]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[idx].add(val)
    return True
