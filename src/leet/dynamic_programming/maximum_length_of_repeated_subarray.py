"""
Maximum Length of Repeated Subarray
-----------------------------------

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that
appears in both arrays.

Intuition
---------

Since a common subarray of A and B must start at some A[i] and B[j], let dp[i][j] be the
longest common prefix of A[i:] and B[j:]. Whenever A[i] == B[j], we know dp[i][j] =
dp[i + 1][j + 1] + 1. Also, the answer is max(dp[i][j]) over all i, j. Our loop
invariant is that the answer is already calculated correctly and stored in dp for any
larger i, j.

Complexity
==========

Time
----

findLength(nums1, nums2): O(m * n).

Space
-----

findLength_bu(nums1, nums2): O(min(m, n)).
"""


def sol_bu(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n, longest = len(nums1), len(nums2), 0
    prev, curr = [0] * (m + 1), [0] * (m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cond = nums1[j - 1] == nums2[i - 1]
            curr[j] = 1 + prev[j - 1] if cond else 0
        longest = max(longest, max(curr))
        prev, curr = curr, prev
    return longest
