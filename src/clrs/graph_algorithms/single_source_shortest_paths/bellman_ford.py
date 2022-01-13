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

Intuition
---------

Bellman-Ford algorithm operates on weighted, directed graphs with positive and negative
weights. The algorithm repeatedly relaxes all edges for |V| - 1 times each.

The algorithm starts from a given (arbitrary) node. If we start with a poor edge choice,
then Bellman-Ford can take more iterations.

Bellman-Ford can detect a negative weight cycle by doing an additional iteration at the
end and seeing if anything relaxes again. If there are negative weights but no negative
weight cycles, Bellman-Ford will still give the correct shortest path answer.

Complexity
==========

The Bellman-Ford algorithm runs in time O(|V| * |E|), since the initialization takes
Theta(V) time, each of the |V| - 1 passes over the edges take Theta(E) time, and the
second for-loop takes O(E) time.

For complete graphs, |E| = |V| * (|V| - 1) / 2 and so Bellman-Ford can take O(|V|^3)
time.

Time
----

bellman_ford(): O(V * E), O(V^3) for complete graphs.
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class BellmanFord(Graph):
    def bellman_ford(self, s):
        assert self.directed
        self.init_single_source(s)
        for _ in range(self.num_vertices - 1):
            for u, v in self.edges:
                self.relax(self.vertices[u], self.vertices[v])
        for u, v in self.edges:
            u, v = self.vertices[u], self.vertices[v]
            if v.d > u.d + self.weights[(u.k, v.k)]:
                return False
        return True
