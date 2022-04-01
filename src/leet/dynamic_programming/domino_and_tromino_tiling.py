"""
Domino and Tromino Tiling
-------------------------

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate
these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer
may be very large, return it modulo 10^9 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and
only if there are two 4-directionally adjacent cells on the board such that exactly one
of the tilings has both squares occupied by a tile.

Intuition
---------

For a board with width k, some of the possible tilings can directly be derived from the
two previous fully covered boards.

However, some of the possible tilings cannot be derived from previous fully covered
boards directly. Instead, they must be derived from partially covered boards with a
width of k - 1 (e.g., a fully covered board of width k = 3 can be derived from a
partially covered board of width k = 2).

Now, let's define:

    - Fully covered board: All tiles on board are covered by a domino or a tromino.
    - Partially covered board: Same as a fully covered board, except leave the tile in
the upper-right corner (the top row of the rightmost column) uncovered. Note, a board
with only the lower-right corner uncovered is also considered "partially covered."
However, as we will discover soon, we do not need to keep track of which corner is
uncovered because of symmetry.
    - f(k): The number of ways to fully cover a board of width k.
    - p(k): The number of ways to partially cover a board of width k.

We can determine the number of ways to fully or partially tile a board of width k by
considering every possible way to arrive at f(k) or p(k) by placing a domino or a
tromino.

All of the ways to arrive at a fully tiled board of width k are as follows:

    - From f(k − 1) we can add 1 vertical domino for each tiling in a fully covered
board with a width of k − 1.
    - From f(k − 2) we can add 2 horizontal dominos for each tiling in a fully covered
board with a width of k − 2.
        - Note that we don't need to add 2 vertical dominos to f(k − 2), since f(k − 1)
will cover that case and it will cause duplicates if we count it again.
    - From p(k − 1) we can add an L-shaped tromino for each tiling in a partially
covered board with a width of k − 1.
        - We will multiply by p(k − 1) by 2 because for any partially covered tiling,
there will be a horizontally symmetrical tiling of it. Logically, there must be an equal
number of ways to fully tile the board from both p(k − 1) states. So rather than count
the number of ways twice, we simply multiply the number of ways from one p(k − 1) state
by 2.

Summing the ways to reach f(k) gives us the following equation:

    - f(k) = f(k - 1) + f(k - 2) + 2 * p(k - 1)

Now that we know where tilings on f(k) are coming from, how about p(k)? Notice that p(k)
can come from the below scenarios:

    - Adding a tromino to a fully covered board of width k − 2 (i.e., f(k − 2))
    - Adding a horizontal domino to a partially covered board of width k − 1 (i.e.,
p(k − 1))

Thus, we arrive at the following conclusion for p(k):

    - p(k) = p(k - 1) + f(k - 2)

For the bottom-up approach, we initialize f and p according to the following base cases:

    - f(1) = 1 because to fully cover a board of width 1, there is only one way, add one
vertical domino.
    - f(2) = 2 because to fully cover a board of width 2, there are two ways, either add
two horizontal dominos or add two vertical dominos.
    - p(2) = 1 because to partially cover a board of width 2, there is only one way
using an L-shaped tromino (leave the upper-right corner uncovered).

However, based on the transition function, we find that only f(n − 1), f(n - 2) and
p(n - 1) are used in each iteration. Thus, instead of using an entire array to store
this information, we can use just 3 numeric variables to store the result of f(k − 1),
f(k - 2), and p(k - 1).

For the top-down approach, we start with the board with of n and recurse down to the
base cases of f(1), f(2), and p(2).

Complexity
==========

Time
----

numTilings(n): O(n), there will be n non-memoized calls to f(n) and p(n) for a total of
2 * n complexity. In addition, there will be 2 * n memoized calls to f(n) and n memoized
calls to p(n). Total is O(5 * n) = O(n).

Space
-----

numTilings_bu(n): O(1).
numTilings_td(n): O(n).
"""


def sol_bu(n):
    if n <= 2:
        return n
    f_prev, f_curr, p_curr = 1, 2, 1
    for _ in range(3, n + 1):
        temp = f_curr
        f_curr = (f_curr + f_prev + 2 * p_curr)
        p_curr = (p_curr + f_prev)
        f_prev = temp
    return f_curr


def sol_td(n):
    memof, memop = {}, {}

    def f(n):
        if n <= 2:
            return n
        if n not in memof:
            memof[n] = (f(n - 1) + f(n - 2) + 2 * p(n - 1))
        return memof[n]

    def p(n):
        if n == 2:
            return 1
        if n not in memop:
            memop[n] = (p(n - 1) + f(n - 2))
        return memop[n]

    return f(n)
