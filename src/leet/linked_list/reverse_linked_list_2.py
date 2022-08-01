"""
Reverse Linked List II
----------------------

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position right, and
return the reversed list.

Intuition
---------

1. Set a pointer to just before the sub-list (temp) to be reversed and a pointer to the
first node in the sublist to be reversed (curr).
2. Set a pointer to the last node of the sub-list before the reversed sub-list (conn)
and a pointer to the tail of the (eventually) reversed sublist (tail).
3. Reverse the sublist between left and right.
4. Connect conn to the reversed sublist.
5. Connect tail to the sublist after the reversed sublist.

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
    temp, curr = None, head
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
