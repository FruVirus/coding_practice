# Repository Library
from clrs.queues.queue import Queue


def test_queue():
    size = 10
    items = list(range(size - 1))
    queue = Queue(size)
    for i in range(size - 1):
        queue.enqueue(i)
    assert queue.a[: size - 1] == items
    assert queue.head == 0
    assert queue.tail == 9
    assert queue.dequeue() == 0
    queue.enqueue(666)
    assert queue.head == 1
    assert queue.tail == 0
    assert queue.dequeue() == 1
    result = [2, 3, 4, 5, 6, 7, 8, 666]
    for i in range(len(result)):
        assert queue.dequeue() == result[i]
    assert queue.head == queue.tail
