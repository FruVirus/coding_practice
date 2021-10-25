"""
Overview
========

Catalan numbers are a sequence of natural numbers that occur in many interesting
counting problems like the following:

1. Count the number of expressions containing n pairs of parentheses which are correctly
matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).

2. Count the number of possible Binary Search Trees with n keys.

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

Exponential time complexity depending on the Catalan number requested (unless using
dynamic programming technique to store previously calculated values).
"""


def catalan(n):
    if n <= 1:
        return 1
    cat_num = 0
    for i in range(n):
        cat_num += catalan(i) * catalan(n - i - 1)
    return cat_num
