"""
Convert Sorted Array to Binary Search Tree
------------------------------------------

Given an integer array nums where the elements are sorted in ascending order, convert it
to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of
every node never differs by more than one.

Complexity
==========

Time
----

sortedArrayToBST(nums): O(n).

Space
-----

sortedArrayToBST(nums): O(lg n).
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


def sol(nums):
    def helper(in_left, in_right):
        if in_left <= in_right:
            mid = in_left + (in_right - in_left) // 2
            root = Node(nums[mid])
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            return root
        return None

    return helper(0, len(nums) - 1)
