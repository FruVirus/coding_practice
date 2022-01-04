# Repository Library
from clrs.data_structures.elementary_data_structures.linked_list import Node
from g4g.lists.singly_linked_list_insertion_sort import SLLInsertionSort


def test_sll_insertion_sort():
    sll = SLLInsertionSort()
    sll.insert(Node(5))
    sll.insert(Node(20))
    sll.insert(Node(4))
    sll.insert(Node(3))
    sll.insert(Node(30))
    assert sll.sort() == [3, 4, 5, 20, 30]
