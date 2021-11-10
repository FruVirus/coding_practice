"""
23.2 The algorithms of Kruskal and Prim
=======================================

Prim's algorithm
----------------

Prim's algorithm has the property that the edges in the set A always form a single tree.
The tree starts from an arbitrary root vertex r and grows until the tree spans all the
vertices in V. Each step adds to the tree A a light edge that connects A to an isolated
vertex---one on which no edge of A is incident (i.e., it will not form a cycle). This
strategy qualifies as greedy since at each step it adds to the tree an edge that
contributes the minimum amount possible to the tree's weight.

In order to implement Prim's algorithm efficiently, we need a fast way to select a new
edge to add to the tree formed by the edges in A. During execution of the algorithm, all
vertices that are not in the tree reside in a min-priority queue Q based on a key
attribute. For each vertex v, the attribute v.key is the minimum weight of any edge
connecting v to a vertex in the tree; by convention v.key = float("inf") if there is no
such edge.

At each step of the algorithm, the vertices in the tree determine a cut of the graph,
and a light edge crossing the cut is added to the tree.

Complexity
==========

The running time of Prim's algorithm depends on how we implement the min-priority queue.
If we implement the queue as a binary min-heap, we can build the heap in O(V) time. The
main while-loop executes |V| times, and since each extract() operation takes O(lg(V))
time, the total time for all calls to extract() is (V * lg(V)). The inner while-loop
executes O(E) times altogether, since the sum of the lengths of all adjacency lists is
2 |E|. Within the inner while-loop, we can implement the test for membership in the
queue in constant time by keeping a bit for each vertex that tells whether or not it is
in the queue, and updating the bit when the vertex is removed from the queue. The
change() operation takes O(lg(V)) time. Thus, the total time for Prim's algorithm is
O(V * lg(V) + E * lg(V)) = O(E * lg(V)), which is asymptotically the same as Kruskal's
algorithm.

Time
----

prim(): O(E * lg(V))
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph
from src.clrs.queues.heap_queue import HeapQueue


class MST(Graph):
    def prim(self):
        root, mst = 0, set()
        for v in self.vertices.values():
            v.key, v.p, v.bit = float("inf"), None, 0
        self.vertices[root].key = 0
        q = HeapQueue([(v.key, v.k) for v in self.vertices.values()], False)
        while q.heap_size != 0:
            u = q.extract()
            u_node, v = self.vertices[u[1]], self.adj_list[u[1]].head
            while v is not None:
                if v.bit == 0 and self.weights[(u[1], v.k)] < v.key:
                    v.p, i = u_node, q.a.index((v.key, v.k))
                    v.key = self.weights[(u[1], v.k)]
                    q.change(i, (v.key, v.k))
                v.bit, v = 1, v.next
        for v in [v for k, v in self.vertices.items() if k != root]:
            mst.add((v.k, v.p.k))
        return mst


num_vertices = 4
graph = MST(num_vertices)
graph.add_edge(2, 3, 7)
graph.add_edge(1, 3, 4)
graph.add_edge(0, 2, 8)
graph.add_edge(0, 1, 4)

# graph.add_edge(1, 2, 8)
# graph.add_edge(1, 7, 11)
# graph.add_edge(2, 3, 7)
# graph.add_edge(2, 5, 4)
# graph.add_edge(2, 8, 2)
# graph.add_edge(3, 4, 9)
# graph.add_edge(3, 5, 14)
# graph.add_edge(4, 5, 10)
# graph.add_edge(5, 6, 2)
# graph.add_edge(6, 7, 1)
# graph.add_edge(6, 8, 6)
# graph.add_edge(7, 8, 7)
mst = graph.prim()
print(mst)
# assert mst == {(0, 1), (1, 2), (3, 4), (2, 3), (6, 7), (5, 6), (2, 5), (2, 8)}
assert len(mst) == num_vertices - 1
