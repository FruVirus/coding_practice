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
edge of least possible weight. The edge that is added must NOT form a cycle in the MST.

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

Intuition
---------

Kruskal's algorithm works for a connected, undirected graph with weights.

A spanning tree is a subgraph of a graph that is acyclic and connects all of the
vertices using exactly |V| - 1 edges while minimizing the total weight of the edges.

The brute force approach to finding a MST is to try all combination of |V| - 1 edges and
check each total weight. However, we can also use a greedy algorithm to find the MST
without having to iterate over all possible combinations.

In Kruskal's algorithm, the set A is a forest whose starting vertices are all of the
graph vertices; i.e., each vertex is a tree. We then apply a greedy approach by adding
an edge to A if it is a least-weight edge AND the newly added edge will connect two
distinct components (i.e., not form a cycle).

Kruskal's algorithm works as follows:

1. From a weighted graph, select the minimum cost edge first.
2. Then, always select the minimum cost edge next unless that edge will create a cycle.

For a disconnected graph, Kruskal's algorithm will NOT find the MST for the overall
graph but it MIGHT find the MST for EACH component.

Two vertices A and B start off as separate trees. Since they are not the same component,
they are joined together to form the same component. Afterwards, if one of the two
vertices is encountered again, it will not be added to the minimum spanning tree if it
belongs to an existing component already.

Complexity
==========

Kruskal's algorithm selects a minimum weight edge out of the set of edges |E| and it has
to do this selection |V| - 1 times. Thus, its running time is O(|V| * |E|). However,
Kruskal's algorithm can be improved by keeping edges in a min-heap data structure.
Deletion from a min-heap is O(lg n) and min-heaps always return the minimum value in
constant time.

Thus, by using min-heaps, Kruskal's algorithm can be O(E * lg V).

By using a disjoint-set data structure, the running time of Kruskal's algorithm is still
O(E * lg V).

Time
----

kruskal(): O(E * lg V) if |E| < |V|^2 else O(E * lg E).
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class Kruskal(Graph):
    def kruskal(self):
        mst = set()
        self.make_set()
        for u, v in dict(sorted(self.weights.items(), key=lambda x: x[1])):
            if not self.same_component(u, v):
                mst.add((u, v))
                self.union(self.vertices[u], self.vertices[v])
        return mst
