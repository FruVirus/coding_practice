# Repository Library
from clrs.queues.heap_queue import HeapQueue


def test_max_heap():
    a = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
    sorted_a = sorted(a, reverse=True)
    queue = HeapQueue(a, is_max=True)
    assert queue.get() == 16
    for i in range(len(a)):
        val = queue.extract()
        assert val == sorted_a[i]
    a = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
    heap_delete = [
        [16, 14, 9, 10, 7, 8, 3, 1, 4, 2],
        [14, 10, 9, 4, 7, 8, 3, 1, 2, 16],
        [14, 7, 9, 4, 2, 8, 3, 1, 10, 16],
        [14, 7, 8, 4, 2, 1, 3, 9, 10, 16],
        [14, 7, 8, 3, 2, 1, 4, 9, 10, 16],
        [14, 7, 8, 3, 1, 2, 4, 9, 10, 16],
        [14, 7, 8, 3, 2, 1, 4, 9, 10, 16],
        [14, 7, 8, 4, 2, 1, 3, 9, 10, 16],
        [14, 7, 9, 4, 2, 1, 3, 8, 10, 16],
        [14, 10, 9, 4, 2, 1, 3, 8, 7, 16],
        [16, 10, 9, 4, 2, 1, 3, 8, 7, 14],
    ]
    queue = HeapQueue(a, is_max=True)
    for i in range(len(a)):
        assert queue.a == heap_delete[i]
        queue.delete(i)
    assert queue.heap_size == 0
    b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap_b = [16, 14, 10, 8, 7, 3, 9, 1, 4, 2]
    for i in range(len(b)):
        queue.insert(b[i])
    assert queue.a == heap_b


def test_min_heap():
    a = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
    sorted_a = sorted(a)
    queue = HeapQueue(a, is_max=False)
    assert queue.get() == 1
    for i in range(len(a)):
        val = queue.extract()
        assert val == sorted_a[i]
    a = [16, 14, 9, 10, 7, 8, 3, 1, 4, 2]
    heap_delete = [
        [1, 2, 3, 4, 7, 8, 9, 10, 14, 16],
        [2, 4, 3, 10, 7, 8, 9, 16, 14, 1],
        [2, 7, 3, 10, 14, 8, 9, 16, 4, 1],
        [2, 7, 8, 10, 14, 16, 9, 3, 4, 1],
        [2, 7, 8, 9, 14, 16, 9, 3, 4, 1],
        [2, 7, 8, 9, 16, 14, 9, 3, 4, 1],
        [2, 7, 8, 9, 14, 16, 9, 3, 4, 1],
        [2, 7, 8, 9, 14, 16, 9, 3, 4, 1],
        [2, 7, 3, 9, 14, 16, 9, 8, 4, 1],
        [2, 4, 3, 9, 14, 16, 9, 8, 7, 1],
    ]
    queue = HeapQueue(a, is_max=False)
    for i in range(len(a)):
        assert queue.a == heap_delete[i]
        queue.delete(i)
    assert queue.heap_size == 0
    b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap_b = [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]
    for i in range(len(b)):
        queue.insert(b[i])
    assert queue.a == heap_b
