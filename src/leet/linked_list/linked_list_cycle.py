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

detectCycle(head): O(n).

Space
-----

detectCycle(head): O(1).
"""


def sol(head):
    if not head:
        return None
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            break
    if not (fast and fast.next):
        return None
    slow, fast = head, fast.next
    while slow is not fast:
        slow, fast = slow.next, fast.next
    return slow
