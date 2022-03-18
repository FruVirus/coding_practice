"""
Contains Duplicate III
----------------------

Given an integer array nums and two integers k and t, return true if there are two
distinct indices i and j in the array such that abs(nums[i] - nums[j]) <= t and
abs(i - j) <= k.

Intuition
---------

If we want the absolute difference between two numbers to be <= t, then this means we
want the bucket windows to be of size w = t + 1 so that we can index into buckets using
nums[i] // w.

If t = 3, then the bucket windows are of size 4 and:

    0 - 3 will go into bucket window 0.
    4 - 7 will go into bucket window 1.
    etc.

Because of the organization, whenever a new number comes in, we only have to check the
current bucket window and its adjacent neighbors to the left and right. All other bucket
windows will be out of the range of t (i.e., it will contain numbers whose absolute
difference with the new number will be greater than t). If the new number is in the
current bucket window, then we know that it satisfies the condition
abs(nums[i] - nums[j]) <= t. If we have to check adjacent bucket windows, then we also
need to check if the absolute difference is <= t.

To take into account the condition abs(i - j) <= k, we use a sliding window where we
delete the key at index nums[i - k] // w if i >= k.

Complexity
==========

Time
----

containsNearbyAlmostDuplicate(nums, k, t): O(n).

Space
-----

containsNearbyAlmostDuplicate(nums, k, t): O(min(n, k)).
"""


# pylint: disable=C0200


def sol(nums, k, t):
    b, w = {}, t + 1
    for i in range(len(nums)):
        j = nums[i] // w
        if j in b:
            return True
        if j - 1 in b and abs(nums[i] - b[j - 1]) < w:
            return True
        if j + 1 in b and abs(nums[i] - b[j + 1]) < w:
            return True
        b[j] = nums[i]
        if i >= k:
            del b[nums[i - k] // w]
    return False
