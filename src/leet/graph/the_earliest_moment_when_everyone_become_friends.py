"""
The Earliest Moment When Everyone Become Friends
------------------------------------------------

There are n people in a social group labeled from 0 to n - 1. You are given an array
logs where logs[i] = [timestamp_i, x_i, y_i] indicates that x_i and y_i will be friends
at the time timestamp_i.

Friendship is symmetric. That means if a is friends with b, then b is friends with a.
Also, person a is acquainted with a person b if a is friends with b, or a is a friend of
someone acquainted with b.

Return the earliest time for which every person became acquainted with every other
person. If there is no such earliest time, return -1.

Intuition
---------

In order to discover the earliest moment, we must first ensure that we read through the
logs in chronological order. Since there is no mentioning whether the logs are ordered
or not in the problem description, we need to sort them first.

Once the logs are sorted by time, we then iterate through them, while applying the
Union-Find data structure.

    - For each log, we connect the two individuals that were involved in the log, by
applying the union(a, b) function.
    - Each log adds more connections among the individuals. A connection is useful if
the two individuals are separated (disjoint), or redundant if the two individuals are
connected already via other individuals.
    - Initially, we treat each individual as a separate group. The number of groups
decreases along with the useful merging operations. The moment when the number of groups
is reduced to one is the earliest moment when everyone becomes connected (friends).

Complexity
==========

Time
----

earliestAcq(logs, n): O(n + m lg m + m), where n is the number of people and m is the
number of logs.

Space
-----

earliestAcq(logs, n): O(n + m).
"""


# Repository Library
from src.leet.graph.number_of_provinces import DisjointSet


def sol(logs, n):
    if len(logs) < n - 1:
        return -1
    dset = DisjointSet(n)
    for ts, u, v in sorted(logs):
        dset.union(u, v)
        if dset.get_count() == 1:
            return ts
    return -1
