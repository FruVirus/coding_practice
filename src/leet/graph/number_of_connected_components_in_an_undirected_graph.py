"""
Number of Connected Components in an Undirected Graph
-----------------------------------------------------

You have a graph of n nodes. You are given an integer n and an array edges where
edges[i] = [a_i, b_i] indicates that there is an edge between a_i and b_i in the graph.

Return the number of connected components in the graph.

Intuition
---------

In an undirected graph, a connected component is a subgraph in which each pair of
vertices is connected via a path. So essentially, all vertices in a connected component
are reachable from one another.

If we run DFS, starting from a particular vertex, it will continue to visit the vertices
depth-wise until there are no more adjacent vertices left to visit. Thus, it will visit
all of the vertices within the connected component that contains the starting vertex.
Each time we finish exploring a connected component, we can find another vertex that has
not been visited yet, and start a new DFS from there. The number of times we start a new
DFS will be the number of connected components.

Complexity
==========

Time
----

countComponents_dfs(n, edges): O(e + v), where e is the number of edges and v is the
number of vertices.
countComponents_dset(n, edges): O(e).

Space
-----

countComponents_dfs(n, edges): O(e + v).
countComponents_dset(n, edges): O(v).
"""


# Repository Library
from src.leet.graph.number_of_provinces import DisjointSet


def sol_dfs(n, edges):
    adj_list, count, seen = [[] for _ in range(n)], 0, set()
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    for u in range(n):
        if u not in seen:
            count += 1
            seen.add(u)
            stack = [u]
            while stack:
                for v in adj_list[stack.pop()]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
    return count


def sol_dset(n, edges):
    dset = DisjointSet(n)
    for u, v in edges:
        dset.union(u, v)
    return dset.get_count()
