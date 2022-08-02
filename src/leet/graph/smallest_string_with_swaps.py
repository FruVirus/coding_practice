"""
Smallest String With Swaps
--------------------------

You are given a string s, and an array of pairs of indices in the string pairs where
pairs[i] = [a, b] indicates 2 indices (0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of
times.

Return the lexicographically smallest string that s can be changed to after using the
swaps.

Intuition
---------

The important point to note here is that if we have pairs like (a, b) and (b, c), then
we can swap characters at indices a and c. Although we don't have the pair (a, c), we
can still swap them by first swapping them with the character at index b. Thus, because
we can swap the characters at these indices any number of times, we can rearrange the
characters a, b, and c into any order.

This demonstrates how we can swap any pair of vertices present in the same connected
component. Thus, we can rearrange the characters such that any character is at any index
within the connected component. To find the lexicographically smallest string, we need
to sort the characters that correspond to these indices in ascending order and then
place the ith character at the ith index.

We can break the solution down into four steps: build a graph using the given pairs,
find the connected components in the graph, sort the characters in each connected
component in ascending order, and build the smallest string.

The biggest challenge in solving this problem was figuring out that, with infinite
swaps, we can arrange all characters that belong to the same connected component in
sorted order.

DFS Approach

We will build the adjacency list using the pairs given i.e., for each pair (x, y) we
will add an edge from x to y and from y to x. Then we will iterate over the indices from
0 to n-1 where n is the length of the given string s. For each index, if it has not been
visited yet, we will perform a DFS and store the vertices (index) and the characters at
these indices in a list. Each list will represent a different component in the graph.
Then we will sort each list of indices and each list of characters and place the ith
character at the ith index in the string smallestString.

DSU Approach

Each list in char_to_indices will represent a different component in the graph. Then
we will sort each list of indices and each list of characters and place the i_th
character at the ith index in the smallest string.

Complexity
==========

Time
----

smallestStringWithSwaps_dfs(s, pairs): O(e + v * lg v), where e is the number of edges
and v is the number of vertices (the length of the given string).
smallestStringWithSwaps_dset(s, pairs): O((e + v) * alpha(v) + v * lg v). e * alpha(v)
is required for the union operations. v * alpha(v) is required for the find operations.
v * lg v is required for the sorting operation.

Space
-----

smallestStringWithSwaps_dfs(s, pairs): O(e + v).
smallestStringWithSwaps_dset(s, pairs): O(v).
"""


# Standard Library
from collections import defaultdict

# Repository Library
from src.leet.graph.number_of_provinces import DisjointSet


def sol_dfs(s, pairs):
    s = list(s)
    n = len(s)
    graph, seen = {i: [] for i in range(n)}, set()
    for u, v in pairs:
        graph[u].append(v)
        graph[v].append(u)
    for u in range(n):
        if u not in seen:
            chars, indices, stack = [], [], [u]
            while stack:
                for v in graph[stack.pop()]:
                    if v not in seen:
                        chars.append(s[v])
                        indices.append(v)
                        seen.add(v)
                        stack.append(v)
            for c, i in zip(sorted(chars), sorted(indices)):
                s[i] = c
    return "".join(s)


def sol_dset(s, pairs):
    s = list(s)
    n = len(s)
    dset = DisjointSet(n)
    for u, v in pairs:
        dset.union(u, v)
    char_to_indices = defaultdict(list)
    for u in range(n):
        char_to_indices[dset.find(u)].append(u)
    for indices in char_to_indices.values():
        chars = sorted([s[i] for i in indices])
        for c, i in zip(chars, indices):
            s[i] = c
    return "".join(s)
