"""
6.1 Heaps
=========

The (binary) heap data structure is an array object that we can view as a nearly
complete binary tree. Each node of the tree corresponds to an element of the array. The
tree is completely filled on all levels except possibly the lowest, which is filled from
the left up to a point. An array A that represents a heap is an object with two
attributes: A.length, which gives hte number of elements in the array, and A.heap-size,
which represents how many elements in the heap are stored within array A. That is,
although A[1...A.length] may contain numbers, only the elements A[1...A.heap-size],
where 0 <= A.heap-size <= A.length, are valid elements of the heap. The root of the tree
is A[1], and given the index i of a node, we can easily compute the indices of its
parent, left child, and right child.

There are two kinds of binary heaps: max-heaps and min-heaps. In both kinds, the values
in the nodes satisfy a heap property, the specifics of which depend on the kind of heap.
In a max-heap, the max-heap property is that for every node i, the value of that node
is at most the value of its parent. Thus, the largest element in a max-heap is stored at
the root, and the subtree rooted at a node contains values no larger than that contained
at the node itself (and vice versa for min-heaps).

Viewing a heap as a tree, we define the height of a node in a heap to be the number of
edges on the longest simple downward path from the node to a leaf, and we define the
height of the heap to be the height of its root. Since a heap of n elements is based on
a complete binary tree, its height is Theta(lg n). Thus, the basic operations on heaps
run in time at most proportional to the height of the tree and thus take O(lg n) time.

6.2 Maintaining the heap property
---------------------------------

In order to maintain the max-heap property, we call the procedure heapify(). Its inputs
are an array A and an index i into the array. When it is called, heapify() assumes that
the binary trees rooted at the left and right of the node are max-heaps, but that A[i]
might be smaller than its children, thus violating the max-heap property. heapify() lets
the value at A[i] "float down" in the max-heap so that the subtree rooted at index i
obeys the max-heap property.

At each step, the largest of the elements A[i], A[left(i)], and A[right(i)] is
determined, and its index is stored. If A[i] is largest, then the subtree rooted at node
i is already a max-heap and the procedure terminates. Otherwise, one of the two children
has the largest element, and A[i] is swapped with A[index], which causes node i and its
children to satisfy the max-heap property. The node at index, however, now has the
original value A[i], and thus, the subtree rooted at index might violate the max-heap
property. Consequently, we call heapify() recursively on that subtree. In other words,
only half the length of the input array needs to be iterated over since a heap is a
complete binary tree, which means that approximately half the nodes are leaves that do
not need to be moved at all during the build process.

6.3 Building a heap
-------------------

We can use the procedure build() in a bottom-up manner to convert an array A[1...n],
where n = A.length, into a max-heap. The elements in the subarray A[(n // 2 + 1)...n]
are all leaves of the tree, and so each is a 1-element heap to begin with. Thus, we do
not have to iterate through these indices when building a max-heap.

6.5 Priority queues
-------------------

The heap data structure itself has many uses, including using it as an efficient
priority queue. As with heaps, priority queues come in two forms: max-priority queues
and min-priority queues.

A priority-queue is a data structure for maintaining a set S of elements, each with an
associated value called a key. A max-priority queue supports the following operations:

1. insert(S, x): inserts the element x into the set S.
2. get(S): returns the element of S with the largest key.
3. extract(S): removes and and returns the element of S with the largest key.
4. change(S, x, k): increases the value of element x's key to the new value k, which is
assumed to be at least as large as x's current key value.

Among their other applications, we can use max-priority queues to schedule jobs on a
shared computer. The max-priority queue keeps track of the jobs to be performed and
their relative priorities. When a job is finished or interrupted, the scheduler selects
the highest-priority job from among those pending by calling extract(). The scheduler
can add a new job to the queue at any time by calling insert().

Alternatively, a min-priority queue can be used in an event-driven simulator. The items
in the queue are events to be simulated, each with an associated time of occurrence
that serves as its key. The events must be simulated in order of their time of
occurrence, because the simulation of an event can cause other events to be simulated in
the future. The simulation program calls extract() at each step to choose the next
event to simulate. As new events are produced, the simulator inserts them into the
min-priority queue by calling insert().

The procedure change() changes the value of element i's key to the new value k, which is
assumed to be at least as large as i's current key value. An index i into the array
identifies the priority-queue element whose key we wish to increase. The procedure first
updates the key of element A[i] to its new value. Because increasing the key of A[i]
might violate the max-heap property the procedure then traverses a simple path from this
node toward the root to find a proper place for the newly changed key. As change()
traverses this path, it repeatedly compares an element to its parent, exchanging their
keys and continuing if the element's key is larger, and terminating if the element's key
is smaller, since the max-heap property now holds.

The procedure delete() deletes a key referenced by the index i. If the key at index i is
greater than or equal to the key at the end of the array, then we exchange keys and
re-heapify at index i to ensure that the subtree rooted at the parent of i remains a
max-heap. Otherwise, we simply change the key value at index i to be the key value at
the end of the array since we know that this operation will maintain the heap property.

The procedure extract() extracts the maximum/minimum element from the heap. For
max-heaps, the priority is that the largest number will always be maintained at the root
node. With each heap element extraction, the largest number is taken out and removed
from the array, and the rest of the heap is then re-heapified to maintain its max-heap
state. Vice versa for min-heaps.

The procedure insert() takes as an input the key of the new element to be inserted into
the max-heap. The procedure first sets the value of the heap array indexed by
self.heap_size to +/-float("inf"). THen it calls change() to set the key of this new
node to its correct value and maintain the max-heap property.

Complexity
==========

Time
----

build(): O(n).
change(), delete(), extract(), heapify(), and insert(): O(lg n).
get(): O(1).
"""

# Standard Library
from operator import gt, lt


class HeapQueue:
    def __init__(self, a, is_max):
        self.a = a
        self.is_max = is_max
        self.compare = lt if self.is_max else gt
        self.heap_size = len(self.a)
        self.build()

    def _exchange(self, i, j):
        self.a[i], self.a[j] = self.a[j], self.a[i]

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _right(i):
        return 2 * i + 2

    def build(self):
        for i in reversed(range(len(self.a) // 2)):
            self.heapify(i)

    def change(self, i, k):
        assert not self.compare(k, self.a[i])
        self.a[i] = k
        while i > 0 and self.compare(self.a[self._parent(i)], self.a[i]):
            self._exchange(i, self._parent(i))
            i = self._parent(i)

    def delete(self, i):
        assert self.heap_size > 0
        self.heap_size -= 1
        if not self.compare(self.a[self.heap_size], self.a[i]):
            self.change(i, self.a[self.heap_size])
        else:
            self._exchange(i, self.heap_size)
            self.heapify(i)

    def extract(self):
        assert self.heap_size > 0
        self.heap_size -= 1
        x = self.get()
        self._exchange(0, self.heap_size)
        self.heapify(0)
        return x

    def get(self):
        return self.a[0]

    def heapify(self, i):
        l, r, index = self._left(i), self._right(i), i
        if l < self.heap_size and not self.compare(self.a[l], self.a[i]):
            index = l
        if r < self.heap_size and not self.compare(self.a[r], self.a[index]):
            index = r
        if index != i:
            self._exchange(i, index)
            self.heapify(index)

    def insert(self, k):
        self.a[self.heap_size] = -float("inf") if self.is_max else float("inf")
        self.change(self.heap_size, k)
        self.heap_size += 1
