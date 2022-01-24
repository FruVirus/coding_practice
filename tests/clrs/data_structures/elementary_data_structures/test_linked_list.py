# Repository Library
from clrs.data_structures.elementary_data_structures.linked_list import DLL, SLL, Node


def test_dll():
    dll = DLL()
    dll.insert(Node(9))
    dll.insert(Node(16))
    x = Node(4)
    dll.insert(x)
    dll.insert(Node(1))
    assert dll.size() == 4
    assert dll.head.k == 1
    dll.delete(x)
    dll.delete(1)
    assert dll.head.k == 16
    assert dll.head.next.k == 9
    assert dll.head.prev is None
    x = dll.search(666)
    assert x is None
    dll = DLL()
    dll.insert(Node(9))
    dll.insert(Node(16))
    x = Node(4)
    dll.insert(x)
    dll.insert(Node(1))
    dll.reverse()
    assert dll.size() == 4
    assert dll.head.k == 9
    dll.delete(16)
    dll.delete(9)
    assert dll.head.k == 4
    dll = DLL()
    dll.insert(Node(9))
    dll.insert(Node(16))
    dll.insert(Node(4))
    dll.insert(Node(1))
    assert dll.sort() == [1, 4, 9, 16]


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
    sll = SLL()
    sll.insert(Node(9))
    sll.insert(Node(16))
    sll.insert(Node(4))
    sll.insert(Node(1))
    assert sll.sort() == [1, 4, 9, 16]
