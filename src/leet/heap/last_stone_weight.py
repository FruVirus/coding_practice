"""
Last Stone Weight
-----------------

You are given an array of integers stones where stones[i] is the weight of the ith
stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones
and smash them together. Suppose the heaviest two stones have weights x and y with
x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new
weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left,
return 0.

Complexity
==========

Time
----

lastStoneWeight(): O(n * lg n).

Space
-----

lastStoneWeight(): O(1).
"""

# Standard Library
import heapq


def sol(stones):
    stones = [-1 * stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y, x = heapq.heappop(stones), heapq.heappop(stones)
        if x != y:
            heapq.heappush(stones, (y - x))
    return 0 if not stones else -stones[0]
