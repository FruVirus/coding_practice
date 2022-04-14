"""
All Paths from Source Lead to Destination
-----------------------------------------

Given the edges of a directed graph where edges[i] = [a_i, b_i] indicates there is an
edge between nodes a_i and b_i, and two nodes source and destination of this graph,
determine whether or not all paths starting from source eventually end at destination,
that is:

    - At least one path exists from the source node to the destination node
    - If a path exists from the source node to a node with no outgoing edges, then that
node is equal to destination.
    - The number of possible paths from source to destination is a finite number.

Return true if and only if all roads from source lead to destination.

Intuition
---------

Let's try to boil the problem down to simpler, more commonly understandable terms.

    - We are given a directed graph.
    - Also, as inputs we are provided a source and a destination.
    - We need to tell if all the paths from the source lead to the destination and we
can split this into a few criteria.
        - If a path exists from the source node to a node with no outgoing edges, then
that node must be equal to destination. Here, we simply need to see that if a node does
not have any neighbors in the adjacency list structure, then it has to be the
destination or else we return false.
        - The number of possible paths from source to destination is a finite number.
This simply means that the graph is actually a tree. Or in other words, there are no
cycles in the graph. If there is a cycle in the graph, there would be an infinite number
of paths from the source to the destination, as each would go around the cycle a
different number of times.

Thus, the problem simply boils down to two things which we need to check during our
graph traversal algorithm. We need to detect any cycles in the traversal and return
false if there are any. Also, we need to ensure that if there is a leaf node encountered
during the traversal, it is the destination node.

We simply need to run a graph traversal algorithm and check for two basic conditions. It
is easy enough to check for a leaf node since the adjacency list entry for that node
would not contain any neighbors. So our first condition can be easily checked; i.e., if
we encounter a leaf node, we check its equality to the destination node.

While doing DFS, if an edge is encountered from current vertex to a GRAY vertex, then
this edge is a back edge and hence there is a cycle. A GRAY node represents a node whose
processing is still ongoing. Thus, if a descendant eventually leads back to a node whose
processing is ongoing, it ends up creating a cycle in the directed graph and we call the
edge leading back to a GRAY node as a backward edge.

NB: In the implementation below, we use None as WHITE, False as GRAY, and True as BLACK.

Complexity
==========

Time
----

leadsToDestination(n, edges, src, dest): O(v).

Space
-----

leadsToDestination(n, edges, src, dest): O(v + e).
"""


def sol(n, edges, source, destination):
    adj_list, done = [[] for _ in range(n)], [None] * n
    for u, v in edges:
        adj_list[u].append(v)

    def backtrack(node):
        if done[node] is not None:
            return done[node]
        if len(adj_list[node]) == 0:
            return node == destination
        done[node] = False
        for next_node in adj_list[node]:
            if not backtrack(next_node):
                return False
        done[node] = True
        return True

    return backtrack(source)
