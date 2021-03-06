"""
Optimize Water Distribution in a Village
----------------------------------------

There are n houses in a village. We want to supply water for all the houses by building
wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1]
(note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to
lay pipes between houses are given by the array pipes where each pipes[j] =
[house1_j, house2_j, cost_j] represents the cost to connect house1_j and house2_j
together using a pipe. Connections are bidirectional, and there could be multiple valid
connections between the same two houses with different costs.

Return the minimum total cost to supply water to all houses.

Intuition
---------

First of all, let us introduce the problem of the minimum spanning tree.

Given a connected, edge-weighted and undirected graph, a minimum spanning tree is a
subset of edges that connect all vertices while the total weights of these edges are
minimum among all possible subsets.

One can draw some similarities between the above definition and our problem here.
Specifically, we can consider each house as a vertex in a graph, and the pipes between
the houses as edges in the graph.

However, there is one major difference between them. In our problem, every vertex and
every edge comes with a cost. While in the setting of MST, only the edges are associated
with the costs.

To bridge the gap, the trick is to add one virtual vertex to the existing graph. Along
with the addition of vertex, we also add edges between the virtual vertex and the rest
of the vertices (to denote the cost of building wells directly inside of houses).
Finally, we reassign the cost of each vertex to the corresponding newly-added edge.

With the converted graph, we then can take into account the costs from the vertex, via
the additional edges. We can focus entirely on selecting the appropriate edges to create
an MST. Thus, our problem is simplified to creating an MST from a list of weighted
edges.

Complexity
==========

Time
----

minCostToSupplyWater_kruskal(n, wells, pipes): O((n + m) * lg (n + m)), where n is the
number of houses and m is the number of pipes.
minCostToSupplyWater_prim(n, wells, pipes): O((n + m) * lg (n + m)).

Space
-----

minCostToSupplyWater_kruskal(n, wells, pipes): O().
minCostToSupplyWater_prim(n, wells, pipes): O(n + m).
"""


# Standard Library
import heapq

# Repository Library
from src.leet.graph.number_of_provinces import DisjointSet


def sol_kruskal(n, wells, pipes):
    edges = [(cost, 0, i) for i, cost in enumerate(wells, 1)]
    for u, v, cost in pipes:
        edges.append((cost, u, v))
    dset, total_cost = DisjointSet(n + 1), 0
    for cost, u, v in sorted(edges):
        if not dset.connected(u, v):
            dset.union(u, v)
            total_cost += cost
    return total_cost


def sol_prim(n, wells, pipes):
    edges = [[] for _ in range(n + 1)]
    for i, cost in enumerate(wells, 1):
        edges[0].append((cost, i))
    for u, v, cost in pipes:
        edges[u].append((cost, v))
        edges[v].append((cost, u))
    heapq.heapify(edges[0])
    heap, mst, total_cost = edges[0], {0}, 0
    while len(mst) < n + 1:
        cost, u = heapq.heappop(heap)
        if u not in mst:
            mst.add(u)
            total_cost += cost
            for new_cost, v in edges[u]:
                if v not in mst:
                    heapq.heappush(heap, (new_cost, v))
    return total_cost
