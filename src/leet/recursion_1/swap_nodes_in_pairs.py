"""
Swap Nodes in Pairs
-------------------

Given a linked list, swap every two adjacent nodes and return its head. You must solve
the problem without modifying the values in the list's nodes (i.e., only nodes
themselves may be changed.)

Complexity
==========

Time
----

swapPairs(head): O(n).

Space
-----

swapPairs(head): O(n).
"""


def sol(head):
    if not (head and head.next):
        return head
    first, second = head, head.next
    first.next, second.next = sol(second.next), first
    return second
