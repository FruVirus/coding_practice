"""
Reverse Linked List II
----------------------

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position right, and
return the reversed list.

Complexity
==========

Time
----

reverseBetween(head, left, right): O(n).

Space
-----

reverseBetween(head, left, right): O(1).
"""


def sol(head, left, right):
    if not head:
        return None
    curr, temp = head, None
    for _ in range(left - 1):
        temp, curr = curr, curr.next
    conn, tail = temp, curr
    for _ in range(right - left + 1):
        next, curr.next = curr.next, temp
        curr, temp = next, curr
    if conn:
        conn.next = temp
    else:
        head = temp
    tail.next = curr
    return head
