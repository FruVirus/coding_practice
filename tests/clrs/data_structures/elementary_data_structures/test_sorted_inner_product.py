# Repository Library
from clrs.data_structures.elementary_data_structures.sorted_inner_product import (
    sorted_inner_product,
)
from tests.conftest import PARAM


@PARAM(
    "l1, l2, result",
    [
        (
            [[3, 2], [4, 1], [6, 1], [8, 1], [9, 1]],
            [[2, 1], [3, 1], [6, 1], [7, 1], [8, 1]],
            4.0,
        )
    ],
)
def test_sorted_inner_product(l1, l2, result):
    assert sorted_inner_product(l1, l2) == result
