"""
Clone Graph
-----------

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

Complexity
==========

Time
----

Solution:
    def clone_graph_stack(self, node): O(n + m), where n is the number of nodes
(vertices) and m is the number of edges.

Space
-----

Solution:
    def clone_graph_stack(self, node): O(n).
"""

# Standard Library
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val, self.neighbors = val, neighbors if neighbors else []


class Sol:
    def __init__(self):
        self.visited = {}

    @staticmethod
    def clone_graph_queue(node):
        if not node:
            return node
        visited, queue = {node: Node(node.val)}, deque([node])
        while queue:
            curr_node = queue.popleft()
            for n in curr_node.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)
                visited[curr_node].neighbors.append(visited[n])
        return visited[node]

    def clone_graph_stack(self, node):
        if not node:
            return node
        if node in self.visited:
            return self.visited[node]
        clone = Node(node.val)
        self.visited[node] = clone
        clone.neighbors = [self.clone_graph_stack(n) for n in node.neighbors]
        return clone
