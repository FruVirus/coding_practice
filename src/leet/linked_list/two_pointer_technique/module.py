"""
Linked List Cycle
-----------------

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer.

Return true if there is a cycle in the linked list. Otherwise, return false.

Linked List Cycle II
--------------------

Given the head of a linked list, return the node where the cycle begins. If there is no
cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer.

Do not modify the linked list.

Complexity
==========

Time
----

detect_cycle() and has_cycle(): O(n).

Space
-----

All: O(1).
"""


# pylint: disable=R0201


class Solution:
    def detect_cycle(self, head):
        if not head:
            return None
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                break
        if not (fast and fast.next):
            return None
        ptr1, ptr2 = head, fast.next
        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next
        return ptr1

    def has_cycle(self, head):
        if not head:
            return False
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
