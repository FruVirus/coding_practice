# Repository Library
from clrs.sorting_and_order_statistics.comparison_sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quicksort,
)
from clrs.sorting_and_order_statistics.comparison_sorting.heap_sort import HeapSort
from tests.conftest import PARAM


@PARAM(
    "a",
    [
        [-5, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 7, 5],
        [4, 7, 2, -4, 7, 5],
        [7, 4, 2, -4, 7, 5],
        [5, 4, 3, 2, 1, -4],
        [-1, -1, -1, -1],
        [1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [-5, -4, -3, -2, -1],
    ],
)
def test_bubble_sort(a):
    bubble_sort.bubble_sort(a)
    assert a == sorted(a)


@PARAM(
    "a",
    [
        [-5, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 7, 5],
        [4, 7, 2, -4, 7, 5],
        [7, 4, 2, -4, 7, 5],
        [5, 4, 3, 2, 1, -4],
        [-1, -1, -1, -1],
        [1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [-5, -4, -3, -2, -1],
    ],
)
def test_insertion_sort(a):
    insertion_sort.insertion_sort(a)
    assert a == sorted(a)


@PARAM(
    "a",
    [
        [-5, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 7, 5],
        [4, 7, 2, -4, 7, 5],
        [7, 4, 2, -4, 7, 5],
        [5, 4, 3, 2, 1, -4],
        [-1, -1, -1, -1],
        [1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [-5, -4, -3, -2, -1],
    ],
)
def test_merge_sort(a):
    assert merge_sort.merge_sort(a) == sorted(a)


@PARAM(
    "a",
    [
        [-5, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 7, 5],
        [4, 7, 2, -4, 7, 5],
        [7, 4, 2, -4, 7, 5],
        [5, 4, 3, 2, 1, -4],
        [-1, -1, -1, -1],
        [1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [-5, -4, -3, -2, -1],
    ],
)
def test_quicksort(a):
    quicksort.quicksort(a, 0, len(a) - 1)
    assert a == sorted(a)


@PARAM(
    "a",
    [
        [16, 14, 9, 10, 7, 8, 3, 1, 4, 2],
        [-5, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 1, 5],
        [5, 4, 3, 2, 1, -4],
        [-1, -1, -1, -1],
        [1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [-5, -4, -3, -2, -1],
    ],
)
def test_max_heap_sort(a):
    queue = HeapSort(a, is_max=True)
    queue.sort()
    assert queue.a == sorted(a)


@PARAM(
    "a",
    [
        [16, 14, 9, 10, 7, 8, 3, 1, 4, 2],
        [-5, 3, 2, -4, 1, 5],
        [4, 3, 2, -4, 1, 5],
        [5, 4, 3, 2, 1, -4],
        [-1, -1, -1, -1],
        [1, 1, 1, 1, 1],
        [0, 1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [-5, -4, -3, -2, -1],
    ],
)
def test_min_heap_sort(a):
    queue = HeapSort(a, is_max=False)
    queue.sort()
    assert queue.a == sorted(a, reverse=True)
