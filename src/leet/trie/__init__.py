"""
What is Trie?
=============

A Trie is a special form of a Nary tree. Typically, a trie is used to store strings.
Each Trie node represents a string (a prefix). Each node might have several children
nodes while the paths to different children nodes represent different characters. And
the strings the child nodes represent will be the origin string represented by the node
itself plus the character on the path.

In the example, the value we mark in each node is the string the node represents. For
instance, we start from the root node and choose the second path 'b', then choose the
first child 'a', and choose child 'd', finally we arrived at the node "bad". The value
of the node is exactly formed by the letters in the path from the root to the node
sequentially.

It is worth noting that the root node is associated with the empty string.

One important property of Trie is that all the descendants of a node have a common
prefix of the string associated with that node. That's why Trie is also called prefix
tree.

Let's look at the example again. For example, the strings represented by nodes in the
subtree rooted at node "b" have a common prefix "b". And vice versa. The strings which
have the common prefix "b" are all in the subtree rooted at node "b" while the strings
with different prefixes will come to different branches.

How to represent a Trie?
========================

In the previous article, we introduce the concept of Trie. In this article, we will talk
about how to represent this data structure in coding languages.

What's special about Trie is the corresponding relationship between characters and
children nodes. There are a lot of different representations of a trie node. Here we
provide two of them.

First Solution - Array
----------------------

The first solution is to use an array to store children nodes.

For instance, if we store strings which only contains letter a to z, we can declare an
array whose size is 26 in each node to store its children nodes. And for a specific
character c, we can use c - 'a' as the index to find the corresponding child node in the
array.

It is really fast to visit a child node. It is comparatively easy to visit a specific
child since we can easily transfer a character to an index in most cases. But not all
children nodes are needed. So there might be some waste of space.

Second Solution - Map
---------------------

The second solution is to use a hashmap to store children nodes.

We can declare a hashmap in each node. The key of the hashmap are characters and the
value is the corresponding child node.

It is even easier to visit a specific child directly by the corresponding character. But
it might be a little slower than using an array. However, it saves some space since we
only store the children nodes we need. It is also more flexible because we are not
limited by a fixed length and fixed range.

More
----

We mentioned how to represent the children nodes in Trie node. Besides, we might need
some other values.

For example, as we know, each Trie node represents a string but not all the strings
represented by Trie nodes are meaningful. If we only want to store words in a Trie, we
might declare a boolean in each node as a flag to indicate if the string represented by
this node is a word or not.

Insertion in Trie
=================

When we insert a target value into a BST, in each node, we need to decide which child
node to go according to the relationship between the value of the node and the target
value. Similarly, when we insert a target value into a Trie, we will also decide which
path to go depending on the target value we insert.

To be more specific, if we insert a string S into Trie, we start with the root node. We
will choose a child or add a new child node depending on S[0], the first character in S.
Then we go down to the second node and we will make a choice according to S[1]. Then we
go down to the third node, so on and so for. Finally, we traverse all characters in S
sequentially and reach the end. The end node will be the node which represents the
string S.

Usually, you will need to build the trie by yourself. Building a trie is actually to
call the insertion function several times. But remember to initialize a root node before
you insert the strings.

Search in Trie
==============

Search Prefix
-------------

As we mentioned in the introduction to Trie, all the descendants of a node have a common
prefix of the string associated with that node. Therefore, it should be easy to search
if there are any words in the trie that starts with the given prefix.

Similarly, we can go down the tree depending on the given prefix. Once we can not find
the child node we want, search fails. Otherwise, search succeeds.

Search Word
-----------

You might also want to know how to search for a specific word rather than a prefix. We
can treat this word as a prefix and search in the same way we mentioned above.

    1. If search fails which means that no words start with the target word, the target
word is definitely not in the Trie.

    2. If search succeeds, we need to check if the target word is only a prefix of words
in Trie or it is exactly a word. To solve this problem, you might want to modify the
node structure a little bit. Hint: A boolean flag in each node might work.

Comparison with Hash Table
--------------------------

You might wonder why not use a hash table to store strings. Let's do a brief comparison
between these two data structures. We assume there are N keys and the maximum length of
a key is M.

1. Time Complexity

    The time complexity to search in hash table is typically O(1), but will be O(log N)
in the worst time if there are too many collisions and we solve collisions using
height-balanced BST.

    The time complexity to search in Trie is O(M).

    The hash table wins in most cases.

2. Space Complexity

    The space complexity of hash table is O(M * N). If you want hash table to have the
same function with Trie, you might need to store several copies of the key. For
instance, you might want to store "a", "ap", "app", "appl" and also "apple" for a
keyword "apple" in order to search by prefix. The space complexity can be even much
larger in that case.

    The space complexity of Trie is O(M * N) as we estimated above. But actually far
smaller than the estimation since there will be a lot of words have the similar prefix
in real cases.

    Trie wins in most cases.
"""
