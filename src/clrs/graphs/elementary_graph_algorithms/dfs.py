"""
22.3 Depth-first search
=======================

Depth-first search (DFS) explores edges out of the most recently discovered vertex v
that still has unexplored edges leaving it. Once all of v's edges have been explored,
the search "backtracks" to explore edges leaving the vertex from which v was discovered.
This process continues until we have discovered all the vertices that are reachable from
the original source vertex. If any undiscovered vertices remain, then DFS selects one of
them as a new source, and it repeats the search from that source. The algorithm repeats
this entire process until it has discovered every vertex.

As in BFS, whenever DFS discovers a vertex v during a scan of hte adjacency list of an
already discovered vertex u, it records this event by setting v's predecessor attribute
v.p = u. Unlike BFS, whose predecessor subgraph forms a tree, the predecessor subgraph
produced by DFS may be composed of several trees, because the search may repeat from
multiple sources. Instead, the predecessor subgraph of DFS forms a depth-first forest
comprising several depth-first trees. The edges are tree edges.

As in BFS, DFS colors vertices during the search to indicate their state. Each vertex is
initially white, is grayed when it is discovered in the search, and is blackened when it
is finished, that is, when its adjacency list has been examined completely. This
technique guarantees that each vertex ends up in exactly one depth-first tree, so that
these trees are disjoint.

Besides creating a depth-first forest, DFS also timestamps each vertex. Each vertex v
has two timestamps: the first timestamp v.d records when v is first discovered (and
grayed), and the second timestamp v.f records when the search finishes examining v's
adjacency list (and blackens v). These timestamps provide important information about
the structure of the graph and are generally helpful in reasoning about the behavior of
DFS. These timestamps are integers between 1 and 2 * |V|, since there is one discovery
event and one finishing event for each of the |V| vertices. For every vertex u,
u.d < u.f. Vertex u is white before time u.d, gray between time u.d and time u.f, and
black thereafter.

The results of DFS may depend upon the order in which the vertices are examined and the
order in which the neighbors of vertices are examined. These different visitation orders
tend not to cause problems in practice, as we can usually use any DFS result
effectively, with essentially equivalent results.

Although DFS can be limited to one source, it is often a subroutine in other graph
algorithms.

Properties of depth-first search
--------------------------------

The most basic property of DFS is that the predecessor subgraph does indeed form a
forest of trees, since the structure of the depth-first trees exactly mirrors the
structure of recursive calls of dfs_visit(). Additionally, vertex v is a descendant of
vertex u in the depth-first forest iff v is discovered during the time in which u is
gray.

Another important property of DFS is that discovery and finishing times have parenthesis
structure. The history discovery and finishing times makes a well-formed expression in
the sense that the parentheses are properly nested. In any DFS, for any two vertices u
and v, either: 1) [u.d, u.f] and [v.d, v.f] are entirely disjoing and neither u nor v is
a descendant of the other in the depth-first forest, 2) [u.d, u.f] is contained entirely
within [v.d, v.f] and u is a descendant of v in a depth-first tree, or 3) [v.d, v.f] is
contained entirely within [u.d, u.f] and v is a descendant of u in a depth-first tree.

Vertex v is a proper descendant of vertex u in a depth-first forest for a graph G iff
u.d < v.d < v.f < u.f.

In a depth-first forest of a graph G = (V, E0, vertex v is a descendant of vertex u iff
at the time u.d that the search discovers u, there is a path from u to v consisting
entirely of white vertices.

Classification of edges
-----------------------

There are four types of edges in terms of the depth-first forest produced by a DFS on G:

1. Tree edges: Edges in depth-first forest. Edge (u, v) is a tree edge if v was first
discovered by exploring edge (u, v).

2. Back edges: Edges (u, v) connecting a vertex u to an ancestor v in a depth-first
tree. We consider self-loops, which may occur in directed graphs, to be back edges.

3. Forward edges: Non-tree edges (u, v) connecting a vertex u to a descendant v in a
depth-first tree.

4. Cross edges: All other edges. They can go between vertices in the same depth-first
tree, as long as one vertex is not an ancestor of the other, or they can go between
vertices in different depth-first trees.

The DFS algorithm has enough information to classify some edges as it encounters them.
THe key idea is that when we first explore an edge (u, v), the color of vertex v tells
us something about the edge:

1. White indicates a tree edge

2. Gray indicates a back edge

3. Black indicates a forward or cross edge

Exploration always proceeds from the deepest gray vertex, so an edge that reaches
another gray vertex has reached an ancestor. If u.d < v.d, the edge(u, v) is a forward
edge; otherwise, it is a cross edge.

An undirected graph may entail some ambiguity in how we classify edges, since (u, v) and
(v, u) are really the same edge. IN such a case, we classify the edge as the first type
in the classification list that applies. Equivalently, we classify the edge according to
whichever of (u, v) or (v, u) the search encounters first. Forward and cross edges never
occur in a DFS of an undirected graph.

22.4 Topological sort
=====================

A topological sort of a directed acyclic graph (DAG) is a linear ordering of all its
vertices such that if G contains an edge (u, v), then u appears before v in the
ordering. If the graph contains a cycle, then no linear ordering is possible. We can
view a topological sort of a graph as an ordering of its vertices along a horizontal
line so that all directed edges go from left to right. The topologically sorted vertices
appear in reverse order of their finishing times.

A directed graph G is acyclic iff a DFS of G yields no back edges.

Complexity
==========

Time
----

The for-loops in dfs() take time Theta(V) each. dfs_visit() is called exactly once for
each vertex v in V, since the vertex u on which dfs_visit() is invoked must be white and
the first thing dfs_visit() does is paint vertex u gray. During an execution of
dfs_visit(), the for-loop executes |Adj[v]| times and the sum of |Adj[v]| for all v in V
is Theta(E).

We can perform a topological sort in time Theta(V + E), since DFS takes Theta(V + E)
time and it takes O(1) time to insert each of the |V| vertices onto the front of the
linked list.

dfs(): O(V + E)
top_sort: O(V + E)
"""

# Repository Library
from src.clrs.graphs.elementary_graph_algorithms.graph import Graph
from src.clrs.lists.singly_linked_list import SLL


class DFSGraph(Graph):
    def __init__(self, num_vertices, directed=False):
        super().__init__(num_vertices, directed)
        self.time, self.top_sort_ll = 0, None

    def dfs(self):
        self.is_dag, self.top_sort_ll = True, self.top_sort_ll or SLL()
        for u in self.vertices.values():
            u.c, u.p = 0, None
        for u, u_node in self.vertices.items():
            if u_node.c == 0:
                self.dfs_visit(u, u_node)

    def dfs_visit(self, u, u_node):
        self.time += 1
        u_node.c, u_node.d = 1, self.time
        v = self.adj_list[u].head
        while v is not None:
            v_node = self.vertices[v.k]
            if v_node.c == 0:
                v_node.p = u_node
                self.dfs_visit(v_node.k, v_node)
            if v_node.c == 1:
                self.is_dag = False
            v = v.next
        u_node.c = 2
        self.time += 1
        u_node.f = self.time
        self.top_sort_ll.insert(u_node)

    def top_sort(self):
        if self.top_sort_ll is None:
            self.dfs()
        return self.top_sort_ll
