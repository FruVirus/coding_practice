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
