"""
Overview
========

The objective of the subset sum problem is to find a subset of weights whose total sum
is equal to the maximum capacity, if such a subset exists.

The subset sum problem asks us for a boolean answer but we can transform it to a
maximization problem using boolean logic formulation where True = 1 and False = 0.

The subset sum problem has identical decisions and state to the Knapsack problem. When
computing v[i][j], we need to consider all the possible values of the weights. Consider
w = [1, 2, 3, 7] and c = 6. In this case, the subset [1, 2, 3] has a total weight equal
to 6. We form the v matrix as follows:

v   0   1   2   3   4   5   6 --> capacity
0   1   1   0   0   0   0   0
1   1   1   1   1   0   0   0
2   1   1   1   1   1   1   1
3   1   1   1   1   1   1   1

items

The first column is all 1's since we can always exclude all items in order to match a
total capacity of 0.

v[0][1] = 1 since we can match a capacity of 1 by including just the first item.

For the rest of the entries, we check whether we can match the capacity without taking
the item i or else we take the item i and see if we can find a subset to get the
remaining capacity.

For example, the value of v[1][2] tells us if we can match a capacity of 2 with some
combination of the first two items (items 0 and 1). If we can match the capacity without
taking item 1, then this is v[0][2] since we keep the same capacity and look at the
entry for the previous item 0. If we cannot match the capacity without taking item 1,
then this is v[0][0] since we take item 1 and subtract its weight to get a remaining
weight of 0. In this case, we can match the capacity of 2 by taking the second item and
not the first.

As another example, the value of v[1][4] tells us if we can match a capacity of 4 with
some combination of the first two items (items 0 and 1). If we can match the capacity
without taking item 1, then this is v[0][4] since we keep the same capacity and look at
the entry for the previous item 0. If we cannot match the capacity without taking item
1, then this is v[0][2] since we take item 1 and subtract its weight to get a remaining
weight of 2. In this case, we cannot match the capacity of 4 using any combination of
the first two items; thus, v[1][4] is 0.

Complexity
==========

Time
----

ss_bottom_up(): O(n * c), where n is the number of items and c is the capacity.
ss_top_down(): O(n * c), where n is the number of items and c is the capacity.

Space
-----

ss_bottom_up(): O(c * n) for v table.
ss_top_down(): O(c * n) for v table.
"""


def ss_bottom_up(w, c, n, v):
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            loc = j - w[i - 1]
            val = -float("inf") if loc < 0 else v[i - 1][loc]
            v[i][j] = max(v[i - 1][j], val)
    return v


def ss_top_down(w, c, n, v):
    if n == 0 or c == 0:
        v[n][c] = 1 if c == 0 else 0
    elif w[n - 1] > c:
        v[n][c] = ss_top_down(w, c, n - 1, v)
    else:
        without_item = ss_top_down(w, c, n - 1, v)
        with_item = ss_top_down(w, c - w[n - 1], n - 1, v)
        v[n][c] = max(with_item, without_item)
    return v[n][c]


def ss_solution(w, c, top_down=False):
    n = len(w)
    v = [[0] * (c + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        v[i][0] = 1
    ss = ss_top_down if top_down else ss_bottom_up
    ss(w, c, n, v)
    return v


def return_ss(w, c, v):
    if v[-1][-1] != 1:
        return None
    n = len(v)
    ss = [0] * (n - 1)
    for i in range(n - 1, -1, -1):
        if v[i][c] != 1:
            ss[i], c = 1, c - w[i]
    return ss
