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

Complexity
==========

XXX

Time
----

bellman_ford(): O(|V| * |E|), O(|V|^3) for complete graphs
init_single_source(): Theta(|V|)
relax(): O(1)
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
