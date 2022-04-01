"""
Delete and Earn
---------------

You are given an integer array nums. You want to maximize the number of points you get
by performing the following operation any number of times:

    - Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete
every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some
number of times.

Intuition
---------

At any operation, we pick a number, let's say x, and delete all occurrences of x - 1 and
x + 1. That means if x occurs multiple times in nums and we take one, we may as well
take all of them because after deleting all x - 1 and x + 1, we can only stand to gain
more points by taking additional x.

Before we start, we can simplify nums by collecting all duplicate numbers together. As
an example, nums can be represented as a hash map with numbers as keys which map to the
number of times the key occurs in nums. [2, 2, 3, 3, 3, 4] would be converted to
{2: 2, 3: 3, 4: 1}. Furthermore, since we are only really concerned about how many
points each number can give us, we can multiply the keys and values to represent how
many points taking the key will give us. In this case, we would have {2: 4, 3: 9, 4: 4}.

In the top-down approach, let's declare a function maxPoints. We want maxPoints(num) to
return the maximum points that we can gain if we only consider all the elements in nums
with values between 0 and num.

The second thing we need is a recurrence relation, a way to move between states. Let's
say that we are currently at some arbitrary number x, where x is in nums one or more
times. How can we find maxPoints(x)? When it comes to x, we have to make a choice: take,
or don't take.

    - If we take x, then we gain points equal to x times the number of times x occurs in
nums - we can pre-compute these values. For now, let's call this value gain. However,
because of the deletion, by taking x, we are no longer allowed to take x - 1. The
largest number that we can still consider is x - 2. Therefore, if we choose to take x,
then the most points that we can have here is gain + maxPoints(x - 2), where gain is how
many points we gain from taking x and maxPoints(x - 2) is the maximum number of points
we can obtain from the numbers between x - 2 and 0.

    - If we choose not to take x, then we don't gain any points here, but we still may
have accumulated some points from numbers smaller than x. Because we didn't take x, we
did not close the door to x - 1. In this case, the most points we can have here is
maxPoints(x - 1).

This forms our recurrence relation: for an arbitrary x, maxPoints(x) =
max(maxPoints(x - 1), maxPoints(x - 2) + gain), where gain is the number of points we
can gain from taking x.

The problem is, even though we figured out how to find maxPoints(x), how do we find
maxPoints(x - 1) and maxPoints(x - 2)? That would involve finding maxPoints(x - 3) and
maxPoints(x - 4) and so on.

The third component of a dynamic programming solution is base cases. Typically, we can
find base cases with a little bit of logical thinking. First, maxPoints(0) will always
be equal to 0. Second, when considering maxPoints(1), we only care about the elements 0
and 1. We do not care about 2 because of how we defined maxPoints(x). Looking at the
recurrence relation, we know that if we arrived at 1, it means that we must not have
taken 2, and because 1 times any quantity will be greater than or equal to the number of
points we can get from taking 0, we should always take 1 (if there are any).

With these base cases, we can find maxPoints(2). With maxPoints(2) calculated, we can
find maxPoints(3), all the way up to maxPoints(max(nums)). Remember, we defined
maxPoints(x) as the maximum points we can gain when we consider the numbers from 0 to x,
so maxPoints(max(nums)) covers the entire input, and stores the answer to the original
problem.

Complexity
==========

Time
----

deleteAndEarn(nums): O(n + k), where n is the length of nums and k is the maximum
element in nums. Because of cache, already solved sub-problems will only cost O(1) time.
Since max_num = k, we will solve k unique sub-problems.

Space
-----

deleteAndEarn(nums): O(n + k). points take up O(n) space in the worst case where every
element is nums is unique. The recursion call stack/array takes up O(k) space as does
the memo dict.
"""


# Standard Library
from collections import defaultdict


def sol_bu(nums):
    max_num, points = max(nums), defaultdict(int)
    for num in nums:
        points[num] += num
    max_points = [0] + [points[1]] + [0] * (max_num - 1)
    for num in range(2, len(max_points)):
        max_points[num] = max(max_points[num - 1], max_points[num - 2] + points[num])
    return max_points[max_num]


def sol_td(nums):
    memo, points = {}, defaultdict(int)
    for num in nums:
        points[num] += num

    def dp(num):
        if num < 2:
            return 0 if num == 0 else points[1]
        if num not in memo:
            memo[num] = max(dp(num - 1), dp(num - 2) + points[num])
        return memo[num]

    return dp(max(nums))
