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

XXX

Time
----

prim(): XXX
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph
from src.clrs.queues.heap_queue import HeapQueue


class MST(Graph):
    def prim(self):
        root, mst = 0, set()
        for v in self.vertices.values():
            v.key, v.p = float("inf"), None
        self.vertices[root].key = 0
        fru = [x for x in self.vertices.keys()]
        poo = [x.key for x in self.vertices.values()]
        print(fru)
        print(poo)
        q = HeapQueue(poo, False)
        index = 0
        while q.heap_size != 0:
            u = q.extract()
            u = fru[index]
            index += 1
            print(u)
        #     u_node, v = self.vertices[u], self.adj_list[u].head
        #     while v is not None:
        #         v_node = self.vertices[v.k]
        #         print(v_node.k)
        #         if v.k in q.a and self.weights[(u, v.k)] < v_node.key:
        #             v_node.key, v_node.p = self.weights[(u, v.k)], u_node
        #         v = v.next
        # for v in [v for k, v in self.vertices.items() if k != root]:
        #     mst.add((v.p.k, v.k))
        return mst


num_vertices = 9
graph = MST(num_vertices)
graph.add_edge(0, 1, 9)
graph.add_edge(0, 7, 8)
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
# assert len(mst) == num_vertices - 1
