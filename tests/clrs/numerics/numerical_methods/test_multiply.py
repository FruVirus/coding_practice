# Repository Library
from clrs.numerics.numerical_methods.multiply import multiply


def test_multiply():
    assert (
        multiply(1234, 5678, is_naive=True)
        == multiply(1234, 5678, is_naive=False)
        == 7006652
    )
