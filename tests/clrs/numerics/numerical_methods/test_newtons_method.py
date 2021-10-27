# Repository Library
from clrs.numerics.numerical_methods.newtons_method import square_root


def test_square_root():
    assert square_root(2, tol=1) == 1.5
    assert square_root(2, tol=0.1) == 1.4166666666666667
    assert square_root(2, tol=0.01) == 1.4142156862745097
    assert square_root(2, tol=0.001) == 1.41421356237469
    assert square_root(2, d=2) == 1.5
    assert square_root(2, d=4) == 1.4142156862745097
    assert square_root(2, d=8) == 1.414213562373095
