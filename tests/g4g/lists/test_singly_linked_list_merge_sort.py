# Repository Library
from clrs.lists.singly_linked_list import Node
from g4g.lists.singly_linked_list_merge_sort import SLLMergeSort


def test_sll_merge_sort():
    sll = SLLMergeSort()
    sll.insert(Node(9))
    sll.insert(Node(16))
    sll.insert(Node(4))
    sll.insert(Node(1))
    assert sll.sort() == [1, 4, 9, 16]
