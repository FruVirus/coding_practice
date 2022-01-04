# Repository Library
from clrs.selected_topics.number_theoretic_algorithms.numerical_methods.multiply import (  # noqa: E501
    multiply,
)


def test_multiply():
    assert (
        multiply(1234, 5678, is_naive=True)
        == multiply(1234, 5678, is_naive=False)
        == 7006652
    )
