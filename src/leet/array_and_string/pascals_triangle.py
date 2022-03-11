"""
Pascal's Triangle
-----------------

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as
shown.

Complexity
==========

Time
----

generate(num_rows): O(num_rows^2).

Space
-----

generate(num_rows): O(num_rows^2).
"""


def sol(num_rows):
    return [get_row(i) for i in range(num_rows)]


def get_row(row):
    pascal = [1] * (row + 1)
    for i in range(1, row):
        for j in range(i, 0, -1):
            pascal[j] += pascal[j - 1]
    return pascal
