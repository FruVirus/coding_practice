# Repository Library
from clrs.hash_tables.hash_open_addressing import HashOpen


def test_hash_open():
    x = HashOpen(10)
    x.insert(8)
    x.insert(3)
    x.insert(13)
    x.insert(6)
    x.insert(4)
    x.insert(10)
    assert x.table[0] == 10
    assert x.table[3] == 3
    assert x.table[4] == 13
    assert x.table[5] == 4
    assert x.table[6] == 6
    assert x.table[8] == 8
    assert x.search(10) == 0
    assert x.search(13) == 4
    assert x.search(8) == 8
    x.delete(13)
    assert x.search(4) == 5
    x = HashOpen(10, hash_func="quadratic_probe")
    x.insert(8)
    x.insert(3)
    x.insert(13)
    x.insert(6)
    x.insert(4)
    x.insert(5)
    x.insert(10)
    assert x.table[0] == 10
    assert x.table[3] == 3
    assert x.table[4] == 13
    assert x.table[5] == 4
    assert x.table[6] == 6
    assert x.table[8] == 8
    assert x.table[9] == 5
    assert x.search(10) == 0
    assert x.search(13) == 4
    assert x.search(8) == 8
    x.delete(13)
    assert x.search(4) == 5
    x = HashOpen(8, hash_func="double_hashing")
    x.insert(8)
    x.insert(3)
    x.insert(13)
    x.insert(6)
    x.insert(4)
    x.insert(5)
    x.insert(10)
    assert x.table[0] == 8
    assert x.table[1] is None
    assert x.table[2] == 10
    assert x.table[3] == 3
    assert x.table[4] == 4
    assert x.table[5] == 13
    assert x.table[6] == 6
    assert x.table[7] == 5
    assert x.search(10) == 2
    assert x.search(13) == 5
    assert x.search(8) == 0
    x.delete(13)
    assert x.search(4) == 4
    assert x.search(6) == 6
    assert x.search(5) == 7
