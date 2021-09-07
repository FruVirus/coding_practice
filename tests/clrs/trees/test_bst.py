# Repository Library
from clrs.trees.bst import BST


def test_bst():
    bst = BST()
    bst.insert(12)
    bst.insert(5)
    bst.insert(2)
    bst.insert(9)
    bst.insert(18)
    bst.insert(15)
    bst.insert(17)
    bst.insert(13)
    bst.insert(19)
    bst.walk()
    bst_max = bst.max()
    bst_min = bst.min()
    assert bst_max.key == 19
    assert bst_min.key == 2
    result = bst.search(18)
    assert (
        result.key == 18
        and result.parent.key == 12
        and result.left.key == 15
        and result.right.key == 19
    )
    next_largest = bst.successor(9)
    assert next_largest.key == 12
    prev_largest = bst.predecessor(13)
    assert prev_largest.key == 12
    k = 5
    deleted = bst.delete(k)
    assert deleted.key == k
    assert deleted.left is None
    assert deleted.right is None
    assert deleted.parent.key == 9
    k = 12
    deleted = bst.delete(k)
    assert deleted.key == k
    assert deleted.left is None
    assert deleted.right is None
    assert deleted.parent.key == 15
    assert bst.root.key == 13
