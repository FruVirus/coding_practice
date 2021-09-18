# Repository Library
from clrs.hash_tables.hash import Hash
from clrs.lists.singly_linked_list import Node


def test_hash():
    x = Hash(10)
    x.insert(Node(8))
    x.insert(Node(3))
    x.insert(Node(13))
    y = Node(6)
    x.insert(y)
    x.insert(Node(4))
    x.insert(Node(10))
    assert x.table[3].head.k == 13
    assert x.table[3].head.next.k == 3
    assert x.table[3].head.prev is None
    x.delete(13)
    assert x.table[3].head.k == 3
    assert x.table[3].head.next is None
    assert x.table[3].head.prev is None
    assert x.search(10).k == 10
    x.delete(y)
    assert x.hash_mul(666) == 942
