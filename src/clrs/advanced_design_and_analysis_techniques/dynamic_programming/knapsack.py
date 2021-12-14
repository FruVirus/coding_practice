"""
Overview
========

The objective of the knapsack problem is to maximize the total profit in the knapsack
with a given weight limit. Given a list of items with corresponding profits and weights,
which items should we include in the knapsack so that we maximize our profit without
going over the given weight limit?

Once we take an item, we gain profit but lose knapsack capacity. If we don't take an
item, we keep the same profit but do not lose knapsack capacity. If taking an item puts
up over the capacity limit, then the profit is the current profit without the item.

Consider p = [1, 2, 5, 6], w = [2, 3, 4, 5], and c = 8. In this case, the answer is
x = [0, 1, 0, 1] which corresponds to taking the second and fourth items only. We form
the v matrix as follows:

v   0   1   2   3   4   5   6   7   8 --> capacity
0   0   0   0   0   0   0   0   0   0
1   0   0   1   1   1   1   1   1   1
2   0   0   1   2   2   3   3   3   3
3   0   0   1   2   5   5   6   7   7
4   0   0   1   2   5   6   6   7   8

items

The first column is all 0's since a capacity of 0 means we can't anything and thus, all
values are 0. The first row is all 0's since taking 0 items means the values are 0
regardless of the capacity.

v[1][2] = 1 since we can take item 1 with weight 2 if we have a capacity of 2.
Similarly, if we only take item 1, then v[1][[3:] = 1 since the total value in the
knapsack remains the same.

For the rest of the entries, we check whether we maximize our value without taking the
item i or else we take the item i and add its value to the total value of the knapsack.

For example, the value of v[2][2] = max(v[1][2], v[1][2 - w[1]] = v[1][-1]) =
max(v[1][2], -float("inf") + p[2]) = 1 since v[1][-1] does not exist. This means that we
cannot take item 2 if our capacity is 2 since item 2's weight is 3 which exceeds the
knapsack capacity. Thus, we look at v[1][2] which is the value if we take item 1
assuming our capacity is 2.

As another example, the value of v[2][3] = max(v[1][3], v[1][3 - w[1]] = v[1][0]) =
max(v[1][3], v[1][0] + p[1]) = 2. This means that we can take item 2 if our capacity is
3. By considering items 1 and 2 with a maximum capacity of 3, the highest value in our
knapsack can be 2.

As a final example, the value of v[3][4] = max(v[2][4], v[2][4 - w[2]] = v[2][0] =
max(v[2][4], v[2][0] + p[2]) = 5. This means that we can take item 3 if our capacity is
4. By considering items 1, 2, and 3 with a maximum capacity of 4, the highest value in
our knapsack can be 5.

Complexity
==========

Time
----

ks_bottom_up(): O(n * c), where n is the number of items and c is the capacity.
ks_top_down(): O(n * c), where n is the number of items and c is the capacity.

Space
-----

ks_bottom_up(): O(c * n) for v table.
ks_top_down(): O(c * n) for v table.
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
