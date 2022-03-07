"""
Perfect Squares
---------------

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is
the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect
squares while 3 and 11 are not.

Complexity
==========

Time
----

numSquares(n): O(n^(h / 2)), where h is the height of the N-ary tree.

Space
-----

numSquares(n): O(sqrt(n)^h).
"""


def sol(n):
    square_nums, level, queue = [i ** 2 for i in range(1, int(n ** 0.5) + 1)], 0, {n}
    while queue:
        level += 1
        next_queue = set()
        for remainder in queue:
            for square_num in square_nums:
                if remainder == square_num:
                    return level
                if remainder < square_num:
                    break
                next_queue.add(remainder - square_num)
        queue = next_queue
    return level
