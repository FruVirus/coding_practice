# Repository Library
from clrs.numerics.numerical_methods.multiply import multiply


def test_multiply():
    assert multiply(1234, 5678, True) == multiply(1234, 5678, False) == 7006652
