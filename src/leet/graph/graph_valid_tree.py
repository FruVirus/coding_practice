"""
Graph Valid Tree
----------------

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a
list of edges where edges[i] = [a_i, b_i] indicates that there is an undirected edge
between nodes a_i and b_i in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Intuition
---------

1. G is fully connected if, and only if, we started a depth-first search from a single
source and discovered all nodes in G during it.

2. G contains no cycles if, and only if, the depth-first search never goes back to an
already discovered node. We need to be careful though not to count trivial cycles of the
form A → B → A that occur with most implementations of undirected edges.

For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, and it
can't possibly be fully connected. Any more, and it has to contain cycles. Additionally,
if the graph is fully connected and contains exactly n - 1 edges, it can't possibly
contain a cycle, and therefore must be a tree!

NB: If len(edges) == n - 1, then it's still possible for a graph to be an invalid tree
if there are disconnected components. For example, n = 5 and edges =
[[0,1],[0,4],[1,4],[2,3]] should return False even though len(edges) == n - 1, since
there are two connected components instead of one.

Complexity
==========

Time
----

validTree_dfs(n, edges) and validTree_dset(n, edges): O(n), where n is the number of
nodes.

Space
-----

validTree_dfs(n, edges) and validTree_dset(n, edges): O(n), where n is the number of
nodes.
"""


# Repository Library
from src.leet.graph.number_of_provinces import DisjointSet


def sol_dfs(n, edges):
    if len(edges) != n - 1:
        return False
    adj_list, seen, stack = [[] for _ in range(n)], set(), [0]
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    while stack:
        u = stack.pop()
        if u not in seen:
            seen.add(u)
            stack.extend(adj_list[u])
    return len(seen) == n


def sol_dset(n, edges):
    if len(edges) != n - 1:
        return False
    dset = DisjointSet(n)
    for u, v in edges:
        if dset.connected(u, v):
            return False
        dset.union(u, v)
    return True
