"""
Encode N-ary Tree to Binary Tree
--------------------------------

Design an algorithm to encode an N-ary tree into a binary tree and decode the binary
tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node
has no more than N children. Similarly, a binary tree is a rooted tree in which each
node has no more than 2 children. There is no restriction on how your encode/decode
algorithm should work. You just need to ensure that an N-ary tree can be encoded to a
binary tree and this binary tree can be decoded to the original N-nary tree structure.

Intuition
---------

BFS Approach

To put it simple, the algorithm can be summarized in two steps.

    1. Link all siblings together, like a singly-linked list.

Each node in the original N-ary tree would correspond uniquely to a node in the
resulting binary tree.

In the first step, we first chain up all the sibling nodes together, i.e. nodes that
share the same parent. By chaining up, we would link the nodes via either left or right
child pointers of the binary tree node. Here we choose to do with the right pointer.

    2. Link the head of the obtained list of siblings with its parent node.

Now that the siblings are chained up, we just need to link this sibling list with their
parent node.

As one can see, we don't have to link each one of the siblings to its parent, and we
cannot do so either, since we only got two pointers for a node in binary tree. It
suffices to pick one of the siblings. Naturally, we could link the head of the list with
its parent node.

As one can imagine, based on the above idea, one can create some variants. For instance,
instead of linking the child nodes with the right pointers, we could use the left
pointers. And accordingly, we could start from the last child node to chain up the
siblings.

DFS Approach

The idea is that while we traverse the N-ary tree node by node in the DFS manner, we
weave the nodes together into a Binary tree, following the same intuition of encoding in
the previous approach.

The main idea of the algorithm is that for each node, we only take care the encoding of
the node itself, and we invoke the function itself to encode each of its child node,
i.e., encode(node.children[i]).

    - At the beginning of the encode(node) function, we create a binary tree node to
contain the value of the current node.

    - Then we put the first child of the N-ary tree node as the left node of the
newly-created binary tree node. We call the encoding function recursively to encode the
first child node as well.

    - For the rest of the children nodes of the N-ary tree node, we chain them up with
the right pointer of the binary tree node. And again, we call recursively the encoding
function to encode each of the child node.

Complexity
==========

Time
----

encode_bfs(root), decode_bfs(data), encode_dfs(root), and decode_dfs(data): O(n).

Space
-----

encode_bfs(root) and decode_bfs(data): O(l), where l is the maximum number of nodes that
reside at the same level.

encode_dfs(root) and decode_dfs(data): O(d), where d is the depth of the n-ary tree.
"""


# Standard Library
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val, self.children = val, children


class TreeNode:
    def __init__(self, x):
        self.val, self.left, self.right = x, None, None


def sol_encode_bfs(root):
    if not root:
        return None
    root_bnode = TreeNode(root.val)
    queue = deque([(root_bnode, root)])
    while queue:
        parent, curr = queue.popleft()
        prev = head = None
        for child in curr.children:
            new_bnode = TreeNode(child.val)
            if prev:
                prev.right = new_bnode
            else:
                head = new_bnode
            prev = new_bnode
            queue.append((new_bnode, child))
        parent.left = head
    return root_bnode


def sol_decode_bfs(data):
    if not data:
        return None
    root = Node(data.val, [])
    queue = deque([(root, data)])
    while queue:
        parent, curr = queue.popleft()
        sib = curr.left
        while sib:
            new_node = Node(sib.val, [])
            parent.children.append(new_node)
            queue.append((new_node, sib))
            sib = sib.right
    return root


def sol_encode_dfs(root):
    if not root:
        return None
    root_bnode = TreeNode(root.val)
    if len(root.children) > 0:
        root_bnode.left = sol_encode_dfs(root.children[0])
    curr = root_bnode.left
    for child in root.children[1:]:
        curr.right = sol_encode_dfs(child)
        curr = curr.right
    return root_bnode


def sol_decode_dfs(data):
    if not data:
        return None
    curr, root = data.left, Node(data.val, [])
    while curr:
        root.children.append(sol_decode_dfs(curr))
        curr = curr.right
    return root
