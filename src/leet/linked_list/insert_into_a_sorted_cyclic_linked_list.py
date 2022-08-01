"""
Insert into a Sorted Cyclic Linked List
---------------------------------------

Given a Circular Linked List node, which is sorted in ascending order, write a function
to insert a value insertVal into the list such that it remains a sorted circular list.
The given node can be a reference to any single node in the list and may not necessarily
be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert
the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is null), you should create a new single
circular list and return the reference to that single node. Otherwise, you should return
the originally given node.

Intuition
---------

We have to handles 4 cases:
    1. Only one node in the linked list: if head is curr.next.
    2. val fits between curr and curr.next: if curr.val < val <= curr.next.val.
    3. val fits before curr: if val >= curr.val > curr.next.val.
    4. val fits between curr and curr.next and is the smallest:
if curr.val > curr.next.val >= val.

Complexity
==========

Time
----

insert(head, val): O(n).

Space
-----

insert(head, val): O(1).
"""


class Node:
    def __init__(self, val=None, next=None):
        self.val, self.next = val, next


def sol(head, val):
    node = Node(val)
    if not head:
        node.next = node
        return node
    curr = head
    while True:
        if head is curr.next:
            break
        if curr.val < val <= curr.next.val:
            break
        if val >= curr.val > curr.next.val or curr.val > curr.next.val >= val:
            break
        curr = curr.next
    node.next, curr.next = curr.next, node
    return head
