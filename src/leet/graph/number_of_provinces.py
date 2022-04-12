"""
Number of Provinces
-------------------

There are n cities. Some of them are connected, while some are not. If city a is
connected directly with city b, and city b is connected directly with city c, then city
a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities
outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city
and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Complexity
==========

Time
----

findCircleNum(is_connected): O(n^2).

Sol:
    def __init__(self, size): O(n).
    def connected(self, x, y): O(1).
    def find(self, x): O(1).
    def get_count(self): O(1).
    def union(self, x, y): O(1).

Space
-----

findCircleNum(is_connected): O(n).

Sol:
    def __init__(self, size): O(n).
"""


class DisjointSet:
    def __init__(self, size):
        self.count, self.rank, self.root = size, [1] * size, list(range(size))

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def get_count(self):
        return self.count

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            else:
                self.root[rootx] = rooty
                if self.rank[rootx] == self.rank[rooty]:
                    self.rank[rooty] += 1
            self.count -= 1


def sol(is_connected):
    n = len(is_connected)
    dset = DisjointSet(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                dset.union(i, j)
    return dset.get_count()
