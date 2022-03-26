"""
kSum
----

Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct.
    - nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Intuition
---------

The two pointers pattern requires the array to be sorted, so we do that first. Also,
it's easier to deal with duplicates if the array is sorted: repeated values are next to
each other and easy to skip.

The hash implementation here is almost the same as in Two Sum: One-pass Hash Table. The
only difference is the check to avoid duplicates. Since the array is sorted, we can
just compare the found pair with the last one in the result sol.

If we have not run out of numbers to add, then there are k remaining values to add to
the sum. The average value of these values is at least target // k.

We cannot obtain a sum of target if the smallest value in nums is greater than
target // k or if the largest value in nums is smaller than target // k.

Consider the three sum problem:

nums = [-4, -1, -1, 0, 1, 2], target = 0, k = 3

The values for nums, target, and k passed to ksum in each iteration of the main for-loop
in ksum are:

[-1, -1, 0, 1, 2], -4, 2
[-1, 0, 1, 2], -1, 2
[1, 2], 0, 2
[2], 1, 2
[], 2, 2

Basically, in each iteration of the main for-loop, we take the i-th element in nums and
see if we can make a sum of target - nums[i] with k - 1 elements in the subarray that
does not contain the i-th element. We skip over the second -1 since that would lead to a
duplicate answer of [-1, 0, 1].

When k = 2, then we have the base recursion problem of twosum, which we can solve
directly using either the hash or two pointers approach.

Complexity
==========

Time
----

fourSum(nums, target, k): O(n^(k - 1)). We have k - 2 loops iterating over n elements
and twosum is O(n). Note that for k > 2, sorting the array does not change the overall
time complexity.

Space
-----

fourSum(nums, target, k): O(n), for the hash set.
"""


# pylint: disable=R1260,C0200,W0612


def sol(nums, target, k):
    def ksum(nums, target, k):
        avg_value, sol = target // k, []
        if not nums or avg_value < nums[0] or avg_value > nums[-1]:
            return sol
        if k == 2:
            return twosum_hash(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in ksum(nums[i + 1 :], target - nums[i], k - 1):
                    sol.append([nums[i]] + subset)
        return sol

    def twosum_hash(nums, target):
        com, sol = set(), []
        for num in nums:
            if (not sol or sol[-1][1] != num) and target - num in com:
                sol.append([target - num, num])
            com.add(num)
        return sol

    def twosum_pointers(nums, target):
        low, high = 0, len(nums) - 1
        n, sol = high, []
        while low < high:
            num = nums[low] + nums[high]
            if num < target or (low > 0 and nums[low] == nums[low - 1]):
                low += 1
            elif num > target or (high < n and nums[high] == nums[high + 1]):
                high -= 1
            else:
                sol.append([nums[low], nums[high]])
                low += 1
                high -= 1
        return sol

    nums.sort()
    return ksum(nums, target, k)
