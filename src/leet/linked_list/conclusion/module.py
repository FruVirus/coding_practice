"""
Rotate List
-----------

Given the head of a linked list, rotate the list to the right by k places.

Complexity
==========

Time
----

rotate_right(): O(n).

Space
-----

All: O(1).
"""


# pylint: disable=R0201


class Solution:
    def rotate_right(self, head, k):
        if not head:
            return None
        if not head.next or k == 0:
            return head
        count, old_tail = 1, head
        while old_tail.next:
            count, old_tail = count + 1, old_tail.next
        k %= count
        old_tail.next, new_tail = head, head
        for _ in range(count - k - 1):
            new_tail = new_tail.next
        head, new_tail.next = new_tail.next, None
        return head
