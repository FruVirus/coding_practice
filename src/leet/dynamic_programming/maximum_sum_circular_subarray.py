"""
Maximum Sum Circular Subarray
-----------------------------

Given a circular integer array nums of length n, return the maximum possible sum of a
non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array.
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of
nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once.
Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist
i <= k1, k2 <= j with k1 % n == k2 % n.

Intuition
---------

There can be two cases for the maximum sum:

    1. The elements that contribute to the maximum sum are arranged such that no
wrapping is there. For example: [-10, 2, -1, 5] and [-2, 4, -1, 4, -1]. In this case,
Kadane's algorithm will produce the result.

    2. The elements that contribute to the maximum sum are arranged such that wrapping
is there. For example: [10, -12, 11] and [12, -5, 4, -8, 11]. In this case, we change
wrapping to non-wrapping. Wrapping of contributing elements implies non-wrapping of
non-contributing elements. Thus, find out the sum of non-contributing elements and
subtract this sum from the total sum. To find the sum of non-contributing elements,
invert the sign of each element and then run Kadane's algorithm (our array is like a
ring and we have to eliminate the maximum continuous negative which is the maximum
continuous positive in the inverted array).

Finally, we compare the sum obtained in both cases and return the maximum of the two
sums.

Note: We can't just return max(max_nonwrap, max_wrap) in case nums contains all
negatives. For example, if nums = [-3, -2, -3], then max_nonwrap = -2 and max_wrap = 0,
and we would return 0 instead of -2.

Complexity
==========

Time
----

maxSubarraySumCircular(nums): O(n).

Space
-----

maxSubarraySumCircular(nums): O(n) for the inverted array.
"""


def sol_bu(nums):
    def kadane(a):
        curr = best = a[0]
        for i in range(1, len(a)):
            curr = max(curr + a[i], a[i])
            best = max(best, curr)
        return best

    inv_nums = [-num for num in nums]
    max_nonwrap = kadane(nums)
    max_wrap = -(sum(inv_nums) - kadane(inv_nums))
    return max_nonwrap if max_wrap == 0 else max(max_nonwrap, max_wrap)
