"""
22.2 Breadth-first search
=========================

Given a graph G = (V, E) and a distinguished source vertex s, breadth-first search (BFS)
systematically explores the edges of G to "discover" every vertex that is reachable from
s. It computes the distance (smallest number of edges) from s to each reachable vertex.
It also produces a "breadth-first tree" with root s that contains all reachable
vertices. For any vertex v reachable from s, the simple path in the breadth-first tree
from s to v corresponds to a "shortest path" from s to v in G, that is, a path
containing the smallest number of edges. The algorithm works on both directed and
undirected graphs.

Breadth-first search is so named because it expands the frontier between discovered and
undiscovered vertices uniformly across the breadth of the frontier. That is, the
algorithm discovers all vertices at distance k from s before discovering any vertices at
distance k + 1.

To keep track of progress, BFS colors each vertex white, gray, or black. All vertices
start out white and may later become gray and then black. A vertex is discovered the
first time it is encountered during the search, at which time it becomes nonwhite. Gray
and black vertices, therefore, have been discovered, but BFS distinguishes between them
to ensure that the search proceeds in a breadth-first manner. If (u, v) in E and vertex
u is black, then vertex v is either gray or black; that is, all vertices adjacent to
black vertices have been discovered. Gray vertices may have some adjacent white
vertices; they represent the frontier between discovered and undiscovered vertices.

BFS constructs a breadth-first tree, initially containing only its root, which is the
source vertex s. Whenever the search discovers a white vertex v in the course of
scanning the adjacency list of an already discovered vertex u, the vertex v and the edge
(u, v) are added to the tree. We say that u is the predecessor or parent of v in the
breadth-first tree. Since a vertex is discovered at most once, it has at most one
parent.

The algorithm uses a FIFO queue to manage the set of gray vertices. The same result is
obtained if we do not distinguish between gray and black vertices.

The BFS procedure assumes that the input graph G = (V, E) is represented using adjacency
lists. It attaches several additional attributes to each vertex in the graph. We store
the color of each vertex u in V in the attribute u.c and the predecessor of u in the
attribute u.p. If u has no predecessor, then u.p = None. The attribute u.d holds the
distance from the source s to vertex u computed by BFS. The algorithm also uses a FIFO
queue to manage the set of gray vertices.

The while-loop iterates as long as there remain any gray vertices, which are discovered
vertices that have not yet had their adjacency lists fully examined.

The results of BFS may depend upon the order in which the neighbors of a given vertex
are visited; the breadth-first tree may vary, but the distances d computed by the
algorithm will not.

Although BFS could proceed from multiple sources, BFS usually serves to find
shortest-path distances (and the associated predecessor subgraph) from a given source.

Shortest paths
--------------

Let G = (V, E) be a directed or undirected graph, and suppose that BFS is run on G from
a given source vertex s in V. Thus, during its execution, BFS discovers every vertex v
in V that is reachable from the source s, and upon termination, v.d is the shortest path
distance for all v in V. Moreover, for any vertex v != s that is reachable from s, one
of the shortest paths from s to v is a shortest path from s to v.p followed by the edge
(v.p, v).

Intuition
---------

BFS works for undirected or directed graphs with no weights (or unit weights).

Undirected graphs only have tree or cross edges. Directed graphs only have tree, cross,
and back edges.

BFS conducts a level-order traversal of a graph. A queue data structure is used to keep
track of visited vertices during the traversal process. We should select the next point
for exploration from the queue only so that we don't explore a vertex more than once.

In BFS, we can start the initial search from any vertex. When we explore a vertex, we
can visit its adjacent vertices in any order.

However, when we select a vertex for exploration, we must visit all of its adjacent
vertices before further exploration.

BFS also produces the shortest-path distances for an unweighted graph (or, equivalently,
a graph with unit weight edges). We can obtain a shortest path from s to v by taking a
shortest path from s to v.p and then traversing the edge (v.p, v).

The results of BFS may depend upon the order in which the neighbors of a given vertex
are visited: the breadth-first tree may vary, but the distances d computed by the
algorithm will not.

Complexity
==========

After initialization, BFS never whitens a vertex, and thus, each vertex is enqueued at
most once, and hence dequeued as most once. The operations of enqueueing and dequeueing
take O(1) time, and so the total time devoted to queue operations is O(V). Because the
procedure scans the adjacency list of each vertex only when the vertex is dequeued, it
scans each adjacency list at most once. Since the sum of the lengths of all the
adjacency lists is Theta(E), the total time spent in scanning adjacency lists is O(E).
The overhead for initialization is O(V), and thus the total running time of the BFS
procedure is O(V + E). Thus, BFS search runs in time linear in the size of the
adjacency-list representation of G.

Time
----

bfs(): O(V + E).
"""

# Repository Library
from src.clrs.data_structures.elementary_data_structures.queue import Queue
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph


class BFS(Graph):
    def bfs(self, s):
        self.init_single_source(s)
        q = Queue(self.num_vertices)
        q.enqueue(s)
        while not q.empty():
            u = q.dequeue()
            u_node, v = self.vertices[u], self.adj_list[u].head
            while v is not None:
                v_node = self.vertices[v.k]
                if v_node.c == 0:
                    v_node.c, v_node.d, v_node.p = 1, u_node.d + 1, u_node
                    q.enqueue(v.k)
                if v_node.d == u_node.d + 1:
                    self.edge_types[(u, v.k)] = "T"
                if v_node.d == u_node.d:
                    self.edge_types[(u, v.k)] = "C"
                if self.directed and 0 <= v_node.d <= u_node.d:
                    self.edge_types[(u, v.k)] = "B"
                v = v.next
