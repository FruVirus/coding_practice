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
    b = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap_b = [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]
    for i in range(len(b)):
        queue.insert(b[i])
    assert queue.a == heap_b
