"""
16.2 Elements of the greedy strategy
====================================

Greedy versus dynamic programming
---------------------------------

In the fractional knapsack problem, the setup is the same as the 0/1 knapsack problem,
except that we can take fractions of items, rather than having to make a binary (i.e.,
0/1) choice for each item.

If we remove a weight w of one item j from the optimal load, the remaining load must be
the most valuable load weighing at most W - w that we can take from n - 1 original items
plus w_j - w pounds of item j.

To solve the fractional problem, we first compute the value per pound v_i / w_i for each
item. Obeying the greedy strategy, we begin by taking as much as possible of the item
with the greatest value per pound. If the supply of that item is exhausted and we can
still carry more, then we take as much as possible of the item with the next greatest
value per pound, and so forth, until we reach the weight limit W. Thus, by sorting the
items by value per pound, the greedy algorithm runs in O(n * lg n) time.

Taking an item with the greatest value per pound doesn't always work in the 0/1 problem
because if we are unable to fill the knapsack to exact capacity, then the remaining
space lowers the effective value per pound of the knapsack load. In the 0/1 problem,
when we consider whether to include an item in the knapsack, we must compare the
solution to the subproblem that includes the item with the solution to the subproblem
that excludes the item before we can make the choice. The problem formulated in this way
gives rise to many overlapping subproblems---a hallmark of dynamic programming.

Intuition
---------

Since we can take fractional items, we compute the value per pound for each item. The
greedy strategy is to begin by taking as much as possible of the item with the greatest
value per pound. If the supply of that item is exhausted and the knapsack can still
carry more, then we take as much as possible of the item with tne next greatest value
per pound, and so forth, until we reach the maximum capacity of the knapsack.

sol is a list of tuples where the first element in the tuple denotes the index of the
item to take and the second element in the tuple denotes the fractional amount of the
item to take.

Complexity
==========

The time complexity is primarily set by the complexity of the algorithm used to sort the
items by value per pound.

Time
----

ks_bu() and ks_td(): O(n * lg n).
"""


def ks_bu(w, c, pw_index, sol):
    for i in pw_index:
        if c - w[i] >= 0:
            sol.append((i, 1))
            c -= w[i]
        else:
            sol.append((i, c / w[i]))
            break


def ks_td(w, c, pw_index, sol):
    w_index = pw_index[0]
    if c - w[w_index] >= 0:
        sol.append((w_index, 1))
        ks_td(w, c - w[w_index], pw_index[1:], sol)
    else:
        sol.append((w_index, c / w[w_index]))


def ks(p, w, c, td=False):
    pw, sol = [i / j for i, j in zip(p, w)], []
    pw_index = sorted(range(len(pw)), key=lambda x: pw[x], reverse=True)
    ks_ = ks_td if td else ks_bu
    ks_(w, c, pw_index, sol)
    return sol, sum(i[1] * p[i[0]] for i in sol)
