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

Edge Cases

1. Two or more buildings share the same left side. In this case, we should sort the
buildings in decreasing order of their heights. Thus, we should process (0, 3, s) first
and then (0, 2, s), where s denotes start.

2. Two or more buildings share the same right side. In this case, we should sort the
buildings in increasing order of their heights. Thus, we should process (5, 2, e) first
and then (5, 3, e), where e denotes end.

3. The right side of a build overlaps with the left side of the next building. In this
case, we should sort the buildings so that the left side of the next building comes
before the right side of the current building. Thus, we should process (7, 3, s) first
and then (7, 2, e), where s/e denotes start/end.

Notes

1. We will sort the building by their left sides first (since we're iterating from left
to right), followed by their heights (heights will be negative since we want to keep a
max heap), followed by their right sides.

2. We account for the first edge case by making the heights negative in the sorted
list. In this manner, if two buildings start at x = 0, the taller building will have a
more negative height and will be considered first in the max heap.

3. We account for the second edge case by adding an extra list of 3-tuples (r, 0, 0) so
that the heights are effectively equal for buildings that end at the same x position.

4. We account for the third edge case by making the heights negative in the sorted list
and by adding an extra list of 3-tuples (r, 0, 0). In this manner, the start of the next
building is always considered before the end of the current building in the sorted list
since the heights are negative.

5. We only encounter the start of a building if the height is negative (i.e., non-zero).
In this case, we immediately push the height of that building along with its right side
to the max heap. If the max in the max heap changes (i.e., it is not the same as the
last max in the solution), then we add the left side of the new building along with the
max in the max heap to the solution.

6. We only encounter the end of a building when the left side coordinate is greater than
or equal to the coordinate of the max entry in the max heap. In this case, we remove
that building from the max heap.

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


def sol(buildings):
    points = [(l, -h, r) for l, r, h in buildings]
    points += [(r, 0, 0) for _, r, _ in buildings]
    points.sort()
    sol, heap = [[0, 0]], [(0, float("inf"))]
    for l, h, r in points:
        while heap[0][1] <= l:
            heapq.heappop(heap)
        if h != 0:
            heapq.heappush(heap, (h, r))
        if sol[-1][1] != -heap[0][0]:
            sol.append((l, -heap[0][0]))
    return sol[1:]
