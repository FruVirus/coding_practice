"""
Rotate Image
------------

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees
(clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D
matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Intuition
---------

Cells move in groups when we rotate the image. We can iterate over each group of four
cells and rotate them. Note that n // 2 + n % 2 is just ceil(n / 2)

We decide on a repeatable rectangle part of the square which can be rotated 4 times
without overlapping.

    - For an even length matrix, this would be 0 <= i < n // 2 and 0 <= j < n // 2
    - For an odd length matrix, this would be 0 <= i < ceil(n / 2) and 0 <= j < n // 2

Since n // 2 == ceil(n / 2) for even matrices, we can just use 0 <= i < ceil(n / 2) and
0 <= j < n // 2

The most elegant solution for rotating the matrix is to firstly transpose the matrix
around the main diagonal, and then reverse it from left to right. These operations are
called transpose and reflect in linear algebra.

Note that you can also reverse the rows of the matrix first and then transpose. In this
setting, reversing the rows of the matrix means swapping the corresponding first and
last rows in the following manner:
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[-i - 1][j] = matrix[-i - 1][j], matrix[i][j]

Complexity
==========

Time
----

rotate_one(matrix) and rotate_two(matrix): O(m), where m is the number of cells in the
matrix.

Space
-----

rotate_one(matrix) and rotate_two(matrix): O(1).
"""


def sol_one(matrix):
    n = len(matrix[0])
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            top_left = matrix[i][j]
            top_right = matrix[j][n - i - 1]
            bottom_right = matrix[n - i - 1][n - j - 1]
            bottom_left = matrix[n - j - 1][i]
            matrix[i][j] = bottom_left
            matrix[j][n - i - 1] = top_left
            matrix[n - i - 1][n - j - 1] = top_right
            matrix[n - j - 1][i] = bottom_right


def sol_two(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
