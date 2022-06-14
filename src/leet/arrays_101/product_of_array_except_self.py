"""
Product of Array Except Self
----------------------------

Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division
operation.

Intuition
---------

Instead of dividing the product of all the numbers in the array by the number at a given
index to get the corresponding product, we can make use of the product of all the
numbers to the left and all the numbers to the right of the index. Multiplying these two
individual products would give us the desired result as well.

For every given index, i, we will make use of the product of all the numbers to the left
of it and multiply it by the product of all the numbers to the right. This will give us
the product of all the numbers except the one at the given index i.

Note: For the element at index 0, there are no elements to the left, so the answer[0]
would be 1.

Note: For the element at index n - 1, there are no elements to the right, so the
answer[-1] would be 1.

Complexity
==========

Time
----

productExceptSelf(nums): O(n).

Space
-----

productExceptSelf(nums): O(1).
"""


def sol(nums):
    n = len(nums)
    sol = [1] * n
    for i in range(1, n):
        sol[i] = nums[i - 1] * sol[i - 1]
    right_prod = 1
    for i in reversed(range(n)):
        sol[i] *= right_prod
        right_prod *= nums[i]
    return sol
