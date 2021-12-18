"""
15.5 Optimal binary search trees
================================

Suppose we are designing a program to translate text from English to French. For each
occurrence of a each English word in the text, we need to look up its French equivalent.
We could perform these lookup operations by building a binary search tree with n English
words as keys and their French equivalents as satellite data. Because we will search the
tree for each individual word in the text, we want the total time spent searching to be
as low as possible. We could ensure an O(lg n) search time per occurrence by using a
balanced BST. Words appears with different frequencies, however, and a frequently used
word suc as "the" may appear far from teh root while a rarely used word may appear near
the root. Such an organization would slow down the translation, since the number of
nodes visited when searching for a key in a BST equals one plus the depth of the node
containing the key. We want words that occur frequently in the text to be placed nearer
the root. Moreover, some words in the text might have no French translation, and such
words would not appear in the BST at all. How do we organize a BST so as to minimize the
number of nodes visited in all searches, given that we know how often each word occurs?

An optimal BST (OBST) is a BST whose total search cost is minimal. To construct an OBST,
we are given an ordered set of n distinct keys for the BST and for each key k_i, we have
a probability p_i that a search will be for k_i. Some searches may be for values not in
any of the keys, and so we also have n + 1 "dummy keys" representing values not in the
keys. For each dummy key d_i, we have a probability q_i that a search will correspond to
d_i. Each key k_i is an internal node, and each dummy key d_i is a leaf. Every search is
either successful (finding some key k_i) or unsuccessful (finding some dummy key d_i).

An OBST is not necessarily a tree whose overall height is smallest. Nor can we
necessarily construct an OBST by always putting the key with the greatest probability at
the root.

Complexity
==========

Time
----

obst_bottom_up(): O(n^3).

Space
-----

obst_bottom_up(): O(n^2) for w table, O(n^2) for e table, and O(n^2) for root table.
"""


def obst_bottom_up(p, q, n):
    e = [[0] * n for _ in range(n)]
    w = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]
    for i in range(n):
        e[i][i] = w[i][i] = q[i]
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            e[i][j], w[i][j] = float("inf"), w[i][j - 1] + p[j] + q[j]
            for r in range(i, j):
                t = e[i][r] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j], root[i][j] = t, r + 1
    return e, root, w


def obst_solution(root, i, j, last=0, obst=None):
    obst = obst or []
    if i != j:
        if last == 0:
            obst.append(str(root[i][j]) + " is the root")
        elif j < last:
            obst.append(str(root[i][j]) + " is the left child of " + str(last))
        else:
            obst.append(str(root[i][j]) + " is the right child of " + str(last))
        obst = obst_solution(root, i, root[i][j] - 1, root[i][j], obst)
        obst = obst_solution(root, root[i][j], j, root[i][j], obst)
    return obst
