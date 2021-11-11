"""
24.2 Single-source shortest paths in directed acyclic graphs
============================================================

By relaxing the edges of a weighted DAG G = (V, E) according to a topological sort of
its vertices, we can compute shortest paths from a single source in Theta(V + E) time.
Shortest paths are always well defined in a DAG, since even if there are negative-weight
edges, no negative-weight cycles can exist.

The algorithm starts by topologically sorting the DAG to impose a linear ordering on the
vertices. If the DAG contains a path from vertex u to vertex v, then u precedes v in the
topological sort. We make just one pass over the vertices in the topologically sorted
order. As we process each vertex, we relax each edge that leaves the vertex.

After calling bellman_ford(), calling print_path(s, v) will print the shortest path
between the source s and a given vertex v in the graph.

The total number of paths in a DAG can be computed by counting the number of paths whose
start point is at each vertex v. Assume that initially, we have v.paths = 0 for all v in
V.

An interesting application of single-source shortest paths in DAGs arises in determining
critical paths in PERT chart analysis. Edges represent jobs to be performed, and edge
weights represent the time required to perform particular jobs. If edge (u, v) enters
vertex v and edge (v, x) leaves v, then job (u, v) must be performed before job (v, x).
A path through this DAG represents a sequences of jobs that must be performed in a
particular order. A critical path is a longest path through the DAG, corresponding to
the longest time to perform any sequence of jobs. Thus, the weight of a critical path
provides a lower bound on the total time to perform all the jobs. We can find a critical
path by either:

1. negating the edge weights and running dag(), or

2. running dag(), with the modification that we replace float("inf") by -float("inf") in
init_single_source() and ">" by "<" in relax().

After the process, calling print_path(s, v) will print the critical path between the
source s and a given vertex v in the graph.

Complexity
==========

top_sort() takes Theta(V + E) time. init_single_source() takes Theta(V) time. The outer
while-loop makes one iteration per vertex. Altogether, the inner while-loop relaxes each
edge exactly once (using aggregate analysis). Because each iteration of the inner
while-loop takes Theta(1) time, the total running time is Theta(V + E), which is linear
in the size of an adjacency-list representation of the graph.

Time
----

dag(): Theta(|V| + |E|)
init_single_source(): Theta(|V|)
num_total_paths(): O(|V| + |E|)
top_sort(): O(|V| + |E|)
"""

# Repository Library
from src.clrs.graph_algorithms.elementary_graph_algorithms.dfs import DFSGraph


class DAG(DFSGraph):
    def dag(self, s):
        self.top_sort()
        self.init_single_source(s)
        node = self.top_sort_ll.head
        while node is not None:
            u_node, v = self.vertices[node.k], self.adj_list[node.k].head
            while v is not None:
                self.relax(u_node, self.vertices[v.k])
                v = v.next
            node = node.next

    def num_total_paths(self):
        for v in self.vertices.values():
            v.paths = 0
        self.top_sort()
        node, top_sort = self.top_sort_ll.head, []
        while node is not None:
            top_sort.append(node.k)
            node = node.next
        for u in reversed(top_sort):
            u_node, v = self.vertices[u], self.adj_list[u].head
            while v is not None:
                v_node = self.vertices[v.k]
                v_node.paths = u_node.paths + 1 + v_node.paths
                v = v.next
        return sum(v.paths for v in self.vertices.values())
