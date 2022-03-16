"""
Largest Rectangle in Histogram
------------------------------

Given an array of integers heights representing the histogram's bar height where the
width of each bar is 1, return the area of the largest rectangle in the histogram.

Intuition
---------

Divide and Conquer Approach

This approach relies on the observation that the rectangle with maximum area will be the
maximum of:

    1. The widest possible rectangle with height equal to the height of the shortest
bar.
    2. The largest rectangle confined to the left of the shortest bar (subproblem).
    3. The largest rectangle confined to the right of the shortest bar (subproblem).

Stack Approach

1. Maintain a stack such that heights are always in increasing order.
2. When we see a column that's lower than what's on the stack:
    - Use it as the right side and compute all the possible rectangles using what's on
the stack to derive left side and height.
    - Remove each considered rectangle / column from the stack.

Complexity
==========

Time
----

largestRectangleArea_dc(heights): O(n * lg n)/O(n^2) average/worst case. Worst case
occurs if the heights are sorted.
largestRectangleArea_stack(heights): O(n).

Space
-----

largestRectangleArea_dc(heights): O(n).
largestRectangleArea_stack(heights): O(n).
"""


def sol_dc(heights):
    def calculate_area(heights, start, end):
        if start <= end:
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(
                heights[min_index] * (end - start + 1),
                calculate_area(heights, start, min_index - 1),
                calculate_area(heights, min_index + 1, end),
            )
        return 0

    return calculate_area(heights, 0, len(heights) - 1)


def sol_stack(heights):
    max_area, stack, heights = 0, [], [0] + heights + [0]
    for i, height in enumerate(heights):
        while stack and stack[-1][1] > height:
            r, h, l = i, stack.pop()[1], stack[-1][0]
            max_area = max((r - l - 1) * h, max_area)
        stack.append((i, height))
    return max_area
