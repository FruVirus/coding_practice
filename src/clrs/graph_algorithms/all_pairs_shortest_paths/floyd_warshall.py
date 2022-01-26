"""
25.2 The Floyd-Warshall algorithm
=================================

Floyd-Warshall assumes that we have a weighted, directed graph with negative-weight
edges but no negative-weight cycles.

The structure of a shortest path
--------------------------------

The Floyd-Warshall algorithm considers the intermediate vertices of a shortest path,
where an intermediate vertex of a simple path p = <v_1, v_2, ..., v_l> is any vertex of
p other than v_1 or v_l, that is, any vertex in the set {v_2, v_3, ..., v_(l - 1)}.

The Floyd-Warshall algorithm exploits a relationship between path p and shortest paths
from i to j with all intermediate vertices in the set {1, 2, ..., k - 1}. The
relationship depends on whether or not k is an intermediate vertex of p.

- If k is not an intermediate vertex of path p, then all intermediate vertices of path p
are in the set {1, 2, ..., k - 1}. Thus, a shortest path from vertex i to vertex j with
all intermediate vertices in the set {1, 2, ..., k - 1} is also a shortest path from i
to j with all intermediate vertices in the set {1, 2, ..., k}.

- If k is an intermediate vertex of path p, then we decompose p into
i -p_1-> k -p_2-> j. p_1 is a shortest path from i to k with all intermediate vertices
in the set {1, 2, ..., k} . Similarly, p_2 is a shortest path from vertex k to vertex j
with all intermediate vertices in the set(1, 2, ..., k}.

A recursive solution to the all-pairs shortest-paths problem
------------------------------------------------------------

Let d_ij^(k) be the weight of a shortest path from vertex i to vertex j for which all
intermediate vertices are in the set {1, 2, ..., k}. When k = 0, a path from vertex i
to vertex j with no intermediate vertex numbered higher than 0 has no intermediate
vertices at all. Such a path has at most one edge, and hence d_ij^(0) = w_ij. We define
d_ij^(k) recursively by

d_ij^(k) =  w_ij                                            if k = 0,
            min(d_ij^(k - 1), d_ik^(k - 1) + d_kj^(k - 1))  if k >= 1.

Because for any path, all intermediate vertices are in teh set {1, 2, ..., n}, the
matrix d^(n) = (d_ij^(n)) gives the final answer: d_ij^(n) = delta(i, j) for all
i, j in V.

Constructing a shortest path
----------------------------

There are a variety of different methods for constructing a shortest paths in the
Floyd-Warshall algorithm.

We can compute the predecessor matrix pi while the algorithm computes the matrices d.
Specifically, we compute a sequence of matrices pi^(0), pi^(1), ..., pi^(n), where
pi = pi^(n) and we define pi_ij^(k) as the predecessor of vertex j on a shortest path
from vertex i with all intermediate vertices in the set {1, 2, ..., k}.

When k = 0, a shortest path from i to j has no intermediate vertices at all (since there
is just a single edge connecting i to j and thus, i is a direct predecessor of j). Thus,

pi_ij^(0)   = None  if i = j or w_ij = float("inf")
            = i     if i != j and w_ij < float("inf")

For k >= 1, if we take the path i -> k -> j, where k != j, then the predecessor of j we
choose is the same as the predecessor of j we chose on a shortest path from k with all
intermediate vertices in the set {1, 2, ..., k - 1}. Otherwise, we choose the same
predecessor of j that we chose on a shortest path from i with all intermediate vertices
in the set {1, 2, ..., k - 1}. In other words, for k >= 1, the predecessor of j is
either the predecessor of j that was chosen on a shortest path from i to j without k,
or the predecessor of j that was chosen on a shortest path from i to j with k as an
intermediate vertex.

Intuition
---------

For any two vertices i and j in G, the shortest path from i to j is either the direct
path from i to j (i.e., no intermediate vertex at all) or some path i -> k -> j where
k is an intermediate vertex also in G. Thus, if w(i, j) <= w(i, k) + w(k, j), then the
direct path from i to j is the shorter one; otherwise, the path that includes k is the
shorter one. We then iterate over all possible k values (i.e., all vertices) to compute
the shortest paths for all pairs. For each k, we use the d matrix computed from the
previous iteration since we do not have to repeat those calculations again. In other
words, once we compute the shorter path between i and j with an intermediate vertex k,
that calculation can be used for other vertices k.

Row i of the d matrix is the solution to the single-source shortest-paths from vertex i.

Element (i, j) of the pi matrix gives the predecessor of j on some shortest path from i.
The subgraph induced by the i-th row of the pi matrix should be a shortest-paths tree
with root i. For example, pi(4, 5) = 1 means the shortest path between 4 and 5 is
4 -> 1 -> 5 so that 1 is the predecessor of 5; then (4, 1) = 4 means the shortest path
between 4 and 1 is 4 -> 1 so that 4 is the predecessor of 1. In this manner, we can
print the shortest paths between 4 and 5 using the pi matrix.

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

floyd_warshall(): Theta(V^3).
print_path(): Linear in the number of vertices in the path printed since each recursive
call is for a path one vertex shorter.

Space
-----

floyd_warshall(): O(V^2) for d matrix.
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class FloydWarshall(Graph):
    def floyd_warshall(self):
        assert self.directed
        self.pred = [[None] * self.num_vertices for _ in range(self.num_vertices)]
        d = [[float("inf")] * self.num_vertices for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i == j:
                    d[i][j] = 0
        for (u, v), w in self.weights.items():
            self.pred[u][v], d[u][v] = u, w
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    if d[i][j] > d[i][k] + d[k][j]:
                        self.pred[i][j] = self.pred[k][j]
                        d[i][j] = d[i][k] + d[k][j]
        return d

    def print_path(self, s, v):
        s, v = self.vertices[s], self.vertices[v]
        if v is s:
            print(s.k)
        elif self.pred[s.k][v.k] is None:
            print("No path!")
            exit(0)
        else:
            self.print_path(s.k, self.pred[s.k][v.k])
            print(v.k)
