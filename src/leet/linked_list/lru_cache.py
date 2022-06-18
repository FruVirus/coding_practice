"""
LRU Cache
---------

Design a data structure that follows the constraints of a Least Recently Used (LRU)
cache.

Implement the LRUCache class:

    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return
-1.
    - void put(int key, int value) Update the value of the key if the key exists.
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the
capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

Intuition
---------

An LRU cache stands for Least Recently Used cache. It is an efficient cache data
structure that can be used to figure out what we should evict when the cache is full. It
has the following features:

    - Fixed-size cache capacity
    - Items are organized in order of from most-recently-used to least-recently-used
    - Whenever an item has exceeded the capacity, the least recently used element is
evicted or removed

A Doubly Linked List is used to maintain the order. The most recently used linked node
will be near the head and the least recent node will be near the tail (or vice versa).

Hashmap maps key to Address of Node in Doubly Linked List. In general, finding an item
in a linked list is O(n) time, since we need to walk the whole list. However, by using
Hashmap, finding an element in our cache’s linked list takes only in O(1) time.

The maximum size of the hashmap will be equal to the cache capacity.

Complexity
==========

Time
----

Sol:
    def get(self, key): O(1).
    def put(self, key, val): O(1).

Space
-----

Sol:
    self.cache: O(capacity).
"""


class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache, self.capacity, self.size = {}, capacity, 0
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def _add_at_head(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev, self.head.next = node, node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_at_head(node)

    def _pop_at_tail(self):
        node = self.tail.prev
        self._remove_node(node)
        return node

    @staticmethod
    def _remove_node(node):
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key, val):
        node = self.cache.get(key, None)
        if not node:
            node = Node(key, val)
            self.size += 1
            self.cache[key] = node
            self._add_at_head(node)
            if self.size > self.capacity:
                tail = self._pop_at_tail()
                self.size -= 1
                del self.cache[tail.key]
        else:
            node.val = val
            self._move_to_head(node)
