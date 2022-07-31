"""
Trapping Rain Water
-------------------

Given n non-negative integers representing an elevation map where the width of each bar
is 1, compute how much water it can trap after raining.

Intuition
---------

For each element in the array, we find the maximum level of water it can trap after the
rain, which is equal to the minimum of maximum height of bars on both the sides minus
its own height.



Complexity
==========

Time
----

trap(height): O().

Space
-----

trap(height): O().
"""


def sol(height):
    areas = max_l = max_r = 0
    l, r = 0, len(height) - 1
    while l < r:
        if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            else:
                areas += max_l - height[l]
            l += 1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                areas += max_r - height[r]
            r -= 1
    return areas
