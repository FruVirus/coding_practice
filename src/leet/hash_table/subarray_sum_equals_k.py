"""
Subarray Sum Equals K
---------------------

Given an array of integers nums and an integer k, return the total number of subarrays
whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

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
    n = len(nums)
    count = 0
    dict_cumsum = defaultdict(
        int
    )  # hashtable for storing the cumsum we have seen so far
    curr_sum = 0  # for cumulative sum at each index
    for i in range(0, n):  # upto the length of the nums array
        curr_sum += nums[i]  # cumulative sum in each index
        if curr_sum == k:  # if current cumsum is equal to target
            count += 1
        # if curr_sum - k in the dict, then let's say
        # curr_sum - k = some_val. so, curr_sum = k + some_val, means
        # if the some_val is already in the dictionary, then there
        # exists a subarray whose sum is k that has lead us to this
        # curr_sum. How lead us? by some_val + k = curr_sum
        # now if some_val occurs more than 1 time, means you have
        # that number of subarray to consider to the count
        # So you need to add that number of occurence of curr_sum - k
        # to the count
        # think about this with example nums list in the solution
        # [3,4,7,2,-3,1,4,2] and also with [3,4,7,2,-3,1,4,2, 1]
        if curr_sum - k in dict_cumsum:
            count += dict_cumsum[curr_sum - k]
        # add the curr_sum entry to the hashtable
        dict_cumsum[curr_sum] += 1
    # print(dict_cumsum)
    return count
