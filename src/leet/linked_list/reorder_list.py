"""
Reorder List
------------

You are given the head of a singly linked-list. The list can be represented as:

L_0 --> L_1 --> ... --> L_(n - 1) --> L_n

Reorder the list to be on the following form:

L_0 --> L_n --> L_1 → L_(n - 1) --> L_2 --> L_(n - 2) --> ...

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Intuition
---------

1. Get the midpoint of the linked list.
2. Reverse the second half of the linked list.
3. Merge the first and second halves one element at a time.

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
    if not head:
        return None
    mid = fast = head
    while fast and fast.next:
        mid, fast = mid.next, fast.next.next
    temp, curr = None, mid
    while curr:
        next, curr.next = curr.next, temp
        curr, temp = next, curr
    first, second = head, temp
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
