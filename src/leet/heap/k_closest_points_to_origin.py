"""
K Closest Points to Origin
--------------------------

Given an array of points where points[i] = [x_i, y_i] represents a point on the X-Y
plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e.,
sqrt((x_1 - x_2)^2 + (y_1 - y_2)^2).

You may return the answer in any order. The answer is guaranteed to be unique (except
for the order that it is in).

Complexity
==========

Time
----

kClosest(points, k): O(n * lg k).

Space
-----

kClosest(points, k): O(k).
"""

# Standard Library
import heapq


def sol(points, k):
    heap = [(-(x ** 2 + y ** 2), i) for i, (x, y) in enumerate(points) if i < k]
    heapq.heapify(heap)
    for i in range(k, len(points)):
        dist = points[i][0] ** 2 + points[i][1] ** 2
        if dist < -heap[0][0]:
            heapq.heappushpop(heap, (-dist, i))
    return [points[i] for _, i in heap]
