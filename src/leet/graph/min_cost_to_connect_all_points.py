"""
Min Cost to Connect All Points
------------------------------

You are given an array points representing integer coordinates of some points on a
2D-plane, where points[i] = [x_i, y_i].

The cost of connecting two points [x_i, y_i] and [x_j, y_j] is the manhattan distance
between them: |x_i - x_j| + |y_i - y_j|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there
is exactly one simple path between any two points.

Complexity
==========

Time
----

minCostConnectPoints_kruskal(points) and minCostConnectPoints_prim(points):
O(n^2 * lg n), where n is the number of points in the input array.

Space
-----

minCostConnectPoints_kruskal(points) and minCostConnectPoints_prim(points): O(n^2).
"""


# Standard Library
import heapq

# Repository Library
from src.leet.graph.number_of_provinces import DisjointSet


def calculate_dist(pointa, pointb):
    return abs(pointa[0] - pointb[0]) + abs(pointa[1] - pointb[1])


def sol_kruskal(points):
    n, cost, edges, num_edges = len(points), 0, [], 0
    dset = DisjointSet(n)
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((calculate_dist(points[i], points[j]), i, j))
    for dist, u, v in sorted(edges):
        if not dset.connected(u, v):
            dset.union(u, v)
            cost += dist
            num_edges += 1
            if num_edges == n - 1:
                break
    return cost


def sol_prim(points):
    n, cost, heap, mst, num_edges = len(points), 0, [(0, 0)], set(), 0
    while num_edges < n:
        dist, i = heapq.heappop(heap)
        if i not in mst:
            mst.add(i)
            cost += dist
            num_edges += 1
            for j in range(n):
                if j not in mst:
                    heapq.heappush(heap, (calculate_dist(points[i], points[j]), j))
    return cost
