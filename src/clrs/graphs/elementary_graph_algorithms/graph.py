"""
22.1 Representation of Graphs
=============================

A graph consists of vertices V and edges E that connect its vertices.

Searching a graph means systematically following the edges of the graph so as to visit
the vertices of the graph. A graph-searching algorithm can discover much about the
structure of a graph.

We can choose between two standard ways to represent a graph G = (V, E): as a collection
of adjacency lists or as an adjacency matrix. Either way applies to both directed and
undirected graphs. Because the adjacency -list representation provides a compact way to
represent sparse graphs---those for which |E| is much less than |V|^2---it is usually
the method of choice. We may prefer an adjacency matrix representation, however, when
the graph is dense---|E| is close to |V|^2---or when we need to be able to tell quickly
if there is an edge connecting two given vertices.

The adjacency-list representation of a graph G = (V, E) consists of an array Adj of |V|
lists, one for each vertex in V. For each u in V, the adjacency list Adj[u] contains all
the vertices v such that there is an edge (u, v) in E. That is, Adj[u] contains all of
the vertices adjacent to u in G.

If G is a directed graph, the sum of the lengths of all the adjacency lists is |E|. If G
is an undirected graph, the sum of the lengths of all the adjacency lists is 2|E|. For
both directed and undirected graphs, the adjacency-list representation has the desirable
property that the amount of memory it requires it Theta(V + E).

A potential disadvantage of the adjacency-list representation is that it provides no
quicker way to determine whether a given edge (u, v) is present in the graph than to
search for v in the adjacency list Adj[u]. An adjacency-matrix representation of the
graph remedies this disadvantage, but at the cost of using asymptotically more memory.

For the adjacency-matrix representation of a graph G = (V, E), we assume that the
vertices are numbered 1, 2, ..., |V| in some arbitrary manner. Then the adjacency-matrix
representation of a graph G consists of a |V| x |V| matrix A = (a_ij) such that a_ij = 1
if (i, j) in E, else 0. The adjacency-matrix representation of a graph requires
Theta(V^2)  memory, independent of the number of edges in the graph.

Since in an undirected graph, (u, v) and (v, u) represent the same edge, the
adjacency-matrix A of an undirected graph is its own transpose: A = A.T. In some
applications, it pays to store only the entries on and above the diagonal of the
adjacency matrix, thereby cutting the memory needed to store the graph almost in half.

Although the adjacency-list representation is asymptotically at least as space-efficient
as the adjacency-matrix representation, adjacency matrices are simpler, and so we may
prefer them when graphs are reasonably small. Moreover, adjacency matrices carry a
further advantage for unweighted graphs: they require only one bit per entry.

Graphs can also be weighted. The graph edges can each have an associated weight,
typically given by a weight function. We simply store the weight w(u, v) of the edge
(u, v) in E with vertex v in u's adjacency list. An adjacency matrix can represent a
weighted graph as well by simply storing the weight w(u, v) of the edge (u, v) in E as
the entry in row u and column v of the adjacency matrix.

Transpose of Graph
------------------

The transpose of a directed graph G = (V, E) is the graph G.T = (V, E.T), where the
direction of the edges are reversed. Given an adjacency-list representation of G, the
time to create G.T is O(V + E). Given an adjacency-matrix representation of G, the time
to create G.T is O(V^2).

Complexity
==========

Time
----

Adjacency list transpose: O(V + E)
Adjacency matrix transpose: O(V^2)

Space
-----

Adjacency list: Theta(V + E)
Adjacency matrix: Theta(V^2)
"""

# pylint: disable=R1722

# Repository Library
from src.clrs.lists.singly_linked_list import SLL, Node


class Graph:
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.adj_list = [SLL() for _ in range(self.num_vertices)]
        self.adj_list_transpose = [SLL() for _ in range(self.num_vertices)]
        self.adj_matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        self.adj_matrix_transpose = [
            [0] * self.num_vertices for _ in range(self.num_vertices)
        ]
        self.directed = directed
        self.is_dag = True
        self.vertices = {}

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].insert(self.vertices[v])
        self.adj_matrix[u][v] = 1
        if not self.directed:
            self.adj_list[v].insert(self.vertices[u])
            self.adj_matrix[v][u] = 1

    def add_vertex(self, v):
        self.vertices[v] = Node(v)

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

    def transpose(self):
        assert self.directed
        for u in self.vertices:
            v = self.adj_list[u].head
            while v is not None:
                self.adj_list_transpose[v.k].insert(Node(u))
                v = v.next
        self.adj_matrix_transpose = list(map(list, zip(*self.adj_matrix)))
