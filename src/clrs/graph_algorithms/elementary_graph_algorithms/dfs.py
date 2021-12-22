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

22.5 Strongly connected components
==================================

A classic application of DFS is to decompose a directed graph into its strongly
connected components using two depth-first searches. Many algorithms that work with
directed graphs being with such a decomposition. After decomposing the graph into
strongly connected components, such algorithms run separately on each one and then
combine the solutions according to the structure of connections among components.

A strongly connected component of a directed graph G = (V, E) is a maximal set of
vertices C such that for every pair of vertices u and v in C, u and v are reachable from
each other.

The algorithm for finding the strongly connected components of a graph G = (V, E) uses
the transpose of G. G and G.T have exactly the same strongly connected components: u and
v are reachable from each other in G iff they are reachable from each other in G.T.

The linear-time algorithm for strongly connected components computes the SCCs of a
directed graph G = (V, E) using two depth-first searches, one on G and one on G.T.

The strongly connected components graph of G (G_SCC) is obtained by contracting all
edges whose incident vertices are within the same strongly connected component of G.
Thus, G_SCC must be a DAG whereas G can be either a DAG or a directed graph. If G_SCC is
not a DAG after contracting all edges, then the strongly connected components that are
formed is incorrect since they are not all inclusive.

By visiting vertices in the second DFS in decreasing order of the finishing times that
were computed in the first DFS, we are, in essence, visiting the vertices of the
component graph (each of which corresponds to a strongly connected component of G) in
topologically sorted order.

Let C and C' be distinct strongly connected components in a directed graph G = (V, E).
Suppose that there is an edge (u, v) in E, where u in C and v in C'. Then f(C) > f(C'),
where f() denotes the latest finishing time of a vertex. In other words, each edge that
goes between different SCCs in G goes from a component with a later finishing time to a
component with an earlier finishing time.

Let C and C' be distinct strongly connected components in a directed graph G = (V, E).
Suppose that there is an edge (u, v) in E.T, where u in C and v in C'. Then,
f(C) < f(C'). In other words, each edge that goes between different SCCs in G.T goes
from a component with an earlier finishing time to a component with a later finishing
time.

The key steps to understanding why the SCC algorithm works:

1. When we perform the second DFS on G.T, we start with the strongly connected component
C whose finishing time f(C) is maximum.

2. The search starts from some vertex x in C, and it visits all vertices in C

3. G.T contains no edges from C to any other strongly connected component, and so the
search from x will not visit vertices in any other component. Thus, the tree rooted at x
contains exactly the vertices of C only.

4. Having completed visiting all vertices in C, the search selects as a root a vertex
from some other strongly connected component C' whose finishing time f(C') is maximum
over all components other than C.

5. Again, the search will visit all vertices in C'. Once again, the only edges in G.T
from C' to any other component must be to C, which we have already visited.

6. In general, when the DFS of G.T visits any strongly connected component, any edges
out of that component must be to components that the search already visited. Each
depth-first tree, therefore, will be exactly one strongly connected component.

Complexity
==========

Time
----

The for-loops in dfs() take time Theta(V) each. dfs_recurse() is called exactly once for
each vertex v in V, since the vertex u on which dfs_recurse() is invoked must be white
and the first thing dfs_recurse() does is paint vertex u gray. During an execution of
dfs_recurse(), the for-loop executes |Adj[v]| times and the sum of |Adj[v]| for all v in
V is Theta(E). dfs_recurse() is called exactly once for each vertex v in V.

We can perform a topological sort in time Theta(V + E), since DFS takes Theta(V + E)
time and it takes O(1) time to insert each of the |V| vertices onto the front of the
linked list.

dfs(): O(V + E)
top_sort(): O(V + E)
scc(): O(V + E)
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.graph import Graph
from src.clrs.lists.singly_linked_list import SLL, Node
from src.clrs.stacks.stack import Stack


class DFS(Graph):
    def _get_vertex(self, transpose=False):
        if transpose:
            return sorted(self.vertices.values(), key=lambda x: x.f, reverse=True)
        return self.vertices.values()

    def dfs(self, recurse=False, transpose=False):
        scc, time, top_sort = [], 0, SLL()
        dfs_ = self.dfs_recurse if recurse else self.dfs_stack
        for v in self.vertices.values():
            v.c, v.p = 0, None
        for v in self._get_vertex(transpose):
            if v.c == 0:
                scc.append(v.k)
                time = dfs_(v, time, top_sort, transpose)
        return scc, top_sort

    def dfs_recurse(self, u_node, time, top_sort, transpose=False):
        time += 1
        u, u_node.c, u_node.d = u_node.k, 1, time
        v = self.adj_list_transpose[u].head if transpose else self.adj_list[u].head
        while v is not None:
            v_node = self.vertices[v.k]
            if v_node.c == 0:
                v_node.p = u_node
                time = self.dfs_recurse(v_node, time, top_sort, transpose)
            if v_node.c == 1:
                self.is_dag = False
            v = v.next
        time += 1
        u_node.c, u_node.f = 2, time
        top_sort.insert(Node(u))
        return time

    def dfs_stack(self, u_node, time, top_sort, transpose=False):
        time += 1
        u, u_node.c, u_node.d = u_node.k, 1, time
        s = Stack(self.num_vertices)
        s.push(u)
        while not s.empty():
            u = s.a[s.top]
            u_node, v = self.vertices[u], self.first_white(u, transpose)
            time += 1
            if v is None:
                u_node.c, u_node.f = 2, time
                top_sort.insert(Node(u))
                s.pop()
            else:
                v.c, v.d, v.p = 1, time, u_node
                s.push(v.k)
        return time

    def first_white(self, s, transpose=False):
        v = self.adj_list_transpose[s].head if transpose else self.adj_list[s].head
        while v is not None:
            v_node = self.vertices[v.k]
            if v_node.c == 1:
                self.is_dag = False
            if v_node.c == 0:
                return v_node
            v = v.next
        return None

    def get_edge_types(self, recurse=False):
        self.dfs(recurse)
        edge_types = {}
        for u, v in self.edges:
            edge_type, u, v = None, self.vertices[u], self.vertices[v]
            if u.d < v.d < v.f < u.f:
                edge_type = "Tree/Forward"
            elif v.d <= u.d < u.f <= v.f:
                edge_type = "Back"
            elif v.d < v.f < u.d < u.f:
                edge_type = "Cross"
            edge_types[(u.k, v.k)] = edge_type
        return edge_types

    def scc(self, recurse=False):
        assert self.directed
        self.dfs(recurse)
        self.transpose()
        return self.dfs(recurse, True)[0]

    def top_sort(self, recurse=False):
        return self.dfs(recurse)[1]
