"""
Overview
========

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

Let G = (V, E) be a directed or undirected graph, and suppose that BFS is run on G from
a given source vertex s in V. Thus, during its execution, BFS discovers every vertex v
in V that is reachable from the source s, and upon termination, v.d is the shortest path
distance for all v in V. Moreover, for any vertex v != s that is reachable from s, one
of the shortest paths from s to v is a shortest path from s to v.p followed by the edge
(v.p, v).

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

bfs(): O(V + E)
print_path(): Linear in the number of vertices in the path printed since each recursive
call is for a path one vertex shorter.

Space
-----

Adjacency list: Theta(V + E)
Adjacency matrix: Theta(V^2)
"""

# pylint: disable=R1722

# Repository Library
from src.clrs.lists.singly_linked_list import SLL, Node
from src.clrs.queues.queue import Queue


class Graph:
    def __init__(self, num_vertices, is_dag=False):
        self.num_vertices = num_vertices
        self.is_dag = is_dag
        self.adj_list = [SLL() for _ in range(self.num_vertices)]
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        self.queue = Queue(self.num_vertices)
        self.vertices = {}

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].insert(self.vertices[v])
        self.adj_matrix[u][v] = 1
        if not self.is_dag:
            self.adj_list[v].insert(self.vertices[u])
            self.adj_matrix[v][u] = 1

    def add_vertex(self, v):
        self.vertices[v] = Node(v)

    def bfs(self, s):
        for k, v in self.vertices.items():
            v.c, v.d, v.p = (0, float("inf"), None) if k != s else (1, 0, None)
        self.queue.enqueue(s)
        while not self.queue.empty():
            u = self.queue.dequeue()
            u_node = self.vertices[u]
            v = self.adj_list[u].head
            while v is not None:
                v_node = self.vertices[v.k]
                if v_node.c == 0:
                    v_node.c, v_node.d, v_node.p = 1, u_node.d + 1, u_node
                    self.queue.enqueue(v.k)
                v = v.next

    def print_path(self, s, v):
        s, v = self.vertices[s], self.vertices[v]
        if v is s:
            print(s.k)
        elif v.p is None:
            print("No path")
            exit(0)
        else:
            self.print_path(s.k, v.p.k)
            print(v.k)
