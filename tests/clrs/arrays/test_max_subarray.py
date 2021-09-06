# Repository Library
from clrs.arrays.max_subarray import find_max
from tests.conftest import PARAM


@PARAM(
    "a, result",
    [
        (
            [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 700],
            (7, 15, 727.0),
        ),
    ],
)
def test_max_subarray(a, result):
    assert find_max(a, 0, len(a) - 1) == result
