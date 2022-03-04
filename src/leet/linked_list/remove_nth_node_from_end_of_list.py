"""
Remove Nth Node From End of List
--------------------------------

Given the head of a linked list, remove the nth node from the end of the list and return
its head.

Complexity
==========

Time
----

remove_nth_from_end(): O(n).

Space
-----

remove_nth_from_end(): O(1).
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def remove_nth_from_end(head, n):
    node = Node()
    node.next, prev, curr = head, node, node
    for _ in range(n + 1):
        curr = curr.next
    while curr:
        prev, curr = prev.next, curr.next
    prev.next = prev.next.next
    return node.next
