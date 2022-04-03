"""
Maximum Score from Performing Multiplication Operations
-------------------------------------------------------

You are given two integer arrays nums and multipliers of size n and m respectively,
where n >= m. The arrays are 1-indexed.

You begin with a score of 0. You want to perform exactly m operations. On the i-th
operation (1-indexed), you will:

    - Choose one integer x from either the start or the end of the array nums.
    - Add multipliers[i] * x to your score.
    - Remove x from the array nums.

Return the maximum score after performing m operations.

Intuition
---------

At each state, we have to perform an operation. As stated in the problem description, we
need to decide whether to take from the left end (nums[left]) or the right end
(nums[right]) of the current nums. Then we need to multiply the number we choose by
multipliers[i], add this value to our score, and finally remove the number we chose from
nums. For implementation purposes, "removing" a number from nums means incrementing our
state variables i and left so that they point to the next two left and right numbers.

Let mult = multipliers[i] and right = nums.length - 1 - (i - left). The only decision we
have to make is whether to take from the left or right of nums.

    - If we choose left, we gain mult * nums[left] points from this operation. Then, the
next operation will occur at (i + 1, left + 1). i gets incremented at every operation
because it represents how many operations we have done, and left gets incremented
because it represents how many left operations we have done. Therefore, our total score
is mult * nums[left] + dp(i + 1, left + 1).

    - If we choose right, we gain mult * nums[right] points from this operation. Then,
the next operation will occur at (i + 1, left). Therefore, our total score is
mult * nums[right] + dp(i + 1, left).

Since we want to maximize our score, we should choose the side that gives more points.
This gives us our recurrence relation:

    - dp(i, left) = max(
        mult * nums[left] + dp(i + 1, left + 1), mult * nums[right] + dp(i + 1, left)
    )

When i = m, that means we have no operations left. Therefore, we should return 0.

Complexity
==========

Time
----

maximumScore(nums, multipliers): O(m^2), where m is the length of multipliers.

Space
-----

maximumScore_bu(nums, multipliers): O(m).
maximumScore_td(nums, multipliers): O(m^2).
"""


def sol_bu(nums, mults):
    n, m = len(nums), len(mults)
    prev, curr = [0] * (m + 1), [0] * (m + 1)
    for i in reversed(range(m)):
        for left in range(i, -1, -1):
            mult, right = mults[i], n - (i - left) - 1
            curr[left] = max(
                mult * nums[left] + prev[left + 1], mult * nums[right] + prev[left]
            )
        prev, curr = curr, prev
    return prev[0]


def sol_td(nums, mults):
    n, m, memo = len(nums), len(mults), {}

    def dp(i, left):
        if i == m:
            return 0
        if (i, left) not in memo:
            mult, right = mults[i], n - (i - left) - 1
            memo[(i, left)] = max(
                mult * nums[left] + dp(i + 1, left + 1),
                mult * nums[right] + dp(i + 1, left),
            )
        return memo[(i, left)]

    return dp(0, 0)
