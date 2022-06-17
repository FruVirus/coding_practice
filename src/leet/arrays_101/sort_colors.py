"""
Sort Colors
-----------

Given an array nums with n objects colored red, white, or blue, sort them in-place so
that objects of the same color are adjacent, with the colors in the order red, white,
and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
respectively.

You must solve this problem without using the library's sort function.

Intuition
---------

Let's use here three pointers to track the rightmost boundary of zeros, the leftmost
boundary of twos and the current element under the consideration.

The idea of solution is to move curr pointer along the array, if nums[curr] = 0 - swap
it with nums[p0], if nums[curr] = 2 - swap it with nums[p2].

Complexity
==========

Time
----

sortColors(nums): O(n).

Space
-----

sortColors(nums): O(1).
"""


def sol(nums):
    i, j, k = 0, 0, len(nums) - 1
    while j <= k:
        if nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] == 2:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        else:
            j += 1
