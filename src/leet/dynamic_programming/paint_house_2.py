"""
Paint House II
--------------

There are a row of n houses, each house can be painted with one of the k colors. The
cost of painting each house with a certain color is different. You have to paint all the
houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost
matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is
the cost of painting house 1 with color 2, and so on...

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

However, we don't need to look at the entire previous row for every cell. When we're
calculating the values for the second row, we're adding the minimum from the first row
onto them. The only cell we can't do this for is the one that was directly below the
minimum, as this would break the adjacency rule. For this one, it makes sense to add the
second minimum.

There is another way we can still solve the problem in O(1) space and O(n * k) time
complexity, and preserving the input. The only thing the algorithm in the previous
approach is really doing is going through the rows, and finding the 2 minimums of each
row. It does this by calculating all the new costs for the row, writing them into the
input, and then finding the minimums. This overwriting isn't necessary though—we can
simply keep track of the 2 smallest values we've seen so far, as we go, in the current
row. We also need to remember the 2 from the previous row.

Complexity
==========

Time
----

minCost_bu(costs): O(n * k), where n is the number of houses and the k is the number of
colors.
minCost_td(costs): O(n * k^2), where n is the number of houses and the k is the number
of colors.

Space
-----

minCost_bu(costs): O(1).
minCost_td(costs): O(n * k).
"""


def sol_bu(costs):
    n, k, prev_min_color = len(costs), len(costs[0]), None
    prev_min_cost = prev_second_min_cost = float("inf")
    for color, cost in enumerate(costs[0]):
        if cost < prev_min_cost:
            prev_min_color = color
            prev_min_cost, prev_second_min_cost = cost, prev_min_cost
        elif cost < prev_second_min_cost:
            prev_second_min_cost = cost
    for i in range(1, n):
        min_color = None
        min_cost = second_min_cost = float("inf")
        for color in range(k):
            cost = costs[i][color]
            cost += prev_second_min_cost if color == prev_min_color else prev_min_cost
            if cost < min_cost:
                min_color = color
                min_cost, second_min_cost = cost, min_cost
            elif cost < second_min_cost:
                second_min_cost = cost
        prev_min_color = min_color
        prev_min_cost, prev_second_min_cost = min_cost, second_min_cost
    return prev_min_cost


def sol_td(costs):
    memo, n, k = {}, len(costs), len(costs[0])

    def dp(i, color):
        if i == n - 1:
            return costs[i][color]
        if (i, color) not in memo:
            cost = float("inf")
            for next_color in range(k):
                if next_color != color:
                    cost = min(cost, costs[i][color] + dp(i + 1, next_color))
            memo[(i, color)] = cost
        return memo[(i, color)]

    return min(dp(0, k_) for k_ in range(k))
