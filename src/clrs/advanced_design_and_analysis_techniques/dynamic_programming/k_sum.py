"""
Overview
========

The objective of the K-sum problem is given n items with corresponding weights, w,
select exactly K items whose weights add up to exactly the capacity, c.

A solution to the K-sum problem looks the same as for the subset sum problem, so we
still have n Boolean decisions to make at each step.

However, the knapsack structure has changed. In the original problem, the knapsack
capacity placed a limit on the total weight of the items, so we needed to keep track of
the total weight of the items that we added---that was our state.

In the K-sum problem, the knapsack also has slots. When deciding whether to add an item
to the knapsack, we need to know if there are any slots available, which is equivalent
to knowing how many slots we have used up. So the problem state needs to track both the
total weight of the bars in the knapsack, and how many slots they take up.

The filling of the v table for K-sum is the same as that for the subset sum problem
except that we have a third for-loop that iterates over the K slots. When we compute the
solution to the K-sum problem, if we find an item that should belong to the solution, we
then decrement k by one to account for the item taking up a slot in the knapsack.

Complexity
==========

Time
----

ksum_bottom_up(): O(n * c * k), where n is the number of items, c is the capacity, and k
is the number of slots.
ksum_top_down(): O(n * c * k), where n is the number of items, c is the capacity, and k
is the number of slots.

Space
-----

ksum_bottom_up(): O(c * n * k) for v table.
ksum_top_down(): O(c * n * k) for v table.
"""


def ksum_bottom_up(w, c, n, k_, v):
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            for k in range(1, k_ + 1):
                loc = j - w[i - 1]
                val = -float("inf") if loc < 0 else v[i - 1][loc][k - 1]
                v[i][j][k] = max(v[i - 1][j][k], val)
    return v


def ksum_top_down(w, c, n, k_, v):
    if n == 0 or (c == 0 and k_ == 0):
        v[n][c][k_] = 1 if c == 0 and k_ == 0 else 0
    elif w[n - 1] > c:
        v[n][c][k_] = ksum_top_down(w, c, n - 1, k_, v)
    else:
        without_item = ksum_top_down(w, c, n - 1, k_, v)
        with_item = ksum_top_down(w, c - w[n - 1], n - 1, k_ - 1, v)
        v[n][c][k_] = max(with_item, without_item)
    return v[n][c][k_]


def ksum_solution(w, c, k_, top_down=False):
    n = len(w)
    v = [[[0] * (k_ + 1) for _ in range(c + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        v[i][0][0] = 1
    ksum = ksum_top_down if top_down else ksum_bottom_up
    ksum(w, c, n, k_, v)
    return v


def return_ksum(w, c, k_, v):
    if v[-1][-1][-1] != 1:
        return None
    n = len(v)
    ksum = [0] * (n - 1)
    for i in range(n - 1, -1, -1):
        if v[i][c][k_] != 1:
            ksum[i], c, k_ = 1, c - w[i], k_ - 1
    return ksum
