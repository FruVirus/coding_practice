# Repository Library
from clrs.lists.singly_linked_list import SLL, Node


def test_sll():
    sll = SLL()
    sll.insert(Node(9))
    sll.insert(Node(16))
    x = Node(4)
    sll.insert(x)
    sll.insert(Node(1))
    assert sll.size() == 4
    assert sll.head.k == 1
    sll.delete(x)
    sll.delete(1)
    assert sll.head.k == 16
    assert sll.head.next.k == 9
    x = sll.search(666)
    assert x is None
    sll = SLL()
    sll.insert(Node(9))
    sll.insert(Node(16))
    sll.insert(Node(4))
    sll.insert(Node(1))
    assert sll.sort() == [1, 4, 9, 16]
    sll = SLL()
    assert sll.sort() == []
