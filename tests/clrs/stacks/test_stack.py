# Repository Library
from clrs.stacks.stack import Stack


def test_stack():
    size = 10
    item = list(range(size))
    stack = Stack(size)
    for i in range(size):
        stack.push(i)
    assert stack.a == item
    for i in range(size):
        assert stack.pop() == item[size - i - 1]
    assert stack.empty()


def test_table_doubling():
    x = Stack(2, table_double=True)
    x.push(1)
    assert x.a == [1, None]
    x.push(2)
    assert x.a == [1, 2]
    x.push(3)
    assert x.a == [1, 2, 3, None]
    x.push(4)
    assert x.a == [1, 2, 3, 4]
    x.push(5)
    assert x.a == [1, 2, 3, 4, 5, None, None, None]
    x.push(6)
    assert x.a == [1, 2, 3, 4, 5, 6, None, None]
    x.push(7)
    assert x.a == [1, 2, 3, 4, 5, 6, 7, None]
    x.push(8)
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8]
    x.push(9)
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None]
    assert x.pop() == 9
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None]
    assert x.pop() == 8
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None]
    assert x.pop() == 7
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None]
    assert x.pop() == 6
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8, 9, None, None, None, None, None, None, None]
    assert x.pop() == 5
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8]
    assert x.pop() == 4
    assert x.a == [1, 2, 3, 4, 5, 6, 7, 8]
    assert x.pop() == 3
    assert x.a == [1, 2, 3, 4]
    assert x.pop() == 2
    assert x.a == [1, 2]
    assert x.pop() == 1
    assert x.a == [1]
    x.push(666)
    assert x.a == [666]
    x.push(667)
    assert x.a == [666, 667]
    x.push(668)
    assert x.a == [666, 667, 668, None]
    x.push(669)
    assert x.a == [666, 667, 668, 669]
