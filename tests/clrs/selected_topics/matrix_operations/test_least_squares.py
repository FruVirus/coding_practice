# Standard Library
import math

# Repository Library
from clrs.selected_topics.matrix_operations.least_squares import (
    is_pos_def,
    least_squares,
)


def test_is_pos_def():
    assert is_pos_def([[1, 2], [3, 0]]) is False


def test_least_squares():
    data = [(-1, 2), (1, 1), (2, 1), (3, 0), (5, 3)]
    x = least_squares(data)
    x_answer = [1.2, -0.757, 0.214]
    for i, item in enumerate(x):
        assert math.isclose(item, x_answer[i], rel_tol=1e-2)
