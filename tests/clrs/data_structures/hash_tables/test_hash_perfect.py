# Repository Library
from clrs.data_structures.hash_tables.hash_perfect import HashPerfect


def test_hash_perfect():
    x = HashPerfect([10, 22, 37, 40, 52, 60, 70, 72, 75], a=3, b=42, p=101)
    assert len(x.table) == 9
    assert x.table[0] == 10
    assert x.table[1] is None
    assert isinstance(x.table[2], list)
    assert 60 in x.table[2]
    assert 72 in x.table[2]
    assert 75 in x.table[2]
    assert x.table[3] is None
    assert x.table[4] is None
    assert x.table[5] == 70
    assert x.table[6] is None
    assert isinstance(x.table[7], list)
    assert 22 in x.table[7]
    assert 37 in x.table[7]
    assert 40 in x.table[7]
    assert 52 in x.table[7]
    assert x.table[8] is None
    assert x.search(10)[0] == 0
    assert x.search(10)[1] is None
    result = x.search(72)
    assert result[0] == 2 and result[1] == 1
    result = x.search(60)
    assert result[0] == 2 and result[1] == 2
