"""
24.3 Dijkstra's algorithm
=========================

Dijkstra's algorithm solves the single-source shortest-paths problem on a weighted,
directed graph G = (V, E) for the case in which all edge weights are non-negative. With
a good implementation, the running time of Dijkstra's algorithm is lower than that of
the Bellman-Ford algorithm.

Dijkstra's algorithm maintains a set S of vertices whose final shortest-path weights
from the source s have already been determined. The algorithm repeatedly selects the
vertex u in V - S with the minimum shortest-path estimate, adds u to S, and relaxes all
edges leaving u. In the following implementation, we use a min-priority queue Q of
vertices, keyed by their d values.

Each time the outer while-loop executes, a vertex u is extracted from Q = V - S and is
added to set S. Vertex u, therefore, has the smallest shortest-path estimate of any
vertex in V - S. The inner while-loop relaxes each edge (u, v) leaving u, thus updating
the estimate v.d and the predecessor v.p if we can improve the shortest path to v found
so far by going through u. Observe that the algorithm never inserts vertices into Q
after initialization and that each vertex is extracted from Q and added to S exactly
once, so that the outer while-loop iterates exactly |V| times.

Because Dijkstra's algorithm always chooses the "lightest" or "closest" vertex in V - S
to add to set S, we say that is uses a greedy strategy. Greedy strategies do not always
yield optimal results in general, but Dijkstra's algorithm does indeed compute shortest
paths.

Dijkstra's algorithm resembles both BFS and Prim's algorithm for MSTs. It is like BFS in
that set S corresponds to a set of black vertices in a breadth-first search; just as
vertices in S have their final shortest-path weights, so do black vertices in a
breadth-first search have their correct breadth-first distances. Dijkstra's algorithm is
like Prim's algorithm in that both algorithms use a min-priority queue to find the
"lightest" vertex outside a given set (the set S in Dijkstra's algorithm and the tree
being grown in Prim's algorithm), add this vertex into the set, and adjust the weights
of the remaining vertices outside the set accordingly.

Complexity
==========

Dijkstra's algorithm maintains the min-priority queue Q by calling three priority-queue
operations: insert(), extract(), and change(). The algorithm calls both insert() and
extract() once per vertex. Because each vertex u in V is added to set S exactly once,
each edge in the adjacency list is examined in the inner while-loop exactly once during
the course of the algorithm. Since the total number of edges in all the adjacency lists
is |E|, the inner while-loop iterates a total of |E| times, and thus the algorithm
calls change() at most |E| times overall.

If we maintain the min-priority queue by taking advantage of the vertices being numbered
1 to |V|, we can simply store v.d in the v-th entry of an array. Each insert() and
change() operation would then take O(1) time, and each extract() operation takes O(V)
time (since we have to search through the entire array), for a total time of
O(V^2 + E) = O(V^2).

If the graph is sufficiently sparse, we can improve the algorithm by implementing the
min-priority queue with a binary min-heap. Each extract() operation then takes time
O(lg(V)). As before, there are |V| such operations. The time to build the binary
min-heap is O(V). Each change() operation takes time O(lg(V)), and there are still at
most |E| such operations. The total running time is O((V + E) * lg(V)), which is
O(E * lg(V)) if all vertices are reachable from the source.

Time
----

dijkstra(): O(E * lg(V))
"""

# Repository Library
from src.clrs.data_structures.elementary_data_structures.heap_queue import HeapQueue
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class Dijkstra(Graph):
    def dijkstra(self, s):
        self.init_single_source(s)
        q = HeapQueue([(v.d, v.k) for v in self.vertices.values()], False)
        while q.heap_size != 0:
            u = q.extract()
            u_node, v = self.vertices[u[1]], self.adj_list[u[1]].head
            while v is not None:
                v_node = self.vertices[v.k]
                old_d = v_node.d
                self.relax(u_node, v_node)
                if v_node.d != old_d:
                    i = q.a[: q.heap_size].index((old_d, v.k))
                    q.change(i, (v_node.d, v.k))
                v = v.next
