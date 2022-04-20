"""
Minimum Height Trees
--------------------

A tree is an undirected graph in which any two vertices are connected by exactly one
path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where
edges[i] = [a_i, b_i] indicates that there is an undirected edge between the two nodes
a_i and b_i in the tree, you can choose any node of the tree as the root. When you
select a node x as the root, the result tree has height h. Among all possible rooted
trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between
the root and a leaf.

Intuition
---------

First of all, let us clarify some concepts.

    - The distance between two nodes is the number of edges that connect the two nodes.

Note, normally there could be multiple paths to connect nodes in a graph. In our case
though, since the input graph can form a tree from any node, as specified in the
problem, there could only be one path between any two nodes. In addition, there would be
no cycle in the graph. As a result, there would be no ambiguity in the above definition
of distance.

The height of a tree can be defined as the maximum distance between the root and all its
leaf nodes.

With the above definitions, we can rephrase the problem as finding out the nodes that
are overall close to all other nodes, especially the leaf nodes.

If we view the graph as an area of circle, and the leaf nodes as the peripheral of the
circle, then what we are looking for are actually the centroids of the circle, i.e.,
nodes that is close to all the peripheral nodes (leaf nodes).

Before we proceed, here we make one assertion which is essential to the algorithm.

    - For the tree-alike graph, the number of centroids is no more than 2.

If the nodes form a chain, it is intuitive to see that the above statement holds, which
can be broken into the following two cases:

    - If the number of nodes is even, then there would be two centroids.
    - If the number of nodes is odd, then there would be only one centroid.

Algorithm

Given the above intuition, the problem is now reduced down to looking for all the
centroid nodes in a tree-alike graph, which in addition are no more than two.

The idea is that we trim out the leaf nodes layer by layer, until we reach the core of
the graph, which are the centroids nodes.

Once we trim out the first layer of the leaf nodes (nodes that have only one
connection), some of the non-leaf nodes would become leaf nodes.

The trimming process continues until there are only two nodes left in the graph, which
are the centroids that we are looking for.

The above algorithm resembles the topological sorting algorithm which generates the
order of objects based on their dependencies. For instance, in the scenario of course
scheduling, the courses that have the least dependency would appear first in the order.

In our case, we trim out the leaf nodes first, which are the farther away from the
centroids. At each step, the nodes we trim out are closer to the centroids than the
nodes in the previous step. At the end, the trimming process terminates at the centroids
nodes.

Complexity
==========

Time
----

findMinHeightTrees(n, edges): O(v).

Space
-----

findMinHeightTrees(n, edges): O(v).
"""


def sol(n, edges):
    graph = {i: set() for i in range(n)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    leaf_nodes = [u for u in range(n) if len(graph[u]) <= 1]
    while n > 2:
        n -= len(leaf_nodes)
        new_leaf_nodes = []
        while leaf_nodes:
            u = leaf_nodes.pop()
            v = graph[u].pop()
            graph[v].remove(u)
            if len(graph[v]) == 1:
                new_leaf_nodes.append(v)
        leaf_nodes = new_leaf_nodes
    return leaf_nodes
