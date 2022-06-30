"""
Partition Equal Subset Sum
--------------------------

Given a non-empty array nums containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.

Intuition
---------

The problem is similar to the classic Knapsack problem. The basic idea is to understand
that to partition an array into two subsets of equal sum say subSetSum, the totalSum of
given array must be twice the subSetSum

tatalSum = subSetSum ∗ 2

This could also be written as, subSetSum = totalSum / 2

Example:

Assume totalSum of an array is 20 and if we want to partition it into 2 subsets of equal
sum, then the subSetSum must be (20 / 2) = 10.

Now, the problem to find the subset with a sum equals a given target. Here target is
subSetSum.

It must be noted that the total sum of an array must be even, only then we can divide it
into 2 equal subsets. For instance, we cannot have an equal subSetSum for an array with
total sum as 21.

Finding a subset with a sum equal to a given target is different than Subarray sum
equals k. Subarray is a contiguous sequence of array elements, whereas the subset could
consist of any array elements regardless of the sequence. But each array element must
belong to exactly one subset.

We maintain a 2D array, dp[n][subSetSum]. For an array element i and sum j in array
nums, dp[i][j] = true if the sum j can be formed by array elements in subset
nums[0] ... nums[i], otherwise dp[i][j] = false.

dp[i][j] is true it satisfies one of the following conditions:

    - Case 1) sum j can be formed without including i-th element -->
if dp[i − 1][j] = true

    - Case 2) sum j can be formed including i-th element -->
if dp[i − 1][j − nums[i]] = true. In this case, we subtract nums[i] since that gives the
remanining sum to be satisified moving forward.

Complexity
==========

Time
----

canPartition_bu(nums) and canPartition_td(nums): O(m * n), where m is the subset sum and
n is the number of array elements.

Space
-----

canPartition_bu(nums): O(m).
canPartition_td(nums): O(m * n).
"""


def sol_bu(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    subset_sum = total_sum // 2
    dp = [False] * (subset_sum + 1)
    dp[0] = True
    for num in nums:
        for j in range(subset_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[subset_sum]


def sol_td(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    memo, subset_sum = {}, total_sum // 2

    def dp(n, subset_sum):
        if subset_sum == 0:
            return True
        if n == 0 or subset_sum < 0:
            return False
        if (n, subset_sum) not in memo:
            result = dp(n - 1, subset_sum - nums[n - 1]) or dp(n - 1, subset_sum)
            memo[(n, subset_sum)] = result
        return memo[(n, subset_sum)]

    return dp(len(nums) - 1, subset_sum)
