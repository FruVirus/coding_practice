"""
Furthest Building You Can Reach
-------------------------------

You are given an integer array heights representing the heights of buildings, some
bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using
bricks or ladders.

While moving from building i to building i + 1 (0-indexed),

    If the current building's height is greater than or equal to the next building's
height, you do not need a ladder or bricks.
    If the current building's height is less than the next building's height, you can
either use one ladder or (h[i + 1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given
ladders and bricks optimally.

Intuition
---------

Min Heap

The best strategy is to use the ladders for the longest climbs and the bricks for the
shortest climbs. This shouldn’t seem too surprising; a ladder is most valuable in the
cases where we would have to use a lot of bricks.

The solution is to move along the buildings sequentially, one climb at a time. At all
times, we should ensure ladders have been allocated to the longest climbs seen so far
and bricks to the shortest. This might sometimes involve going back and changing an
earlier allocation.

This code loops over all buildings, starting from the first and ending at the
second-to-last. For each building, it calculates the difference between the next
building and itself. If this difference is non-positive, then we know this is not a
climb and therefore should be skipped. Otherwise, it's a climb that we will need to
allocate bricks or a ladder to.

Anyway, the next thing to do is to decide how we're going to handle the allocation of
ladders and bricks. We decided above that the strategy we'll use is to use a ladder if
we have one available. If we're out of ladders, we'll replace the most wasteful (i.e.,
the ladder that was used with the smallest climb) ladder allocation with bricks. In
code, this means we'll need a data structure that we can insert climbs into, and then
when needed, retrieve the smallest climb.

Max Heap

This approach is similar to Approach 1, except instead of initially allocating ladders,
we allocate bricks. When we run out of bricks, we replace the longest climb with a
ladder. This was in contrast to before when we were replacing the shortest climb with
bricks. Because we now need to retrieve maximums instead of minimums, we should use a
max-heap instead of a min-heap.

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
