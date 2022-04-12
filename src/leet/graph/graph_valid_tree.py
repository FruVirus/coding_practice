"""
Graph Valid Tree
----------------

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a
list of edges where edges[i] = [a_i, b_i] indicates that there is an undirected edge
between nodes a_i and b_i in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

According to the definition of tree on Wikipedia: “a tree is an undirected graph in
which any two vertices are connected by exactly one path. In other words, any connected
graph without simple cycles is a tree.”

Complexity
==========

Time
----

validTree(n, edges): O(n), where n is the number of nodes.

Space
-----

validTree(n, edges): O(n).
"""


class DisjointSet:
    def __init__(self, size):
        self.count, self.rank, self.root = size, [1] * size, list(range(size))

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def get_count(self):
        return self.count

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                if self.rank[rootx] == self.rank[rooty]:
                    self.rank[rooty] += 1
            self.count -= 1


def sol(n, edges):
    if len(edges) != n - 1:
        return False
    dset = DisjointSet(n)
    for u, v in edges:
        if dset.connected(u, v):
            return False
        dset.union(u, v)
    return True
