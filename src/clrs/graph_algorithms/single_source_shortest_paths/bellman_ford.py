"""
24.1 The Bellman-Ford algorithm
===============================

The Bellman-Ford algorithm solves the single-source shortest-paths problem in the
general case in which edge weights may be negative. Given a weighted, directed graph
G = (V, E) with source s and weight function w: E -> R, the Bellman-Ford algorithm
returns a boolean value indicating whether or not there is a negative-weight cycle that
is reachable from the source. If there is such a cycle, the algorithm indicates that no
solution exists. If there is no such cycle, the algorithm produces the shortest paths
and their weights.

The algorithm relaxes edges, progressively decreasing an estimate v.d on the weight of a
shortest path from the source s to each vertex v in V until it achieves the actual
shortest-path weight delta(s, v). The algorithm return True iff the graph contains no
negative-weight cycles that are reachable from the source.

Each pass is one iteration of the first for-loop and consists of relaxing each edge of
the graph once. After making |V| - 1 passes, the second for-loop checks for a
negative-weight cycle and returns the appropriate boolean value.

After calling bellman_ford(), calling print_path(s, v) will print the shortest path
between the source s and a given vertex v in the graph.

Corollary 24.3
--------------

Let G = (V, E) be a weighted, directed graph with source vertex s and weight function
w: E -> R. Then, for each vertex v in V, there is a path from s to v iff the
Bellman-Ford algorithm terminates with v.d < float("inf") when it is run on G. This
corollary allows G to have negative-weight cycles that are reachable from s.

Complexity
==========

The Bellman-Ford algorithm runs in time O(|V| * |E|), since the initialization takes
Theta(V) time, each of the |V| - 1 passes over the edges take Theta(E) time, and the
second for-loop takes O(E) time.

For complete graphs, |E| = |V| * (|V| - 1) / 2 and so Bellman-Ford can take O(|V|^3)
time.

Time
----

bellman_ford(): O(|V| * |E|), O(|V|^3) for complete graphs
init_single_source(): Theta(|V|)
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
        w = self.weights[(u.k, v.k)]
        if v.d > u.d + w:
            v.d, v.p = u.d + w, u

    def bellman_ford(self, s):
        self.init_single_source(s)
        for _ in range(len(self.vertices) - 1):
            for edge in self.edges:
                self.relax(self.vertices[edge[0]], self.vertices[edge[1]])
        for edge in self.edges:
            u, v = self.vertices[edge[0]], self.vertices[edge[1]]
            if v.d > u.d + self.weights[(u.k, v.k)]:
                return False
        return True
