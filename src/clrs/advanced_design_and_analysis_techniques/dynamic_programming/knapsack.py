"""
Overview
========

The objective of the knapsack problem is to maximize the total profit in the knapsack
with a given weight limit. Given a list of items with corresponding profits and weights,
which items should we include in the knapsack so that we maximize our profit without
going over the given weight limit?

Once we take an item, we gain profit but lose knapsack capacity.
If we don't take an item, we keep the same profit but do not lose knapsack capacity.
If taking an item puts up over the capacity limit, then the profit is the current profit
without the item.

Complexity
==========

Time
----

ks_bottom_up(): O(n * c), where n is the number of items and c is the capacity.
ks_top_down(): O(n * c), where n is the number of items and c is the capacity.
"""


def ks_bottom_up(p, w, c, n, v):
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            loc = j - w[i - 1]
            val = -float("inf") if loc < 0 else v[i - 1][loc]
            v[i][j] = max(v[i - 1][j], val + p[i - 1])
    return v


def ks_top_down(p, w, c, n, v):
    if n == 0 or c == 0:
        v[n][c] = 0
    elif w[n - 1] > c:
        v[n][c] = ks_top_down(p, w, c, n - 1, v)
    else:
        without_item = ks_top_down(p, w, c, n - 1, v)
        with_item = ks_top_down(p, w, c - w[n - 1], n - 1, v) + p[n - 1]
        v[n][c] = max(with_item, without_item)
    return v[n][c]


def ks_solution(p, w, c, top_down=False):
    n = len(p)
    v = [[0] * (c + 1) for _ in range(n + 1)]
    ks = ks_top_down if top_down else ks_bottom_up
    ks(p, w, c, n, v)
    return v


def return_ks(p, v):
    n = len(v)
    ks, val = [0] * (n - 1), v[-1][-1]
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if val in v[j]:
                ks[j] = 0
                break
        else:
            ks[i - 1], val = 1, val - p[i - 1]
    return ks
