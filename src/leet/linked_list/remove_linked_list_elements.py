"""
Remove Linked List Elements
---------------------------

Given the head of a linked list and an integer val, remove all the nodes of the linked
list that has Node.val == val, and return the new head.

Complexity
==========

Time
----

remove_elements(): O(n).

Space
-----

remove_elements(): O(1).
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def remove_elements(head, val):
    node = Node()
    node.next, prev, curr = head, node, head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return node.next
