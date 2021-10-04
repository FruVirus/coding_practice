# Repository Library
from clrs.lists.singly_linked_list import Node
from g4g.lists.doubly_linked_list_quick_sort import DLLQuickSort


def test_dll_quick_sort():
    dll = DLLQuickSort()
    dll.insert(Node(9))
    dll.insert(Node(16))
    dll.insert(Node(4))
    dll.insert(Node(1))
    assert dll.sort() == [1, 4, 9, 16]
