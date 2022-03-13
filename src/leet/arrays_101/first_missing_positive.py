"""
First Missing Positive
----------------------

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Intuition
---------

We will partition the array into two sides, with one copy of each number on the left, in
order, when possible:

    [1, 2, 3, 4, 5, ..., n][..., everything else except for n + 1, ...]

Call left the interval [1, ..., i - 1] and right the interval
[nums[j], nums[len(nums) - 1]].

Initially, both are empty. At the end, when i and j meet, call the result final_left and
final_right. Then, the answer to the problem is 1 + len(final_left).

We build these intervals in-place, by swapping elements when necessary and updating i
and j.

If val == i + 1, then the number is in the right place and we may consider it as part of
the interval left and increment i.

If any of the below statements are true, then the number doesn't belong in the interval
final_left and so we can put it into the interval final_right (via swapping) and advance
j. After the swap, nums[i] has some new value that we haven't considered before, so we
leave i as is and loop again:

    1. If val > j, then this number should go into the interval final_left but it would
overlap with the interval final_right.

    2. If val <= 0, then the number is negative and it cannot possibly belong in the
interval final_left.

    3. If nums[val - 1] == val, then this number is a duplicate and doesn't belong in
the interval final_left.

Otherwise, we don't yet know whether val should be in the interval final_left or
final_right, so put it in neither. In order to consider another value, place val so that
it matches its own index; that is, place it where it will be if it indeed ends up in
the interval final_left, and next consider the element there. We learned nothing new
about what elements will be in the interval final_left or the interval final_right, and
nums[i] has the previous value of nums[val - 1], which we haven't dealt with yet. So
continue the loop without advancing either pointer. But we did make useful progress in
this branch: now in the future, if we see the same val again, we will know it's a
duplicate, because of the nums[val - 1] == val check above.

Complexity
==========

Time
----

firstMissingPositive(nums): O(n).

Space
-----

firstMissingPositive(nums): O(1).
"""


def sol(nums):
    i, j = 0, len(nums)
    while i != j:
        val = nums[i]
        if val == i + 1:
            i += 1
        elif val > j or val <= 0 or nums[val - 1] == val:
            j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            nums[i], nums[val - 1] = nums[val - 1], nums[i]
    return i + 1
