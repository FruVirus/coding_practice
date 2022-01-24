"""
Overview
========

Catalan numbers are a sequence of natural numbers that occur in many interesting
counting problems like the following:

1. Count the number of expressions containing n pairs of parentheses which are correctly
matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

2. Count the number of possible binary search trees with n keys.

3. Count the number of full binary trees (a rooted binary tree is full if every vertex
has either two children or no children) with n + 1 leaves.

4. Given a number n, return the number of ways you can draw n chords in a circle with
2 x n points such that no 2 chords intersect.

5. How many paths are there from (0, 0) to (n, n) without crossing the main diagonal
line that goes from (0, 0) to (n, n)? For this problem, if you write out the possible
combination of East (E) and North (N) paths from (0, 0) to (n, n), you'll see that the
paths must always have as many E's as N's. In other words, a path like EENNENEN can be
interpreted as (())()(), where the E's are left parens and the N's are right parens.

Complexity
==========

The recursive algorithm for finding the Catalan numbers is given by:

def catalan(n):
    return 1 if n <= 1 else sum(catalan(i) * catalan(n - i - 1) for i in range(n))

This algorithm has exponential time complexity depending on the Catalan number
requested and is inefficient. Thus, we use dynamic programming to help us store
previously calculated values.

Time
----

catalan_bu() and catalan_td(): O(n^2).
"""


def catalan_bu(n, sol):
    sol[0] = sol[1] = 1
    for i in range(2, n + 1):
        for j in range(i):
            sol[i] += sol[j] * sol[i - j - 1]


def catalan_td(n, sol):
    if sol[n] > 0:
        c = sol[n]
    elif n == 0:
        c = 1
    else:
        c = sum(catalan_td(i, sol) * catalan_td(n - i - 1, sol) for i in range(n))
    sol[n] = c
    return c


def catalan(n, td=False):
    sol = [0] * (n + 1)
    catalan_ = catalan_td if td else catalan_bu
    catalan_(n, sol)
    return sol, sol[n]
