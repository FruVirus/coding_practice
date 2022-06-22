"""
Reorder List
------------

You are given the head of a singly linked-list. The list can be represented as:

L_0 --> L_1 --> ... --> L_(n - 1) --> L_n

Reorder the list to be on the following form:

L_0 --> L_n --> L_1 → L_(n - 1) --> L_2 --> L_(n - 2) --> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Complexity
==========

Time
----

reorderList(head): O(n).

Space
-----

reorderList(head): O(1).
"""


def sol(head):
    if not (head and head.next):
        return head
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    temp, curr = None, slow
    while curr:
        next, curr.next = curr.next, temp
        curr, temp = next, curr
    first, second = head, temp
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
