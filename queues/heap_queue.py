"""HeapQueue is a class that implements Heap Sort on an unordered input array as well as
a heap-based priority queue.

1. _exchange() is a helper method to exchange two elements in the queue array.

2. _left(), _parent(), and _right() computes the indices of a node's left child, parent,
and right child, respectively, given the node index i.

3. build(), which runs in O(n) time, produces a heap (either maximum or minimum) from an
unordered input array using heapify() and builds the heap in a bottom-up manner.
heapify(), which runs in O(lg(n)) time, maintains the heap (either maximum or minimum)
property. Whenever heapify() is called, the two subtrees of that node are both heaps
(either maximum or minimum).

4. sort(), which which runs in O(n * lg(n)) time, sorts an unordered array in place. It
sorts the unordered input array by first building an initial heap, then moving the 0-th
item in the heap array to the i-th element. Each time the movement is conducted, the
heap array is rebuilt with a smaller heap size.

5. extract() extracts the maximum/minimum element from the heap. For max heaps, the
priority is that the largest number will always be maintained at the root node. With
each heap element extraction, the largest number is taken out and removed from the
array, and the rest of the heap is then re-heapified to maintain its max heap state.
Vice versa for min heaps.

6. get() simply returns the maximum/minimum element from the heap.

7. insert() inserts an element into the key at the correct heap position.

O(n * lg(n))
"""


from operator import gt, lt


class HeapQueue:
    def __init__(self, a, is_max=True):
        self.a = a
        self.heap_size = len(self.a)
        self.is_max = is_max
        self.compare_op, self.change_op = (gt, lt) if self.is_max else (lt, gt)
        self.build()

    def _exchange(self, i, j):
        t = self.a[i]
        self.a[i], self.a[j] = self.a[j], t

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _parent(i):
        return max(0, (i - 1) // 2)

    @staticmethod
    def _right(i):
        return 2 * i + 2

    def build(self):
        for i in range(len(self.a) // 2 - 1, -1, -1):
            self.heapify(i)

    def change(self, i, k):
        assert self.compare_op(k, self.a[i])
        self.a[i] = k
        parent = self._parent(i)
        while i > 0 and self.change_op(self.a[parent], self.a[i]):
            self._exchange(i, parent)
            i = parent
            parent = self._parent(i)

    def extract(self):
        assert self.heap_size > 0
        self.heap_size -= 1
        val = self.a[0]
        self.a[0] = self.a[self.heap_size]
        self.heapify(0)
        self.a.pop(-1)
        return val

    def get(self):
        return self.a[0]

    def heapify(self, i):
        l, r, index = self._left(i), self._right(i), i
        if l < self.heap_size and self.compare_op(self.a[l], self.a[i]):
            index = l
        if r < self.heap_size and self.compare_op(self.a[r], self.a[index]):
            index = r
        if index != i:
            self._exchange(i, index)
            self.heapify(index)

    def insert(self, k):
        limit = -float("inf") if self.is_max else float("inf")
        self.a.append(limit)
        self.change(self.heap_size, k)
        self.heap_size += 1

    def sort(self):
        assert self.heap_size > 0
        for i in range(len(self.a) - 1, -1, -1):
            self._exchange(0, i)
            self.heap_size -= 1
            self.heapify(0)


# Max-Heap
a = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
sorted_a = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
queue = HeapQueue(a, is_max=True)
assert queue.get() == 16
for i in range(len(a)):
    val = queue.extract()
    sorted_val = sorted_a[len(sorted_a) - i - 1]
    assert val == sorted_val
b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
for i in range(len(b)):
    queue.insert(b[i])
queue.sort()
assert queue.a == sorted_a

# Min-Heap
a = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
sorted_a = [16, 14, 10, 9, 8, 7, 4, 3, 2, 1]
queue = HeapQueue(a, is_max=False)
assert queue.get() == 1
for i in range(len(a)):
    val = queue.extract()
    sorted_val = sorted_a[len(sorted_a) - i - 1]
    assert val == sorted_val
b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
for i in range(len(b)):
    queue.insert(b[i])
queue.sort()
assert queue.a == sorted_a
