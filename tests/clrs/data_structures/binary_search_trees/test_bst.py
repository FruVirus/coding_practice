# Repository Library
from clrs.data_structures.binary_search_trees.bst import BST, BSTNode


def test_bst():
    bst = BST(12)
    bst.insert(5)
    bst.insert(2)
    bst.insert(9)
    bst.insert(18)
    bst.insert(15)
    bst.insert(17)
    x = BSTNode(13)
    bst.insert(x)
    bst.insert(19)
    bst.walk(12)
    assert bst.select(5).key == 13
    assert bst.rank(x) == 5
    assert bst.rank_key(-1) == 0
    assert bst.rank_key(2) == 1
    assert bst.rank_key(5) == 2
    assert bst.rank_key(9) == 3
    assert bst.rank_key(12) == 4
    assert bst.rank_key(13) == 5
    assert bst.rank_key(15) == 6
    assert bst.rank_key(17) == 7
    assert bst.rank_key(18) == 8
    assert bst.rank_key(19) == 9
    assert bst.count(1, 19) == 9
    assert bst.count(1, 200) == 9
    assert bst.count(0, 200) == 9
    assert bst.count(2, 19) == 9
    assert bst.count(2, 5) == 2
    assert bst.count(13, 19) == 5
    assert bst.count(-1, 19) == 9
    assert bst.count(2, 20) == 9
    assert bst.count(-1, 20) == 9
    assert bst.list(2, 19) == sorted([12, 5, 2, 9, 18, 15, 13, 17, 19])
    assert bst.list(13, 19) == sorted([18, 15, 13, 17, 19])
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
    assert bst.rank_key(-1) == 0
    assert bst.rank_key(2) == 1
    assert bst.rank_key(9) == 2
    assert bst.rank_key(12) == 3
    assert bst.rank_key(13) == 4
    assert bst.rank_key(15) == 5
    assert bst.rank_key(17) == 6
    assert bst.rank_key(18) == 7
    assert bst.rank_key(19) == 8
    assert bst.count(2, 19) == 8
    assert bst.count(13, 19) == 5
    assert bst.count(-1, 19) == 8
    assert bst.count(2, 20) == 8
    assert bst.count(-1, 20) == 8
    k = 12
    bst.delete(k)
    k = 2
    bst.delete(k)
    assert bst.root.key == 13
    bst_min = bst.min(13)
    assert bst_min.key == 9
