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

validPath_bfs(n, edges, src, dst) and
validPath_dfs(n, edges, src, dst): O(v + e).

Space
-----

validPath_bfs(n, edges, src, dst) and
validPath_dfs(n, edges, src, dst): O(v + e).
"""


# Standard Library
from collections import deque


def sol_bfs(n, edges, src, dst):
    adj_list, queue, seen = [[] for _ in range(n)], deque([src]), set()
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    while queue:
        u = queue.popleft()
        if u == dst:
            return True
        if u not in seen:
            seen.add(u)
            queue.extend(adj_list[u])
    return False


def sol_dfs(n, edges, src, dst):
    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    seen, stack = set(), [src]
    while stack:
        node = stack.pop()
        if node == dst:
            return True
        if node not in seen:
            seen.add(node)
            stack.extend(adj_list[node])
    return False
