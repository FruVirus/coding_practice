"""
All Paths From Source to Target
-------------------------------

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all
possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
(i.e., there is a directed edge from node i to node graph[i][j]).

Complexity
==========

Time
----

allPathsSourceTarget_bfs(graph) and allPathsSourceTarget_dfs(graph): O(2^n * n), where
n is the number of nodes.

Space
-----

allPathsSourceTarget_bfs(graph) and allPathsSourceTarget_dfs(graph): O(2^n * n).
"""


# Standard Library
from collections import deque


def sol_bfs(graph):
    queue, sol = deque([(0, [])]), []
    while queue:
        u, vlist = queue.popleft()
        if u == len(graph) - 1:
            sol.append(vlist + [u])
        else:
            queue.extend((v, vlist + [u]) for v in graph[u])
    return sol


def sol_dfs(graph):
    stack, sol = [(0, [])], []
    while stack:
        u, vlist = stack.pop()
        if u == len(graph) - 1:
            sol.append(vlist + [u])
        else:
            stack.extend((v, vlist + [u]) for v in graph[u])
    return sol
