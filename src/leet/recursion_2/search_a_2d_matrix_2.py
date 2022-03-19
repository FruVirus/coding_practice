"""
Search a 2D Matrix II
---------------------

Write an efficient algorithm that searches for a value target in an m x n integer
matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Intuition
---------

Divide and Conquer Approach

Because this algorithm operates recursively, its correctness can be asserted via the
correctness of its base and recursive cases.

Base Case

For a sorted two-dimensional array, there are two ways to determine in constant time
whether an arbitrary element target can appear in it. First, if the array has zero area,
it contains no elements and therefore cannot contain target. Second, if target is
smaller than the array's smallest element (found in the top-left corner) or larger than
the array's largest element (found in the bottom-right corner), then it definitely is
not present.

Recursive Case

If the base case conditions have not been met, then the array has positive area and
target could potentially be present. Therefore, we seek along the matrix's middle column
for an index row such that matrix[row - 1][mid] < target < matrix[row][mid] (obviously,
if we find target during this process, we immediately return true). The existing matrix
can be partitioned into four submatrices around this index; the top-left and
bottom-right submatrices cannot contain target (via the argument outlined in Base Case
section), so we can prune them from the search space. Additionally, the bottom-left and
top-right submatrices are sorted two-dimensional matrices, so we can recursively apply
this algorithm to them.

Search Space Reduction Approach

First, we initialize a (row, col) pointer to the bottom-left of the matrix. Then, until
we find target and return true (or the pointer points to a (row, col) that lies outside
of the dimensions of the matrix), we do the following: if the currently-pointed-to value
is larger than target we can move one row "up". Otherwise, if the currently-pointed-to
value is smaller than target, we can move one column "right". It is not too tricky to
see why doing this will never prune the correct answer; because the rows are sorted from
left-to-right, we know that every value to the right of the current value is larger.
Therefore, if the current value is already larger than target, we know that every value
to its right will also be too large. A very similar argument can be made for the
columns, so this manner of search will always find target in the matrix (if it is
present).

Complexity
==========

Time
----

searchMatrix_dc(matrix, target): O(n * lg n).
searchMatrix_ssr(matrix, target): O(n + m).

Space
-----

searchMatrix_dc(matrix, target): O(lg n).
searchMatrix_ssr(matrix, target): O(1).
"""


def sol_dc(matrix, target):
    if not matrix:
        return False

    def search(l, r, u, d):
        if l > r or u > d or target < matrix[u][l] or target > matrix[d][r]:
            return False
        mid, row = l + (r - l) // 2, u
        while row <= d and matrix[row][mid] <= target:
            if matrix[row][mid] == target:
                return True
            row += 1
        return search(l, mid - 1, row, d) or search(mid + 1, r, u, row - 1)

    return search(0, len(matrix[0]) - 1, 0, len(matrix) - 1)


def sol_ssr(matrix, target):
    if not matrix:
        return False
    h, w = len(matrix), len(matrix[0])
    row, col = h - 1, 0
    while col < w and row >= 0:
        if matrix[row][col] > target:
            row -= 1
        elif matrix[row][col] < target:
            col += 1
        else:
            return True
    return False
