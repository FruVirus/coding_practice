# Repository Library
from clrs.lists.doubly_linked_list import DLL, Node


def test_dll():
    dll = DLL()
    dll.insert(Node(9))
    dll.insert(Node(16))
    x = Node(4)
    dll.insert(x)
    dll.insert(Node(1))
    dll.delete(x)
    dll.delete(1)
    assert dll.head.k == 16
    assert dll.head.next.k == 9
    assert dll.head.prev is None
    x = dll.search(666)
    assert x is None
