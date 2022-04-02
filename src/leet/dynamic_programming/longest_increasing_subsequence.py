"""
Longest Increasing Subsequence
------------------------------

Given an integer array nums, return the length of the longest strictly increasing
subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no
elements without changing the order of the remaining elements. For example, [3, 6, 2, 7]
is a subsequence of the array [0, 3, 1, 6, 2, 2, 7].

Intuition
---------

We need a way to transition between states, such as dp[5] and dp[7]. This is called a
recurrence relation and can sometimes be tricky to figure out. Let's say we know dp[0],
dp[1], and dp[2]. How can we find dp[3] given this information? Well, since dp[2]
represents the length of the longest increasing subsequence that ends with nums[2], if
nums[3] > nums[2], then we can simply take the subsequence ending at i = 2 and append
nums[3] to it, increasing the length by 1. The same can be said for nums[0] and nums[1]
if nums[3] is larger. Of course, we should try to maximize dp[3], so we need to check
all 3. Formally, the recurrence relation is: dp[i] = max(dp[j] + 1) for all j where
nums[j] < nums[i] and j < i.

Binary Search Algorithm

It appears the best way to build an increasing subsequence is: for each element num, if
num is greater than the largest element in our subsequence, then add it to the
subsequence. Otherwise, perform a linear scan through the subsequence starting from the
smallest element and replace the first element that is greater than or equal to num with
num. This opens the door for elements that are greater than num but less than the
element replaced to be included in the sequence.

One thing to add: this algorithm does not always generate a valid subsequence of the
input, but the length of the subsequence will always equal the length of the longest
increasing subsequence. For example, with the input [3, 4, 5, 1], at the end we will
have sub = [1, 4, 5], which isn't a subsequence, but the length is still correct. The
length remains correct because the length only changes when a new element is larger than
any element in the subsequence. In that case, the element is appended to the subsequence
instead of replacing an existing element.

Since sub is in sorted order, we can use binary search instead to greatly improve the
efficiency of our algorithm.

Complexity
==========

Time
----

lengthOfLIS_bu(nums): O(n^2).
lengthOfLIS_bs(nums): O(n * lg n).

Space
-----

lengthOfLIS_bu(nums) and lengthOfLIS_bs: O(n).
"""


def sol_bu(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def sol_bs(nums):
    sub = [nums[0]]
    for num in nums[1:]:
        if num > sub[-1]:
            sub.append(num)
        else:
            low, high = 0, len(sub) - 1
            while low < high:
                mid = low + (high - low) // 2
                if sub[mid] < num:
                    low = mid + 1
                else:
                    high = mid
            sub[low] = num
    return len(sub)
