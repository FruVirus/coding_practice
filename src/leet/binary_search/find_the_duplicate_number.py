"""
Find the Duplicate Number
-------------------------

Given an array of integers nums containing n + 1 integers where each integer is in the
range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra
space.

Intuition
---------

Binary Search Approach

Consider an array that has n distinct numbers in the range [1, n]. For example:
[1, 2, 3, 4, 5]. If we pick any one of these 5 numbers and count how many numbers are
less than or equal to it, the answer will be equal to that number. So in
[1, 2, 3, 4, 5], if you pick the number 4, there's exactly 4 numbers that are less than
or equal to 4. If you pick 3, there's exactly 3 numbers that are less than or equal to
3, and so on.

However, when you have duplicates in the array, this count will exceed the number at
some point. For example: in [4, 3, 4, 5, 2, 4, 1], 3 has 3 numbers less than or equal to
it. However, the duplicate number will have a count of numbers less than or equal to
itself, that is greater than itself. In this example, 4, which is the duplicate, has 6
numbers that are less than or equal to it. Hence, the smallest number that satisfies
this property is the duplicate number.

In the binary search approach, instead of doing a linear scan from 1 to n, we can apply
a binary search with a goal of finding the smallest number that satisfies the
aforementioned property. We start with a search space of [1, n] that has a midpoint mid.
If mid satisfies the property, we narrow our search space to the left half [1, mid - 1]
and continue searching. Otherwise, we narrow our search space to the right half
[mid + 1, n].

NB: Binary search will be applied to the numbers in the range [1, n] (inclusive)
regardless of the contents of the array. So even if a number does not exist in the
array, we will still evaluate it. For example, if the array is [1, 2, 4, 2, 5], the
algorithm will first evaluate the number 3 even though that number does not exist in the
array.

Floyd's Algorithm Approach

The idea is to reduce the problem to finding the cyclic node in a linked list.

First of all, where does the cycle come from? Let's use the function f(x) = nums[x] to
construct the sequence: x, nums[x], nums[nums[x]], nums[nums[nums[x]]], ....

Each new element in the sequence is an element in nums at the index of the previous
element. If one starts from x = nums[0], such a sequence will produce a linked list with
a cycle.

The cycle appears because nums contains duplicates. The duplicate node is a cycle
entrance.

Complexity
==========

Time
----

findDuplicate(nums): O(n * lg n).
findDuplicate_cycle(nums): O(n).

Space
-----

findDuplicate(nums) and findDuplicate_cycle(nums): O(1).
"""


def sol_bs(nums):
    low, high = 1, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        count = sum(num <= mid for num in nums)
        if count > mid:
            dup, high = mid, mid - 1
        else:
            low = mid + 1
    return dup


def sol_cycle(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow, fast = nums[slow], nums[nums[fast]]
    slow, fast = nums[0], nums[fast]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow
