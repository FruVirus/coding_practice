"""
Copy List with Random Pointer
-----------------------------

A linked list of length n is given such that each node contains an additional random
pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new
nodes, where each new node has its value set to the value of its corresponding original
node. Both the next and random pointer of the new nodes should point to new nodes in the
copied list such that the pointers in the original list and copied list represent the
same list state. None of the pointers in the new list should point to nodes in the
original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y,
then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is
represented as a pair of [val, random_index] where:

    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer
points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.

Complexity
==========

Time
----

copyRandomList(head): O(n).

Space
-----

copyRandomList(head): O(1).
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val, self.next, self.random = int(x), next, random


def sol(head):
    if not head:
        return None
    node = head
    while node:
        clone = Node(node.val)
        clone.next, node.next = node.next, clone
        node = clone.next
    node = head
    while node:
        if node.random:
            node.next.random = node.random.next
        node = node.next.next
    head_old, head_new, head_clone = head, head.next, head.next
    while head_old:
        head_old.next = head_old.next.next
        head_new.next = head_new.next.next if head_new.next else None
        head_old, head_new = head_old.next, head_new.next
    return head_clone
