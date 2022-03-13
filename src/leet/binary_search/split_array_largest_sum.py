"""
Split Array Largest Sum
-----------------------

Given an array nums which consists of non-negative integers and an integer m, you can
split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

Intuition
---------

The goal of this problem is to find the minimum largest subarray sum with m subarrays.
Instead of finding the answer directly, what if we try to guess the answer (say X), and
check whether this particular value could be the largest subarray sum with m subarrays.
If this is possible, we can check all values for X >= 0, and the first value that
satisfies the condition will be the answer. Thus, by repeatedly solving the following
problem, we can find the minimum largest subarray sum needed to split nums into m
subarrays:

    Given an array of n integers and a value X, determine the minimum number of
subarrays the array needs to be divided into such that no subarray sum is greater than
X.

If the minimum number of subarrays required is less than or equal to m then the value X
could be the largest subarray sum.

The solution to this newly defined problem is as follows

    1. First, make sure X is greater than or equal to the maximum element in the array.
Otherwise, no solution would be possible because we cannot divide an element.

    2. Start from 0th index and keep adding elements to sum only if adding the element
does not make sum greater than X.

    3. If adding the current element would make the sum greater than X then we have to
split the subarray here. So we will increment the number of splits required and set sum
to the value of current element (signifying that the current subarray only contains the
current element).

    4. Once we traversed the whole array, return splitsRequired + 1. This is the minimum
number of subarrays required.

Now the issue with the current solution is that the value of X can be as large as the
sum of integers in the given array. Hence, checking for all values of X is not feasible.

The key observation here is that if we are able to split the array into m or fewer
subarrays for a value X then we will also be able to do it for any value greater than X.
This is because the number of subarrays would be even less in case of any value greater
than X. Similarly, if it's not possible for a value X it will not be possible to have m
or fewer splits for any value less than X.

Therefore, instead of searching linearly for X, we can do a binary search! If we can
split the array into m or fewer subarrays all with a sum that is less than or equal to X
then we will try a smaller value for X otherwise we will try a larger value for X. Each
time we will select X so that we reduce the size of the search space by half.

Complexity
==========

Time
----

splitArray(nums, m): O(n * lg s), where n is the length of nums and s is the sum of
integers in the nums.

Space
-----

splitArray(nums, m): O(1).
"""


def sol(nums, m):
    def get_num_splits(max_sum):
        curr_sum = num_splits = 0
        for num in nums:
            if curr_sum + num <= max_sum:
                curr_sum += num
            else:
                curr_sum, num_splits = num, num_splits + 1
        return num_splits + 1

    low, high = max(nums), sum(nums)
    while low <= high:
        mid = low + (high - low) // 2
        if get_num_splits(mid) > m:
            low = mid + 1
        else:
            max_sum, high = mid, mid - 1
    return max_sum
