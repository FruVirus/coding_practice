# Third Party Library
import pytest

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
    x = HashOpen(10, hash_func="hash_quadratic")
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
    with pytest.raises(OverflowError):
        x.insert(9)
    x.delete(13)
    assert x.search(4) == 5
    x.insert(1)
    x.insert(2)
    x.insert(7)
    assert x.search(666) is None
    x = HashOpen(8, hash_func="hash_double")
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
    x = HashOpen(11, hash_func="hash_double")
    x.insert(8)
    x.insert(3)
    x.insert(13)
    x.insert(6)
    x.insert(4)
    x.insert(5)
    x.insert(10)
    assert x.table[0] is None
    assert x.table[1] is None
    assert x.table[2] == 13
    assert x.table[3] == 3
    assert x.table[4] == 4
    assert x.table[5] == 5
    assert x.table[6] == 6
    assert x.table[7] is None
    assert x.table[8] == 8
    assert x.table[9] is None
    assert x.table[10] == 10
    assert x.search(10) == 10
    assert x.search(13) == 2
    assert x.search(8) == 8
    x.delete(4)
    assert x.search(13) == 2
    assert x.search(3) == 3
    assert x.search(5) == 5


def test_table_doubling():
    x = HashOpen(size=2, table_double=True)
    x.insert(1)
    x.insert(2)
    x.insert(3)
    x.insert(4)
    x.insert(5)
    x.insert(6)
    x.insert(7)
    x.insert(8)
    x.insert(9)
    assert len(x.table) == 16
    assert x.table[1] == 1
    assert x.table[2] == 2
    assert x.table[3] == 3
    assert x.table[4] == 4
    assert x.table[5] == 5
    assert x.table[6] == 6
    assert x.table[7] == 7
    assert x.table[8] == 8
    assert x.table[9] == 9
    assert x.table[0] is None
    assert x.table[10] is None
    assert x.table[11] is None
    assert x.table[12] is None
    assert x.table[13] is None
    assert x.table[14] is None
    assert x.table[15] is None
    x.delete(9)
    x.delete(8)
    x.delete(7)
    x.delete(6)
    x.delete(5)
    assert len(x.table) == 8
    assert x.table[1] == 1
    assert x.table[2] == 2
    assert x.table[3] == 3
    assert x.table[4] == 4
    assert x.table[0] is None
    assert x.table[5] is None
    assert x.table[6] is None
    assert x.table[7] is None
    x.insert(1)
    x.insert(1)
    x.insert(1)
    x.insert(1)
    assert x.table == [1, 1, 2, 3, 4, 1, 1, 1]
    x.insert(1)
    assert x.table == [
        None,
        1,
        1,
        2,
        3,
        4,
        1,
        1,
        1,
        1,
        None,
        None,
        None,
        None,
        None,
        None,
    ]
