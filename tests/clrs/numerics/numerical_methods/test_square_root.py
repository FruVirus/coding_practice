# Repository Library
from clrs.numerics.numerical_methods.square_root import newtons_method


def test_method_method():
    assert newtons_method(2, 1) == 1.5
    assert newtons_method(2, 0.1) == 1.4166666666666665
    assert newtons_method(2, 0.01) == 1.4142156862745097
    assert newtons_method(2, 0.001) == 1.4142135623746899
    assert newtons_method(2, d=2) == 1.5
    assert newtons_method(2, d=4) == 1.4142156862745097
    assert newtons_method(2, d=8) == 1.414213562373095
