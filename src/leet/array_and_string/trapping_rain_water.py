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

If height[left] < height[right], then for pointer left, he knows a taller bar exists on
his right side, then if leftMax is taller than him, he can contain some water for sure.
So we go ans += (left_max - height[left]). But if leftMax is shorter than him, then
there isn't a left side bar can help him contain water, then he will become other bars'
leftMax. so execute (left_max = height[left]). Same idea for right part.

Complexity
==========

Time
----

trap(height): O(n).

Space
-----

trap(height): O(1).
"""


def sol(height):
    num_rain = max_l = max_r = 0
    l, r = 0, len(height) - 1
    while l < r:
        if height[l] < height[r]:
            if height[l] > max_l:
                max_l = height[l]
            else:
                num_rain += max_l - height[l]
            l += 1
        else:
            if height[r] > max_r:
                max_r = height[r]
            else:
                num_rain += max_r - height[r]
            r -= 1
    return num_rain
