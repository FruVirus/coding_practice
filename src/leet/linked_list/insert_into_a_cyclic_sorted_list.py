"""
Insert into a Cyclic Sorted List
--------------------------------

Given a Circular Linked List node, which is sorted in ascending order, write a function
to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily
be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert
the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single
circular list and return the reference to that single node. Otherwise, you should return
the originally given node.

Complexity
==========

Time
----

insert(): O(n).

Space
-----

insert(): O(1).
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val, self.next = val, next


def insert(head, insert_val):
    node = Node(insert_val)
    if not head:
        node.next = node
        return node
    curr = head
    while True:
        if head is curr.next:
            break
        if curr.val <= insert_val <= curr.next.val:
            break
        if insert_val >= curr.val > curr.next.val:
            break
        if curr.val > curr.next.val >= insert_val:
            break
        curr = curr.next
    node.next, curr.next = curr.next, node
    return head
