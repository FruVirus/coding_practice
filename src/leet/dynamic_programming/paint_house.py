"""
Paint House
-----------

There is a row of n houses, where each house can be painted one of three colors: red,
blue, or green. The cost of painting each house with a certain color is different. You
have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost
matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2]
is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.

Intuition
---------

First thing to realize is that we don't need to do anything to the last row. Like in the
tree, these costs are the total costs because there are no further houses after them.

Now, what about the second-to-last row? Well, we know that if we painted that house red,
that it'd cost itself and the cheapest out of blue and green from the next row, which is
8. So the total cost there would be 14, and we can put that into the cell.

Just like we did with the tree, we can work our way up through the grid, repeatedly
applying the same algorithm to determine the total value for each cell. Once we have
updated all the cells, we then simply need to take the minimum value from the first row
and return it.

We only needed to look at the previous row, and the row we're currently working on. The
rest could have been thrown away. So to avoid overwriting the input, we keep track of
the previous row and the current row as length-3 arrays.

Complexity
==========

Time
----

minCost(costs): O(n).

Space
-----

minCost_bu(costs): O(1), since we're only remembering up to 6 calculations using 2 x 3
arrays.
minCost_td(costs): O(n).
"""

# Standard Library
import copy


def sol_bu(costs):
    prev = costs[-1]
    for n in reversed(range(len(costs) - 1)):
        curr = copy.deepcopy(costs[n])
        curr[0] += min(prev[1], prev[2])
        curr[1] += min(prev[0], prev[2])
        curr[2] += min(prev[0], prev[1])
        prev = curr
    return min(prev)


def sol_td(costs):
    memo = {}

    def dp(n, color):
        total_cost = costs[n][color]
        if n == len(costs) - 1:
            return total_cost
        if (n, color) not in memo:
            if color == 0:
                total_cost += min(dp(n + 1, 1), dp(n + 1, 2))
            elif color == 1:
                total_cost += min(dp(n + 1, 0), dp(n + 1, 2))
            else:
                total_cost += min(dp(n + 1, 0), dp(n + 1, 1))
            memo[(n, color)] = total_cost
        return memo[(n, color)]

    return min(dp(0, 0), dp(0, 1), dp(0, 2))
