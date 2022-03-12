"""
Find Minimum in Rotated Sorted Array II
---------------------------------------

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
For example, the array nums = [0,1,4,4,5,6,7] might become:

    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the
array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum
element of this array.

You must decrease the overall operation steps as much as possible.

Intuition
---------

In this problem, the numbers do not have to be unique; thus, it is a more general
problem.

This problem needs to address three cases:

    1. nums[mid] < nums[high]: The mid element resides in the same half as the high
element. Therefore, the desired minimum element should reside to the left-hand side of
the mid element. As a result, we then move high down to the mid index.

    2. nums[mid] > nums[high]: THe mid element resides in the different half of the
array as the high element. Therefore, the desired minimum element should reside in the
right-hand side of the mid element. As a result, we move the low index one past the mid
index.

    3. nums[mid] == nums[high]: In this case, we are not sure which side of the mid
element the desired minimum resides in. To further reduce the search scope, a safe
measure would be to reduce the high index by one rather than aggressively moving the mid
index.

Complexity
==========

Time
----

findMin(nums): O(lg n)/O(n) expected/worse case. Worst case occurs when the array
contains all identical elements.

Space
-----

findMin(nums): O(1).
"""


def sol(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        elif nums[mid] < nums[high]:
            high = mid
        else:
            high -= 1
    return nums[low]
