# Repository Library
from clrs.data_structures.elementary_data_structures.singly_linked_list import SLL, Node


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
    x = Node(4)
    sll.insert(x)
    sll.insert(Node(1))
    sll.reverse()
    assert sll.size() == 4
    assert sll.head.k == 9
    sll.delete(16)
    sll.delete(9)
    assert sll.head.k == 4
