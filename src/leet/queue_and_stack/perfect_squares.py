"""
Perfect Squares
---------------

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is
the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect
squares while 3 and 11 are not.

Intuition
---------

1. First, for the square numbers that can be formed from n.
2. We then create a queue variable which would keep all the remainders to enumerate at
each level.
3. In the main loop, we iterate over the queue variable. At each iteration, we check if
the remainder is one of the square numbers. If the remainder is not a square number, we
subtract it with one of the square numbers to obtain a new remainder and then add the
new remainder to the next_queue for the iteration of the next level. We break out of the
loop once we encounter a remainder that is of a square number, which also means that we
find the solution.

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
                if remainder > square_num:
                    next_queue.add(remainder - square_num)
        queue = next_queue
    return level
