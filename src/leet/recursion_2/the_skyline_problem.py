"""
The Skyline Problem
-------------------

A city's skyline is the outer contour of the silhouette formed by all the buildings in
that city when viewed from a distance. Given the locations and heights of all the
buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where
buildings[i] = [left_i, right_i, height_i]:

    left_i is the x coordinate of the left edge of the ith building.
    right_i is the x coordinate of the right edge of the ith building.
    height_i is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat
surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate
in the form [[x_1, y_1], [x_2, y_2], ...]. Each key point is the left endpoint of some
horizontal segment in the skyline except the last point in the list, which always has a
y-coordinate 0 and is used to mark the skyline's termination where the rightmost
building ends. Any ground between the leftmost and rightmost buildings should be part of
the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output
skyline. For instance, [..., [2 3], [4 5], [7 5], [11 5], [12 7], ...] is not
acceptable; the three lines of height 5 should be merged into one in the final output as
such: [..., [2 3], [4 5], [12 7], ...].

Intuition
---------

All the information for the final answer comes from either the start or end of the
buildings. In addition, the height of the buildings are critical as well.

We move from left to right, encountering the starts and ends of the buildings.

Whenever we encounter the start of a building, we push the height of that building into
a priority queue. If the max in the priority queue changes, it means that this building,
at this start point, must be taller than every other building which overlaps with that
start point. Thus, this building must be part of the final answer.

Whenever we encounter the end of a building, we need to remove that building from the
priority queue. If the max in the priority queue changes, it means that the building
needs to be part of the final answer.

Example

buildings = [[1, 3, 3], [2, 4, 4], [5, 8, 2], [6, 7, 4], [8, 9, 4]]

1. We will split the left and right sides of the buildings into two different points.
The left side of the building will have a positive height and the right side of the
building will have a negative height. This way, we can sort all the buildings by their
x-coordinate (i.e., left side) first.

walls = [
    (1, 3), (2, 4), (3, -3), (4, -4), (5, 2), (6, 4), (7, -4), (8, -2), (8, 4), (9, -4)
]

2. As we iterate through walls, if we encounter a left side (i.e., a tuple with a
positive height), we add the height of the building into the queue, and then check if
adding the building height changes the max in the queue. For every time the queue's max
changes upon adding a new building height, we add the tuple to the final answer.

3. As we iterate through walls, if we encounter a right side (i.e., a tuple with a
negative height), we remove its corresponding height from the queue, and then check if
removing the building height changes the max in the queue. For every time the queue's
max changes upon removing a building's height. we add the tuple (right side, max(queue))
to the final answer.

Edge Cases

1. Two or more buildings share the same left side. In this case, we should sort the
buildings in decreasing order of their heights. Thus, we should process (0, 3) first and
then (0, 2).

2. Two or more buildings share the same right side. In this case, we should sort the
buildings in increasing order of their heights. Thus, we should process (5, 2) first and
then (5, 3).

3. The right side of a build overlaps with the left side of the next building. In this
case, we should sort the buildings so that the left side of the next building comes
before the right side of the current building. Thus, we should process (7, 3, s) first
and then (7, 2, e), where s/e denotes start/end.

Complexity
==========

Time
----

getSkyline(buildings): O(n * lg n).

Space
-----

getSkyline(buildings): O(n).
"""

# Standard Library
import heapq

from collections import defaultdict


def sol(buildings):
    counter, heap, sol, walls = defaultdict(int), [], [], []
    for left, right, height in buildings:
        walls.append((left, height))
        walls.append((right, -height))
    walls.sort()
    for pos, height in walls:
        if height > 0:
            if not heap or height > -heap[0]:
                if sol and sol[-1][0] == pos:
                    sol[-1][1] = height
                else:
                    sol.append([pos, height])
            heapq.heappush(heap, -height)
            counter[height] += 1
        else:
            counter[-height] -= 1
            while heap and counter[-heap[0]] == 0:
                heapq.heappop(heap)
            new_height = 0 if not heap else -heap[0]
            if sol[-1][0] == pos:
                sol[-1][1] = new_height
            else:
                sol.append([pos, new_height])
        if len(sol) > 1 and sol[-1][1] == sol[-2][1]:
            sol.pop()
    return sol
