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

We can break the solution down into four steps: build a graph using the given pairs,
find the connected components in the graph, sort the characters in each connected
component in ascending order, and build the smallest string.

Each list in root_to_component will represent a different component in the graph. Then
we will sort each list of indices and each list of characters and place the i_th
character at the i_th index in the smallest string.

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
    n, seen = len(s), set()
    graph = {i: [] for i in range(n)}
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
    root_to_component = defaultdict(list)
    for i in range(n):
        root_to_component[dset.find(i)].append(i)
    for components in root_to_component.values():
        chars = sorted([s[i] for i in components])
        for c, i in zip(chars, components):
            s[i] = c
    return "".join(s)
