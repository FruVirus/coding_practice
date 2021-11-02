"""
Overview
========

Depth-first search (DFS) explores edges out of the most recently discovered vertex v
that still has unexplored edges leaving it. Once all of v's edges have been explored,
the search "backtracks" to explore edges leaving the vertex from which v was discovered.
This process continues until we have discovered all the vertices that are reachable from
the original source vertex. If any undiscovered vertices remain, then DFS selects one of
them as a new source, and it repeats the search from that source. The algorithm repeats
this entire process until it has discovered every vertex.

Although DFS can be limited to one source, it is often a subroutine in other graph
algorithms.

Complexity
==========

Time
----

dfs(): O(V + E)
print_path(): Linear in the number of vertices in the path printed since each recursive
call is for a path one vertex shorter.
"""

# pylint: disable=R1722

# Repository Library
from src.clrs.graphs.elementary_graph_algorithms.graph import Graph


class DFSGraph(Graph):
    def dfs(self, s):
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
