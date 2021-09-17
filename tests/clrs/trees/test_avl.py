# Repository Library
from clrs.trees.avl import AVL


def test_avl():
    avl = AVL(12)
    avl.insert(5)
    avl.insert(2)
    avl.insert(9)
    avl.insert(18)
    avl.insert(15)
    avl.insert(17)
    avl.insert(13)
    avl.insert(19)
    avl.walk(12)
    assert avl.rank(-1) == 0
    assert avl.rank(2) == 1
    assert avl.rank(5) == 2
    assert avl.rank(9) == 3
    assert avl.rank(12) == 4
    assert avl.rank(13) == 5
    assert avl.rank(15) == 6
    assert avl.rank(17) == 7
    assert avl.rank(18) == 8
    assert avl.rank(19) == 9
    assert avl.count(2, 19) == 9
    assert avl.count(2, 5) == 2
    assert avl.count(13, 19) == 5
    assert avl.count(-1, 19) == 9
    assert avl.count(2, 20) == 9
    assert avl.count(-1, 20) == 9
    root = avl.root
    assert (
        root.key == 12
        and root.h == 4
        and root.p is None
        and root.left.key == 5
        and root.left.h == 2
        and root.left.left.key == 2
        and root.left.left.h == 1
        and root.left.right.key == 9
        and root.left.right.h == 1
        and root.right.key == 17
        and root.right.h == 3
        and root.right.left.key == 15
        and root.right.left.h == 2
        and root.right.left.left.key == 13
        and root.right.left.left.h == 1
        and root.right.right.key == 18
        and root.right.right.h == 2
        and root.right.right.right.key == 19
        and root.right.right.right.h == 1
    )
    assert avl.list(2, 19) == [12, 5, 2, 9, 17, 15, 13, 18, 19]
    assert avl.list(13, 19) == [17, 15, 13, 18, 19]
    assert avl.height(12) == 4
    avl_max = avl.max(12)
    avl_min = avl.min(12)
    assert avl_max.key == 19
    assert avl_min.key == 2
    result = avl.search(12, 18)
    assert result.key == 18 and result.h == 2
    next_largest = avl.successor(9)
    assert next_largest.key == 12
    prev_largest = avl.predecessor(13)
    assert prev_largest.key == 12
    k = 5
    avl.delete(k)
    k = 12
    avl.delete(k)
    k = 2
    avl.delete(k)
    assert avl.root.key == 17 and avl.root.h == 4
    avl_min = avl.min(17)
    assert avl_min.key == 9
