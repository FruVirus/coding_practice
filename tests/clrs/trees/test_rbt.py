# Repository Library
from clrs.trees.rbt import RBT


def test_rbt():
    rbt = RBT(7)
    rbt.insert(2)
    rbt.insert(11)
    rbt.insert(1)
    rbt.insert(5)
    rbt.insert(8)
    rbt.insert(14)
    rbt.insert(4)
    rbt.insert(15)
    rbt.walk(7)
    assert rbt.root.key == 7
    assert rbt.root.color == 1
    assert rbt.root.left.key == 2
    assert rbt.root.left.color == 0
    assert rbt.root.right.key == 11
    assert rbt.root.right.color == 0
    assert rbt.successor(8).key == 11
    assert rbt.predecessor(4).key == 2
    rbt.delete(11)
    assert rbt.root.key == 7
    assert rbt.root.color == 1
    assert rbt.root.left.key == 2
    assert rbt.root.left.color == 0
    assert rbt.root.right.key == 14
    assert rbt.root.right.color == 0
    assert rbt.root.right.right.key == 15
    assert rbt.root.right.right.color == 1
