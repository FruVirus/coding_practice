"""
Search a 2D Matrix II
---------------------

Write an efficient algorithm that searches for a value target in an m x n integer
matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Complexity
==========

Time
----

searchMatrix(matrix, target): O(n * lg n).

Space
-----

searchMatrix(matrix, target): O(lg n).
"""


def sol(matrix, target):
    if not matrix:
        return False

    def search(l, u, r, d):
        if l > r or u > d or target < matrix[u][l] or target > matrix[d][r]:
            return False
        mid, row = l + (r - l) // 2, u
        while row <= d and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1
        return search(l, row, mid - 1, d) or search(mid + 1, u, r, row - 1)

    return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)
