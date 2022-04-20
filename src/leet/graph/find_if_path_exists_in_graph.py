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
    graph, queue, seen = {i: [] for i in range(n)}, deque([src]), set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    while queue:
        u = queue.popleft()
        if u == dst:
            return True
        if u not in seen:
            seen.add(u)
            queue.extend(graph[u])
    return False


def sol_dfs(n, edges, src, dst):
    graph, stack, seen = {i: [] for i in range(n)}, [src], set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    while stack:
        u = stack.pop()
        if u == dst:
            return True
        if u not in seen:
            seen.add(u)
            stack.extend(graph[u])
    return False
