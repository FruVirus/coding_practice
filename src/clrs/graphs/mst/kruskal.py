"""
23.2 The algorithms of Kruskal and Prim
=======================================

Kruskal's algorithm
-------------------

In Kruskal's algorithm, the set A is a forest whose vertices are all those of the given
graph. The safe edge added to A is always a least-weight edge in the graph that connects
two distinct components without forming a cycle.

Kruskal's algorithm finds a safe edge to add to the growing forest by finding, of all
the edges that connect any two trees in the forest, an edge (u, v) of least weight. The
algorithm qualifies as a greedy algorithm because at each step it adds to the forest an
edge of least possible weight. The edge that is adds must NOT form a cycle in the MST.

For disconnected graphs, Kruskal's algorithm will not find the MST for the overall
graph. However, it might find the MST for each disconnected component.

Our implementation uses a disjoint-set data structure to maintain several disjoint sets
of elements. Each set contains the vertices in one tree of the current forest. The
operation find_set(u) returns a representative element from the set that contains u.
Thus, we can determine whether two vertices u and v belong to the same tree by testing
whether find_set(u) equals find_set(v). To combine trees, we use union().

The main for-loop in kruskal() examines edges in order of increasing edge weight. The
loop checks, for each edge (u, v), whether the endpoints u and v belong to the same
tree. If they do, then the edge (u, v) cannot be added to the forest without creating a
cycle, and the edge is discarded. Otherwise, the two vertices belong to different trees.
In this case, the edge (u, v) is added to A and the vertices in the two trees are merged
together in the final MST.

Complexity
==========

Kruskal's algorithm selects a minimum weight edge out of the set of edges |E| and it has
to do this selection |V| - 1 times. Thus, its running time is O(|V| * |E|). However,
Kruskal's algorithm can be improved by keeping edges in a min-heap data structure.
Deletion from a min-heap if O(lg(n)) and min-heaps always return the minimum value in
constant time.

Thus, by using min-heaps, Kruskal's algorithm can be O(E * lg(V)).

By using a disjoint-set data structure, the running time of Kruskal's algorithm is still
O(E * lg(V)).

Time
----

kruskal(): O(E * lg(V))
"""

# Repository Library
from src.clrs.graphs.elementary_graph_algorithms.graph import Graph


class MST(Graph):
    def kruskal(self):
        mst = set()
        self.make_set()
        for edge in dict(sorted(self.weights.items(), key=lambda x: x[1])):
            u, v = self.vertices[edge[0]], self.vertices[edge[1]]
            if self.find_set(u) != self.find_set(v):
                mst.add(edge)
                self.union(u, v)
        return mst
