# Repository Library
from clrs.hash_tables.hash_chain import HashChain, is_prime, next_prime
from clrs.lists.singly_linked_list import Node


def test_hash_chain():
    x = HashChain(10)
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
    assert x.hash_uni(5, [0, 1, 2, 3, 4, 5], a=4, b=5) == 4


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(25) is False
    assert is_prime(700) is False
    assert is_prime(701) is True


def test_next_prime():
    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(700) == 701
