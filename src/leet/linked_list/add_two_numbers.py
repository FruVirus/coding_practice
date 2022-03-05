"""
Add Two Numbers
---------------

You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit. Add
the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Complexity
==========

Time
----

addTwoNumbers(l1, l2): O(max(m, n)).

Space
-----

addTwoNumbers(l1, l2): O(max(m, n)).
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def sol(l1, l2):
    node = Node()
    carry, curr = 0, node
    while l1 or l2:
        val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry, val = val // 10, val % 10
        curr.next = Node(val)
        curr = curr.next
        l1, l2 = l1.next if l1 else None, l2.next if l2 else None
    if carry > 0:
        curr.next = Node(carry)
    return node.next
