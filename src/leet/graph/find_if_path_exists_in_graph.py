"""
Find if Path Exists in Graph
----------------------------

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to
n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges,
where each edges[i] = [u_i, v_i] denotes a bi-directional edge between vertex u_i and
vertex v_i. Every vertex pair is connected by at most one edge, and no vertex has an
edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex
destination.

Given edges and the integers n, source, and destination, return true if there is a valid
path from source to destination, or false otherwise.

Complexity
==========

Time
----

validPath_dfs(n, edges, source, destination): O(v + e).

Space
-----

validPath_dfs(n, edges, source, destination): O(v + e).
"""


def sol_dfs(n, edges, source, destination):
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    seen, stack = set(), [source]
    while stack:
        node = stack.pop()
        if node == destination:
            return True
        if node in seen:
            continue
        seen.add(node)
        stack.extend(adj_list[node])
    return False
