"""
Furthest Building You Can Reach
-------------------------------

You are given an integer array heights representing the heights of buildings, some
bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using
bricks or ladders.

While moving from building i to building i+1 (0-indexed),

    If the current building's height is greater than or equal to the next building's
height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can
either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given
ladders and bricks optimally.

Complexity
==========

Time
----

furthestBuilding_bricks(heights, bricks, ladders): O(n * lg L), where L is the number of
ladders.
furthestBuilding_ladders(heights, bricks, ladders): O(n * lg n), where n is the number
of climbs.

Space
-----

furthestBuilding_bricks(heights, bricks, ladders): O(L).
furthestBuilding_ladders(heights, bricks, ladders): O(n).
"""

# Standard Library
import heapq


def sol_bricks(heights, bricks, ladders):
    climb = []
    for i in range(len(heights) - 1):
        height_diff = heights[i + 1] - heights[i]
        if height_diff <= 0:
            continue
        heapq.heappush(climb, height_diff)
        if len(climb) <= ladders:
            continue
        bricks -= heapq.heappop(climb)
        if bricks < 0:
            return i
    return len(heights) - 1


def sol_ladders(heights, bricks, ladders):
    climb = []
    for i in range(len(heights) - 1):
        height_diff = heights[i + 1] - heights[i]
        if height_diff <= 0:
            continue
        heapq.heappush(climb, -height_diff)
        bricks -= height_diff
        if bricks < 0 and ladders == 0:
            return i
        if bricks < 0:
            bricks += -heapq.heappop(climb)
            ladders -= 1
    return len(heights) - 1
