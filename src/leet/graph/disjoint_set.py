"""
Summary of the “disjoint set” data structure
--------------------------------------------

The main idea of a “disjoint set” is to have all connected vertices have the same parent
node or root node, whether directly or indirectly connected. To check if two vertices
are connected, we only need to check if they have the same root node.

The two most important functions for the “disjoint set” data structure are the find
function and the union function. The find function locates the root node of a given
vertex. The union function connects two previously unconnected vertices by giving them
the same root node. There is another important function named connected, which checks
the “connectivity” of two vertices. The find and union functions are essential for any
question that uses the “disjoint set” data structure.

Complexity
==========

Time
----

Sol:
    def __init__(self, size): O(n).
    def connected(self, x, y): O(1).
    def find(self, x): O(1).
    def union(self, x, y): O(1).

Space
-----

Sol:
    def __init__(self, size): O(n).
"""


class Sol:
    def __init__(self, size):
        self.rank, self.root = [1] * size, list(range(size))

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                if self.rank[rootx] == self.rank[rooty]:
                    self.rank[rooty] += 1
