# Repository Library
from coding_practice.sorting import bubble_sort


def test_bubble_sort():
    assert bubble_sort([-5, 3, 2, -4, 1, 5]) == [-5, -4, 1, 2, 3, 5]
