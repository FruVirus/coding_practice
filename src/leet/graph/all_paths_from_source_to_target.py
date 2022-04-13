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

allPathsSourceTarget_dfs(graph): O(2^n * n), where n is the number of nodes.

Space
-----

allPathsSourceTarget_dfs(graph): O(2^n * n).
"""


def sol_dfs(graph):
    stack, sol = [(0, [])], []
    while stack:
        node, vlist = stack.pop()
        if node == len(graph) - 1:
            sol.append(vlist + [node])
        else:
            stack.extend((v, vlist + [node]) for v in graph[node])
    return sol
