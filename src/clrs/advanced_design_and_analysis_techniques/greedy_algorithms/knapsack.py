"""
16.2 Elements of the greedy strategy
====================================

Greedy versus dynamic programming
---------------------------------

In the (fractional) Knapsack problem, the setup is the same as the 0/1 Knapsack problem,
except that we can take fractions of items, rather than having to make a binary (0/1)
choice for each item.

If we remove a weight w of one item j from the optimal load, the remaining load must be
the most valuable load weighing at most W - w that we can take from n - 1 original items
plus w_j - w pounds of item j.

To solve the fractional problem, we first compute the value per pound v_i / w_i for each
item. Obeying the greedy strategy, we begin by taking as much as possible of the item
with the greatest value per pound. If the supply of that item is exhausted and we can
still carry more, then we take as much as possible of the item with the next greatest
value per pound, and so forth, until we reach the weight limit W. Thus, by sorting the
items by value per pound, the greedy algorithm runs in O(n * lg n) time.

Taking item 1 doesn't work in the 0/1 problem because if we are unable to fill the
knapsack to exact capacity, then the remaining space lowers the effective value per
pound of the knapsack load. In the 0/1 problem, when we consider whether to include an
item in the knapsack, we must compare the solution to the subproblem that includes the
item with the solution to the subproblem that excludes the item before we can make the
choice. The problem formulated in this way gives rise to many overlapping subproblems---
a hallmark of dynamic programming.

Complexity
==========

Time
----

ks_bottom_up(): O(n * lg n).
ks_top_down(): O(n * lg n).
"""


def ks_bottom_up(c, w, p_w_index, sol):
    for i in p_w_index:
        if c - w[i] >= 0:
            c -= w[i]
            sol.append((i, 1))
        else:
            sol.append((i, c / w[i]))
            break
    return sol


def ks_top_down(c, w, p_w_index, sol):
    if c - w[p_w_index[0]] >= 0:
        sol.append((p_w_index[0], 1))
        ks_top_down(c - w[p_w_index[0]], w, p_w_index[1:], sol)
    else:
        sol.append((p_w_index[0], c / w[p_w_index[0]]))
    return sol


def ks_solution(p, w, c, top_down=False):
    p_w, sol = [i / j for i, j in zip(p, w)], []
    p_w_index = sorted(range(len(p_w)), key=lambda x: p_w[x], reverse=True)
    ks = ks_top_down if top_down else ks_bottom_up
    ks(c, w, p_w_index, sol)
    return sol, sum(i[1] * p[i[0]] for i in sol)
