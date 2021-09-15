# Repository Library
from clrs.arrays.minmax import minmax
from tests.conftest import PARAM


@PARAM(
    "a, result",
    [
        (
            [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 700],
            (-25, 700),
        ),
        (
            [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4],
            (-25, 20),
        ),
    ],
)
def test_minmax(a, result):
    assert minmax(a) == result
