"""
15.5 Optimal binary search trees
================================

Suppose we are designing a program to translate text from English to French. For each
occurrence of each English word in the text, we need to look up its French equivalent.
We could perform these lookup operations by building a binary search tree with n English
words as keys and their French equivalents as satellite data. Because we will search the
tree for each individual word in the text, we want the total time spent searching to be
as low as possible. We could ensure an O(lg n) search time per occurrence by using a
balanced BST. Words appear with different frequencies, however, and a frequently used
word such as "the" may appear far from the root while a rarely used word may appear near
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

Intuition
---------

We are given a set of keys, the probabilities of successful searches for each key (p),
and the probabilities of unsuccessful searches for each key (q). The cost of a search is
the height of a node times its probability.

keys:       10,         20,         30,         40
p:          0.1,        0.2,        0.1,        0.2
q:      0.1,    0.05,       0.15,       0.05,       0.05

p_0 is the probability of searching for 10.
q_0 is the probability of searching (-float("inf"), 9).
q_4 is the probability of searching (41, float("inf")).

If 20 is the root, 10 is the left child of 20, 30 is the right child of 20 and 40 is the
right child of 30, then the cost for successful searches would be:

c(k) = height * p[k]
c(20) = 1 * 0.2
c(10) = 2 * 0.1
c(30) = 2 * 0.1
c(40) = 3 * 0.2

The calculation of the w matrix involves prefixes that can be reused. For example:

w[0][2] = q[0] + p[1] + q[1] + p[2] + q[2]
w[0][3] = q[0] + p[1] + q[1] + p[2] + q[2] + p[3] + q[3]

The matrix e contains the expected cost of a subtree with keys k_i, ..., k_j. If e[i][j]
= e[1][2] = 0.90, then this means that the OBST with keys k_1 and k_2 has an expected
cost of 0.90.

The matrix w contains the sum of probabilities for a subtree with keys k_i, ..., k_j.
Element w[i][j] denotes the sum of all the probabilities in the subtree with keys
k_i, ..., k_j. Thus, if p_1 = 0.15, p_2 = 0.10, q_0 = 0.05, q_1 = 0.10, and q_2 = 0.05,
then w[0][2] = 0.45 is the sum of all the p's and q's from 0 to 2.

The matrix r contains the index r for which k_r is the root of an OBST containing keys
k_i, ..., k_j. If element r[i][j] = r[1][2] = 1, then this means that the OBST with keys
k_1 and k_2 has k_1 as its root.

Complexity
==========

Time
----

obst_bu(): O(n^3).

Space
-----

obst_bu(): O(n^2) for w table, O(n^2) for e table, and O(n^2) for root table.
"""


def obst_bu(p, q):
    n = len(p)
    e = [[0] * n for _ in range(n)]
    r = [[0] * n for _ in range(n)]
    w = [[0] * n for _ in range(n)]
    for i in range(n):
        e[i][i] = w[i][i] = q[i]
    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            e[i][j], w[i][j] = float("inf"), w[i][j - 1] + p[j] + q[j]
            for k in range(i, j):
                t = e[i][k] + e[k + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j], r[i][j] = t, k + 1
    return e, r, w


def obst(r, i=None, j=None, last=0, sol=None):
    if sol is None:
        i, j, sol = 0, len(r) - 1, []
    if i != j:
        node, parent = str(r[i][j]), str(last)
        if last == 0:
            sol.append(node + " is the root")
        elif j < last:
            sol.append(node + " is the left child of " + parent)
        else:
            sol.append(node + " is the right child of " + parent)
        sol = obst(r, i, r[i][j] - 1, r[i][j], sol)
        sol = obst(r, r[i][j], j, r[i][j], sol)
    return sol
