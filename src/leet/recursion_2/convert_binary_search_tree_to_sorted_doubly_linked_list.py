"""
Convert Binary Search Tree to Sorted Doubly Linked List
-------------------------------------------------------

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and
successor pointers in a doubly-linked list. For a circular doubly linked list, the
predecessor of the first element is the last element, and the successor of the last
element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of
the tree node should point to its predecessor, and the right pointer should point to its
successor. You should return the pointer to the smallest element of the linked list.

Complexity
==========

Time
----

treeToDoublyList_iterative(root) and treeToDoublyLst_recursive(root): O(n).

Space
-----

treeToDoublyList_iterative(root) and treeToDoublyLst_recursive(root): O(n).
"""


def sol_iterative(root):
    if not root:
        return None
    first, node, last, stack = None, root.left, None, [root]
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if not first:
            first = node
        if last:
            last.right, node.left = node, last
        last, node = node, node.right
    last.right, first.left = first, last
    return first


def sol_recursive(root):
    if not root:
        return None

    def helper(node):
        nonlocal first, last
        if node:
            helper(node.left)
            if last:
                last.right, node.left = node, last
            else:
                first = node
            last = node
            helper(node.right)

    first = last = None
    helper(root)
    last.right, first.left = first, last
    return first
