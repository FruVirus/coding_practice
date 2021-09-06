# Repository Library
from clrs.queues.queue import Queue


def test_queue():
    size = 10
    items = list(range(size - 1))
    queue = Queue(size)
    for i in range(size - 1):
        queue.enqueue(i)
    assert queue.a[: size - 1] == items
    for i in range(size - 1):
        assert queue.dequeue() == items[i]
    assert queue.head == queue.tail
