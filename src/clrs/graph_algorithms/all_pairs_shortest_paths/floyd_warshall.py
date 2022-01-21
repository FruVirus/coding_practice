"""
25.2 The Floyd-Warshall algorithm
=================================

XXX

Intuition
---------

Row i of the d matrix is the solution to the single-source shortest-paths from vertex i.

We can do one of two things to detect the presence of negative-weight cycles using the
Floyd-Warshall algorithm:

1. Run the normal Floyd-Warshall algorithm one extra iteration using the d matrix
calculated from the initial run to see if any of the d values change. If there are
negative-weight cycles, then some shortest-path costs will be lower. If there are no
such negative-weight cycles, then no d values will change because the algorithm gives
the correct shortest-path costs.

2. Check the main diagonal entries of the d matrix for a negative value. There is a
negative-weight cycle iff a main diagonal entry is < 0 for some vertex i. Since d[i][i]
is a path weight from i to itself, if it is negative, then this means that there is a
path from i to itself (i.e., a cycle) with negative weight. Note that the values in the
d matrix never increase during the Floyd-Warshall algorithm. Initially, the values are
either 0 along the main diagonal. Each iteration sets a value in the d matrix whose
minimum value is always non-negative.

Complexity
==========

The Floyd-Warshall algorithm implemented here first needs to initialize the d matrix
corresponding to the identity matrix for shortest paths (i.e., 0 along the main diagonal
and float("inf") elsewhere). Then, it sets its elements corresponding to the edge
weights in the graph. Initializing the d matrix takes O(V^2) time. Setting the elements
in d matrix corresponding to the edge weights takes O(V^2) in the worst case for a dense
graph. Thus, these two steps take O(V^2 + V^2) time. Since the main Floyd-Warshall
algorithm takes O(V^3) time, the overall procedure still takes O(V^3) time.

Time
----

floyd_warshall(): O(V^3).

Space
-----

floyd_warshall(): O(V^2) for d matrix.
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class FloydWarshall(Graph):
    def floyd_warshall(self):
        assert self.directed
        d = [[float("inf")] * self.num_vertices for _ in range(self.num_vertices)]
        for r in range(self.num_vertices):
            for c in range(self.num_vertices):
                if r == c:
                    d[r][c] = 0
        for (u, v), w in self.weights.items():
            d[u][v] = w
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d
