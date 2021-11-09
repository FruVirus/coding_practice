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

# Standard Library
from operator import gt, lt

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class HeapQueue:
    def __init__(self, a, is_max):
        self.a = a
        self.heap_size = len(self.a)
        self.is_max = is_max
        self.compare = gt if self.is_max else lt
        self.build()

    def _exchange(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _right(i):
        return 2 * i + 2

    def build(self):
        for i in range(len(self.a) // 2 - 1, -1, -1):
            self.heapify(i)

    def change(self, i, k):
        assert self.compare(k, self.a[i])
        self.a[i] = k
        while i > 0 and self.compare(self.a[i], self.a[self._parent(i)]):
            self._exchange(i, self._parent(i))
            i = self._parent(i)

    def extract(self):
        assert self.heap_size > 0
        self.heap_size -= 1
        x = self.a[0]
        self.a[0] = self.a[self.heap_size]
        self.heapify(0)
        self.a.pop(-1)
        return x

    def get(self):
        return self.a[0]

    def heapify(self, i):
        l, r, index = self._left(i), self._right(i), i
        if l < self.heap_size and self.compare(self.a[l], self.a[i]):
            index = l
        if r < self.heap_size and self.compare(self.a[r], self.a[index]):
            index = r
        if index != i:
            self._exchange(i, index)
            self.heapify(index)

    def insert(self, k):
        self.a.append(-float("inf") if self.is_max else float("inf"))
        self.change(self.heap_size, k)
        self.heap_size += 1


class MST(Graph):
    def prim(self):
        root, mst = 0, set()
        for v in self.vertices.values():
            v.key, v.p = float("inf"), None
        self.vertices[root].key = 0
        q = HeapQueue([(v.k, v.key) for v in self.vertices.values()], False)
        while q.heap_size != 0:
            u = q.extract()
            u_node, v = self.vertices[u[0]], self.adj_list[u[0]].head
            while v is not None:
                v_node = self.vertices[v.k]
                if (v_node.k, v_node.key) in q.a and self.weights[
                    (u[0], v_node.k)
                ] < v_node.key:
                    v_node.p = u_node
                    x = q.a.index((v_node.k, v_node.key))
                    v_node.key = self.weights[(u[0], v.k)]
                    q.change(x, (v_node.k, v_node.key))
                v = v.next
            print(q.a)
        for v in [v for k, v in self.vertices.items() if k != root]:
            mst.add((v.p.k, v.k))
        return mst


num_vertices = 4
graph = MST(num_vertices)
graph.add_edge(2, 3, 7)
graph.add_edge(1, 3, 4)
graph.add_edge(0, 2, 8)
graph.add_edge(0, 1, 9)

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
