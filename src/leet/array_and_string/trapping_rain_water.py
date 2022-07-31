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

Notice that as long as right_max[i] > left_max[i] (from element 0 to 6), the water
trapped depends upon the left_max, and similar is the case when
left_max[i] > right_max[i] (from element 8 to 11). So, we can say that if there is a
larger bar at one end (say right), we are assured that the water trapped would be
dependant on height of bar in current direction (from left to right). As soon as we find
the bar at other end (right) is smaller, we start iterating in opposite direction (from
right to left). We must maintain left_max and right_max during the iteration, but now we
can do it in one iteration using 2 pointers, switching between the two.

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
