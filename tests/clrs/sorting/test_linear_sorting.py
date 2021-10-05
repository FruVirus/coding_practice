# Repository Library
from clrs.sorting.linear_sorting import (
    bucket_sort,
    counting_sort,
    pigeonhole_sort,
    radix_sort,
)
from tests.conftest import PARAM


@PARAM(
    "a",
    [
        [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68],
        [7.8, 1.7, 3.9, 2.6, 7.2, 9.4, 2.1, 1.2, 2.3, 6.8],
    ],
)
def test_bucket_sort(a):
    assert bucket_sort.bucket_sort(a) == sorted(a)


@PARAM(
    "a, k",
    [
        ([2, 5, 3, 0, 2, 3, 0, 3], 5),
        ([1, 1, 1, 1, 1], 1),
        ([0, 1, 2, 3, 4], 5),
        ([5, 4, 3, 2, 1], 5),
        ([329, 457, 657, 839, 436, 720, 355], 900),
    ],
)
def test_counting_sort(a, k):
    assert counting_sort.counting_sort(a, k) == sorted(a)


def test_pigeonhole_sort():
    a = [(5, "king"), (3, "pie"), (8, "apple"), (5, "hello")]
    pigeonhole_sort.pigeonhole_sort(a)
    assert a == [(3, "pie"), (5, "king"), (5, "hello"), (8, "apple")]


@PARAM(
    "a",
    [
        [329, 457, 657, 839, 436, 720, 355],
        [170, 45, 75, 90, 802, 24, 2, 66],
    ],
)
def test_radix_sort(a):
    assert radix_sort.radix_sort(a) == sorted(a)
