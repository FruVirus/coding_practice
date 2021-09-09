# Repository Library
from clrs.trees.bst import BST


def test_bst():
    bst = BST(12)
    bst.insert(5)
    bst.insert(2)
    bst.insert(9)
    bst.insert(18)
    bst.insert(15)
    bst.insert(17)
    bst.insert(13)
    bst.insert(19)
    bst.walk(12)
    bst_max = bst.max(12)
    bst_min = bst.min(12)
    assert bst_max.key == 19
    assert bst_min.key == 2
    result = bst.search(12, 18)
    assert (
        result.key == 18
        and result.p.key == 12
        and result.left.key == 15
        and result.right.key == 19
    )
    next_largest = bst.successor(9)
    assert next_largest.key == 12
    prev_largest = bst.predecessor(13)
    assert prev_largest.key == 12
    k = 5
    bst.delete(k)
    k = 12
    bst.delete(k)
    k = 2
    bst.delete(k)
    assert bst.root.key == 13
    bst_min = bst.min(13)
    assert bst_min.key == 9
