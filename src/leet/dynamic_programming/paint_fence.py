"""
Paint Fence
-----------

You are painting a fence of n posts with k different colors. You must paint the posts
following these rules:

    - Every post must be painted exactly one color.
    - There cannot be three or more consecutive posts with the same color.
    - Given the two integers n and k, return the number of ways you can paint the fence.

Intuition
---------

If we have one post, there are k ways to paint it. If we have two posts, then there are
k * k ways to paint it (since we are allowed to paint have two posts in a row be the
same color). Therefore, totalWays(1) = k, totalWays(2) = k * k.

Let's think about how many ways there are to paint the i-th post. We have two options:

    1. Use a different color than the previous post. If we use a different color, then
there are k - 1 colors for us to use. This means there are (k - 1) * totalWays(i - 1)
ways to paint the i-th post a different color than the (i − 1)-th post.

    2. Use the same color as the previous post. There is only one color for us to use,
so there are 1 * totalWays(i - 1) ways to paint the i-th post the same color as the
(i − 1)-th post. However, we have the added restriction of not being allowed to paint
three posts in a row the same color. Therefore, we can paint the i-th post the same
color as the (i − 1)-th post only if the (i − 1)-th post is a different color than the
(i − 2)-th post. So, how many ways are there to paint the (i − 1)-th post a different
color than the (i − 2)-th post? Well, as stated in the first option, there are
(k - 1) * totalWays(i - 1) ways to paint the i-th post a different color than the
(i − 1)-th post, so that means there are 1 * (k - 1) * totalWays(i - 2) ways to paint
the (i − 1)-th post a different color than the (i − 2)-th post.

Complexity
==========

Time
----

numWays(n, k): O(n).

Space
-----

numWays_bu(n, k): O(1).
numWays_td(n, k): O(n).
"""


def sol_bu(n, k):
    if n <= 2:
        return k ** n
    one, two = k * k, k
    for _ in range(3, n + 1):
        one, two = (k - 1) * (one + two), one
    return one


def sol_td(n, k):
    memo = {}

    def dp(n):
        if n <= 2:
            return k ** n
        if n not in memo:
            memo[n] = (k - 1) * (dp(n - 1) + dp(n - 2))
        return memo[n]

    return dp(n)
