# Repository Library
from clrs.data_structures.red_black_trees.rbt import RBT


def test_rbt():
    rbt = RBT(11)
    rbt.insert(2)
    rbt.insert(14)
    rbt.insert(1)
    rbt.insert(7)
    rbt.insert(15)
    rbt.insert(5)
    rbt.insert(8)
    assert rbt.root.key == 11
    assert rbt.root.c == 1
    assert rbt.root.left.key == 2
    assert rbt.root.left.c == 0
    assert rbt.root.right.key == 14
    assert rbt.root.right.c == 1
    assert rbt.root.left.left.key == 1
    assert rbt.root.left.left.c == 1
    assert rbt.root.right.right.key == 15
    assert rbt.root.right.right.c == 0
    assert rbt.root.left.right.key == 7
    assert rbt.root.left.right.c == 1
    assert rbt.root.left.right.left.key == 5
    assert rbt.root.left.right.left.c == 0
    assert rbt.root.left.right.right.key == 8
    assert rbt.root.left.right.right.c == 0
    rbt.insert(4)
    assert rbt.root.key == 7
    assert rbt.root.c == 1
    assert rbt.root.left.key == 2
    assert rbt.root.left.c == 0
    assert rbt.root.right.key == 11
    assert rbt.root.right.c == 0
    assert rbt.root.left.left.key == 1
    assert rbt.root.left.left.c == 1
    assert rbt.root.right.right.key == 14
    assert rbt.root.right.right.c == 1
    assert rbt.root.left.right.key == 5
    assert rbt.root.left.right.c == 1
    assert rbt.root.left.right.left.key == 4
    assert rbt.root.left.right.left.c == 0
    assert rbt.root.right.left.key == 8
    assert rbt.root.right.left.c == 1
    assert rbt.root.right.right.right.key == 15
    assert rbt.root.right.right.right.c == 0
    assert rbt.predecessor(7).key == 5
    assert rbt.successor(7).key == 8
    assert rbt.predecessor(14).key == 11
    assert rbt.successor(14).key == 15
    assert rbt.min(7).key == 1
    assert rbt.max(7).key == 15
    assert rbt.lca(1, 15).key == 7
    assert rbt.lca(1, 5).key == 2
    assert rbt.lca(14, 15).key == 14
    assert rbt.lca(8, 15).key == 11
    assert rbt.list(1, 15) == [1, 2, 4, 5, 7, 8, 11, 14, 15]
    assert rbt.list(8, 15) == [8, 11, 14, 15]
    assert rbt.search(7, 15).key == 15
    assert rbt.root.size == 9
    assert rbt.root.left.size == 4
    assert rbt.root.right.size == 4
    assert rbt.root.left.right.size == 2
    assert rbt.root.right.right.size == 2
    assert rbt.rank(1) == 1
    assert rbt.rank(7) == 5
    assert rbt.rank(15) == 9
    assert rbt.count(1, 15) == 9
    assert rbt.count(2, 15) == 8
    assert rbt.count(3, 15) == 7
    assert rbt.count(4, 15) == 7
    assert rbt.count(4, 16) == 7
    assert rbt.count(3, 12) == 5
    assert rbt.count(4, 11) == 5
    rbt.walk(7)
    rbt.delete(11)
    assert rbt.root.key == 7
    assert rbt.root.c == 1
    assert rbt.root.left.key == 2
    assert rbt.root.left.c == 0
    assert rbt.root.left.left.key == 1
    assert rbt.root.left.left.c == 1
    assert rbt.root.left.right.key == 5
    assert rbt.root.left.right.c == 1
    assert rbt.root.left.right.left.key == 4
    assert rbt.root.left.right.left.c == 0
    assert rbt.root.right.key == 14
    assert rbt.root.right.c == 0
    assert rbt.root.right.left.key == 8
    assert rbt.root.right.left.c == 1
    assert rbt.root.right.right.key == 15
    assert rbt.root.right.right.c == 1
    rbt.delete(2)
    assert rbt.root.key == 7
    assert rbt.root.c == 1
    assert rbt.root.left.key == 4
    assert rbt.root.left.c == 0
    assert rbt.root.left.left.key == 1
    assert rbt.root.left.left.c == 1
    assert rbt.root.left.right.key == 5
    assert rbt.root.left.right.c == 1
    assert rbt.root.right.key == 14
    assert rbt.root.right.c == 0
    assert rbt.root.right.left.key == 8
    assert rbt.root.right.left.c == 1
    assert rbt.root.right.right.key == 15
    assert rbt.root.right.right.c == 1
