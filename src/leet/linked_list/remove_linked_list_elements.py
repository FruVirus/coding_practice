"""
Remove Linked List Elements
---------------------------

Given the head of a linked list and an integer val, remove all the nodes of the linked
list that has Node.val == val, and return the new head.

Complexity
==========

Time
----

removeElements(head, val): O(n).

Space
-----

removeElements(head, val): O(1).
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def sol(head, val):
    node = Node()
    node.next, prev, curr = head, node, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return node.next
