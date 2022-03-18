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

If we have not run out of numbers to add, then there are k remaining values to add to
the sum. The average value of these values is at least target // k.

We cannot obtain a sum of target if the smallest value in nums is greater than
target // k or if the largest value in nums is smaller than target // k.

Complexity
==========

Time
----

fourSum(nums, target): O(n^(k - 1)). We have k - 2 loops iterating over n elements and
twosum is O(n). Note that for k > 2, sorting the array does not change the overall time
complexity.

Space
-----

fourSum(nums, target): O(n), for the has set.
"""


# pylint: disable=R1260,C0200,W0612


def sol(nums, target):
    def ksum(nums, target, k):
        average_value, sol = target // k, []
        if not nums or average_value < nums[0] or nums[-1] < average_value:
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
        for i in range(len(nums)):
            if (not sol or sol[-1][1] != nums[i]) and target - nums[i] in com:
                sol.append([target - nums[i], nums[i]])
            com.add(nums[i])
        return sol

    def twosum_pointers(nums, target):
        low, high, sol = 0, len(nums) - 1, []
        n = high
        while low < high:
            curr_sum = nums[low] + nums[high]
            if curr_sum < target or (low > 0 and nums[low] == nums[low - 1]):
                low += 1
            elif curr_sum > target or (high < n and nums[high] == nums[high + 1]):
                high -= 1
            else:
                sol.append([nums[low], nums[high]])
                low += 1
                high -= 1
        return sol

    nums.sort()
    return ksum(nums, target, 4)
