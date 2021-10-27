# Repository Library
from clrs.numerics.numerical_methods.newtons_method import newton


def test_newton():
    assert (
        newton(lambda x: x ** 3 - x ** 2 - 1, lambda x: 3 * x ** 2 - 2 * x, 1, 1e-10)
        == 1.4655712318767877
    )
    assert (
        newton(lambda x: x ** 3 - 3, lambda x: 3 * x ** 2, 1, 1e-10)
        == 1.4422495703074416
    )
    assert (
        newton(
            lambda x: x ** (1 / 3), lambda x: (1 / 3) * x ** (-2 / 3), 0.1, 1e-2, 100
        )
        is None
    )
