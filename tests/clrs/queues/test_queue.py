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


def test_table_doubling():
    x = Queue(size=2, table_double=True)
    x.enqueue(1)
    x.enqueue(2)
    x.enqueue(3)
    x.enqueue(4)
    x.enqueue(5)
    x.enqueue(6)
    x.enqueue(7)
    x.enqueue(8)
    x.enqueue(9)
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None]
    assert x.dequeue() == 1
    assert x.dequeue() == 2
    assert x.dequeue() == 3
    assert x.dequeue() == 4
    assert x.dequeue() == 5
    assert x.dequeue() == 6
    assert x.dequeue() == 7
    assert x.dequeue() == 8
    assert x.dequeue() == 9
    assert x.a == [None, None, None, None]
    x.enqueue(666)
    assert x.a == [666, None, None, None]
    assert x.dequeue() == 666
    assert x.a == [None, None]
    x.enqueue(667)
    assert x.a == [667, None]
    assert x.dequeue() == 667
    assert x.a == [None]
    x.enqueue(1)
    x.enqueue(2)
    x.enqueue(3)
    x.enqueue(4)
    x.enqueue(5)
    x.enqueue(6)
    x.enqueue(7)
    x.enqueue(8)
    x.enqueue(9)
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None]
