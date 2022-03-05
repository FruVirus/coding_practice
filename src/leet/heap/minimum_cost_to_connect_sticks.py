"""
Minimum Cost to Connect Sticks
------------------------------

You have some number of sticks with positive integer lengths. These lengths are given as
an array sticks, where sticks[i] is the length of the ith stick.

You can connect any two sticks of lengths x and y into one stick by paying a cost of
x + y. You must connect all the sticks until there is only one stick remaining.

Return the minimum cost of connecting all the given sticks into one stick in this way.

Complexity
==========

Time
----

connectSticks(sticks): O(n * lg n).

Space
-----

connectSticks(sticks): O(n).
"""

# Standard Library
import heapq


def sol(sticks):
    cost = 0
    heapq.heapify(sticks)
    for _ in range(len(sticks) - 1):
        one, two = heapq.heappop(sticks), heapq.heappop(sticks)
        cost += one + two
        heapq.heappush(sticks, one + two)
    return cost
