"""
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

detect_cycle(): O(n).

Space
-----

detect_cycle(): O(1).
"""


def detect_cycle(head):
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
    while ptr1 is not ptr2:
        ptr1, ptr2 = ptr1.next, ptr2.next
    return ptr1
