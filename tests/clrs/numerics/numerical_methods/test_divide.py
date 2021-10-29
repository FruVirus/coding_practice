# Repository Library
from clrs.numerics.numerical_methods.divide import divide, power_of_two


def test_divide():
    assert divide(2, 64) == 0.5
    assert divide(5, 64) == 0.2
    assert divide(6, 64) == 0.16666666666666666
    assert divide(7, 64) == 0.14285714285714285


def test_power_of_two():
    assert power_of_two(0) == 0
    assert power_of_two(1) == 0
    assert power_of_two(187) == 7
