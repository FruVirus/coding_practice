"""
Subarray Sum Equals K
---------------------

Given an array of integers nums and an integer k, return the total number of subarrays
whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Intuition
---------

The HashMap will store with the key being any particular sum, and the value being the
number of times it has happened till the current iteration of the loop as we traverse
the array from left to right.

For example:
    k = 26.

    If a sub-array sums up to k, then the sum at the end of this sub-array will be
sumEnd = sumStart + k. That implies: sumStart = sumEnd - k. In the beginning of the
iteration, sumStart = 0.

    Suppose, at index 10, sum = 50, and the next 6 numbers are 8,-5,-3,10,15,1.

    At index 13, sum will be 50 again (the numbers from indexes 11 to 13 add up to 0).

    Then at index 16, sum = 76.

    Now, when we reach index 16, sumEnd - k = 76 - 26 = 50. So, if this is the end index
of a sub-array which sums up to k, then before this, just before the start of the
sub-array, the sum should be 50 (which it is).

    As we found sum = 50 at two places before reaching index 16, we indeed have two
sub-arrays which sum up to k (26): from indexes 14 to 16 and from indexes 11 to 16.

Complexity
==========

Time
----

subarraySum_one(nums, k): O(n^2).
subarraySum_two(nums, k): O(n).

Space
-----

subarraySum_one(nums, k): O(1).
subarraySum_two(nums, k): O(n).
"""

# Standard Library
from collections import defaultdict


def sol_one(nums, k):
    count, n = 0, len(nums)
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += nums[j]
            if sum_ == k:
                count += 1
    return count


def sol_two(nums, k):
    cum_sum, curr_sum, count = defaultdict(int), 0, 0
    for num in nums:
        curr_sum += num
        if curr_sum == k:
            count += 1
        if curr_sum - k in cum_sum:
            count += cum_sum[curr_sum - k]
        cum_sum[curr_sum] += 1
    return count
