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
    def __init__(self): O(1].
    def clone_bfs(node) and def clone_dfs(self, node): O(n + m), where n is the number
of nodes (vertices) and m is the number of edges.

Space
-----

Solution:
    def clone_bfs(node) and def clone_dfs(self, node): O(n).
"""

# Standard Library
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val, self.neighbors = val, neighbors if neighbors else []


class Sol:
    def __init__(self):
        self.seen = {}

    def clone_bfs(self, node):
        if not node:
            return node
        queue, self.seen[node] = deque([node]), Node(node.val)
        while queue:
            curr_node = queue.popleft()
            for n in curr_node.neighbors:
                if n not in self.seen:
                    self.seen[n] = Node(n.val)
                    queue.append(n)
                self.seen[curr_node].neighbors.append(self.seen[n])
        return self.seen[node]

    def clone_dfs(self, node):
        if not node:
            return node
        if node in self.seen:
            return self.seen[node]
        clone = Node(node.val)
        self.seen[node] = clone
        clone.neighbors = [self.clone_dfs(n) for n in node.neighbors]
        return clone
