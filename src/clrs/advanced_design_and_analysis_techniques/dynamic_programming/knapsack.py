"""
Overview
========

The objective of the 0/1 knapsack problem is to maximize the total profit in the
knapsack with a given weight limit. Given a list of items with corresponding profits and
weights, which items should we include in the knapsack so that we maximize our profit
without going over the given weight limit?

Once we take an item, we gain profit but lose knapsack capacity. If we don't take an
item, we keep the same profit but do not lose knapsack capacity. In other words, if
taking an item puts us over the capacity limit, then the profit is the current profit
without the item.

Note that we cannot take fractional amounts of an item. We either take the whole item or
none of it; hence, this is known as the 0/1 knapsack problem.

Consider p = [1, 2, 5, 6], w = [2, 3, 4, 5], and c = 8. In this case, the answer is
x = [0, 1, 0, 1] which corresponds to taking the second and fourth items only. We form
the v matrix, which tabulates the profits for every single possible combination of
items, as follows:

v   0   1   2   3   4   5   6   7   8 --> capacity
0   0   0   0   0   0   0   0   0   0
1   0   0   1   1   1   1   1   1   1
2   0   0   1   2   2   3   3   3   3
3   0   0   1   2   5   5   6   7   7
4   0   0   1   2   5   6   6   7   8

items

The first column is all 0's since a capacity of 0 means we can't take anything and thus,
all values are 0. The first row is all 0's since taking 0 items means the values are 0
regardless of the capacity.

v[1][2] = 1 since we can take item 1 with weight 2 if we have a capacity of 2.
Similarly, if we only take item 1, then v[1][[3:] = 1 since the total value in the
knapsack remains the same. Similarly, if we only have a capacity of 2, then v[:][2] = 1
since the only item we can take with a capacity of 2 is item 1 and item 1's profit is 1.

For the rest of the entries, we check whether we maximize our value without taking item
i or else we take item i and add its value to the total value of the knapsack.

For example, the value of v[2][2] = max(v[1][2], v[1][2 - w[2]] = v[1][-1] + p[2]) =
max(v[1][2], -float("inf") + p[2]) = 1 since v[1][-1] does not exist. This means that we
cannot take item 2 if our capacity is 2 since item 2's weight is 3 which exceeds the
knapsack capacity. Thus, we look at v[1][2] which is the value if we take item 1
assuming our capacity is 2.

As another example, the value of v[2][3] = max(v[1][3], v[1][3 - w[2]] = v[1][0] + p[2])
= 2. This means that we can safely take item 2 if our capacity is 3. By considering
items 1 and 2 with a maximum capacity of 3, the highest value in our knapsack can be 2,
which corresponds to taking item 2 only.

As a final example, the value of v[3][4] = max(v[2][4], v[2][4 - w[3]] = v[2][0] + p[3])
= 5. This means that we can safely take item 3 if our capacity is 4. By considering
items 1, 2, and 3 with a maximum capacity of 4, the highest value in our knapsack can be
5, which corresponds to taking item 3 only.

Intuition
---------

In order to maximize our total profit, we have to put items into our knapsack. We can
put items into our knapsack as long as the weights of the items do not exceed the
capacity of the knapsack. If we take an item, we have to ensure that its weight does not
put us over the knapsack capacity. If it does not, then the total profit is increased by
the value of the added object and our knapsack capacity is decreased appropriately for
the next item to consider.

Complexity
==========

Time
----

ks_bu() and ks_td(): O(n * c), where n is the number of items and c is the capacity.

Space
-----

ks_bu() and ks_td(): O(c * n) for v table.
"""


def ks_bu(p, w, c, n, v):
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            loc = j - w[i - 1]
            val = -float("inf") if loc < 0 else v[i - 1][loc] + p[i - 1]
            v[i][j] = max(v[i - 1][j], val)


def ks_td(p, w, c, n, v):
    if not (n == 0 or c == 0):
        if w[n - 1] > c:
            v[n][c] = ks_td(p, w, c, n - 1, v)
        else:
            without_item = ks_td(p, w, c, n - 1, v)
            with_item = ks_td(p, w, c - w[n - 1], n - 1, v) + p[n - 1]
            v[n][c] = max(with_item, without_item)
    return v[n][c]


def ks(p, w, c, td=False):
    n = len(p)
    v = [[0] * (c + 1) for _ in range(n + 1)]
    ks_ = ks_td if td else ks_bu
    ks_(p, w, c, n, v)
    n = len(v)
    sol, val = [0] * (n - 1), v[-1][-1]
    for i in reversed(range(n)):
        for j in reversed(range(i)):
            if val in v[j]:
                break
        else:
            sol[i - 1], val = 1, val - p[i - 1]
    return sol
