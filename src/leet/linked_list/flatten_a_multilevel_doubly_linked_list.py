"""
Flatten a Multilevel Doubly Linked List
---------------------------------------

You are given a doubly linked list, which contains nodes that have a next pointer, a
previous pointer, and an additional child pointer. This child pointer may or may not
point to a separate doubly linked list, also containing these special nodes. These child
lists may have one or more children of their own, and so on, to produce a multilevel
data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes
appear in a single-level, doubly linked list. Let curr be a node with a child list. The
nodes in the child list should appear after curr and before curr.next in the flattened
list.

Return the head of the flattened list. The nodes in the list must have all of their
child pointers set to null.

Complexity
==========

Time
----

flatten(head): O(n).

Space
-----

flatten(head): O(n).
"""


class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val, self.prev, self.next, self.child = val, prev, next, child


def sol(head):
    if not head:
        return None
    node = Node()
    prev, stack = node, [head]
    while stack:
        curr = stack.pop()
        prev.next, curr.prev = curr, prev
        if curr.next:
            stack.append(curr.next)
        if curr.child:
            stack.append(curr.child)
            curr.child = None
        prev = curr
    node.next.prev = None
    return node.next
