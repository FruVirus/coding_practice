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
    assert x.search(1) is None
    x.delete(y)
    assert x.hash_mul(666) == 942
    assert x.hash_uni(5, [0, 1, 2, 3, 4, 5], a=4, b=5) == 4


def test_table_doubling():
    x = HashChain(size=2)
    x.insert(Node(1))
    x.insert(Node(2))
    x.insert(Node(3))
    x.insert(Node(5))
    x.insert(Node(6))
    x.insert(Node(7))
    x.insert(Node(12))
    x.insert(Node(13))
    x.insert(Node(14))
    x.insert(Node(15))
    for i in range(len(x.table)):
        if i == 0:
            assert x.table[i] is None
        else:
            assert x.table[i] is not None
    assert x.table[1].head.k == 1
    assert x.table[1].head.next is None
    assert x.table[1].head.prev is None
    assert x.table[2].head.k == 2
    assert x.table[2].head.next is None
    assert x.table[2].head.prev is None
    assert x.table[3].head.k == 3
    assert x.table[3].head.next is None
    assert x.table[3].head.prev is None
    assert x.table[4].head.k == 12
    assert x.table[4].head.next is None
    assert x.table[4].head.prev is None
    assert x.table[5].head.k == 13
    assert x.table[5].head.next.k == 5
    assert x.table[5].head.prev is None
    assert x.table[5].head.next.k == 5
    assert x.table[5].head.next.next is None
    assert x.table[5].head.next.prev.k == 13
    assert x.table[6].head.k == 14
    assert x.table[6].head.next.k == 6
    assert x.table[6].head.prev is None
    assert x.table[6].head.next.k == 6
    assert x.table[6].head.next.next is None
    assert x.table[6].head.next.prev.k == 14
    assert x.table[7].head.k == 15
    assert x.table[7].head.next.k == 7
    assert x.table[7].head.prev is None
    assert x.table[7].head.next.k == 7
    assert x.table[7].head.next.next is None
    assert x.table[7].head.next.prev.k == 15
    x.delete(15)
    x.delete(14)
    x.delete(13)
    x.delete(12)
    x.delete(7)
    x.delete(6)
    x.delete(5)
    assert len(x.table) == 8
    x.delete(3)
    assert len(x.table) == 4
    assert x.table[0] is None
    assert x.table[3] is None
    assert x.table[1].head.k == 1
    assert x.table[2].head.k == 2


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
