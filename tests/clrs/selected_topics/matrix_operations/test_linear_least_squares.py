# Standard Library
import math

# Repository Library
from clrs.selected_topics.matrix_operations.linear_least_squares import llss


def test_llss():
    data = [(-1, 2), (1, 1), (2, 1), (3, 0), (5, 3)]
    x = llss(data)
    x_answer = [1.2, -0.757, 0.214]
    for i, item in enumerate(x):
        assert math.isclose(item, x_answer[i], rel_tol=1e-2)
