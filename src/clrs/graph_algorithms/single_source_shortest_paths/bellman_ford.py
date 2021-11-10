"""
24.1 The Bellman-Ford algorithm
===============================

Complexity
==========

XXX

Time
----

sssp(): XXX
init_single_source(): Theta(V)
relax(): O(1)
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class BellmanFord(Graph):
    def init_single_source(self, s):
        for v in self.vertices.values():
            v.d, v.p = float("inf"), None
        self.vertices[s].d = 0

    def relax(self, u, v):
        w = self.weights[(u, v)]
        u, v = self.vertices[u], self.vertices[v]
        if v.d > u.d + w:
            v.d, v.p = u.d + w, u
