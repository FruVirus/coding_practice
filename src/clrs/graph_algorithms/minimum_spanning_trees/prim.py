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


class Prim(Graph):
    def prim(self):
        root, mst = 0, set()
        for v in self.vertices.values():
            v.key, v.p = float("inf"), None
        self.vertices[root].key = 0
        q = HeapQueue([(v.key, v.k) for v in self.vertices.values()], False)
        while q.heap_size != 0:
            u = q.extract()
            u_node, v = self.vertices[u[1]], self.adj_list[u[1]].head
            while v is not None:
                v_node = self.vertices[v.k]
                if (v_node.key, v.k) in q.a and self.weights[(u[1], v.k)] < v_node.key:
                    v_node.p, i = u_node, q.a.index((v_node.key, v.k))
                    v_node.key = self.weights[(u[1], v.k)]
                    q.change(i, (v_node.key, v.k))
                v = v.next
        for v in self.vertices.values():
            if v.p is not None:
                mst.add((v.k, v.p.k))
        return mst
